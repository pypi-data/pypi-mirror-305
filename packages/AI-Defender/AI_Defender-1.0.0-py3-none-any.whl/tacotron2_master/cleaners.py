import re
import logging
from unidecode import unidecode  # Converts text to ASCII
from num2words import num2words  # Converts numbers to words

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Cleaning functions

def _clean_text(text, cleaner_names):
    """Apply a series of cleaners to the text."""
    for name in cleaner_names:
        try:
            cleaner = globals()[name]  # Fetch cleaner function from global scope
            text = cleaner(text)
        except KeyError:
            logger.error(f'Unknown cleaner: {name}')
            raise Exception(f'Unknown cleaner: {name}')
    return text

# Cleaner functions for various languages and specific needs

def english_cleaners(text):
    """Pipeline for English text, including number and abbreviation expansion."""
    text = convert_to_ascii(text)
    text = lowercase(text)
    text = expand_numbers(text)
    text = expand_abbreviations(text)
    text = collapse_whitespace(text)
    return text

def japanese_cleaners(text):  
    """Placeholder for Japanese text cleaners."""
    # TODO: Implement Japanese text cleaning logic here
    return text

def japanese_cleaners2(text):
    """Placeholder for an alternative Japanese text cleaning pipeline."""
    return text

def korean_cleaners(text):
    """Pipeline for Korean text."""
    text = latin_to_hangul(text)
    text = number_to_hangul(text)
    text = collapse_whitespace(text)
    return text

def basic_cleaners(text):
    """Basic pipeline that lowercases and collapses whitespace without transliteration."""
    text = lowercase(text)
    text = collapse_whitespace(text)
    return text

def transliteration_cleaners(text):  
    """Pipeline for non-English text that transliterates to ASCII."""
    text = convert_to_ascii(text)
    text = lowercase(text)
    text = collapse_whitespace(text)
    return text  

def custom_cleaners(text):
    """Custom pipeline for users to define their own cleaning."""
    return text

# Utility functions used by cleaners

def lowercase(text):
    """Convert text to lowercase."""
    return text.lower()

def convert_to_ascii(text):
    """Convert text to ASCII using unidecode."""
    return unidecode(text)

def collapse_whitespace(text):
    """Collapse multiple whitespace characters into a single space."""
    return re.sub(r'\s+', ' ', text)

def expand_abbreviations(text):
    """Expand common abbreviations."""
    for regex, replacement in _abbreviations:
        text = re.sub(regex, replacement, text)
    return text  

def expand_numbers(text):
    """Expand numbers into words."""
    return re.sub(r'\d+', lambda x: num2words(int(x.group())), text)

def latin_to_hangul(text):  
    """Convert Latin script to Hangul."""
    # Placeholder: Add your conversion logic
    return text

def number_to_hangul(text):
    """Convert numbers to Hangul representation."""
    return text

# Abbreviations to expand

_abbreviations = [
    (re.compile(r'\bmrs\.', re.IGNORECASE), 'misess'),
    (re.compile(r'\bmr\.', re.IGNORECASE), 'mister'),
    (re.compile(r'\bdr\.', re.IGNORECASE), 'doctor'),
    (re.compile(r'\bst\.', re.IGNORECASE), 'saint'),
    (re.compile(r'\bco\.', re.IGNORECASE), 'company'),
    (re.compile(r'\bjr\.', re.IGNORECASE), 'junior'),
    (re.compile(r'\bmaj\.', re.IGNORECASE), 'major'),
    (re.compile(r'\bgen\.', re.IGNORECASE), 'general'),
    (re.compile(r'\bdrs\.', re.IGNORECASE), 'doctors'),
    (re.compile(r'\brev\.', re.IGNORECASE), 'reverend'),
    (re.compile(r'\blt\.', re.IGNORECASE), 'lieutenant'),
    (re.compile(r'\bhon\.', re.IGNORECASE), 'honorable'),
    (re.compile(r'\bsgt\.', re.IGNORECASE), 'sergeant'),
    (re.compile(r'\bcapt\.', re.IGNORECASE), 'captain'),
    (re.compile(r'\besq\.', re.IGNORECASE), 'esquire'),
    (re.compile(r'\bltd\.', re.IGNORECASE), 'limited'),
    (re.compile(r'\bcol\.', re.IGNORECASE), 'colonel'),
    (re.compile(r'\bft\.', re.IGNORECASE), 'fort'),
]

# Testing the cleaners
if __name__ == "__main__":
    test_text = "Dr. John is a well-known figure in St. Mary's Church. He has 2 cats."
    cleaned_text = _clean_text(test_text, ['english_cleaners'])
    logger.info(f"Cleaned text: {cleaned_text}")
