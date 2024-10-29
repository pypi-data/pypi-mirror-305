"""
A very simple python wrapper for running code on CUDA devices.
```python
@cuda.run()
def myCudaFunc():
    print("Look! I'm running on the GPU!")
```
If no CUDA device is found, the code will run normally on the CPU.
"""

import torch

def run(func):
    """
    
    """
    if torch.cuda.is_available():
        def wrapper(*args, **kwargs):
            device = torch.device('cuda')

            args_cuda = [arg.to(device) if isinstance(arg, torch.Tensor) else arg for arg in args]
            kwargs_cuda = {k: v.to(device) if isinstance(v, torch.Tensor) else v for k, v in kwargs.items()}

            with torch.cuda.device(device):
                result = func(*args_cuda, **kwargs_cuda)

            return result
    else:
        print("WARN: No CUDA device found!")
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

    return wrapper