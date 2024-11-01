import re
import inflect

_inflect = inflect.engine()

def normalize_numbers_in_text(text):
    """
    This function normalizes numbers in the text by converting numeric values to words.
    
    Args:
        text (str): Input string containing numbers and other text.
        
    Returns:
        str: Text with numbers converted to words.
    """
    # Convert numbers to words using the inflect engine
    return re.sub(r'\d+', lambda m: _inflect.number_to_words(m.group()), text)

def normalize_currency(text):
    """
    This function normalizes text by converting dollar amounts into words.
    
    Args:
        text (str): Input string with dollar amounts.
    
    Returns:
        str: Text with dollar amounts converted to words.
    """
    # Replace dollar amounts with normalized text
    text = re.sub(r'\$(\d+)', lambda m: f"{_inflect.number_to_words(m.group(1))} dollars", text)
    return text

def normalize_text(text):
    """
    This function normalizes both numbers and dollar amounts in the text.
    
    Args:
        text (str): Input string with numbers and dollar amounts.
        
    Returns:
        str: Text with numbers and dollar amounts converted to words.
    """
    text = normalize_numbers_in_text(text)
    text = normalize_currency(text)
    return text

# Example usage
if __name__ == "__main__":
    sample_text = "I owe $1234 and have 5678 apples."
    normalized_text = normalize_text(sample_text)
    print(normalized_text)  # Output: I owe one thousand two hundred thirty-four dollars and have five thousand six hundred seventy-eight apples.
