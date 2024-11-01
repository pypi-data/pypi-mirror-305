# test_imports.py

from tacotron2_master import (
    Tacotron2, text_to_sequence, HParams, GionySTFT, Tacotron2Logger,
    Tacotron2Loss, TextMelCollate, TextMelLoader, ConvNorm, LinearNorm,
    symbols, MAX_WAV_VALUE, files_to_list, create_hparams,
    apply_gradient_allreduce, create_cmudict_file
)

# Test the core functionality to ensure everything is imported correctly
print(Tacotron2)
print(text_to_sequence("Testing the import"))
print(HParams)
print(GionySTFT)
print(Tacotron2Logger)
print(Tacotron2Loss)
print(TextMelCollate)
print(TextMelLoader)
print(ConvNorm)
print(LinearNorm)
print(symbols)
print(MAX_WAV_VALUE)
print(files_to_list)
print(create_hparams)
print(apply_gradient_allreduce)
print(create_cmudict_file)
