import os
import random
import torch
import torch.utils.data
import json
import logging
import numpy as np
from pydub import AudioSegment
from .utils_audio import files_to_list, MAX_WAV_VALUE, load_wav_to_torch
from .stft import GionySTFT

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Load configuration from JSON file
def load_config(config_path):
    try:
        with open(config_path, 'r') as f:
            config = json.load(f)
            return config
    except FileNotFoundError:
        logger.error(f"Config file '{config_path}' not found.")
        exit(1)  # Exit program if the file is missing
    except json.JSONDecodeError:
        logger.error(f"Failed to decode the config file '{config_path}'. Please check the format.")
        exit(1)  # Exit program if the JSON format is incorrect
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        exit(1)

# Example of loading the config
config_path = 'D:/ai/AI DEFENDER 2.1/tacotron2_master/settings.json'
config = load_config(config_path)

# Load an MP3 file into a PyTorch tensor
def load_mp3_to_torch(file_path):
    """Loads an mp3 file into a PyTorch tensor."""
    audio = AudioSegment.from_mp3(file_path)
    audio_samples = np.array(audio.get_array_of_samples())
    if audio.channels == 2:  # Convert stereo to mono
        audio_samples = audio_samples.reshape((-1, 2)).mean(axis=1)
    return torch.FloatTensor(audio_samples), audio.frame_rate

# Mel2Samp class
class Mel2Samp(torch.utils.data.Dataset):
    MAX_WAV_VALUE = 32768.0  # Define this constant at the class level to avoid reassignment.

    def __init__(self, training_files, segment_length, **audio_config):
        self.audio_files = files_to_list(training_files)
        random.seed(1234)
        random.shuffle(self.audio_files)

        # Initialize STFT using the provided configuration
        self.stft = GionySTFT(
            filter_length=audio_config["filter_length"],
            hop_length=audio_config["hop_length"],
            win_length=audio_config["win_length"],
            sampling_rate=audio_config["sampling_rate"],
            mel_fmin=audio_config["mel_fmin"],
            mel_fmax=audio_config["mel_fmax"],
        )

        self.segment_length = segment_length
        self.sampling_rate = audio_config["sampling_rate"]
        self.use_log_mel = audio_config.get("use_log_mel", True)

        # Initialize dynamic range compression parameters
        self.compress_dynamic_range = audio_config.get("compress_dynamic_range", False)
        self.clip_val = audio_config.get("clip_val", 1e-5)

    def dynamic_range_compression(self, x, C=1, clip_val=1e-5):
        """Apply dynamic range compression to the input tensor."""
        return torch.log(torch.clamp(x, min=clip_val) * C)

    def get_mel(self, audio):
        """Converts audio into a mel-spectrogram using the STFT module."""
        audio_norm = audio / self.MAX_WAV_VALUE
        audio_norm = audio_norm.unsqueeze(0)

        # Pass to the mel_spectrogram function
        melspec = self.stft.mel_spectrogram(audio_norm)
        melspec = torch.squeeze(melspec, 0)

        # Apply dynamic range compression if enabled
        if self.compress_dynamic_range:
            melspec = self.dynamic_range_compression(melspec, clip_val=self.clip_val)

        # Convert to log mel if enabled
        if self.use_log_mel:
            melspec = torch.log(torch.clamp(melspec, min=1e-5))

        return melspec

    def __getitem__(self, index):
        filename = self.audio_files[index]
        try:
            audio, sampling_rate = load_wav_to_torch(filename)
        except Exception as e:
            logger.error(f"Error loading audio file {filename}: {e}")
            return None, None

        if sampling_rate != self.sampling_rate:
            logger.warning(f"Sampling rate mismatch in {filename}: {sampling_rate} SR doesn't match target {self.sampling_rate} SR. Skipping this file.")
            return None, None

        if audio.size(0) >= self.segment_length:
            max_audio_start = audio.size(0) - self.segment_length
            audio_start = random.randint(0, max_audio_start)
            audio = audio[audio_start:audio_start + self.segment_length]
        else:
            audio = torch.nn.functional.pad(audio, (0, self.segment_length - audio.size(0)), 'constant').data

        mel = self.get_mel(audio)
        audio = audio / self.MAX_WAV_VALUE
        return mel, audio

    def __len__(self):
        return len(self.audio_files)

# Main function to process audio files and generate mel-spectrograms
def main(filelist_path, config_path, output_dir):
    """Main function to process audio files and generate mel-spectrograms."""

    # Load the configuration
    config = load_config(config_path)
    data_config = config["data_config"]

    # Initialize Mel2Samp object
    mel2samp = Mel2Samp(
        training_files=data_config["training_files"],
        segment_length=data_config["segment_length"],
        sampling_rate=data_config["sampling_rate"],
        filter_length=data_config["filter_length"],
        hop_length=data_config["hop_length"],
        win_length=data_config["win_length"],
        mel_fmin=data_config["mel_fmin"],
        mel_fmax=data_config["mel_fmax"]
    )

    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Process each audio file and save mel-spectrograms
    filepaths = files_to_list(filelist_path)
    for filepath in filepaths:
        audio, sr = load_wav_to_torch(filepath)
        if audio is None or sr is None:
            logger.warning(f"Skipping {filepath} due to loading error.")
            continue

        melspectrogram = mel2samp.get_mel(audio)
        output_filepath = os.path.join(output_dir, os.path.basename(filepath) + '.pt')
        torch.save(melspectrogram, output_filepath)
        logger.info(f"Saved: {output_filepath}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('-f', "--filelist_path", required=True, help="Path to the filelist")
    parser.add_argument('-c', '--config', type=str, required=True, help='Path to the config JSON')
    parser.add_argument('-o', '--output_dir', type=str, required=True, help='Output directory')
    args = parser.parse_args()

    main(args.filelist_path, args.config, args.output_dir)
