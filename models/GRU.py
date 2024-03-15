from typing import Any, Optional

import torch as t
import torch.nn as nn
import torch.nn.functional as F


class GRUcell(nn.Module):
    def __init__(self,
                 n_inputs: int,
                 n_outputs: int,
                 d_hidden: int,
                 dropout: float=0.2,
                 device: str="cpu"):
        super().__init__()
        self.device = device
        self.d_hidden = d_hidden
        self.n_outputs = n_outputs
        self.dpout = nn.Dropout(dropout)

        self.i2h = nn.Linear(n_inputs+d_hidden, d_hidden)
        self.i2u = nn.Linear(n_inputs+d_hidden, d_hidden)
        self.i2r = nn.Linear(n_inputs+d_hidden, d_hidden)
        self.h2o = nn.Linear(d_hidden, n_outputs)

        self.hbn = nn.BatchNorm1d(d_hidden)
        self.ubn = nn.BatchNorm1d(d_hidden)
        self.rbn = nn.BatchNorm1d(d_hidden)
        
    def forward(self, X) -> Any:
        """
        X: (batch_size, n_seq, n_inputs)
        """
        X = self.dpout(X)
        hidden = t.zeros(X.shape[0], self.d_hidden, requires_grad=False).to(self.device)
        # reshape X to (n_seq, batch_size, n_inputs)
        X = X.transpose(0, 1)
        out = t.zeros(X.shape[0], X.shape[1], self.n_outputs, requires_grad=False).to(self.device)
        for i in range(X.shape[0]):
            combined = t.cat([X[i], hidden], dim=-1)
            update = F.sigmoid(self.ubn(self.i2u(combined)))
            reset = F.sigmoid(self.rbn(self.i2r(combined)))
            combined = t.cat([X[i], reset*hidden], dim=-1)
            candidate_hidden = F.tanh(self.hbn(self.i2h(combined)))
            hidden = (1-update)*candidate_hidden + update*hidden
            out[i] = F.tanh(self.h2o(hidden))
        return out.transpose(0, 1)

class GRU(nn.Module):
    def __init__(self,
                 n_inputs: int,
                 n_outputs: int,
                 n_layers: int,
                 d_hidden: int,
                 d_model: Optional[int],
                 dropout: float=0.2,
                 device: str="cpu"):
        super().__init__()
        assert n_layers > 0
        d_model = d_hidden if d_model is None else d_model
        layers = []
        for _ in range(n_layers):
            block = GRUcell(n_inputs, d_model, d_hidden, dropout, device)
            n_inputs = block.n_outputs
            layers.append(block)
        self.layers = nn.Sequential(*layers)     
        self.ln_out = nn.Linear(n_inputs, n_outputs)   

    def forward(self, X) -> Any:
        out = self.layers(X)
        out = self.ln_out(out[:, -1, :])
        return out