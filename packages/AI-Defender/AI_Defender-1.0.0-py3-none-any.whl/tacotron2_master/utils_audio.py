# utils_audio.py
import torch
import numpy as np
from scipy.io.wavfile import read

def files_to_list(filename):
    with open(filename, 'r') as f:
        files = f.readlines()
    return [x.strip() for x in files]

MAX_WAV_VALUE = 32768.0

def load_wav_to_torch(full_path):
    sampling_rate, data = read(full_path)
    return torch.FloatTensor(data.astype(np.float32)), sampling_rate

def dynamic_range_compression(x, C=1, clip_val=1e-5):
    """
    Apply dynamic range compression.
    """
    return torch.log(torch.clamp(x, min=clip_val) * C)

def dynamic_range_decompression(x, C=1):
    """
    Apply dynamic range decompression.
    """
    return torch.exp(x) / C

def get_mask_from_lengths(lengths):
    """
    Creates a mask for padding based on sequence lengths.
    """
    max_len = torch.max(lengths).item()
    ids = torch.arange(0, max_len, out=torch.cuda.LongTensor(max_len))
    mask = (ids < lengths.unsqueeze(1)).bool()
    return mask
# utils_audio.py

def files_to_list(filename):
    with open(filename, 'r') as f:
        files = f.read().splitlines()
    return files
