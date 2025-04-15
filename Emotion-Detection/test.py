import netron

# Method 1: Auto-select port (no need to specify)
netron.start("best.onnx")  # Opens in default browser on random port

# Method 2: Use CLI-style syntax
netron.start("best.onnx", address=('localhost', 8080))  # Specific port
