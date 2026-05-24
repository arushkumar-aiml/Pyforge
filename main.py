from model import SimpleNet
from trainer import PyForge  # Red ki jagah PyForge

model = SimpleNet()
forge = PyForge(model)  # red ki jagah forge

print(forge.device_info)
print(f"[PyForge] Supported: {PyForge.supported_devices()}")

forge.train(epochs=3)
forge.validate()