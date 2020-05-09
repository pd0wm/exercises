#!/usr/bin/env python3
from tqdm import tqdm

from torchvision import datasets, transforms
from torch.utils.tensorboard import SummaryWriter


import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

from ignite.engine import Events, create_supervised_trainer, create_supervised_evaluator
from ignite.metrics import Accuracy, Loss


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 6, 3)
        self.conv2 = nn.Conv2d(6, 16, 3)

        self.fc1 = nn.Linear(16 * 5 * 5, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):
        batch_size = x.shape[0]

        # Input: 1 x 28 x 28, after conv2d: 6 x 26 x 26, after max pool: 6 x 13 x 13
        x = F.max_pool2d(F.relu(self.conv1(x)), 2)

        # Input: 6 x 13 x 13, after conv2d: 16 x 11 x 11, after max pool: 16 x 5 x 5
        x = F.max_pool2d(F.relu(self.conv2(x)), 2)

        # Flatten 16 x 5 x 5 into 1 x 400
        x = x.view(batch_size, -1)

        # Dense 400 -> 120
        x = F.relu(self.fc1(x))
        # Dense 120 -> 84
        x = F.relu(self.fc2(x))
        # Dense 84 -> 10
        x = F.softmax(self.fc3(x), 1)
        return x


if __name__ == "__main__":
    batch_size = 32

    device = torch.device("cuda")

    train_loader, val_loader = [
        torch.utils.data.DataLoader(
            datasets.MNIST('data', train=train, download=True, transform=transforms.ToTensor()),
            batch_size=batch_size, pin_memory=True, num_workers=4
        )
        for train in [True, False]
    ]

    model = Net()

    # Create writer
    writer = SummaryWriter()
    x, y = next(iter(train_loader))
    writer.add_graph(model, x)

    # Set up trainer & evaluator
    optimizer = optim.Adam(model.parameters(), lr=1e-4)
    loss_fn = F.nll_loss

    model = model.to(device)
    trainer = create_supervised_trainer(model, optimizer, loss_fn, device=device)
    evaluator = create_supervised_evaluator(
        model, metrics={"accuracy": Accuracy(), "nll": Loss(loss_fn)}, device=device
    )
    log_interval = 100

    @trainer.on(Events.ITERATION_COMPLETED(every=log_interval))
    def log_training_loss(engine):
        writer.add_scalar("training/loss", engine.state.output, engine.state.iteration)

    @trainer.on(Events.EPOCH_COMPLETED)
    def log_training_results(engine):
        evaluator.run(val_loader)
        metrics = evaluator.state.metrics
        print(f"Epoch: {engine.state.epoch}  Avg accuracy: {metrics['accuracy']:.2f}")
        writer.add_scalar("training/avg_accuracy", metrics['accuracy'], engine.state.epoch)

    trainer.run(train_loader, max_epochs=16)
