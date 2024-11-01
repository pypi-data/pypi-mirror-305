import os
import re
import logging
from typing import Union, List
from argparse import Namespace

# Importing PyTorch and utility functions
import torch
from torch import nn
from torch.nn import functional as F
from torch.autograd import Variable

# Import tacotron-related modules
from .utils_custom import to_gpu, get_mask_from_lengths
from .helper import process_data
from .layers import ConvNorm, LinearNorm
from .platform_helper import get_group_info
from .symbols import symbols
from .cmudict import CMUDict
from .cleaners import english_cleaners
from .text_processing import text_to_sequence
from .tacotron2_model import Tacotron2


# Example usage of torch
x = torch.tensor([1.0, 2.0, 3.0], requires_grad=True)
print(x)

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Define valid symbols for CMUdict
_valid_symbol_set = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")

# Define the path to the CMU dictionary file
RESOURCE_PATH = os.path.join(os.path.dirname(__file__), 'resources', 'cmudict.txt')

# Ensure the CMU dictionary file exists
if not os.path.exists(RESOURCE_PATH):
    # Create a sample CMU dictionary file if it doesn't exist
    words_to_add = ["HELLO", "WORLD", "COMPUTER", "AI", "VOICE", "ASSISTANT", "GIONYTTS"]
    create_cmudict_file(words_to_add, RESOURCE_PATH)
    logger.info(f"CMU dictionary file created at {RESOURCE_PATH}")

# Load the CMU dictionary
try:
    cmu_dict = CMUDict(RESOURCE_PATH)  # Load the CMU dictionary from the file
    logger.info(f"CMU dictionary loaded with {len(cmu_dict)} entries.")
except Exception as e:
    logger.error(f"Error loading CMUDict: {e}")
    raise

# Define a simple model class using PyTorch
class CMUDict:
    def __init__(self, path):
        self.path = path
        self.data = {}  # Initialize an empty dictionary to hold CMU pronunciations
        try:
            absolute_path = os.path.abspath(path)
            logger.info(f"Loading CMUDict from: {absolute_path}")
            if not os.path.exists(path):
                logger.error(f"CMUDict file not found at {path}")
                raise FileNotFoundError(f"CMUDict file not found at {path}")
            with open(path, 'r') as f:
                for line in f:
                    if line.startswith(';;;'):
                        continue
                    parts = line.strip().split("  ")
                    if len(parts) == 2:
                        word, pronunciation = parts
                        self.data[word.lower()] = [pronunciation.split()]
            logger.info(f"CMU dictionary loaded with {len(self.data)} entries.")
        except FileNotFoundError:
            logger.error(f"CMUDict file not found at {path}")
            raise

    def lookup(self, word):
        return self.data.get(word)

    def __len__(self):
        return len(self.data)
        # Example of using the CMUDict class
class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.fc1 = nn.Linear(10, 5)  # Example of a linear layer

    def forward(self, x):
        x = self.fc1(x)
        return x

# Create an instance of the model
model = SimpleModel()
input_data = torch.randn(1, 10)  # Assuming input size of 10 based on the model definition
output = model(input_data)
print(output)

# Example of using the Namespace class to manage hyperparameters
hparams = Namespace(
    learning_rate=0.001,
    batch_size=32,
    num_epochs=10,
)

print(hparams.learning_rate)  # Output: 0.001

