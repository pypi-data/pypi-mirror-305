import logging
import os
import torch
from tacotron2_master.cmudict import CMUDict
from tacotron2_master.model import Tacotron2
from tacotron2_master.text_processing import text_to_sequence
from tacotron2_master.hparams import create_hparams
from tacotron2_master.constants import MAX_WAV_VALUE, LOG_DIRECTORY
from tacotron2_master.train import load_checkpoint
from tacotron2_master.denoiser import Denoiser
from tacotron2_master.distributed import DistributedDataParallel
import torch.distributed as dist
import numpy as np
import soundfile as sf

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    logging.info("Starting Tacotron2")

    # Initialize distributed backend
    dist.init_process_group(backend='nccl', init_method='env://')

    # Define the path to CMUDict file
    cmudict_path = 'D:\\ai\\AI DEFENDER 2.1\\tacotron2_master\\cmudict.txt'
    logging.info(f"CMU Dictionary file path: {cmudict_path}")

    try:
        # Instantiate CMUDict
        cmu_dict = CMUDict(cmudict_path)
        logging.info("CMU dictionary loaded successfully.")

        # Check if CMUDict is loaded properly
        if len(cmu_dict) == 0:
            logging.error("CMUDict is empty, cannot proceed.")
            return

        # Example text to sequence conversion
        sample_text = "hello world"
        logging.info(f"Converting text to sequence: {sample_text}")

        sequence = text_to_sequence(
            sample_text,
            cleaner_names=["english_cleaners"],
            use_phonemes=True,
            cmu_dict=cmu_dict
        )
        logging.info(f"Text sequence for '{sample_text}': {sequence}")

        # Create hyperparameters
        hparams = create_hparams()

        # Instantiate Tacotron2 model
        logging.info("Instantiating Tacotron2 model.")
        tacotron2_model = Tacotron2(hparams).cuda()

        # Wrap the model in DistributedDataParallel
        tacotron2_model = DistributedDataParallel(tacotron2_model)

        logging.info("Tacotron2 model instantiated successfully.")

        # Load model checkpoint
        checkpoint_path = os.path.join(LOG_DIRECTORY, "checkpoint_100000")
        if not os.path.exists(checkpoint_path):
            logging.error(f"Checkpoint not found at: {checkpoint_path}")
            return
        load_checkpoint(checkpoint_path, tacotron2_model)
        logging.info("Model checkpoint loaded successfully.")

        # Set model to evaluation mode
        tacotron2_model.eval()

        # Example: Generate mel-spectrogram from input sequence
        input_sequence = torch.LongTensor([sequence]).cuda()
        with torch.no_grad():
            mel_outputs, mel_outputs_postnet, _, _ = tacotron2_model.module.inference(input_sequence)

        # Example: Use WaveGlow to generate audio (assuming you have WaveGlow loaded)
        # waveglow = torch.load('path/to/waveglow_model.pt')['model']
        # waveglow.cuda().eval()
        # audio = waveglow.infer(mel_outputs_postnet, sigma=0.7)

        # Apply denoising to the generated audio
        # denoiser = Denoiser(waveglow)
        # denoised_audio = denoiser(audio, strength=0.1)

        # Save the generated audio to file (if audio is generated)
        # output_path = 'output_audio.wav'
        # sf.write(output_path, denoised_audio.cpu().numpy(), hparams.sampling_rate)
        # logging.info(f"Denoised audio saved at {output_path}")

    except Exception as e:
        logging.error(f"An error occurred: {e}", exc_info=True)

if __name__ == "__main__":
    main()
