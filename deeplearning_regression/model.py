# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 13:27:08 2020

@author: User
"""

import torch.nn as nn

class Image_regression(nn.Module):
    
    def __init__(self):
        super(Image_regression, self).__init__()
        
        self.layer = nn.Sequential(
            nn.Conv2d(3, 16, 3, padding = 1),
            nn.BatchNorm2d(16),
            
            nn.Conv2d(16, 16, 3, padding = 1),
            nn.BatchNorm2d(16),
            nn.MaxPool2d(2),
            
            
            nn.Conv2d(16, 32, 3, padding=1),
            nn.BatchNorm2d(32),
            nn.MaxPool2d(2),
            
            nn.Conv2d(32, 64, 3, padding = 1),
            nn.BatchNorm2d(64),
            
            nn.Conv2d(64, 64, 3, padding = 1),
            nn.BatchNorm2d(64),
            nn.MaxPool2d(2)
            )
        
        self.fc = nn.Sequential(
            nn.Linear(50176, 56),
            nn.Linear(56, 1)
        )
        
    def forward(self, x):
        out = self.layer(x)
        out = out.view(out.size(0), -1)
        out = self.fc(out)
        out = out.view(-1)
        return out
