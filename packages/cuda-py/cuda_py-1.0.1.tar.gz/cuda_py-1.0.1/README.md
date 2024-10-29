# cuda-py

A very simple python wrapper for running code on CUDA devices.

```python
@cuda.run()
def myCudaFunc():
    print("Look! I'm running on the GPU!")

myCudaFunc() # Run the function normally.
```

If no CUDA device is found, the code will run normally on the CPU and `WARN: No CUDA device found!` will be printed.
