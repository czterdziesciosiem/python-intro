import re
from datetime import datetime

def is_valid_email(email):
    """Sprawdza, czy e-mail jest poprawny."""
    return bool(re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email))

def calculate_area(width, height):
    """Oblicza pole prostokąta."""
    return width * height

def sort_numbers(numbers):
    """Sortuje listę liczb rosnąco."""
    return sorted(numbers)

def format_date(date_str):
    """Konwertuje datę z formatu YYYY-MM-DD na DD.MM.YYYY."""
    return datetime.strptime(date_str, "%Y-%m-%d").strftime("%d.%m.%Y")

def is_palindrome(text):
    """Sprawdza, czy dany tekst jest palindromem."""
    return text == text[::-1]
