"""
Przykład użycia biblioteki spaCy.
Wymagana instalacja:
    pip install spacy
    python -m spacy download en_core_web_sm
"""

import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("Apple is looking at buying a UK startup for $1 billion.")

# Tokenizacja i analiza składniowa
print("Tokeny i części mowy:")
for token in doc:
    print(f"{token.text:12} {token.pos_:10} {token.dep_}")

print("\nRozpoznane byty (NER):")
for ent in doc.ents:
    print(f"{ent.text:20} {ent.label_}")
