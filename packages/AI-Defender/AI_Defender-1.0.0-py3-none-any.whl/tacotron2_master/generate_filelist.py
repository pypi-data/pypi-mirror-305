import os

# Define the directory where your WAV files are stored
wav_dir = "D:\\ai\\AI DEFENDER 2.1\\tacotron2_master\\audio_converted"
filelist_path = "D:\\ai\\AI DEFENDER 2.1\\tacotron2_master\\filelist.txt"

# Create or overwrite the filelist.txt file
with open(filelist_path, 'w') as filelist:
    # Loop through all WAV files in the audio_converted directory
    for filename in os.listdir(wav_dir):
        if filename.endswith('.wav'):
            full_path = os.path.join(wav_dir, filename)
            filelist.write(full_path + '\n')

print("filelist.txt has been updated with all WAV files.")
