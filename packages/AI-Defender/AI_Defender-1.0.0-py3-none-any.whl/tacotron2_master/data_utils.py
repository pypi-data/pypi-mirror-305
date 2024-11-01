import sys
import os
import random
import numpy as np
import torch
import torch.utils.data
from typing import Optional

# Adding the path to ensure the tacotron2_master modules can be imported
sys.path.append(os.path.abspath('D:/ai/AI DEFENDER 2.1'))

# Importing necessary modules after ensuring package structure
from .layers import ConvNorm, LinearNorm, GionySTFT
from .cmudict import CMUDict
from .text_processing import text_to_sequence
from .utils_custom import load_wav_to_torch, load_filepaths_and_text


# GionySTFT class for handling STFT
class GionySTFT:
    def __init__(self, filter_length: int, hop_length: int, win_length: int, 
                 n_fft: Optional[int] = None, sampling_rate: Optional[int] = None, 
                 mel_fmin: Optional[float] = None, mel_fmax: Optional[float] = None):
        self.filter_length = filter_length
        self.hop_length = hop_length
        self.win_length = win_length
        self.n_fft = n_fft
        self.sampling_rate = sampling_rate
        self.mel_fmin = mel_fmin
        self.mel_fmax = mel_fmax


# HParams class for storing hyperparameters
class HParams:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


# Define the TextMelLoader class
class TextMelLoader(torch.utils.data.Dataset):
    """
    Loads audio and text pairs, normalizes text, and computes mel-spectrograms from audio files.
    """
    def __init__(self, audiopaths_and_text, hparams):
        # Specify the file path for the CMUDict dictionary
        cmudict_path = 'D:/ai/AI DEFENDER 2.1/tacotron2_master/cmudict.txt'  # Replace with the correct path if different
        self.cmudict = CMUDict(cmudict_path)  # Initialize CMUDict with the required file path
        
        self.audiopaths_and_text = load_filepaths_and_text(audiopaths_and_text)
        self.text_cleaners = hparams.text_cleaners
        self.max_wav_value = hparams.max_wav_value
        self.sampling_rate = hparams.sampling_rate
        self.load_mel_from_disk = hparams.load_mel_from_disk

        # Create an instance of GionySTFT using hparams
        self.stft = GionySTFT(
            filter_length=hparams.filter_length,
            hop_length=hparams.hop_length,
            win_length=hparams.win_length,
            n_fft=hparams.n_fft,
            sampling_rate=hparams.sampling_rate,
            mel_fmin=hparams.mel_fmin,
            mel_fmax=hparams.mel_fmax
        )
        
        # Example of using ConvNorm (adding a convolution layer)
        self.conv_layer = ConvNorm(in_channels=1, out_channels=16, kernel_size=3, stride=1, padding=1)
        
        # Example of using LinearNorm (adding a linear layer)
        self.linear_layer = LinearNorm(in_dim=128, out_dim=64)  # Hypothetical input and output dimensions
        
        random.seed(hparams.seed)
        random.shuffle(self.audiopaths_and_text)

    def get_mel_text_pair(self, audiopath_and_text):
        audiopath, text = audiopath_and_text[0], audiopath_and_text[1]
        text = self.get_text(text)
        mel = self.get_mel(audiopath)

        # Example of applying the convolution to mel spectrogram
        mel = mel.unsqueeze(0)  # Add a channel dimension to match ConvNorm requirements
        mel = self.conv_layer(mel)  # Apply the convolution
        mel = mel.squeeze(0)  # Remove the channel dimension

        # Example of applying LinearNorm to processed mel spectrogram
        mel_flat = mel.view(-1, 128)  # Reshape to match expected input dimension (dummy example)
        mel = self.linear_layer(mel_flat)  # Apply the linear layer

        return (text, mel)

    def get_mel(self, filename):
        if not self.load_mel_from_disk:
            audio, sampling_rate = load_wav_to_torch(filename)
            if sampling_rate != self.stft.sampling_rate:
                raise ValueError(f"{sampling_rate} SR doesn't match target {self.stft.sampling_rate} SR")
            audio_norm = audio / self.max_wav_value
            audio_norm = audio_norm.unsqueeze(0)
            audio_norm = torch.autograd.Variable(audio_norm, requires_grad=False)
            melspec = self.stft.mel_spectrogram(audio_norm)
            melspec = torch.squeeze(melspec, 0)
        else:
            melspec = torch.from_numpy(np.load(filename))
            assert melspec.size(0) == self.stft.n_fft, (
                f'Mel dimension mismatch: given {melspec.size(0)}, expected {self.stft.n_fft}'
            )

        return melspec

    def get_text(self, text):
        # Using CMUDict to enhance text processing for better pronunciation
        if self.cmudict is not None:
            text = self.cmudict.lookup(text) or text
        text_norm = torch.IntTensor(text_to_sequence(text, self.text_cleaners))
        return text_norm

    def __getitem__(self, index):
        return self.get_mel_text_pair(self.audiopaths_and_text[index])

    def __len__(self):
        return len(self.audiopaths_and_text)


# TextMelCollate class for padding
class TextMelCollate:
    """Zero-pads model inputs and targets based on the number of frames per step."""
    def __init__(self, n_frames_per_step):
        self.n_frames_per_step = n_frames_per_step

    def __call__(self, batch):
        input_lengths, ids_sorted_decreasing = torch.sort(
            torch.LongTensor([len(x[0]) for x in batch]), dim=0, descending=True
        )
        max_input_len = input_lengths[0]

        text_padded = torch.LongTensor(len(batch), max_input_len)
        text_padded.zero_()
        for i in range(len(ids_sorted_decreasing)):
            text = batch[ids_sorted_decreasing[i]][0]
            text_padded[i, :text.size(0)] = text

        num_mels = batch[0][1].size(0)
        max_target_len = max([x[1].size(1) for x in batch])
        if max_target_len % self.n_frames_per_step != 0:
            max_target_len += self.n_frames_per_step - max_target_len % self.n_frames_per_step
            assert max_target_len % self.n_frames_per_step == 0

        mel_padded = torch.FloatTensor(len(batch), num_mels, max_target_len)
        mel_padded.zero_()
        gate_padded = torch.FloatTensor(len(batch), max_target_len)
        gate_padded.zero_()
        output_lengths = torch.LongTensor(len(batch))
        for i in range(len(ids_sorted_decreasing)):
            mel = batch[ids_sorted_decreasing[i]][1]
            mel_padded[i, :, :mel.size(1)] = mel
            gate_padded[i, mel.size(1) - 1:] = 1
            output_lengths[i] = mel.size(1)

        return text_padded, input_lengths, mel_padded, gate_padded, output_lengths


# Example instantiation to verify if everything works fine
try:
    hparams = HParams(
        filter_length=1024,
        hop_length=256,
        win_length=1024,
        n_fft=1024,
        sampling_rate=22050,
        mel_fmin=0.0,
        mel_fmax=8000.0,
        max_wav_value=32768.0,
        text_cleaners=["english_cleaners"],
        seed=1234,
        load_mel_from_disk=False
    )

    text_mel_loader = TextMelLoader(audiopaths_and_text=[("sample_audio_path.wav", "sample text")], hparams=hparams)
    print("TextMelLoader instantiated successfully.")
except Exception as e:
    print(f"Error during instantiation: {e}")
