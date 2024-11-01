import os
import re
import logging
from typing import Union, List

# Import constants using the full module name
from tacotron2_master.constants import VALID_SYMBOLS

# Setup logging
logger = logging.getLogger(__name__)
if not logger.hasHandlers():
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
    logger.addHandler(handler)

# Set of valid symbols for quick lookup
_valid_symbol_set = set(VALID_SYMBOLS)

# List of words to ignore during lookup
IGNORED_WORDS = ['A', 'AN', 'THE']

# Dictionary for handling irregular pronunciations
irregular_dict = {
    'KNIGHT': 'N AY1 T',
    'PSYCHOLOGY': 'S AY2 K AA1 L AH0 JH IY0',
    'COLONEL': 'K ER1 N AH0 L'
}

class CMUDict:
    """Thin wrapper around CMUDict data."""

    def __init__(self, file_or_path, keep_ambiguous=True):
        self._entries = {}

        # Ensure that file_or_path is a valid type
        if isinstance(file_or_path, list):
            logger.error(f"Expected a string or file-like object, got a list: {file_or_path}")
            raise ValueError("Expected a string or file-like object, got a list.")

        try:
            if isinstance(file_or_path, str):
                file_path = file_or_path
                logger.info(f"Opening CMU dictionary file at: {file_path}")

                # Ensure the path is a valid file
                if not os.path.isfile(file_path):
                    raise FileNotFoundError(f"CMUdict file not found at: {file_path}")

                with open(file_path, encoding='latin-1') as f:
                    self._entries = self.parse_cmudict(f)
            elif hasattr(file_or_path, 'read'):
                logger.info("Parsing CMU dictionary from file-like object.")
                self._entries = self.parse_cmudict(file_or_path)
            else:
                raise ValueError(f"file_or_path must be a string or a file-like object, got {type(file_or_path)} instead.")

        except FileNotFoundError as e:
            logger.error(str(e))
            self._entries = {}
        except Exception as e:
            logger.error(f"Error loading CMUdict: {e}")
            raise

        # Optionally remove ambiguous entries with multiple pronunciations
        if not keep_ambiguous:
            self._entries = {word: pron for word, pron in self._entries.items() if len(pron) == 1}

        logger.info(f"CMU dictionary loaded with {len(self._entries)} entries.")

    def __len__(self):
        return len(self._entries)

    def parse_cmudict(self, file):
        cmudict = {}
        for line_num, line in enumerate(file, start=1):
            logger.debug(f"Parsing line {line_num}: {line.strip()}")

            if line.startswith(';;') or not line.strip():
                continue

            try:
                parts = re.split(r'\s{2,}', line.strip())
                if len(parts) != 2:
                    logger.warning(f"Skipping malformed line {line_num}: {line.strip()}")
                    continue

                word = re.sub(r'\([0-9]+\)', '', parts[0])
                pronunciation = parts[1].strip()

                invalid_symbols = [p for p in pronunciation.split() if p not in _valid_symbol_set]
                if invalid_symbols:
                    logger.warning(f"Invalid symbols in pronunciation for word '{word}': {invalid_symbols}")
                    continue

                cmudict[word] = pronunciation.split()

            except (ValueError, IndexError) as e:
                logger.error(f"Error parsing line {line_num}: {e}")

        logger.info(f"Parsed {len(cmudict)} valid entries from CMU dictionary.")
        return cmudict

    def lookup(self, word: str) -> Union[List[str], None]:
        if not isinstance(word, str):
            logger.error(f"Invalid word type: expected str, got {type(word)}")
            return None

        word_upper = word.upper()
        if word_upper in IGNORED_WORDS:
            logger.info(f"Word '{word}' is ignored.")
            return None

        if word_upper in irregular_dict:
            pronunciation = irregular_dict[word_upper]
            logger.info(f"Found irregular pronunciation for '{word}': {pronunciation}")
            return [pronunciation]

        pronunciations = self._entries.get(word_upper)
        if pronunciations is None:
            logger.warning(f"No pronunciations found for '{word}'")
            return None

        return pronunciations

if __name__ == "__main__":
    # Ensure correct type for path, not a list
    cmu_dict_path = r"D:/ai/AI DEFENDER 2.1/tacotron2_master/cmudict.txt"  # Make sure this is a valid string path
    cmu_dict = CMUDict(cmu_dict_path)

    word = "apple"
    pronunciations = cmu_dict.lookup(word)
    if pronunciations:
        logger.info(f"Pronunciations for '{word}': {' '.join(pronunciations)}")
    else:
        logger.warning(f"Word '{word}' not found in CMUDict.")
