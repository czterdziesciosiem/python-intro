"""
Przykład użycia biblioteki TextBlob.
Wymagana instalacja:
    pip install textblob
    python -m textblob.download_corpora
"""

from textblob import TextBlob

text = TextBlob("I really enjoy learning natural language processing.")

# Analiza sentymentu
print("Sentyment (polaryzacja, subiektywność):")
print(text.sentiment)


