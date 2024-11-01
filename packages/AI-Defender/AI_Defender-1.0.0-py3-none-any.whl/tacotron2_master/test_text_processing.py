import re
import logging
from .symbols import symbols, _arpabet  # Use relative import if in the same package
from .cmudict import CMUDict

# Logger setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Mappings from symbol to numeric ID and vice versa
_symbol_to_id = {s: i for i, s in enumerate(symbols)}
_id_to_symbol = {i: s for i, s in enumerate(symbols)}

# Regular expression for detecting ARPAbet sequences inside curly braces
_curly_re = re.compile(r'(.*?)\{(.+?)\}(.*)')

def text_to_sequence(text, cleaner_names, use_phonemes=False, cmu_dict=None):
    """
    Converts a string of text to a sequence of IDs corresponding to the symbols in the text.

    Args:
        text (str): The input text to convert.
        cleaner_names (list): A list of cleaner function names to apply to the text.
        use_phonemes (bool): Whether to use phonemes for conversion. Defaults to False.
        cmu_dict (CMUDict): An instance of CMUDict to use for phoneme lookup. Defaults to None.

    Returns:
        list: A list of integer IDs corresponding to the symbols in the text.
    """
    sequence = []

    # Apply cleaning
    cleaned_text = _clean_text(text, cleaner_names)
    
    # Split the cleaned text into words and symbols
    words = re.findall(r"[\w']+|[.,!?;]", cleaned_text)

    for word in words:
        if use_phonemes and cmu_dict:
            pronunciation = cmu_dict.lookup(word.lower())  # Use lowercase to match CMUDict
            if pronunciation:
                logger.debug(f"Word '{word}' found in CMUDict with pronunciation: {pronunciation}")
                # Iterate over each phoneme
                for phoneme in pronunciation:
                    phoneme = phoneme.strip()  # Ensure no leading/trailing spaces
                    if phoneme in _symbol_to_id:
                        sequence.append(_symbol_to_id[phoneme])
                    else:
                        logger.warning(f"Phoneme '{phoneme}' is not in the valid symbol set.")
            else:
                logger.warning(f"Word '{word}' not found in CMUDict. Adding character-level IDs.")
                sequence.extend(_symbols_to_sequence(list(word)))
        else:
            # If no CMUDict is provided or not using phonemes, convert word into character sequence
            sequence.extend(_symbols_to_sequence(list(word)))

    logger.info(f"Converted sequence: {sequence}")
    return sequence


def sequence_to_text(sequence):
    """
    Converts a sequence of IDs back to a string.
    """
    result = ''
    for symbol_id in sequence:
        if symbol_id in _id_to_symbol:
            s = _id_to_symbol[symbol_id]
            if len(s) > 1 and s[0] == '@':
                s = '{%s}' % s[1:]
            result += s
    return result.replace('}{', ' ')

def _clean_text(text, cleaner_names):
    """
    Applies cleaner functions to the text.
    """
    for name in cleaner_names:
        try:
            cleaner = globals()[name]  # Changed to use globals to access cleaner functions
            text = cleaner(text)
        except KeyError:
            logger.error(f'Unknown cleaner: {name}')
            raise ValueError(f'Unknown cleaner: {name}')
    return text

def _symbols_to_sequence(symbols):
    """
    Convert a list of symbols to a list of corresponding numeric IDs.
    """
    return [_symbol_to_id.get(s, _symbol_to_id[' ']) for s in symbols if _should_keep_symbol(s)]

def _should_keep_symbol(s):
    """
    Returns True if the symbol should be kept.
    """
    return s in _symbol_to_id and s != '_'

# Define basic and custom cleaners
def english_cleaners(text):
    """Basic pipeline that lowercases and removes punctuation."""
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    return text

def custom_cleaners(text):
    """Custom text cleaner based on specific needs."""
    # Add your custom cleaning logic here
    return text

# Example usage
if __name__ == "__main__":
    cmu_dict_path = 'tacotron2_master/resources/cmudict.txt'
    try:
        cmu_dict = CMUDict(cmu_dict_path)
        logger.info(f"CMUDict successfully loaded with {len(cmu_dict)} entries.")
    except FileNotFoundError as e:
        logger.error(f"Failed to load CMUDict: {e}")
        cmu_dict = None

    sample_text = "Hello world!"
    cleaner_names = ['english_cleaners']

    # Convert text to sequence
    sequence = text_to_sequence(sample_text, cleaner_names, use_phonemes=True, cmu_dict=cmu_dict)
    print(f"Sequence for '{sample_text}': {sequence}")

    # Convert back to text to verify the process
    reconstructed_text = sequence_to_text(sequence)
    print(f"Reconstructed text: {reconstructed_text}")