# Class to manage hyperparameters
class HParams:
    def __init__(self, **kwargs):
        # Set default hyperparameters
        self.learning_rate = kwargs.get("learning_rate", 1e-3)
        self.batch_size = kwargs.get("batch_size", 32)
        self.epochs = kwargs.get("epochs", 100)
        self.n_mels = kwargs.get("n_mels", 80)
        self.sampling_rate = kwargs.get("sampling_rate", 22050)
        self.filter_length = kwargs.get("filter_length", 1024)
        self.hop_length = kwargs.get("hop_length", 256)
        self.win_length = kwargs.get("win_length", 1024)
        self.n_symbols = kwargs.get("n_symbols", len(symbols))
        self.symbols_embedding_dim = kwargs.get("symbols_embedding_dim", 512)
        self.decoder_rnn_dim = kwargs.get("decoder_rnn_dim", 1024)
        self.prenet_dim = kwargs.get("prenet_dim", 256)
        self.max_decoder_steps = kwargs.get("max_decoder_steps", 1000)
        self.gate_threshold = kwargs.get("gate_threshold", 0.5)
        self.p_attention_dropout = kwargs.get("p_attention_dropout", 0.1)
        self.p_decoder_dropout = kwargs.get("p_decoder_dropout", 0.1)
        self.attention_rnn_dim = kwargs.get("attention_rnn_dim", 1024)
        self.attention_dim = kwargs.get("attention_dim", 128)
        self.postnet_n_convolutions = kwargs.get("postnet_n_convolutions", 5)
        self.postnet_kernel_size = kwargs.get("postnet_kernel_size", 5)
        self.postnet_embedding_dim = kwargs.get("postnet_embedding_dim", 512)
        self.encoder_n_convolutions = kwargs.get("encoder_n_convolutions", 3)
        self.encoder_kernel_size = kwargs.get("encoder_kernel_size", 5)
        self.encoder_embedding_dim = kwargs.get("encoder_embedding_dim", 512)
        self.n_frames_per_step = kwargs.get("n_frames_per_step", 1)
        self.n_mel_channels = kwargs.get("n_mel_channels", 80)

        # Load or create CMUdict
        self.cmudict_path = kwargs.get("cmudict_path", RESOURCE_PATH)
        try:
            if not os.path.exists(self.cmudict_path):
                # Create CMUdict if it doesn't exist
                words_to_add = ["HELLO", "WORLD", "COMPUTER", "AI", "VOICE", "ASSISTANT", "GIONYTTS"]
                HParams.create_cmudict_file(words_to_add, output_file=self.cmudict_path)

            # Load the CMUDict from the file path
            self.cmudict = CMUDict(self.cmudict_path)
            logger.info(f"CMU dictionary loaded with {len(self.cmudict)} entries.")

        except Exception as e:
            logger.error(f"Failed to create or load CMU dictionary: {e}")
            self.cmudict = None

        # Validate hyperparameter ranges
        if not (0 <= self.p_attention_dropout <= 1):
            raise ValueError("p_attention_dropout must be between 0 and 1")
        if not (0 <= self.p_decoder_dropout <= 1):
            raise ValueError("p_decoder_dropout must be between 0 and 1")

    def __repr__(self):
        return str(self.__dict__)

    @staticmethod
    def create_cmudict_file(words: List[str], output_file: str):
        """Create a simple CMUdict file."""
        with open(output_file, 'w', encoding='utf-8') as file:
            for word in words:
                file.write(f"{word}  {' '.join(list(word))}\n")  # Simplistic ARPAbet transcription

# Utility functions for hyperparameter creation and printing
def create_hparams(**kwargs):
    return HParams(**kwargs)

def print_hparams(hparams):
    """Function to print the current hyperparameters."""
    print("Current Hyperparameters:")
    for key, value in vars(hparams).items():
        print(f"{key}: {value}")

# Test cases for HParams
import unittest

class TestHParams(unittest.TestCase):

    def test_create_hparams_default_values(self):
        """Test default values of hyperparameters."""
        hparams = create_hparams()
        self.assertEqual(hparams.max_decoder_steps, 1000)
        self.assertEqual(hparams.gate_threshold, 0.5)
        self.assertEqual(hparams.p_attention_dropout, 0.1)
        self.assertEqual(hparams.p_decoder_dropout, 0.1)

    def test_create_hparams_custom_values(self):
        """Test custom values passed to hyperparameters."""
        custom_hparams = {
            'max_decoder_steps': 1500,
            'gate_threshold': 0.6,
            'p_attention_dropout': 0.2,
            'p_decoder_dropout': 0.15
        }
        hparams = create_hparams(**custom_hparams)
        self.assertEqual(hparams.max_decoder_steps, 1500)
        self.assertEqual(hparams.gate_threshold, 0.6)
        self.assertEqual(hparams.p_attention_dropout, 0.2)
        self.assertEqual(hparams.p_decoder_dropout, 0.15)

    def test_create_hparams_value_ranges(self):
        """Test that invalid values for hyperparameters raise ValueError."""
        with self.assertRaises(ValueError):
            create_hparams(p_attention_dropout=-0.1)
        with self.assertRaises(ValueError):
            create_hparams(p_decoder_dropout=1.1)

if __name__ == '__main__':
    unittest.main()

# Example usage
def new_func(hparams, print_hparams):
    print_hparams(hparams)

if __name__ == "__main__":
    print("Starting hparams script...")

    # Create an instance of hyperparameters with default values
    hparams = create_hparams()

    # Print the current hyperparameters
    new_func(hparams, print_hparams)

    # Example usage of overriding some parameters
    print("\nOverridden Hyperparameters:")
    hparams = create_hparams(batch_size=16, learning_rate=2e-4)

    print("\nhparams.py execution completed.")
