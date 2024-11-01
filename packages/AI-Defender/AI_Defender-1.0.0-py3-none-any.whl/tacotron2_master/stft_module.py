import torch
import numpy as np
from scipy.signal import get_window
from librosa.filters import mel as librosa_mel_fn
import torch.nn.functional as F

class GionySTFT:
    def __init__(self, filter_length=1024, hop_length=256, win_length=1024, sampling_rate=22050, mel_fmin=0.0, mel_fmax=8000.0):
        self.filter_length = filter_length
        self.hop_length = hop_length
        self.win_length = win_length
        self.sampling_rate = sampling_rate
        self.mel_fmin = mel_fmin
        self.mel_fmax = mel_fmax

        # Create mel filter bank
        mel_basis = librosa_mel_fn(sr=sampling_rate, n_fft=filter_length, n_mels=80, fmin=mel_fmin, fmax=mel_fmax)
        self.mel_basis = torch.from_numpy(mel_basis).float()

        # STFT window
        window = get_window('hann', win_length, fftbins=True)
        self.stft_window = torch.from_numpy(window).float()

    def stft(self, y):
        """Compute the STFT of the input signal."""
        return torch.stft(y, n_fft=self.filter_length, hop_length=self.hop_length,
                          win_length=self.win_length, window=self.stft_window, return_complex=False)

    def mel_spectrogram(self, y):
        """Compute the mel-spectrogram from the input audio signal."""
        stft_output = self.stft(y)
        magnitude = torch.sqrt(stft_output.pow(2).sum(-1))

        mel_output = torch.matmul(self.mel_basis, magnitude)
        mel_output = torch.log(torch.clamp(mel_output, min=1e-5))
        return mel_output

# Dynamic range compression and decompression functions
def dynamic_range_compression(x, C=1, clip_val=1e-5):
    return torch.log(torch.clamp(x, min=clip_val) * C)

def dynamic_range_decompression(x, C=1):
    return torch.exp(x) / C
