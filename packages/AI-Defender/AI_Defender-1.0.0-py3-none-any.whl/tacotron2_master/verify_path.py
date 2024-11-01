# In tacotron2_master/verify_path.py

import os

resource_path = os.path.join(os.path.dirname(__file__), 'cmudict.txt')
if os.path.exists(resource_path):
    print(f"File found: {resource_path}")
else:
    print(f"File not found: {resource_path}")
