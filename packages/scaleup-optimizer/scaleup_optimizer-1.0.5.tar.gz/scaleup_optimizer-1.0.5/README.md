# scaleup-optimizer

`scaleup-optimizer` is a Python library for hyperparameter optimization using scalable algorithms. It integrates Bayesian optimization techniques to handle both small-scale (Experiment System) and large-scale (Production System) machine learning models.

## Problem Statement

Training and optimizing large-scale machine learning models presents several challenges:

- Computational Cost: Direct hyperparameter optimization on large models is extremely expensive in terms of both time and computational resources.
- Limited Iterations: Due to resource constraints, we can only perform a small number of optimization iterations on large models.
- Inefficient Search: Traditional approaches may waste valuable compute exploring suboptimal regions of the hyperparameter space.

## Description

This library is designed to help you efficiently optimize hyperparameters of machine learning models using Bayesian Optimization technique. It provides tools for working with both small-scale (e.g., experimental) and large-scale (e.g., production) systems, the large-scale leverages optimization history from small-scale.

## Architecture

The library consists of two main components:

### 1. SmallScaleOptimizer

- Performs initial Bayesian optimization on a smaller version of the model (Experiment System)
- Minimizes the objective function through multiple iterations
- Collects optimization history (best_params, X_iters, Y_iters) to inform the second stage
- Uses Small Scale Gaussian Process with acquisition functions

### 2. LargeScaleOptimizer

- Leverages optimization history from SmallScaleOptimizer
- Incorporates transfer learning to warm-start the optimization process
- Efficiently explores promising regions of the hyperparameter space
- Uses Large Scale Gaussian Process with acquisition functions

## Installation

### scaleup-optimizer requires

- `numpy>=1.21.0`
- `scipy>=1.10.0`
- `scikit-optimize>=0.8.1`
- `matplotlib>=3.4.0`

### Install via pip

You can install the library from PyPI or your local environment:

#### From PyPI

```bash
pip install scaleup-optimizer

```

## Getting Started

### Define the Experiment Model and decide on parameters to optimize then define objective function to minimize.

#### Load Dataset

```bash
import numpy as np
import torch
import torch.nn as nn
import torchvision.datasets as datasets
from torch.utils.data import Subset
from torch.utils.data import DataLoader,random_split
import torchvision.transforms as transforms

data_transform = transforms.ToTensor()

train_dataset = datasets.FashionMNIST(root="datasets", train=True, transform=data_transform, download=True)
test_dataset = datasets.FashionMNIST(root="datasets", train=False, transform=data_transform, download=True)

# Calculate 5% of the datasets
test_subset_size = int(0.05 * len(test_dataset))
test_subset, _ = random_split(test_dataset, [test_subset_size, len(test_dataset) - test_subset_size])

train_data_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)
test_data_loader = DataLoader(test_subset, batch_size=64, shuffle=True)
test_data_loader_L = DataLoader(test_dataset, batch_size=64, shuffle=True)
```

#### Define Experiment Model

