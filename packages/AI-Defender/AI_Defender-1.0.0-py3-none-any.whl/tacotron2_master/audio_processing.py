import torch
from librosa.filters import mel as librosa_mel_fn
from tacotron2_master.stft import STFT  # Use relative import based on the package structure
import logging
import numpy as np

# Logging setup
logging.basicConfig(level=logging.DEBUG)
logging.debug('Starting audio_processing.py')

# Define the LinearNorm class
class LinearNorm(torch.nn.Module):
    def __init__(self, in_dim, out_dim, bias=True, w_init_gain='linear'):
        super(LinearNorm, self).__init__()
        self.linear_layer = torch.nn.Linear(in_dim, out_dim, bias=bias)
        torch.nn.init.xavier_uniform_(
            self.linear_layer.weight,
            gain=torch.nn.init.calculate_gain(w_init_gain)
        )

    def forward(self, x):
        return self.linear_layer(x)

# Define the ConvNorm class
class ConvNorm(torch.nn.Module):
    def __init__(self, in_channels, out_channels, kernel_size=1, stride=1,
                 padding=None, dilation=1, bias=True, w_init_gain='linear'):
        super(ConvNorm, self).__init__()
        if padding is None:
            assert kernel_size % 2 == 1
            padding = int(dilation * (kernel_size - 1) / 2)

        self.conv = torch.nn.Conv1d(in_channels, out_channels,
                                    kernel_size=kernel_size, stride=stride,
                                    padding=padding, dilation=dilation,
                                    bias=bias)
        torch.nn.init.xavier_uniform_(
            self.conv.weight, gain=torch.nn.init.calculate_gain(w_init_gain)
        )

    def forward(self, signal):
        return self.conv(signal)

# Define the GionySTFT class
class GionySTFT(torch.nn.Module):
    def __init__(self, filter_length=1024, hop_length=256, win_length=1024,
                 n_mel_channels=80, sampling_rate=22050, mel_fmin=0.0,
                 mel_fmax=8000.0):
        super(GionySTFT, self).__init__()
        self.n_mel_channels = n_mel_channels
        self.sampling_rate = sampling_rate
        self.stft_fn = STFT(filter_length, hop_length, win_length)
        mel_basis = librosa_mel_fn(
            sr=sampling_rate, n_fft=filter_length, n_mels=n_mel_channels,
            fmin=mel_fmin, fmax=mel_fmax
        )
        mel_basis = torch.from_numpy(mel_basis).float()
        self.register_buffer('mel_basis', mel_basis)

    def mel_spectrogram(self, y):
        """Computes mel-spectrograms from a batch of waves
        PARAMS
        ------
        y: torch.FloatTensor with shape (B, T) in range [-1, 1]

        RETURNS
        -------
        mel_output: torch.FloatTensor of shape (B, n_mel_channels, T)
        """
        assert torch.min(y.data) >= -1
        assert torch.max(y.data) <= 1

        magnitudes, _ = self.stft_fn.transform(y)
        mel_output = torch.matmul(self.mel_basis, magnitudes.data)
        return mel_output

# Testing LinearNorm, ConvNorm, and GionySTFT classes
def test_LinearNorm():
    lin_layer = LinearNorm(10, 5)
    input_tensor = torch.randn(3, 10)
    output = lin_layer(input_tensor)
    logging.debug(f"LinearNorm output: {output}")

def test_ConvNorm():
    conv_layer = ConvNorm(3, 5, kernel_size=3)
    input_tensor = torch.randn(3, 3, 10)
    output = conv_layer(input_tensor)
    logging.debug(f"ConvNorm output: {output}")

def test_GionySTFT():
    giony_stft = GionySTFT()
    input_waveform = torch.randn(10, 16000)  # Generate random waveforms
    input_waveform = input_waveform / input_waveform.abs().max()  # Scale to [-1, 1]

    # Log the min and max values of the input_waveform
    logging.debug(f"Input waveform min: {input_waveform.min().item()}, max: {input_waveform.max().item()}")

    mel_spectrogram = giony_stft.mel_spectrogram(input_waveform)
    logging.debug(f"GionySTFT Mel-Spectrogram: {mel_spectrogram.size()}")

if __name__ == "__main__":
    test_LinearNorm()
    test_ConvNorm()
    test_GionySTFT()
