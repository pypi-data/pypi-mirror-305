import torch
import numpy as np
import torch.nn.functional as F
from scipy.signal import get_window
from librosa.util import pad_center, tiny
import os

# Add the correct path where utils_imports.py is located
import sys
utils_path = "D:/ai/AI DEFENDER 2.1/tacotron2_master"
if os.path.exists(utils_path):
    sys.path.append(utils_path)  # Adjust this path accordingly

# Import the required functions from utils_imports.py
try:
    from utils_imports import dynamic_range_compression, dynamic_range_decompression, window_sumsquare
except ImportError as e:
    print(f"Error importing from utils_imports: {e}")
    # Use the local fallback implementations if import fails

    def dynamic_range_compression(x, C=1, clip_val=1e-5):
        """
        Applies dynamic range compression to the input tensor `x`.
        """
        return torch.log(torch.clamp(x, min=clip_val) * C)

    def dynamic_range_decompression(x, C=1):
        """
        Reverts dynamic range compression.
        """
        return torch.exp(x) / C

    def window_sumsquare(window, n_frames, hop_length=200, win_length=800, n_fft=800, dtype=np.float32, norm=None):
        """
        Computes the sum-square envelope of a window function.
        """
        # Your window_sumsquare logic here
        pass

# Utility functions that should also be in utils_custom.py
def to_gpu(tensor):
    """Moves tensor to GPU if available."""
    return tensor.cuda() if torch.cuda.is_available() else tensor

def get_mask_from_lengths(lengths):
    """Creates a binary mask to prevent attention on padding."""
    max_len = torch.max(lengths).item()
    mask = torch.arange(max_len).expand(len(lengths), max_len) < lengths.unsqueeze(1)
    return mask

# Your main code logic continues below with dynamic range compression and decompression functions available
