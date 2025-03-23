# my_awesome_lib/data_utils.py

def convert_to_celsius(fahrenheit: float) -> float:
    """Konwertuje temperaturę z Fahrenheita na Celsjusza."""
    return (fahrenheit - 32) * 5.0/9.0

def flatten_list(nested_list: list) -> list:
    """Spłaszcza zagnieżdżoną listę."""
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result
 
