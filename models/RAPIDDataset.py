from typing import Tuple
import torch as t
from torch.utils.data import Dataset


class RAPIDDataset(Dataset):
    """
    TODO:
    - fold in all data loading, preprocessing and reshaping.
    - train/val/test split.
    """

    def __init__(self, X: t.Tensor, Y: t.Tensor, device: str):
        super().__init__()
        self.X = X[0].double()
        self.X1 = X[1].double()
        self.Y = Y.double()
        self.device = device

    def __len__(self) -> int:
        return len(self.X)

    def __getitem__(self, ix: int) -> Tuple[Tuple[t.Tensor, t.Tensor], t.Tensor]:
        return (self.X[ix].to(self.device), self.X1[ix].to(self.device)), self.Y[ix].to(self.device)