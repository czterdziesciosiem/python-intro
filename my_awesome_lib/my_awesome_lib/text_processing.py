# my_awesome_lib/text_processing.py

def count_words(text):
    """
    Zlicza liczbę słów w tekście, traktując słowo jako ciąg znaków alfanumerycznych oddzielony spacjami lub znakami interpunkcyjnymi.
    :param text: Tekst, w którym będą liczone słowa.
    :return: Liczba słów w tekście.
    """
    # Usuwamy nadmiarowe białe znaki na początku i końcu
    text = text.strip()

    # Usuwamy znaki interpunkcyjne tylko na końcach słów
    text = re.sub(r'\b[^\w\s]+|[^\w\s]+\b', '', text)

    # Zliczamy słowa
    words = re.findall(r'\b\w+\b', text)

    return len(words)















 
