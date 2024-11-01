import os
import logging

# Set up logging
logger = logging.getLogger(__name__)

class CMUDict:
    """
    A class to handle operations related to the CMU Pronouncing Dictionary.

    Attributes:
        dictionary (dict): A dictionary with words as keys and lists of ARPAbet phoneme sequences as values.
    """

    def __init__(self, file_path=None, dictionary=None):
        """
        Initializes the CMUDict class by loading the dictionary from a file or from a given dictionary.

        Args:
            file_path (str): The path to the CMU dictionary file.
            dictionary (dict): A dictionary to initialize the CMUDict directly.
        """
        self.dictionary = dictionary if dictionary else {}

        if file_path:
            if not os.path.isfile(file_path):
                logger.error(f"CMUDict file not found at {file_path}")
                raise FileNotFoundError(f"CMUDict file not found at {file_path}")

            logger.info(f"Loading CMUDict from: {file_path}")
            try:
                with open(file_path, encoding='latin-1') as f:
                    for line in f:
                        # Skip comments
                        if line.startswith(';'):
                            continue
                        # Split word and pronunciation
                        parts = line.strip().split('  ')
                        if len(parts) == 2:
                            word, pronunciation = parts
                            self.dictionary[word.lower()] = pronunciation.split()
                logger.info(f"CMUDict successfully loaded with {len(self.dictionary)} entries.")
            except Exception as e:
                logger.error(f"Failed to load CMUDict: {e}")
                raise

    def lookup(self, word):
        """
        Look up the word in the CMU dictionary.

        Args:
            word (str): The word to look up.

        Returns:
            list: A list of ARPAbet phonemes for the word, or None if not found.
        """
        return self.dictionary.get(word.lower())

    def add_word(self, word, pronunciation):
        """
        Adds a new word and its pronunciation to the dictionary.

        Args:
            word (str): The word to add.
            pronunciation (list of str): The pronunciation of the word as a list of ARPAbet phonemes.
        """
        if word.lower() in self.dictionary:
            logger.warning(f"Word '{word}' already exists in the dictionary. Overwriting.")
        self.dictionary[word.lower()] = pronunciation
        logger.info(f"Added word '{word}' with pronunciation: {' '.join(pronunciation)}")

    def save_to_file(self, file_path):
        """
        Saves the current dictionary to a file.

        Args:
            file_path (str): The path to save the CMU dictionary.
        """
        try:
            with open(file_path, 'w', encoding='latin-1') as f:
                for word, pronunciation in self.dictionary.items():
                    f.write(f"{word.upper()}  {' '.join(pronunciation)}\n")
            logger.info(f"CMUDict successfully saved to {file_path}")
        except Exception as e:
            logger.error(f"Failed to save CMUDict: {e}")
            raise

    def guess_pronunciation(self, word):
        """
        Generate a guessed pronunciation for a word using simple heuristic rules.

        Args:
            word (str): The word for which to guess the pronunciation.

        Returns:
            list: A list of ARPAbet phonemes representing the guessed pronunciation.
        """
        logger.info(f"Guessing pronunciation for word '{word}'")
        # A simple heuristic for guessing pronunciations (e.g., breaking into individual letters).
        guessed_pronunciation = [f"{char}" for char in word]
        logger.info(f"Guessed pronunciation for '{word}': {' '.join(guessed_pronunciation)}")
        return guessed_pronunciation

# Utility function to load CMU dictionary from a file
def load_cmu_dict_from_file(file_path):
    """
    Utility function to load the CMU dictionary.

    Args:
        file_path (str): The path to the CMU dictionary file.

    Returns:
        CMUDict: An instance of the CMUDict class.
    """
    return CMUDict(file_path)

# Example Usage:
if __name__ == "__main__":
    # Example path - update with the actual path to your dictionary file
    cmu_dict_path = r"D:\ai\AI DEFENDER 2.1\tacotron2_master\resources\cmudict.txt"

    # Create an instance of CMUDict
    try:
        cmu_dict = load_cmu_dict_from_file(cmu_dict_path)
    except FileNotFoundError:
        logger.error(f"Failed to find CMU dictionary at {cmu_dict_path}")

    # Test lookup
    word = "Hello"
    pronunciation = cmu_dict.lookup(word)
    if pronunciation:
        logger.info(f"Pronunciation for '{word}': {' '.join(pronunciation)}")
    else:
        logger.warning(f"Word '{word}' not found in CMUDict. Generating a guess.")
        guessed_pronunciation = cmu_dict.guess_pronunciation(word)
        logger.info(f"Guessed Pronunciation: {' '.join(guessed_pronunciation)}")
