import os
import random

# Path to your audio folder
audio_folder = "D:/ai/AI DEFENDER 2.1/tacotron2_master/audio"

# Path to save the train and val data files
train_file = "D:/ai/AI DEFENDER 2.1/tacotron2_master/train_data.txt"
val_file = "D:/ai/AI DEFENDER 2.1/tacotron2_master/val_data.txt"

# Get all .wav files from the audio folder
audio_files = [f for f in os.listdir(audio_folder) if f.endswith(".wav")]

# Shuffle and split into train and validation sets (80% train, 20% validation)
random.shuffle(audio_files)
split_idx = int(0.8 * len(audio_files))
train_files = audio_files[:split_idx]
val_files = audio_files[split_idx:]

# Example text placeholder (replace with actual text if available)
placeholder_text = "This is a sample transcription for the audio file."

# Create train_data.txt
with open(train_file, 'w', encoding='utf-8') as f_train:
    for file in train_files:
        f_train.write(f"{audio_folder}/{file}|{placeholder_text}\n")

# Create val_data.txt
with open(val_file, 'w', encoding='utf-8') as f_val:
    for file in val_files:
        f_val.write(f"{audio_folder}/{file}|{placeholder_text}\n")

print(f"train_data.txt and val_data.txt have been created successfully.")
