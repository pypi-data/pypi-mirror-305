import torch
import json
import numpy as np
from types import SimpleNamespace

def load_config(path):
    with open(path, 'r') as file:
        data = json.load(file)
    return SimpleNamespace(**data)

def save_config(config, path):
    with open(path, 'w') as file:
        json.dump(vars(config), file, indent=4)

class GradNormFunction(torch.autograd.Function):
    @staticmethod
    def forward(ctx, x):
        return x.clone()
    @staticmethod
    def backward(ctx, grad_output):
        grad_output_norm = torch.linalg.norm(grad_output, dim=0, keepdim=True)
        grad_output_normalized = grad_output / (grad_output_norm + 1e-8)
        return grad_output_normalized
def gradnorm(x):
    return GradNormFunction.apply(x)

def minus_cosine_warmup(i_step, config):
    scale = 0.5 * (np.log10(config.max_lr) - np.log10(config.min_lr))
    angle =  np.pi * i_step / (config.warmup_steps//config.plot_update)
    log_lr = np.log10(config.min_lr) + scale * (1 - np.cos(angle))
    lr = 10 ** log_lr
    return lr/config.min_lr

def size_distribution():
    sizes = [(w, h) for w in range(128, 385, 64) for h in range(128, 385, 64)]
    adjusted_weights = []
    aspect_weight_factors = {
        'landscape': 3.0024,
        'square': 1.7074,
        'portrait': 1.0
    }
    min_area = 128 * 128
    for w, h in sizes:
        area = w * h
        # Size weight inversely proportional to area
        size_weight = min_area / area
        aspect_ratio = w / h
        if aspect_ratio > 1.3:
            aspect = 'landscape'
        elif aspect_ratio < 1 / 1.3:
            aspect = 'portrait'
        else:
            aspect = 'square'
        aspect_weight = aspect_weight_factors[aspect]
        adjusted_weight = size_weight * aspect_weight
        adjusted_weights.append(adjusted_weight)
    
    total_weight = sum(adjusted_weights)
    probabilities = [w / total_weight for w in adjusted_weights]
    return sizes, probabilities


def infinite_decay_with_warmup(i_step, config):
    """
    Computes the learning rate with a warmup phase followed by an infinite decay.

    and then decays asymptotically using a scaled cosine decay with an arctan function.

    Parameters:
    - i_step (int): The current training step.
    - config (SimpleNamespace): Configuration object containing:
        - min_lr (float): Minimum learning rate.
        - max_lr (float): Maximum learning rate.
        - warmup (int): Number of steps for the warmup phase.
        - decay_rate (float): Decay rate after the warmup phase.

    Returns:
    - float: The scaled learning rate.

    Example:      
        config = SimpleNamespace()
        config.min_lr = 1e-6
        config.max_lr = 4e-4
        config.plot_update = 128
        config.warmup = 50000//config.plot_update
        config.decay_rate=1
                
        optimizer = torch.optim.AdamW(
            params=Layer2D(64,64).parameters(),
            lr=config.min_lr,
        )
        
        schedule = torch.optim.lr_scheduler.LambdaLR(
            optimizer,
            lr_lambda = lambda i_step: infinite_decay_with_warmup(i_step, config),
        )
        
        learning_rates = [optimizer.param_groups[0]['lr']]
        
        for i_step in range(50*10000):
            if (i_step+1) % config.plot_update == 0:
                schedule.step()
                learning_rates.append(optimizer.param_groups[0]['lr'])
        
        plt.semilogy(learning_rates)
    """
    x = i_step / config.warmup
    scale = (np.log10(config.max_lr) - np.log10(config.min_lr))
    if x < 1:
        log_lr = 0.5 * (1 - np.cos(np.pi * x))
    else:
        log_lr = np.cos(np.arctan(config.decay_rate * (x - 1)))
    log_lr = np.log10(config.min_lr) + scale * log_lr
    lr = 10 ** log_lr
    return lr / config.min_lr

