from pydub import AudioSegment
import os

input_directory = "D:/ai/AI DEFENDER 2.1/audio/"
output_directory = "D:/ai/AI DEFENDER 2.1/tacotron2-master/audio_converted/"


if not os.path.exists(output_directory):
    os.makedirs(output_directory)

print("Input directory:", input_directory)
print("Output directory:", output_directory)

for file_name in os.listdir(input_directory):
    if file_name.endswith(".mp3"):
        print(f"Found MP3 file: {file_name}")
        mp3_file = os.path.join(input_directory, file_name)
        wav_file = os.path.join(output_directory, file_name.replace(".mp3", ".wav"))
        audio = AudioSegment.from_mp3(mp3_file)
        audio.export(wav_file, format="wav")
        print(f"Converted {file_name} to {wav_file}")
    else:
        print(f"Skipping non-MP3 file: {file_name}")
