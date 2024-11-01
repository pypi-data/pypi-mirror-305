import logging
import os
from cmudict import CMUDict

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
def main():
    # Correct the resource path to match the directory inside Docker
    resource_path = "resources/cmudict.txt"  # Updated to match the directory structure

    # Debugging output
    logging.info(f"Resource path for CMUDict: {resource_path}")

    # Check if the CMU dictionary file exists
    if not os.path.exists(resource_path):
        logging.error(f"CMUDict file not found at {resource_path}")
        return

    # Load the CMUDict
    try:
        cmu_dict = CMUDict(resource_path)
        logging.info(f"CMUDict loaded with {len(cmu_dict)} entries.")
    except Exception as e:
        logging.error(f"Error loading CMUDict: {e}")

if __name__ == "__main__":
    main()
