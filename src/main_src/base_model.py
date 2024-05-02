import torch
import torch.nn as nn

class ModelV2(nn.Module):
    def __init__(self):
        super().__init__()

        self.layer_stack = nn.Sequential(
            nn.Tanh(),
            nn.Linear(in_features=7, out_features=1),
            nn.ReLU()
        )

    def forward(self, x):
        return self.layer_stack(x)
