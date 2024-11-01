import torch
import torch.nn as nn
import torch.nn.functional as F
from .layers import ConvNorm, LinearNorm
from .utils import to_gpu, get_mask_from_lengths
from.utils_audio import files_to_list, MAX_WAV_VALUE, load_wav_to_torch
from waveglow.denoiser import Denoiser
import sys
import soundfile as sf
import sys

sys.path.append('d:/ai/AI DEFENDER 2.1/.venv/lib/site-packages')
sys.path.append('d:/ai/ai defender 2.1/.venv/lib/site-packages/waveglow')

class GionySTFT:
    def __init__(self, filter_length, hop_length, win_length, sampling_rate, mel_fmin, mel_fmax):
        self.filter_length = filter_length
        self.hop_length = hop_length
        self.win_length = win_length
        self.sampling_rate = sampling_rate
        self.mel_fmin = mel_fmin
        self.mel_fmax = mel_fmax

        # Example mel basis, adjust accordingly
        self.mel_basis = torch.randn((80, filter_length // 2 + 1))  # Adjust mel basis size

    def mel_spectrogram(self, audio):
        # Calculate short-time Fourier transform (STFT)
        spectrogram = torch.stft(
            audio, 
            n_fft=self.filter_length, 
            hop_length=self.hop_length, 
            win_length=self.win_length, 
            return_complex=False
        )
        
        # Convert to mel spectrogram (example logic)
        mel_spectrogram = torch.matmul(self.mel_basis, spectrogram)
        return mel_spectrogram
    
class GModule(nn.Module):
    def __init__(self, hparams):
        super(GModule, self).__init__()
        self.hparams = hparams
        self.stft = GionySTFT(
            filter_length=hparams.filter_length,
            hop_length=hparams.hop_length,
            win_length=hparams.win_length,
            sampling_rate=hparams.sampling_rate,
            mel_fmin=hparams.mel_fmin,
            mel_fmax=hparams.mel_fmax
        )
        self.denoiser = Denoiser(hparams)

    def preprocess_text(self, text):
        normalized_text = text.lower().strip()  # Basic normalization
        return normalized_text

    def synthesize(self, text, model, denoise=False):
        text = self.preprocess_text(text)
        text_sequence = self.text_to_sequence(text)
        
        with torch.no_grad():
            mel_outputs, mel_outputs_postnet, _, alignments = model.inference(text_sequence)

        if denoise:
            mel_outputs_postnet = self.denoiser(mel_outputs_postnet)

        return mel_outputs_postnet

    def text_to_sequence(self, text):
        symbols = self.hparams.symbols  # Ensure symbols are accessible from hparams
        sequence = [symbols.index(s) for s in text if s in symbols]
        return torch.tensor(sequence).unsqueeze(0)  # Convert to PyTorch tensor

    def postprocess(self, mel_outputs, output_path="output.wav"):
        audio = self.mel_to_audio(mel_outputs)
        self.save_wav(audio, output_path)
        return output_path

    def mel_to_audio(self, mel_outputs):
        # Implement vocoder conversion logic here (e.g., using WaveGlow)
        return mel_outputs  # Placeholder

    def save_wav(self, audio, output_path):
        sf.write(output_path, audio.cpu().numpy(), self.hparams.sampling_rate)
        print(f"Audio saved to {output_path}")
