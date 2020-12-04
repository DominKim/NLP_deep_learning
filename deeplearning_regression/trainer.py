# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 13:42:19 2020

@author: User
"""

from copy import deepcopy

import numpy as np

import torch
import torch.nn as nn
import torch.optim as optim

class Trainer():
    
    def __init__(self, model, optimizer, crit):
        super(Trainer, self).__init__()
        self.model = model
        self.optimizer = optimizer
        self.crit = crit
        
        
    def _train(self, train_loader, config):
        self.model.train()
        
        total_loss = 0
        
        for i, (x_i, y_i) in enumerate(train_loader):
            x_i, y_i = x_i.to(config.device), y_i.to(config.device)
            y_i = y_i.type(torch.float)
            y_hat_i = self.model(x_i)
            loss_i = self.crit(y_hat_i, y_i)
            self.optimizer.zero_grad()
            loss_i.backward()
            
            self.optimizer.step()
            
            if config.verbose >= 2:
                print("Train Iteraion(%d/%d) : loss : %.4e" % (
                    i + 1, 6000, loss_i))
                
            total_loss += float(loss_i)
            
        return total_loss / 6000
    
    def _validate(self, valid_loader, config):
        self.model.eval()
        
        total_loss = 0
        
        with torch.no_grad():
            for i, (x_i, y_i) in enumerate(valid_loader):
                x_i, y_i = x_i.to(config.device), y_i.to(config.device)
                y_i = y_i.type(torch.float)
                y_hat_i = self.model(x_i)
                loss_i = self.crit(y_hat_i, y_i)
                
                if config.verbose >= 2:
                    print("Valid Iteraion(%d/%d) : loss: %.4e" % (
                        i + 1, 6000, loss_i))
                total_loss += float(loss_i)
                
            return total_loss / 6000
        
        
    def train(self, train_loader, valid_loader, config):
        lowest_loss = np.inf
        best_model = None
        
        for epoch in range(config.n_epochs):
            train_loss = self._train(train_loader, config)
            valid_loss = self._validate(valid_loader, config)
            
            if valid_loss <= lowest_loss:
                lowest_loss = valid_loss
                best_model = deepcopy(self.model.state_dict())
                
            print("Epoch(%d/%d): train_los: %.4e, valid_loss=%.4e, lowest_loss=%.4e" %(
                epoch, config.n_epochs, train_loss, valid_loss, lowest_loss
                ))
            
            
        self.model.load_state_dict(best_model)
    
            