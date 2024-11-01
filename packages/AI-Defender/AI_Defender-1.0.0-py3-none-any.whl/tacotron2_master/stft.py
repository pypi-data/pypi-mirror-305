import sys
import os
import argparse
import torch
import torch.nn.functional as F
import numpy as np
from librosa.filters import mel as librosa_mel_fn
from scipy.signal import get_window
from torch.autograd import Variable
import random
import logging
from importlib import import_module
from .utils_audio import MAX_WAV_VALUE, files_to_list


sys.path.append(r"D:\ai\AI DEFENDER 2.1\tacotron2_master")

# Setup logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Define ArgumentParser instance before using it
parser = argparse.ArgumentParser()
parser.add_argument('-l', '--log_directory', type=str, help='Directory to save tensorboard logs', required=False)

def load_stft():
    stft_module = import_module('tacotron2_master.stft')
    return stft_module.GionySTFT()

# Utility function for padding
def pad_center(data, size, axis=-1):
    n = data.shape[axis]
    pad_size = size - n
    if pad_size < 0:
        raise ValueError("Target size must be larger than input size.")
    padding = [(0, 0)] * data.ndim
    padding[axis] = (pad_size // 2, pad_size - pad_size // 2)
    return np.pad(data, padding, mode='constant')

class GionySTFT(torch.nn.Module):
    def __init__(self, filter_length=1024, hop_length=256, win_length=1024,
                 sampling_rate=22050, mel_fmin=0.0, mel_fmax=None, window='hann',
                 use_dynamic_range_compression=False, use_normalization=True):
        super(GionySTFT, self).__init__()

        # Input validation
        if filter_length <= 0 or hop_length <= 0 or win_length <= 0:
            raise ValueError("filter_length, hop_length, and win_length must be positive integers.")
        if filter_length < win_length:
            raise ValueError("filter_length must be greater than or equal to win_length.")

        self.filter_length = filter_length
        self.hop_length = hop_length
        self.win_length = win_length
        self.window = window
        self.use_dynamic_range_compression = use_dynamic_range_compression
        self.use_normalization = use_normalization

        # Scale factor for the inverse transform
        scale = self.filter_length / self.hop_length

        # Create the Fourier basis
        fourier_basis = np.fft.fft(np.eye(self.filter_length))
        cutoff = int((self.filter_length / 2) + 1)
        fourier_basis = np.vstack([np.real(fourier_basis[:cutoff, :]), np.imag(fourier_basis[:cutoff, :])])

        # Convert to PyTorch tensors and reshape for convolution
        forward_basis = torch.FloatTensor(fourier_basis[:, None, :])
        inverse_basis = torch.FloatTensor(np.linalg.pinv(scale * fourier_basis).T[:, None, :])

        if window is not None:
            # Get window and zero-center pad it to filter_length
            fft_window = get_window(window, win_length, fftbins=True)
            fft_window = pad_center(fft_window, filter_length)
            fft_window = torch.from_numpy(fft_window).float()

            # Window the bases
            forward_basis *= fft_window
            inverse_basis *= fft_window

        # Register as buffers to ensure they are moved with the model to GPU/CPU
        self.register_buffer('forward_basis', forward_basis.float())
        self.register_buffer('inverse_basis', inverse_basis.float())

        # Create mel filter bank
        mel_fmax = mel_fmax or sampling_rate / 2
        mel_basis = librosa_mel_fn(
            sr=sampling_rate,
            n_fft=filter_length,
            n_mels=80,
            fmin=mel_fmin,
            fmax=mel_fmax
        )
        self.mel_basis = torch.from_numpy(mel_basis).float()

    def mel_spectrogram(self, y):
        """Compute the mel-spectrogram from the input audio signal."""
        # Normalize audio using MAX_WAV_VALUE
        audio_norm = y / MAX_WAV_VALUE
        stft_output = self.stft(audio_norm)
        magnitude = torch.sqrt(stft_output.real.pow(2) + stft_output.imag.pow(2))
        mel_output = torch.matmul(self.mel_basis, magnitude)
        return torch.log(torch.clamp(mel_output, min=1e-5))

    def stft(self, y):
        """Compute the STFT of the input signal."""
        fft_window = get_window(self.window, self.win_length, fftbins=True)
        stft_window = torch.from_numpy(pad_center(fft_window, self.filter_length)).float()
        return torch.stft(y, n_fft=self.filter_length, hop_length=self.hop_length,
                          win_length=self.win_length, window=stft_window, return_complex=True)

class Mel2Samp(torch.utils.data.Dataset):
    def __init__(self, training_files, segment_length, **audio_config):
        self.audio_files = files_to_list(training_files)
        random.seed(1234)
        random.shuffle(self.audio_files)

        self.segment_length = segment_length
        self.sampling_rate = audio_config["sampling_rate"]
        self.use_log_mel = audio_config.get("use_log_mel", True)
        self.compress_dynamic_range = audio_config.get("compress_dynamic_range", False)
        self.clip_val = audio_config.get("clip_val", 1e-5)

        # Initialize GionySTFT lazily within the method scope
        self.stft = self.initialize_stft(audio_config)

    def initialize_stft(self, audio_config):
        from tacotron2_master.stft import GionySTFT  # Lazy import
        return GionySTFT(
            filter_length=audio_config["filter_length"],
            hop_length=audio_config["hop_length"],
            win_length=audio_config["win_length"],
            sampling_rate=audio_config["sampling_rate"],
            mel_fmin=audio_config["mel_fmin"],
            mel_fmax=audio_config["mel_fmax"],
        )

    def get_mel(self, audio):
        audio_norm = audio / MAX_WAV_VALUE  # Normalize the audio using the defined constant
        audio_norm = audio_norm.unsqueeze(0)  # Add a channel dimension to make it suitable for STFT

        # Pass to the mel_spectrogram function
        melspec = self.stft.mel_spectrogram(audio_norm)
        melspec = torch.squeeze(melspec, 0)  # Remove the added dimension

        # Apply dynamic range compression if enabled
        if self.compress_dynamic_range:
            melspec = dynamic_range_compression(melspec, clip_val=self.clip_val)

        # Convert to log mel if enabled
        if self.use_log_mel:
            melspec = torch.log(torch.clamp(melspec, min=1e-5) * 1)

        return melspec

# Dynamic range compression function
def dynamic_range_compression(x, C=1, clip_val=1e-5):
    return torch.log(torch.clamp(x, min=clip_val) * C)

# Dynamic range decompression function
def dynamic_range_decompression(x, C=1):
    return torch.exp(x) / C

# Utility function for window sumsquare calculation
def window_sumsquare(window, n_frames, hop_length, win_length, n_fft, dtype=np.float32):
    window_fn = get_window(window, win_length, fftbins=True)
    window_fn = pad_center(window_fn, n_fft)
    window_fn = window_fn.astype(dtype)

    overlap_count = np.zeros(n_frames * hop_length + n_fft, dtype=dtype)
    for i in range(n_frames):
        start = i * hop_length
        end = start + n_fft
        overlap_count[start:end] += window_fn ** 2

    return overlap_count

class STFT(torch.nn.Module):
    """Implements the Short-Time Fourier Transform (STFT) and its inverse."""

    def __init__(self, filter_length=800, hop_length=200, win_length=800, window='hann', 
                 use_dynamic_range_compression=False, use_normalization=True):
        super(STFT, self).__init__()

        if filter_length <= 0 or hop_length <= 0 or win_length <= 0:
            raise ValueError("filter_length, hop_length, and win_length must be positive integers.")
        if filter_length < win_length:
            raise ValueError("filter_length must be greater than or equal to win_length.")

        self.filter_length = filter_length
        self.hop_length = hop_length
        self.win_length = win_length
        self.window = window
        self.use_dynamic_range_compression = use_dynamic_range_compression
        self.use_normalization = use_normalization

        # Scale factor for the inverse transform
        scale = self.filter_length / self.hop_length

        # Create the Fourier basis
        fourier_basis = np.fft.fft(np.eye(self.filter_length))
        cutoff = int((self.filter_length / 2) + 1)
        fourier_basis = np.vstack([np.real(fourier_basis[:cutoff, :]), np.imag(fourier_basis[:cutoff, :])])

        # Convert to PyTorch tensors and reshape for convolution
        forward_basis = torch.FloatTensor(fourier_basis[:, None, :])
        inverse_basis = torch.FloatTensor(np.linalg.pinv(scale * fourier_basis).T[:, None, :])

        if window is not None:
            fft_window = get_window(window, win_length, fftbins=True)
            fft_window = pad_center(fft_window, filter_length)
            fft_window = torch.from_numpy(fft_window).float()

            forward_basis *= fft_window
            inverse_basis *= fft_window

        self.register_buffer('forward_basis', forward_basis.float())
        self.register_buffer('inverse_basis', inverse_basis.float())

    def transform(self, input_data):
        """Computes the STFT of the input data.

        Args:
            input_data (torch.Tensor): The input audio data of shape (batch_size, num_samples).

        Returns:
            tuple: A tuple containing the magnitude and phase spectrograms.
        """
        if input_data.dim() != 2:
            raise ValueError("Input data should be of shape (batch_size, num_samples)")

        num_batches = input_data.size(0)
        num_samples = input_data.size(1)

        # Reflect-pad the input to handle edge effects
        input_data = input_data.view(num_batches, 1, num_samples)
        input_data = F.pad(
            input_data.unsqueeze(1),
            (int(self.filter_length / 2), int(self.filter_length / 2), 0, 0),
            mode='reflect'
        )
        input_data = input_data.squeeze(1)

        # Perform the convolution (STFT)
        forward_transform = F.conv1d(
            input_data, 
            Variable(self.forward_basis, requires_grad=False), 
            stride=self.hop_length, 
            padding=0
        )

        cutoff = int((self.filter_length / 2) + 1)
        real_part = forward_transform[:, :cutoff, :]
        imag_part = forward_transform[:, cutoff:, :]

        magnitude = torch.sqrt(real_part ** 2 + imag_part ** 2)
        phase = torch.atan2(imag_part, real_part)

        if self.use_dynamic_range_compression:
            magnitude = dynamic_range_compression(magnitude)

        return magnitude, phase

    def inverse(self, magnitude, phase):
        """Computes the inverse STFT from magnitude and phase spectrograms."""
        if magnitude.dim() != 3 or phase.dim() != 3:
            raise ValueError("Magnitude and phase should be of shape (batch_size, num_frequencies, n_frames)")
        if magnitude.size() != phase.size():
            raise ValueError("Magnitude and phase should have the same shape")

        if self.use_dynamic_range_compression:
            magnitude = dynamic_range_decompression(magnitude)

        recombine_magnitude_phase = torch.cat([magnitude * torch.cos(phase), magnitude * torch.sin(phase)], dim=1)

        inverse_transform = F.conv_transpose1d(recombine_magnitude_phase, Variable(self.inverse_basis, requires_grad=False), stride=self.hop_length, padding=0)

        if self.use_normalization and self.window is not None:
            window_sum = window_sumsquare(self.window, magnitude.size(-1), hop_length=self.hop_length, win_length=self.win_length, n_fft=self.filter_length, dtype=np.float32)
            approx_nonzero_indices = torch.from_numpy(np.where(window_sum > 1e-5)[0])
            window_sum = torch.from_numpy(window_sum).float()
            window_sum = window_sum.to(magnitude.device)
            inverse_transform[:, :, approx_nonzero_indices] /= window_sum[approx_nonzero_indices]

            inverse_transform *= float(self.filter_length) / self.hop_length

        start = int(self.filter_length / 2)
        inverse_transform = inverse_transform[:, :, start:]
        inverse_transform = inverse_transform[:, :, :-start]

        return inverse_transform

    def forward(self, input_data):
        """Performs the forward and inverse STFT transformations to reconstruct the audio signal."""
        input_data = input_data.to(self.forward_basis.device)

        magnitude, phase = self.transform(input_data)

        reconstruction = self.inverse(magnitude, phase)

        return reconstruction

if __name__ == "__main__":
    # Main code for running the STFT module directly
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)

    try:
        stft = GionySTFT()
        logger.info("Initialized GionySTFT successfully.")
        dummy_audio = torch.sin(2 * torch.pi * torch.linspace(0, 1, 22050)) * MAX_WAV_VALUE
        mel_spectrogram = stft.mel_spectrogram(dummy_audio)
        logger.info(f"Mel spectrogram shape: {mel_spectrogram.shape}")
    except Exception as e:
        logger.error(f"Error occurred while running GionySTFT: {e}")
