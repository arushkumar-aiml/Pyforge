import torch
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset
from hardware import detect_device
from model import SimpleNet

class PyForge:          
    def __init__(self, model):
        self.device = detect_device()
        self.model = model.to(self.device)
        print(f"[PyForge] Device: {self.device}")
    
    @staticmethod
    def supported_devices():
        return ["cuda", "mps", "cpu"]
    
    @property
    def device_info(self):
        return f"[Pyforge] Running on {self.device}"
    
    def load_data(self, batch_size=32):
        X = torch.randn(100, 10)
        y = torch.randn(100, 1)
        dataset = TensorDataset(X, y)
        return DataLoader(dataset, batch_size=batch_size)
    
    def train(self, epochs=3):
        loader = self.load_data()
        optimizer = torch.optim.Adam(
            self.model.parameters()
        )
        criterion = nn.MSELoss()
        
        for epoch in range(epochs):
            for X, y in loader:
                X = X.to(self.device)
                y = y.to(self.device)
                optimizer.zero_grad()
                pred = self.model(X)
                loss = criterion(pred, y)
                loss.backward()
                optimizer.step()
            print(f"[Pyforge] Epoch {epoch+1} Loss: {loss.item():.4f}")
    
    def validate(self):
        loader = self.load_data()
        criterion = nn.MSELoss()
        self.model.eval()
        
        with torch.no_grad():
            for X, y in loader:
                X = X.to(self.device)
                y = y.to(self.device)
                pred = self.model(X)
                loss = criterion(pred, y)
        
        print(f"[Pyforge] Validation Loss: {loss.item():.4f}")