```bash
class ModelS(nn.Module):
    def __init__(self, dropout_rate=0.2, conv_kernel_size=3, pool_kernel_size=2):
        super(ModelS, self).__init__()
        self.features = nn.Sequential(
            nn.Conv2d(1, 64, kernel_size=conv_kernel_size, stride=1, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=pool_kernel_size),
            self.merge_channels(64, 32),
        )

        self._compute_linear_input_size()

        self.classifier = nn.Sequential(
            nn.Dropout(dropout_rate),
            nn.Linear(self.linear_input_size, 10),
            nn.LogSoftmax(dim=1),
        )

    def merge_channels(self, in_channels, out_channels):
        assert in_channels == 2 * out_channels, "in_channels should be twice out_channels"
        return nn.Sequential(
            nn.Conv2d(in_channels, out_channels, kernel_size=1, stride=1),
        )

    def _compute_linear_input_size(self):
        with torch.no_grad():
            dummy_input = torch.zeros(1, 1, 28, 28)
            features_output = self.features(dummy_input)
            num_channels, height, width = features_output.size()[1:]
            self.linear_input_size = num_channels * height * width

    def forward(self, x):
        x = self.features(x)
        x = torch.flatten(x, 1)
        x = self.classifier(x)
        return x

nll_loss = nn.NLLLoss()

# Select the device on which to perform the calculation.
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Transfer the model to the device that will perform the calculation.
model = ModelS().to(device)
# Create an Optimizer.
optim = torch.optim.Adam(model.parameters())

def train(model, device, data_loader, optim):
    model.train()

    total_loss = 0
    total_correct = 0
    for data, target in data_loader:
        # Transfer the data and labels to the device performing the calculation.
        data, target = data.to(device), target.to(device)

        # Sequential propagation.
        output = model(data)

        loss = nll_loss(output, target)
        total_loss += float(loss)

        # Reverse propagation or backpropagation
        optim.zero_grad()
        loss.backward()

        # Update parameters.
        optim.step()

        # The class with the highest probability is the predictive label.
        pred_target = output.argmax(dim=1)

        total_correct += int((pred_target == target).sum())

    avg_loss = total_loss / len(data_loader.dataset)
    accuracy = total_correct / len(data_loader.dataset)

    return avg_loss, accuracy

def test(model, device, data_loader):
    model.eval()

    with torch.no_grad():
        total_loss = 0
        total_correct = 0
        for data, target in data_loader:
            data, target = data.to(device), target.to(device)

            output = model(data)

            loss = nll_loss(output, target)
            total_loss += float(loss)

            pred_target = output.argmax(dim=1)

            total_correct += int((pred_target == target).sum())

    avg_loss = total_loss / len(data_loader.dataset)
    accuracy = total_correct / len(data_loader.dataset)

    return avg_loss, accuracy
```

#### Define Objective Function

```bash
def objective_function_S(params):
    dropout_rate, learning_rate, conv_kernel_size, pool_kernel_size = params

    conv_kernel_size = int(conv_kernel_size)
    pool_kernel_size = int(pool_kernel_size)

    model = ModelS(dropout_rate=dropout_rate, conv_kernel_size=conv_kernel_size, pool_kernel_size=pool_kernel_size).to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

    n_epochs = 20
    patience = 5
    min_val_loss = float('inf')
    epochs_no_improve = 0

    for epoch in range(n_epochs):
        train_loss, train_accuracy = train(model, device, train_data_loader, optimizer)
        val_loss, val_accuracy = test(model, device, test_data_loader)

        # Check if validation loss has improved
        if val_loss < min_val_loss:
            min_val_loss = val_loss
            epochs_no_improve = 0
        else:
            epochs_no_improve += 1

        if epochs_no_improve >= patience:
            print(f"Early stopping at epoch {epoch+1}")
            break

    return min_val_loss
```

Define bound of search space (Unified for both Experiment and Production System)

```bash
# List of hyperparameters to optimize.
# For each hyperparameter, we specify:
# - The bounds within which values will be selected.
# - The corresponding parameter name as recognized by scikit-learn.
# - The sampling distribution to guide value selection.
#   For instance, the learning rate uses a 'log-uniform' distribution.

from skopt.space import Real, Integer, Categorical

search_space = [
    Real(0.1, 1, name='dropout_rate'),
    Real(0.0001, 10, name='learning_rate', prior='log-uniform'),

    Integer(1, 10, name='conv_kernel_size'),
    Integer(1, 3, name='pool_kernel_size'),
]
```

#### Optimize Experiment System

```bash
from scaleup_bo import SmallScaleOptimizer

small_optimizer = SmallScaleOptimizer(objective_function_S, search_space, n_steps=20, n_initial_points=1)

# Collect history from SmallScaleOptimizer
best_params_s = small_optimizer.best_params
best_hyperparameters = dict(zip(['dropout_rate', 'learning_rate', 'conv_kernel_size', 'pool_kernel_size'], best_params_s))
print("Best Hyperparameter of Small Model: ", best_hyperparameters)

X_iters_small = small_optimizer.X_iters
print('X_iters_small: ', X_iters_small)

Y_iters_small = small_optimizer.Y_iters
print('Y_iters_small: ', Y_iters_small)

```

