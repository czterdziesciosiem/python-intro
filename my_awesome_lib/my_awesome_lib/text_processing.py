# my_awesome_lib/text_processing.py

import re

def count_words(text):
    """
    Zlicza liczbę słów w tekście, traktując słowo jako ciąg znaków oddzielony spacjami lub znakami interpunkcyjnymi.
    
    :param text: Tekst, w którym będą liczone słowa.
    :return: Liczba słów w tekście.
    """
    # Usuwamy interpunkcję na końcu słów, ale nie w środku
    text = re.sub(r'[^\w\s]', '', text)
    words = text.split()
    return len(words)




 
