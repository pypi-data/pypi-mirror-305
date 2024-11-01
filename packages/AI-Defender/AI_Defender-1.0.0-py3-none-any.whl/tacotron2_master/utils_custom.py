import torch
import numpy as np
import soundfile as sf

# Function to load wav file and return as tensor
def load_wav_to_torch(full_path):
    """Loads a .wav file and returns a torch tensor."""
    data, sampling_rate = sf.read(full_path)
    return torch.FloatTensor(data), sampling_rate

# Function to load filepaths and text
def load_filepaths_and_text(filename, delimiter="|"):
    """Reads a file and returns list of file paths and text"""
    with open(filename, encoding='utf-8') as f:
        filepaths_and_text = [line.strip().split(delimiter) for line in f]
    return filepaths_and_text

def dynamic_range_compression(x, C=1, clip_val=1e-5):
    """Applies dynamic range compression to the input tensor."""
    return torch.log(torch.clamp(x, min=clip_val) * C)

def dynamic_range_decompression(x, C=1):
    """Reverts dynamic range compression."""
    return torch.exp(x) / C

def window_sumsquare(window, n_frames, hop_length=200, win_length=800, n_fft=800, dtype=np.float32, norm=None):
    """Computes the sum-square envelope of a window function."""
    pass

def to_gpu(tensor):
    """Moves tensor to GPU if available."""
    return tensor.cuda() if torch.cuda.is_available() else tensor

def get_mask_from_lengths(lengths):
    """Creates a binary mask to prevent attention on padding."""
    max_len = torch.max(lengths).item()
    mask = torch.arange(max_len).expand(len(lengths), max_len) < lengths.unsqueeze(1)
    return mask
