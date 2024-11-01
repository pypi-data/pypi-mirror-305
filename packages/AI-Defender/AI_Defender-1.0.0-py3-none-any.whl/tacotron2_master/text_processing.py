import os
import sys
import logging
from typing import Optional, Union, List
from pathlib import Path

# Configure paths
PROJECT_ROOT = Path(__file__).resolve().parent
sys.path.append(str(PROJECT_ROOT))

# Direct imports
import text_processing
import cmudict
import hparams
import model
import utils
import numpy

# Enhanced logging configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(PROJECT_ROOT / 'tacotron2.log')
    ]
)
logger = logging.getLogger(__name__)

class Tacotron2Master:
    def __init__(self, 
                 cmu_dict_path: Union[str, Path] = PROJECT_ROOT / 'resources/cmudict.txt',
                 model_path: Union[str, Path] = PROJECT_ROOT / 'checkpoints/model.pth'):
        """
        Initialize the Tacotron2 master module with enhanced path handling and type safety.
        
        Args:
            cmu_dict_path: Path to CMU dictionary file
            model_path: Path to pretrained model weights
        """
        self.model: Optional[model.Tacotron2] = None
        self.cmu_dict: Optional[cmudict.CMUDict] = None
        
        # Convert paths to Path objects
        self.cmu_dict_path = Path(cmu_dict_path)
        self.model_path = Path(model_path)
        
        # Initialize components
        self.load_cmudict(self.cmu_dict_path)
        self.load_model(self.model_path)

    def load_cmudict(self, path: Path) -> None:
        """
        Load CMU dictionary with enhanced error handling.
        """
        try:
            absolute_path = path.resolve(strict=True)
            self.cmu_dict = cmudict.CMUDict(str(absolute_path))
            logger.info(f"CMUDict loaded successfully: {len(self.cmu_dict)} words")
        except FileNotFoundError:
            logger.warning(f"CMUDict file not found: {path}")
            self.cmu_dict = None
        except Exception as e:
            logger.error(f"CMUDict loading error: {str(e)}")
            self.cmu_dict = None

    def load_model(self, model_path: Path) -> None:
        """
        Load Tacotron2 model with enhanced error handling.
        """
        try:
            absolute_path = model_path.resolve(strict=True)
            self.model = utils.load_model(str(absolute_path), hparams.hparams)
            logger.info(f"Tacotron2 model loaded: {absolute_path}")
        except FileNotFoundError:
            logger.error(f"Model file not found: {model_path}")
            self.model = None
        except Exception as e:
            logger.error(f"Model loading error: {str(e)}")
            self.model = None

    def synthesize(self, text: str) -> Optional[numpy.ndarray]:
        """
        Convert text to speech with comprehensive error handling.
        """
        if not self.model:
            logger.error("Model not loaded - synthesis unavailable")
            return None
        
        try:
            logger.info(f"Processing text: {text}")
            sequence = text_processing.text_to_sequence(text, cmu_dict=self.cmu_dict)
            
            if not sequence:
                logger.error("Text to sequence conversion failed")
                return None
                
            logger.info(f"Sequence generated: length={len(sequence)}")
            audio = utils.synthesize_audio(self.model, sequence)
            logger.info("Audio synthesis completed")
            return audio
            
        except Exception as e:
            logger.error(f"Synthesis error: {str(e)}")
            return None

    def lookup_word_pronunciation(self, word: str) -> Optional[List[str]]:
        """
        Look up word pronunciation with enhanced error handling.
        """
        if not self.cmu_dict:
            logger.error("CMUDict not loaded - lookup unavailable")
            return None
            
        try:
            pronunciation = self.cmu_dict.lookup(word)
            if pronunciation:
                logger.info(f"Found pronunciation: {word} → {' '.join(pronunciation)}")
                return pronunciation
            logger.warning(f"No pronunciation found: {word}")
            return None
            
        except Exception as e:
            logger.error(f"Pronunciation lookup error: {str(e)}")
            return None

def main():
    """
    Main execution with enhanced error handling and status reporting.
    """
    try:
        # Initialize paths
        cmu_dict_path = PROJECT_ROOT / 'resources/cmudict.txt'
        model_path = PROJECT_ROOT / 'checkpoints/model.pth'

        # Create Tacotron2 instance
        tacotron2 = Tacotron2Master(cmu_dict_path, model_path)

        # Test synthesis
        input_text = "Hello, how are you?"
        if audio := tacotron2.synthesize(input_text):
            print("✓ Audio synthesis successful")
        else:
            print("✗ Audio synthesis failed")

        # Test pronunciation lookup
        if pronunciation := tacotron2.lookup_word_pronunciation("hello"):
            print(f"✓ Pronunciation found: {' '.join(pronunciation)}")
        else:
            print("✗ Pronunciation lookup failed")
            
    except Exception as e:
        logger.critical(f"Critical error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
