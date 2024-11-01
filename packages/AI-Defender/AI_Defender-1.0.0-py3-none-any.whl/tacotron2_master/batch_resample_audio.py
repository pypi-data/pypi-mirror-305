import os
import subprocess
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Define input and output folders
input_folder = "D:/ai/AI DEFENDER 2.1/tacotron2_master/audio_converted/"
output_folder = "D:/ai/AI DEFENDER 2.1/tacotron2_master/audio_resampled/"

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)
logger.info(f"Output folder: {output_folder}")

# Iterate over the files in the input folder
for file_name in os.listdir(input_folder):
    if file_name.endswith(".wav"):
        input_file = os.path.join(input_folder, file_name)
        output_file = os.path.join(output_folder, file_name)
        
        # Check if the file has already been processed
        if os.path.exists(output_file):
            logger.info(f"Skipping {output_file}, already processed.")
            continue

        # Run ffmpeg to resample to 22050 Hz
        command = [
            "ffmpeg", "-i", input_file, "-ar", "22050", output_file
        ]
        logger.info(f"Resampling {input_file} to {output_file}...")
        
        try:
            result = subprocess.run(command, check=True)
            logger.info(f"Successfully resampled {input_file} to {output_file}.")
        except subprocess.CalledProcessError as e:
            logger.error(f"Error occurred while processing {input_file}: {e}")

logger.info("Resampling complete.")
