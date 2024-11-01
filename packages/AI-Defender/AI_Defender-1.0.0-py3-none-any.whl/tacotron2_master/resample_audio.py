import os
import subprocess

input_folder = "D:/ai/AI DEFENDER 2.1/tacotron2_master/audio_converted"
output_folder = "D:/ai/AI DEFENDER 2.1/tacotron2_master/audio_resampled"
desired_sample_rate = 22050

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Iterate through all files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith(".wav"):
        input_file = os.path.join(input_folder, filename)
        output_file = os.path.join(output_folder, filename)

        # Skip the file if it has already been processed
        if os.path.exists(output_file):
            print(f"Skipping {output_file}, already processed.")
            continue

        # Resample the audio file using ffmpeg
        command = f'ffmpeg -i "{input_file}" -ar {desired_sample_rate} "{output_file}"'
        subprocess.run(command, shell=True)

print("Resampling complete.")
