# my_awesome_lib/text_processing.py

import re

def count_words(text: str) -> int:
    """Zlicza liczbę słów w tekście."""
    words = text.split()
    return len(words)

def remove_special_chars(text: str) -> str:
    """Usuwa znaki specjalne z tekstu."""
    return re.sub(r'[^a-zA-Z0-9\s]', '', text)
 
