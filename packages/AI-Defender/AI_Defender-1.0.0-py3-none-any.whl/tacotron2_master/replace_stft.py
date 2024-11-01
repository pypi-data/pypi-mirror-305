import os

def replace_in_file(file_path, old_str, new_str):
    # Try reading the file with utf-8 encoding
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
    except UnicodeDecodeError:
        # If utf-8 fails, fall back to a different encoding
        with open(file_path, "r", encoding="latin-1") as file:
            content = file.read()

    # Check if the old string exists in the file before replacing
    if old_str in content:
        print(f"Replacing in: {file_path}")
        content = content.replace(old_str, new_str)

        # Write the changes back to the file
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)
        print(f"Successfully replaced '{old_str}' with '{new_str}' in {file_path}")
    else:
        print(f"No occurrences of '{old_str}' found in {file_path}")

def replace_in_directory(directory, old_str, new_str, extensions):
    # Walk through all files in the directory
    for root, _, files in os.walk(directory):
        for file in files:
            # Only process files with the specified extensions
            if file.endswith(tuple(extensions)):
                file_path = os.path.join(root, file)
                replace_in_file(file_path, old_str, new_str)

# Configuration for replacing 'from GionyTTS' with the correct path
def fix_imports(directory, old_import, new_import, extensions):
    replace_in_directory(directory, old_import, new_import, extensions)

# Configuration
project_directory = "C:/Users/giony/Desktop/AI DEFENDER 2.1/GionyTTS"
old_import_string = "from ."
new_import_string = "from ."
file_extensions = [".py", ".json", ".txt"]  # Adjust extensions as needed

# Run the replacement for import paths
fix_imports(project_directory, old_import_string, new_import_string, file_extensions)
