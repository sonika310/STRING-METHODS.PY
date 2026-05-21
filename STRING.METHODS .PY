: Convert a string to uppercase

def convert_to_uppercase(text):
    """
    Converts a given string to uppercase.
    """
    return text.upper()

# Example usage:
print(convert_to_uppercase("hello world"))  # Output: HELLO WORLD

2: Replace substrings

def replace_substring(original_string, old_substring, new_substring):
    """
    Replaces all occurrences of old_substring with new_substring.
    """
    return original_string.replace(old_substring, new_substring)

# Example usage:
print(replace_substring("I like apples", "apples", "bananas"))  # Output: I like bananas

3: Check if a string starts with a specific substring

def check_starts_with(text, prefix):
    """
    Checks if the text starts with the specified prefix.
    """
    return text.startswith(prefix)

# Example usage:
print(check_starts_with("Python programming", "Python"))  # Output: True
print(check_starts_with("Python programming", "Java"))    # Output: False
