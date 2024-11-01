import torch
import torch.nn.functional as F
import numpy as np
import librosa
from scipy.signal import get_window
import os
import sys
import random
import torch.utils.data
import json
import logging
import argparse
from utils_audio import files_to_list, MAX_WAV_VALUE, load_wav_to_torch
from pydub import AudioSegment

# Logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class GionySTFT:
    def __init__(self, filter_length=1024, hop_length=256, win_length=1024, sampling_rate=22050, mel_fmin=0.0, mel_fmax=8000.0):
        self.filter_length = filter_length
        self.hop_length = hop_length
        self.win_length = win_length
        self.sampling_rate = sampling_rate
        self.mel_fmin = mel_fmin
        self.mel_fmax = mel_fmax

        # Set up the mel filter bank
        mel_basis = librosa.filters.mel(sr=sampling_rate, n_fft=filter_length, n_mels=80, fmin=mel_fmin, fmax=mel_fmax)
        self.mel_basis = torch.from_numpy(mel_basis).float()

        # Set up the STFT window
        window = get_window('hann', win_length, fftbins=True)
        self.stft_window = torch.from_numpy(window).float()

    def mel_spectrogram(self, audio):
        """
        Computes the mel-spectrogram from an audio signal.
        :param audio: Input audio tensor
        :return: Mel-spectrogram tensor
        """
        # Compute the Short-Time Fourier Transform (STFT)
        stft_matrix = self.stft(audio)
        
        # Apply the mel filter bank
        magnitude = torch.abs(stft_matrix)
        mel_output = torch.matmul(self.mel_basis, magnitude)
        
        # Convert to decibels
        mel_spectrogram = 20 * torch.log10(torch.clamp(mel_output, min=1e-5))
        return mel_spectrogram

    def stft(self, audio):
        """
        Computes the Short-Time Fourier Transform (STFT) of the input audio.
        :param audio: Input audio tensor
        :return: STFT matrix
        """
        # Pad the window if necessary
        pad = (self.filter_length - self.hop_length) // 2
        audio = F.pad(audio.unsqueeze(0), (pad, pad), mode='reflect').squeeze(0)

        # Perform STFT using PyTorch
        stft_matrix = torch.stft(audio, n_fft=self.filter_length, hop_length=self.hop_length,
                                 win_length=self.win_length, window=self.stft_window,
                                 center=False, return_complex=True)
        return stft_matrix

# Example usage of GionySTFT
if __name__ == "__main__":
    audio_path = "path_to_audio_file.wav"
    audio, sr = load_wav_to_torch(audio_path)
    giony_stft = GionySTFT()
    mel_spectrogram = giony_stft.mel_spectrogram(audio)
    print("Mel-spectrogram shape:", mel_spectrogram.shape)
