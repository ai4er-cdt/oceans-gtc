import os

import numpy as np
import torch as t
import torch.nn as nn
from torch.utils.data import DataLoader
import matplotlib.pyplot as plt
from itertools import cycle
from tqdm import trange
from models import SimDataset


parent_dir = os.path.dirname(os.path.abspath("train.py"))
t.manual_seed(123456)

# default hyperparameters
batch_size = 32
max_iters = 2500
lr = 1e-3
# ---------------


def train_model(
    model: nn.Module,
    name: str,
    X: np.ndarray,
    y: np.ndarray,
    X_val: np.ndarray,
    y_val: np.ndarray,
    val_interval: 5,
    save_dir: str,
    device: str | None = None,
):

    if device == None:
        device = "cuda" if t.cuda.is_available() else "cpu"
    print(f"device: {device}")

    # print number of parameters
    print(f"{sum([p.numel() for p in model.parameters()])} parameters.")

    # get training data
    train_dataset = SimDataset.SimDataset(X, y, device)
    train_DL = DataLoader(train_dataset, batch_size, shuffle=True)
    data_iterator = cycle(train_DL)

    # get validation data
    if X_val is not None:
        best_val_loss = float("inf")
        valid_dataset = SimDataset.SimDataset(X_val, y_val, device)
        valid_DL = DataLoader(valid_dataset, 1, shuffle=False)

    # training
    model.train()
    criterion = nn.MSELoss()
    opt = t.optim.AdamW(model.parameters(), lr=lr)
    full_loss = []
    for iter in trange(max_iters):
        # use dataloader to sample a batch
        x, y = next(data_iterator)
        # update model
        out = model(x)
        loss = criterion(out.squeeze(-1), y)
        full_loss.append(loss.item())
        opt.zero_grad(set_to_none=True)
        loss.backward()
        opt.step()

        # Validation check
        if X_val is not None and iter % val_interval == 0:
            model.eval()
            with t.no_grad():
                val_loss = 0
                for val_x, val_y in valid_DL:
                    val_out = model(val_x)
                    val_loss += criterion(val_out.squeeze(-1), val_y).item()
                val_loss /= len(valid_DL)

                if val_loss < best_val_loss:
                    best_val_loss = val_loss
                    wait = 0
                else:
                    wait += 1
                    if wait >= 5:
                        print(
                            f"Stopping early at iteration {iter}. Best validation loss: {best_val_loss}"
                        )
                        break
            model.train()

    t.save(
        model.state_dict(),
        os.path.join(parent_dir, f"{save_dir}/saved_models/{name}.pt"),
    )

    fig, ax = plt.subplots(figsize=(10, 3))
    ax.plot(full_loss, linestyle="--", color="red", alpha=0.5)
    ax.set_ylabel("MSE")
    ax.set_xlabel("Training Step")
    ax.set_title(f"{name}: Loss")
    plt.savefig(os.path.join(parent_dir, f"{save_dir}/loss_curves/{name}.png"), dpi=400)
    plt.show()
    plt.close()

    print(f"final loss: {loss.item()}")
    print(f"model saved to {save_dir}/saved_models/{name}.pt")
    print(f"loss curve saved to {save_dir}/loss_curves/{name}.png")

    return full_loss


def predict(
    model: nn.Module,
    name: str,
    X: np.ndarray,
    y: np.ndarray,
    save_dir: str,
    device: str | None = None,
):

    if device == None:
        device = "cuda" if t.cuda.is_available() else "cpu"
    print(f"device: {device}")

    # get training data
    test_dataset = SimDataset.SimDataset(X, y, device)
    test_DL = DataLoader(test_dataset, 1, shuffle=False)

    y_pred = []

    # training
    model.eval()
    with t.no_grad():
        for x, y in test_DL:
            outputs = model(x)
            y_pred.extend(outputs.cpu().numpy())

    return y_pred
