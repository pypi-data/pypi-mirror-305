import os
import sys
import logging
from typing import Optional, Union, List
from pathlib import Path

# Add the parent directory to system path to enable imports
current_dir = Path(__file__).resolve().parent
if str(current_dir) not in sys.path:
    sys.path.append(str(current_dir))

# Local imports
import text_processing
import cmudict
import hparams
import model
import utils

# Setup logging with more detailed configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('tacotron2.log')
    ]
)
logger = logging.getLogger(__name__)

class Tacotron2Master:
    def __init__(self, 
                 cmu_dict_path: Union[str, Path] = 'resources/cmudict.txt',
                 model_path: Union[str, Path] = 'checkpoints/model.pth'):
        """
        Initialize the Tacotron2 master module with enhanced path handling and type safety.
        
        Args:
            cmu_dict_path: Path to CMU dictionary file
            model_path: Path to pretrained model weights
        """
        self.model: Optional[model.Tacotron2] = None
        self.cmu_dict: Optional[cmudict.CMUDict] = None
        
        # Convert paths to Path objects for robust path handling
        self.cmu_dict_path = Path(cmu_dict_path)
        self.model_path = Path(model_path)
        
        # Initialize components
        self.load_cmudict(self.cmu_dict_path)
        self.load_model(self.model_path)

    def load_cmudict(self, path: Path) -> None:
        """
        Load CMU dictionary with enhanced error handling.
        
        Args:
            path: Path to the CMU dictionary file
        """
        try:
            absolute_path = path.resolve(strict=True)
            self.cmu_dict = cmudict.CMUDict(str(absolute_path))
            logger.info(f"Successfully loaded CMUDict with {len(self.cmu_dict)} words.")
        except FileNotFoundError:
            logger.warning(f"CMUDict file not found at {path}")
            self.cmu_dict = None
        except Exception as e:
            logger.error(f"Error loading CMUDict: {str(e)}")
            self.cmu_dict = None

    def load_model(self, model_path: Path) -> None:
        """
        Load Tacotron2 model with enhanced error handling.
        
        Args:
            model_path: Path to the model weights file
        """
        try:
            absolute_path = model_path.resolve(strict=True)
            self.model = utils.load_model(str(absolute_path), hparams.hparams)
            logger.info(f"Successfully loaded Tacotron2 model from {absolute_path}")
        except FileNotFoundError:
            logger.error(f"Model file not found at {model_path}")
            self.model = None
        except Exception as e:
            logger.error(f"Error loading model: {str(e)}")
            self.model = None

    def synthesize(self, text: str) -> Optional[numpy.ndarray]:
        """
        Convert text to speech with comprehensive error handling.
        
        Args:
            text: Input text to synthesize
            
        Returns:
            Synthesized audio array if successful, None otherwise
        """
        if not self.model:
            logger.error("Model not loaded. Cannot synthesize speech.")
            return None
        
        try:
            logger.info(f"Processing text: {text}")
            sequence = text_processing.text_to_sequence(text, cmu_dict=self.cmu_dict)
            
            if not sequence:
                logger.error("Text to sequence conversion failed")
                return None
                
            logger.info(f"Generated sequence length: {len(sequence)}")
            audio = utils.synthesize_audio(self.model, sequence)
            logger.info("Audio synthesis successful")
            return audio
            
        except Exception as e:
            logger.error(f"Speech synthesis failed: {str(e)}")
            return None

    def lookup_word_pronunciation(self, word: str) -> Optional[List[str]]:
        """
        Look up word pronunciation with enhanced error handling.
        
        Args:
            word: Word to look up
            
        Returns:
            List of pronunciation tokens if found, None otherwise
        """
        if not self.cmu_dict:
            logger.error("CMUDict not loaded. Cannot look up pronunciation.")
            return None
            
        try:
            pronunciation = self.cmu_dict.lookup(word)
            if pronunciation:
                logger.info(f"Found pronunciation for '{word}': {' '.join(pronunciation)}")
                return pronunciation
            logger.warning(f"No pronunciation found for '{word}'")
            return None
            
        except Exception as e:
            logger.error(f"Pronunciation lookup failed: {str(e)}")
            return None

if __name__ == "__main__":
    try:
        # Example usage with robust error handling
        cmu_dict_path = Path('resources/cmudict.txt')
        model_path = Path('checkpoints/model.pth')

        tacotron2 = Tacotron2Master(cmu_dict_path, model_path)

        # Synthesis example
        input_text = "Hello, how are you?"
        if audio := tacotron2.synthesize(input_text):
            print("✓ Audio synthesis successful")
        else:
            print("✗ Audio synthesis failed")

        # Pronunciation lookup example
        if pronunciation := tacotron2.lookup_word_pronunciation("hello"):
            print(f"✓ Pronunciation: {' '.join(pronunciation)}")
        else:
            print("✗ Pronunciation lookup failed")
            
    except Exception as e:
        logger.critical(f"Application error: {str(e)}")
        sys.exit(1)
