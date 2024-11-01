import torch
import numpy as np
from scipy.io.wavfile import read
from scipy.signal import get_window  # Import get_window for different window types
import logging
import sys
import os

log_level = os.getenv('LOG_LEVEL', 'DEBUG').upper()
logging.basicConfig(level=log_level, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('Starting utils.py')

# Function to apply dynamic range compression
def dynamic_range_compression(x, C=1, clip_val=1e-5):
    return torch.log(torch.clamp(x, min=clip_val) * C)

# Function to apply dynamic range decompression
def dynamic_range_decompression(x, C=1):
    return torch.exp(x) / C

# Function to compute the sum-square envelope of a window function
def window_sumsquare(window_type='hann', n_frames=100, hop_length=200, win_length=800, n_fft=800, dtype=np.float32, norm=None):
    if win_length is None:
        win_length = n_fft

    n = n_fft + hop_length * (n_frames - 1)
    x = np.zeros(n, dtype=dtype)

    win_sq = get_window(window_type, win_length) ** 2  # Allows different windows (e.g., 'hann', 'hamming')
    pad_amount = (n_fft - len(win_sq)) // 2
    win_sq = np.pad(win_sq, (pad_amount, n_fft - len(win_sq) - pad_amount), mode='constant')

    for i in range(n_frames):
        sample = i * hop_length
        x[sample:min(n, sample + n_fft)] += win_sq[:max(0, min(n_fft, n - sample))]

    return x

# Function to load a waveform from a WAV file
def load_wav_to_torch(full_path):
    sampling_rate, data = read(full_path)
    return torch.FloatTensor(data.astype(np.float32)), sampling_rate

# Function to load file paths and corresponding text from a file
def load_filepaths_and_text(filename, split="|"):
    with open(filename, encoding='utf-8') as f:
        filepaths_and_text = [line.strip().split(split) for line in f]
    return filepaths_and_text

# Function to generate a mask from lengths of sequences
def get_mask_from_lengths(lengths):
    max_len = torch.max(lengths).item()
    device = lengths.device
    ids = torch.arange(0, max_len, device=device, dtype=torch.long)
    mask = (ids < lengths.unsqueeze(1)).bool()
    return mask

# Function to move tensors to GPU if available
def to_gpu(x):
    """
    Move tensor to GPU if available.

    Args:
        x (torch.Tensor): The input tensor.

    Returns:
        torch.autograd.Variable: Tensor moved to GPU if available.
    """
    x = x.contiguous()
    if torch.cuda.is_available() and not x.is_cuda:
        x = x.cuda(non_blocking=True)
    return torch.autograd.Variable(x)

    return torch.autograd.Variable(x)

# Append the module path if it's not already present in sys.path
sys.path.append(r"C:\Users\giony\Desktop\AI DEFENDER 2.1")

# Logging setup
logging.basicConfig(level=logging.DEBUG)
logging.debug('Starting utils.py')

# Expose core functions when package is imported
__all__ = [
    'dynamic_range_compression',
    'dynamic_range_decompression',
    'window_sumsquare',
    'load_wav_to_torch',
    'load_filepaths_and_text',
    'get_mask_from_lengths',
    'to_gpu'
]
