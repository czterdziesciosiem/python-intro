# Raport z analizy wielokryterialnej (MCDM)

## 1. Konfiguracja analizy

- Biblioteka: `pymcdm`
- Metody decyzyjne: `TOPSIS`, `SPOTIS`
- Normalizacja: `minmax_normalization`
- Wagi: wyznaczone metodą `entropy`
- Liczba alternatyw: 4 (A1–A4)
- Liczba kryteriów: 3
- Typy kryteriów: [-1, 1, -1] (koszt – min, zysk – max, czas – min)

## 2. Macierz decyzyjna (data)

| Alternatywa | Koszt | Zysk | Czas |
|-------------|-------|------|------|
| A1          | 250   | 16   | 12   |
| A2          | 200   | 20   | 8    |
| A3          | 300   | 18   | 10   |
| A4          | 275   | 22   | 9    |

## 3. Wagi (metoda entropii)

[0.4764, 0.1670, 0.3566]

## 4. Wyniki

| Alternatywa | TOPSIS | SPOTIS | TOPSIS rank | SPOTIS rank |
|-------------|--------|--------|-------------|-------------|
| A4          | 0.5290 | 0.4443 | 1           | 2           |
| A2          | 0.5279 | 0.4000 | 2           | 1           |
| A3          | 0.4721 | 0.6000 | 3           | 4           |
| A1          | 0.4090 | 0.5857 | 4           | 3           |

## 5. Wnioski

- **TOPSIS** wskazuje, że najlepszą alternatywą jest **A4**.
- **SPOTIS** jako najlepszą wskazuje **A2**.
- Obie metody uznają A3 i A1 za mniej korzystne, choć w odwrotnej kolejności.
- Różnice wynikają z odmiennych mechanizmów obu metod (TOPSIS – idealne rozwiązanie, SPOTIS – odległość od punktu odniesienia).
- Największy wpływ na decyzję miało kryterium **kosztu** (waga 0.4764).

## 6. Pliki

- `zad4.py` – kod analizy
- `zad4.md` – ten raport
