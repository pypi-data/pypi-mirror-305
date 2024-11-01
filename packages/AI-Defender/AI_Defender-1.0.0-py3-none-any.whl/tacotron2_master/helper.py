import torch
import numpy as np
from scipy.io.wavfile import read
import os

if os.name != 'nt':  # Only import 'grp' if the OS is not Windows
    import grp

def process_data():
    """
    Example function to process the input data.
    """
    pass  # Your logic for process_data

def to_gpu(x):
    """
    Transfer data to GPU if CUDA is available.
    """
    x = x.contiguous()
    if torch.cuda.is_available():
        x = x.cuda(non_blocking=True)
    return torch.autograd.Variable(x)

def get_mask_from_lengths(lengths):
    """
    Generates a mask based on the lengths of sequences, used for padding handling.
    """
    max_len = torch.max(lengths).item()
    ids = torch.arange(0, max_len, out=torch.cuda.LongTensor(max_len))
    mask = (ids < lengths.unsqueeze(1)).bool()
    return mask

def load_wav_to_torch(full_path):
    """
    Load a waveform from a file and convert it to a PyTorch tensor.
    """
    sampling_rate, data = read(full_path)
    return torch.FloatTensor(data.astype(np.float32)), sampling_rate

def load_filepaths_and_text(filename, split="|"):
    """
    Loads file paths and corresponding text from a given file, used for data processing pipelines.
    """
    with open(filename, encoding='utf-8') as f:
        filepaths_and_text = [line.strip().split(split) for line in f]
    return filepaths_and_text