#### Output
```bash
Best Hyperparameter of Small Model: {'dropout_rate': 0.46107083370527213, 'learning_rate': 0.0007872294922492846, 'conv_kernel_size': 3, 'pool_kernel_size': 1}

X_iters_small: array([[0.7212782130832402, 9.11909599279224, 8, 3],
       [0.1, 0.00010000000000000009, 1, 1],
       [0.17831151285271135, 0.0013001860006168898, 6, 2],
       [0.9567315586602373, 0.007821186315540811, 3, 1],
       [0.5977370337930041, 0.000179564534100882, 10, 3],
       [0.46107083370527213, 0.0007872294922492846, 3, 1],
       [0.26653819968237247, 4.922704457640138, 10, 3],
       [0.5625151004228182, 0.0027628620014393526, 1, 2],
       [0.6410323069524553, 0.007774471792101114, 6, 2],
       [0.45048454026714646, 0.003496367707371376, 3, 3],
       [0.36205892327355405, 0.03322512906660999, 5, 1]])

Y_iters_small: array([2.74909311e+00, 4.19949134e-03, 4.28927182e-03, 7.97836488e-03,
       5.17605326e-03, 3.61941135e-03, 5.52667749e+00, 5.05799869e-03,
       5.82460719e-03, 4.26776901e-03, 3.69501462e-02])
```

### Define the Production Model to optimize and the parameters are the same as Experiment System then define objective function to minimize using history leverage from Experiment System

#### Define Production Model

```bash
class ModelL(nn.Module):
    def __init__(self, dropout_rate=0.2, conv_kernel_size=1, pool_kernel_size=2):
        super(ModelL, self).__init__()
        self.features = nn.Sequential(
            nn.Conv2d(1, 32, kernel_size=conv_kernel_size, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=pool_kernel_size, stride=2),
            nn.Conv2d(32, 64, kernel_size=conv_kernel_size, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=pool_kernel_size, stride=2),
        )

        self._compute_linear_input_size()

        self.classifier = nn.Sequential(
            nn.Dropout(dropout_rate),
            nn.Linear(self.linear_input_size, 128),
            nn.ReLU(),
            nn.Dropout(dropout_rate),
            nn.Linear(128, 10),
            nn.LogSoftmax(dim=1),
        )

    def _compute_linear_input_size(self):
        with torch.no_grad():
            dummy_input = torch.zeros(1, 1, 28, 28)
            features_output = self.features(dummy_input)
            num_channels, height, width = features_output.size()[1:]
            self.linear_input_size = num_channels * height * width

    def forward(self, x):
        x = self.features(x)
        x = torch.flatten(x, 1)
        x = self.classifier(x)
        return x

# Transfer the model to the device that will perform the calculation.
modelL = ModelL().to(device)

# Create an Optimizer for ModelL
optimL = torch.optim.Adam(modelL.parameters())

```

#### Define Objective Function

```bash

def objective_function_L(params):
    dropout_rate, learning_rate, conv_kernel_size, pool_kernel_size = params

    conv_kernel_size = int(conv_kernel_size)
    pool_kernel_size = int(pool_kernel_size)

    modelL = ModelL(dropout_rate=dropout_rate, conv_kernel_size=conv_kernel_size, pool_kernel_size=pool_kernel_size).to(device)
    optimizer = torch.optim.Adam(modelL.parameters(), lr=learning_rate)

    n_epochs = 30
    patience = 5
    min_val_loss = float('inf')
    epochs_no_improve = 0

    for epoch in range(n_epochs):
        train_loss, train_accuracy = train(modelL, device, train_data_loader, optimizer)
        val_loss, val_accuracy = test(modelL, device, test_data_loader_L)

        # Check if validation loss has improved
        if val_loss < min_val_loss:
            min_val_loss = val_loss
            epochs_no_improve = 0
        else:
            epochs_no_improve += 1

        if epochs_no_improve >= patience:
            print(f"Early stopping at epoch {epoch+1}")
            break

    return min_val_loss
```

#### Optimize Production System

```bash
from scaleup_bo import LargeScaleOptimizer

large_optimizer = LargeScaleOptimizer(objective_function_L, search_space, best_params=best_params_s, X_iters_small=X_iters_small, Y_iters_small=Y_iters_small,  n_steps=10)

best_params_l = large_optimizer.best_params
best_hyperparameters_l = dict(zip(['dropout_rate', 'learning_rate', 'conv_kernel_size', 'pool_kernel_size'], best_params_s))
print("Best Hyperparameter of Large Model: ", best_hyperparameters_l)

best_score_l = large_optimizer.best_score
print("Best score of Large Model: ", best_score_l)
```

#### Output
```bash
Best Hyperparameter of Large Model: {'dropout_rate': 0.4585345500162007, 'learning_rate': 0.0004661314197784108, 'conv_kernel_size': 2, 'pool_kernel_size': 2}


```