"""
This module defines various constants used throughout the AI assistant project.
"""

# constants.py

# Phonetic transcription symbols
VALID_SYMBOLS = [
    'AA', 'AA0', 'AA1', 'AA2', 'AE', 'AE0', 'AE1', 'AE2', 'AH', 'AH0', 'AH1', 'AH2',
    'AO', 'AO0', 'AO1', 'AO2', 'AW', 'AW0', 'AW1', 'AW2', 'AY', 'AY0', 'AY1', 'AY2',
    'B', 'CH', 'D', 'DH', 'EH', 'EH0', 'EH1', 'EH2', 'ER', 'ER0', 'ER1', 'ER2',
    'EY', 'EY0', 'EY1', 'EY2', 'F', 'G', 'H', 'HH', 'IH', 'IH0', 'IH1', 'IH2', 'IY',
    'IY0', 'IY1', 'IY2', 'JH', 'K', 'L', 'M', 'N', 'NG', 'OW', 'OW0', 'OW1', 'OW2',
    'OY', 'OY0', 'OY1', 'OY2', 'P', 'R', 'S', 'SH', 'T', 'TH', 'UH', 'UH0', 'UH1',
    'UH2', 'UW', 'UW0', 'UW1', 'UW2', 'V', 'W', 'Y', 'Z', 'ZH'
]

# Maximum value for waveform normalization
MAX_WAV_VALUE = 32768.0

# Example sampling rate for audio
SAMPLING_RATE = 22050

# Example file paths
TRAINING_FILES = "filelists/train_filelist.txt"
VALIDATION_FILES = "filelists/val_filelist.txt"
LOG_DIRECTORY = "log_dir"

# Number of Mel bins used for mel-spectrogram computation
N_MELS = 80

# Frequency range for mel-spectrogram computation
MEL_FMIN = 0.0
MEL_FMAX = 8000.0

# STFT parameters
FILTER_LENGTH = 1024
HOP_LENGTH = 256
WIN_LENGTH = 1024
WINDOW = 'hann'

# Padding symbol
_pad = '_'

# Punctuation symbols used by the model
_punctuation = "!\'(),.:;? "

# Special characters
_special = '-'

# Letters used by the model
_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

# Define ARPAbet symbols prefixed with '@' to ensure uniqueness
_arpabet = ['@' + s for s in VALID_SYMBOLS]

# Final list of symbols used by the model
symbols = [_pad] + list(_special) + list(_punctuation) + list(_letters) + _arpabet

# Dynamic range compression parameters
CLIP_VAL = 1e-5

# Configuration for normalization
USE_NORMALIZATION = True
USE_DYNAMIC_RANGE_COMPRESSION = False

# Text cleaner configurations
CLEANERS = ['basic_cleaners']
