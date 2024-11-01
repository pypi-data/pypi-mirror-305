import random
import torch
from torch.utils.tensorboard import SummaryWriter
from plotting_utils import plot_alignment_to_numpy, plot_spectrogram_to_numpy
from plotting_utils import plot_gate_outputs_to_numpy
import logging


# Setup package-level logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Add handler only if it doesn't exist
if not logger.hasHandlers():
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
    logger.addHandler(handler)


class Tacotron2Logger(SummaryWriter):
    def __init__(self, logdir):
        super(Tacotron2Logger, self).__init__(logdir)

    def log_training(self, reduced_loss, grad_norm, learning_rate, duration, iteration):
        self.add_scalar("training.loss", reduced_loss, iteration)
        self.add_scalar("grad.norm", grad_norm, iteration)
        self.add_scalar("learning.rate", learning_rate, iteration)
        self.add_scalar("duration", duration, iteration)

    def log_validation(self, reduced_loss, model, y, y_pred, iteration):
        self.add_scalar("validation.loss", reduced_loss, iteration)
        _, mel_outputs, gate_outputs, alignments = y_pred
        mel_targets, gate_targets = y

        # plot distribution of parameters
        for tag, value in model.named_parameters():
            tag = tag.replace('.', '/')
            self.add_histogram(tag, value.data.cpu().numpy(), iteration)

        # plot alignment, mel target and predicted, gate target and predicted
        idx = random.randint(0, alignments.size(0) - 1)
        self.add_image(
            "alignment",
            plot_alignment_to_numpy(alignments[idx].data.cpu().numpy().T),
            iteration, dataformats='HWC')
        self.add_image(
            "mel_target",
            plot_spectrogram_to_numpy(mel_targets[idx].data.cpu().numpy()),
            iteration, dataformats='HWC')
        self.add_image(
            "mel_predicted",
            plot_spectrogram_to_numpy(mel_outputs[idx].data.cpu().numpy()),
            iteration, dataformats='HWC')
        self.add_image(
            "gate",
            plot_gate_outputs_to_numpy(
                gate_targets[idx].data.cpu().numpy(),
                torch.sigmoid(gate_outputs[idx]).data.cpu().numpy()),
            iteration, dataformats='HWC')


# Import necessary modules for Tacotron2
from cmudict import CMUDict
from cleaners import basic_cleaners, custom_cleaners
from symbols import symbols, _arpabet
from model import Tacotron2
from utils_custom import to_gpu, get_mask_from_lengths, load_wav_to_torch, load_filepaths_and_text
from data_utils import TextMelLoader, TextMelCollate
from loss_function import Tacotron2Loss
from distributed import apply_gradient_allreduce
from layers import ConvNorm, LinearNorm
from text_processing import text_to_sequence
from utils_audio import MAX_WAV_VALUE, files_to_list
from stft import GionySTFT
from hparams import create_hparams, HParams


# Optional: Load CMU dictionary during package import if necessary
try:
    import os
    cmu_dict_path = os.path.join(os.path.dirname(__file__), 'cmudict.txt')
    logger.info(f"Loading CMU dictionary from path: {cmu_dict_path}")
    cmu_dict = CMUDict(cmu_dict_path)
    logger.info(f"Loaded CMU dictionary with {len(cmu_dict)} entries.")
except Exception as e:
    logger.error(f"Error during CMU dictionary instantiation: {e}")


# Expose core functionality when the package is imported
__all__ = [
    'Tacotron2',
    'TextMelLoader',
    'TextMelCollate',
    'to_gpu',
    'get_mask_from_lengths',
    'Tacotron2Loss',
    'Tacotron2Logger',
    'create_hparams',
    'symbols',
    'basic_cleaners',
    'custom_cleaners',
    'CMUDict',
    'ConvNorm',
    'LinearNorm',
    'GionySTFT',
    'HParams',
    'text_to_sequence',
    'load_wav_to_torch',
    'load_filepaths_and_text',
    'apply_gradient_allreduce'
]
