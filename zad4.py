import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from pymcdm.methods import TOPSIS, SPOTIS
from pymcdm.normalizations import minmax_normalization
from pymcdm.weights import entropy_weights

# 1. Przygotowanie danych
data = np.array([
    [25000, 30000, 12],
    [30000, 35000, 10],
    [20000, 28000, 14],
    [27000, 33000, 11]
])

alternatives = ['A1', 'A2', 'A3', 'A4']
criteria = ['Koszt', 'Zysk', 'Czas']

# Wagi z góry ustalone
weights = np.array([0.4, 0.4, 0.2])

# Typy kryteriów: -1 - minimalizacja, 1 - maksymalizacja
criteria_types = [-1, 1, -1]

# 2. Normalizacja danych
norm_data = minmax_normalization(data, criteria_types)

# 3. Obliczanie metodą TOPSIS
topsis = TOPSIS()
topsis_scores = topsis(data, weights, criteria_types)

# 4. Obliczanie metodą SPOTIS – wymagane granice
bounds = [[min(data[:, i]), max(data[:, i])] for i in range(data.shape[1])]
spotis = SPOTIS(bounds)
spotis_scores = spotis(data, weights, criteria_types)

# 5. Tworzenie DataFrame z wynikami
results = pd.DataFrame({
    'Alternatywa': alternatives,
    'TOPSIS': topsis_scores,
    'SPOTIS': spotis_scores
})
results['TOPSIS_rank'] = results['TOPSIS'].rank(ascending=False)
results['SPOTIS_rank'] = results['SPOTIS'].rank(ascending=True)

print("\nWyniki analizy:")
print(results.sort_values('TOPSIS_rank'))

# 6. (Opcjonalnie) Wyznaczanie wag metodą entropy
entropy_w = entropy_weights(data, criteria_types)
print("\nEntropy weights:", entropy_w)

# 7. Wizualizacja wyników
plt.figure(figsize=(8, 5))
results.set_index('Alternatywa')[['TOPSIS', 'SPOTIS']].plot(kind='bar')
plt.title('Porównanie wyników TOPSIS i SPOTIS')
plt.ylabel('Ocena')
plt.tight_layout()
plt.show()
