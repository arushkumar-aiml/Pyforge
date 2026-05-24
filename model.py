import torch.nn as nn

class SimpleNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.layer1 = nn.Linear(10, 5)
        self.layer2 = nn.Linear(5, 1)
    
    def forward(self, x):
        x = self.layer1(x)
        x = self.layer2(x)
        return x