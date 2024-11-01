import os
import sys
import torch
import torch.nn as nn
from scipy.io.wavfile import write

# Use absolute imports for all local modules
from .mel2samp import files_to_list, MAX_WAV_VALUE
from .denoiser import Denoiser
from .stft_module import GionySTFT

# ConvNorm Implementation
class ConvNorm(nn.Module):
    def __init__(self, in_channels, out_channels, kernel_size=1, stride=1, padding=None, dilation=1, bias=True, w_init_gain='linear'):
        super(ConvNorm, self).__init__()
        if padding is None:
            padding = int((kernel_size - 1) / 2)
        self.conv = nn.Conv1d(in_channels, out_channels, kernel_size=kernel_size, stride=stride,
                              padding=padding, dilation=dilation, bias=bias)
        torch.nn.init.xavier_uniform_(self.conv.weight, gain=torch.nn.init.calculate_gain(w_init_gain))

    def forward(self, x):
        return self.conv(x)

# LinearNorm Implementation
class LinearNorm(nn.Module):
    def __init__(self, in_dim, out_dim, bias=True, w_init_gain='linear'):
        super(LinearNorm, self).__init__()
        self.linear = nn.Linear(in_dim, out_dim, bias=bias)
        torch.nn.init.xavier_uniform_(self.linear.weight, gain=torch.nn.init.calculate_gain(w_init_gain))

    def forward(self, x):
        return self.linear(x)

# Add the path of the parent directory of tacotron2_master to sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Main function for audio synthesis
def main(mel_files, waveglow_path, sigma, output_dir, sampling_rate, is_fp16, denoiser_strength):
    # Convert file list to a list of file paths
    mel_files = files_to_list(mel_files)
    
    # Load WaveGlow model
    waveglow = torch.load(waveglow_path)['model']
    waveglow = waveglow.remove_weightnorm(waveglow)
    waveglow.cuda().eval()  # Move model to GPU and set to evaluation mode
    
    # Optionally convert model to FP16 for faster inference using PyTorch native FP16 support
    if is_fp16:
        waveglow = waveglow.half()
    
    # Initialize denoiser if denoiser strength is greater than 0
    if denoiser_strength > 0:
        denoiser = Denoiser(waveglow).cuda()

    # Process each mel-spectrogram file
    for i, file_path in enumerate(mel_files):
        file_name = os.path.splitext(os.path.basename(file_path))[0]
        mel = torch.load(file_path)  # Load the mel-spectrogram file
        mel = torch.autograd.Variable(mel.cuda())  # Move mel to GPU
        mel = torch.unsqueeze(mel, 0)  # Add batch dimension

        # Use FP16 for mel if requested
        mel = mel.half() if is_fp16 else mel
        
        # Generate audio
        with torch.no_grad():
            audio = waveglow.infer(mel, sigma=sigma)
            
            # Apply denoiser if required
            if denoiser_strength > 0:
                audio = denoiser(audio, denoiser_strength)
            
            # Scale the audio to the proper range
            audio = audio * MAX_WAV_VALUE

        # Convert the audio tensor to numpy and save it as a .wav file
        audio = audio.squeeze().cpu().numpy().astype('int16')
        audio_path = os.path.join(output_dir, f"{file_name}_synthesis.wav")
        write(audio_path, sampling_rate, audio)
        print(f"Saved: {audio_path}")

if __name__ == "__main__":
    import argparse

    # Set up argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', "--filelist_path", required=True, help="Path to the file containing list of mel-spectrogram files")
    parser.add_argument('-w', '--waveglow_path', required=True, help='Path to WaveGlow decoder checkpoint with model')
    parser.add_argument('-o', "--output_dir", required=True, help="Directory to save synthesized audio")
    parser.add_argument("-s", "--sigma", default=1.0, type=float, help="Controls the variance of the output audio")
    parser.add_argument("--sampling_rate", default=22050, type=int, help="Sampling rate for the output audio")
    parser.add_argument("--is_fp16", action="store_true", help="Use half-precision (FP16) for faster inference")
    parser.add_argument("-d", "--denoiser_strength", default=0.0, type=float, help="Strength of the denoiser. Start with 0.1 and adjust")

    # Parse command-line arguments
    args = parser.parse_args()

    # Call the main function
    main(args.filelist_path, args.waveglow_path, args.sigma, args.output_dir, args.sampling_rate, args.is_fp16, args.denoiser_strength)
