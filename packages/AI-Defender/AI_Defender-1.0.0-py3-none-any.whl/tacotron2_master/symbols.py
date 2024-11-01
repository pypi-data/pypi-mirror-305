import os
import sys
from pathlib import Path

# Add project root to path
PROJECT_ROOT = Path(__file__).resolve().parent
sys.path.append(str(PROJECT_ROOT))

# Direct imports
from constants import VALID_SYMBOLS

# Padding symbol
_pad = '_'

# Punctuation symbols used by the model
_punctuation = "!\'(),.:;? "

# Special characters
_special = '-'

# Letters used by the model
_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

# Combine all symbols to be used by the model
_arpabet = ['@' + s for s in VALID_SYMBOLS]

# Final list of symbols used by the model
symbols = [_pad] + list(_special) + list(_punctuation) + list(_letters) + _arpabet

# Export all necessary symbols
__all__ = ['symbols', '_arpabet', '_pad']
