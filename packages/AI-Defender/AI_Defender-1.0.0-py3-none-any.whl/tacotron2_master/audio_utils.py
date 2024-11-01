import torch
import numpy as np

# Function to compute the sum-square envelope of a window function
def window_sumsquare(window, n_frames, hop_length=200, win_length=800, n_fft=800, dtype=np.float32, norm=None):
    """
    Compute the sum-square envelope of a window function at a given hop length.

    Parameters:
    ----------
    window : numpy.ndarray or callable
        The window function or array to use.
    n_frames : int
        Number of frames for which to compute the sum-square envelope.
    hop_length : int
        The hop length.
    win_length : int
        The length of the window.
    n_fft : int
        The FFT size.
    dtype : data-type
        The desired data type for the output.
    norm : {None, 'ortho'}
        Normalization mode.

    Returns:
    -------
    np.ndarray
        Sum-square envelope of the window function.
    """
    if win_length is None:
        win_length = n_fft

    n = n_fft + hop_length * (n_frames - 1)
    x = np.zeros(n, dtype=dtype)

    win_sq = np.hanning(win_length)  # Assuming a Hann window for simplicity
    pad_amount = (n_fft - len(win_sq)) // 2
    win_sq = np.pad(win_sq, (pad_amount, n_fft - len(win_sq) - pad_amount), mode='constant')

    for i in range(n_frames):
        sample = i * hop_length
        x[sample:min(n, sample + n_fft)] += win_sq[:max(0, min(n_fft, n - sample))]

    return x

# Function to apply dynamic range compression
def dynamic_range_compression(x, C=1, clip_val=1e-5):
    """
    Apply dynamic range compression.

    Parameters:
    ----------
    x : torch.Tensor
        The input tensor to compress.
    C : float
        Constant for scaling the dynamic range.
    clip_val : float
        Clipping value to avoid taking the logarithm of zero.

    Returns:
    -------
    torch.Tensor
        The compressed tensor.
    """
    return torch.log(torch.clamp(x, min=clip_val) * C)

# Function to apply dynamic range decompression
def dynamic_range_decompression(x, C=1):
    """
    Apply dynamic range decompression.

    Parameters:
    ----------
    x : torch.Tensor
        The input tensor to decompress.
    C : float
        Constant used during compression.

    Returns:
    -------
    torch.Tensor
        The decompressed tensor.
    """
    return torch.exp(x) / C
