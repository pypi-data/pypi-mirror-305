from torch import nn
import torch.nn as nn

class Tacotron2Loss(nn.Module):
    def __init__(self):
        super(Tacotron2Loss, self).__init__()

    def forward(self, model_output, targets):
        # Extract targets
        mel_target, gate_target = targets[0], targets[1]

        # Ensure that the gradients are not computed for the target
        mel_target.requires_grad = False
        gate_target.requires_grad = False
        gate_target = gate_target.view(-1, 1)

        # Extract model outputs
        mel_out, mel_out_postnet, gate_out, _ = model_output
        gate_out = gate_out.view(-1, 1)

        # Compute losses
        # Mean Squared Error loss for mel-spectrogram prediction
        mel_loss = nn.MSELoss()(mel_out, mel_target) + \
            nn.MSELoss()(mel_out_postnet, mel_target)

        # Binary Cross Entropy with Logits for gate prediction
        gate_loss = nn.BCEWithLogitsLoss()(gate_out, gate_target)

        # Total loss is the sum of mel and gate losses
        total_loss = mel_loss + gate_loss
        return total_loss
