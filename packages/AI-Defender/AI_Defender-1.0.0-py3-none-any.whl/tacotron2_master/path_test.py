import sys
import os

# Append the main directory to sys.path for imports
try:
    # Test if we can import all modules without any issues
    from .model import Tacotron2
    from .utils_custom import dynamic_range_compression
    from .cmudict import CMUDict

    print("All imports are successful.")

    # Check if the CMU dictionary file is located correctly
    import os
    cmu_dict_path = os.path.join(os.path.dirname(__file__), 'cmudict.txt')
    if os.path.exists(cmu_dict_path):
        print("CMU Dictionary found successfully.")
    else:
        print("Error: CMU Dictionary not found at the expected location.")

except ImportError as e:
    print(f"Import error: {e}")
except Exception as ex:
    print(f"Unexpected error: {ex}")

