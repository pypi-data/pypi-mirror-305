import logging
from .cmudict import CMUDict  # Use relative import
import os

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def main():
    logger.info("Running Tacotron2 Master Initialization")

    # Example usage: Loading CMUdict
    try:
        # Construct the path to cmudict.txt relative to this file
        cmu_dict_path = os.path.join(os.path.dirname(__file__), 'cmudict.txt')
        logger.info(f"Loading CMU dictionary from path: {cmu_dict_path}")

        cmu_dict = CMUDict(cmu_dict_path)
        logger.info(f"Loaded CMU dictionary with {len(cmu_dict)} entries.")

        # Example: Look up pronunciation for a word
        word = 'hello'
        pronunciations = cmu_dict.lookup(word)
        if pronunciations:
            logger.info(f"Pronunciations for '{word}': {pronunciations}")
        else:
            logger.warning(f"No pronunciations found for '{word}'.")
            # Uncomment the following lines if you have a `guess_pronunciation` method
            # guessed_pronunciation = cmu_dict.guess_pronunciation(word.upper())
            # logger.info(f"Guessed pronunciation for '{word}': {guessed_pronunciation}")

    except Exception as e:
        logger.error(f"Error during CMUdict usage: {e}")

if __name__ == "__main__":
    main()
