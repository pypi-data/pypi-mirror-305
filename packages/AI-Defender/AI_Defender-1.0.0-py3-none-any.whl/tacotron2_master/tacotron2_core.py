import sys
import torch
import torch.nn.functional as F
import os
import random
import torch.utils.data
import json
import logging
import argparse
from .utils_audio import files_to_list, MAX_WAV_VALUE, load_wav_to_torch
from pydub import AudioSegment
import numpy as np

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Function to dynamically import GionySTFT when needed (to avoid circular imports)
def get_giony_stft():
    from .giony_stft import GionySTFT  # Import here to avoid circular import issue
    return GionySTFT

# Function to load configuration from JSON
def load_config(config_path):
    try:
        with open(config_path, 'r') as f:
            config = json.load(f)
            logger.info(f"Loaded config from {config_path}")
            return config
    except Exception as e:
        logger.error(f"Error loading config file: {e}")
        sys.exit(1)

# Dataset class for Mel-spectrogram generation
class Mel2Samp(torch.utils.data.Dataset):
    def __init__(self, training_files, segment_length, **audio_config):
        # Lazy import GionySTFT to avoid circular imports
        GionySTFT = get_giony_stft()

        self.audio_files = files_to_list(training_files)
        random.seed(1234)
        random.shuffle(self.audio_files)

        # Initialize STFT using GionySTFT
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
        self.compress_dynamic_range = audio_config.get("compress_dynamic_range", False)
        self.clip_val = audio_config.get("clip_val", 1e-5)

    def get_mel(self, audio):
        """Converts audio into a mel-spectrogram using the STFT module."""
        audio_norm = audio / MAX_WAV_VALUE
        audio_norm = audio_norm.unsqueeze(0)

        # Generate mel spectrogram
        melspec = self.stft.mel_spectrogram(audio_norm)
        melspec = torch.squeeze(melspec, 0)

        # Apply dynamic range compression if enabled
        if self.compress_dynamic_range:
            melspec = torch.log(torch.clamp(melspec, min=self.clip_val) * 1)

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
            audio = F.pad(audio, (0, self.segment_length - audio.size(0)), 'constant').data

        mel = self.get_mel(audio)
        audio = audio / MAX_WAV_VALUE
        return mel, audio

    def __len__(self):
        return len(self.audio_files)

# Main function to process audio files and generate mel-spectrograms
def main(filelist_path, config_path, output_dir):
    # Load the configuration
    config = load_config(config_path)
    data_config = config["data_config"]

    # Initialize Mel2Samp object
    mel2samp = Mel2Samp(
        training_files=data_config["training_files"],
        segment_length=data_config["segment_length"],
        **data_config
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
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', "--filelist_path", required=True, help="Path to the filelist")
    parser.add_argument('-c', '--config', type=str, required=True, help='Path to the config JSON')
    parser.add_argument('-o', '--output_dir', type=str, required=True, help='Output directory')
    args = parser.parse_args()

    main(args.filelist_path, args.config, args.output_dir)
