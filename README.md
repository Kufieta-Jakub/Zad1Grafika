# Zad1Grafika
 
Zadanie #1 - podstawy operacji na obrazach w Pythonie (Akademia WSB).
 
Program wczytuje obraz rastrowy (zdalny lub lokalny), zmniejsza jego rozdzielczość o 50%, zamienia go na skalę szarości, obraca o 90° i wyświetla oryginał obok wyniku. Na końcu wypisuje macierz liczb obrazu wynikowego.
 
## Co robi program
 
1. Wczytuje obraz z internetu (`urllib`) lub z pliku lokalnego.
2. Wyświetla obraz oryginalny (`matplotlib`).
3. Zmniejsza rozdzielczość o 50% i konwertuje obraz do skali szarości (`cv2`).
4. Obraca obraz o 90°.
5. Wyświetla obraz wynikowy obok oryginału.
6. Wypisuje macierz obrazu w postaci tablicy liczb (0–255).
## Wymagania
 
- Python 3.8 lub nowszy
- Biblioteki: `opencv-python`, `matplotlib`, `numpy`
Przed uruchomieniem programu należy zainstalować poniższe biblioteki:
 
```bash
pip install opencv-python matplotlib numpy
```

 
## Zmiana obrazu
 
Na początku pliku `zadanie1_obrazy.py` znajduje się zmienna `SOURCE`. Można w niej podać adres URL obrazu albo ścieżkę do pliku lokalnego:
 
```python
SOURCE = "link do obrazu"
```
 
Obrazy pochodzą z [Wikimedia Commons]
 
## Użyte biblioteki
 
| Biblioteka | Zastosowanie |
|---|---|
| `urllib` | pobranie obrazu zdalnego |
| `opencv-python` (`cv2`) | zmiana rozmiaru, skala szarości, obrót |
| `numpy` | przechowywanie obrazu jako macierzy liczb |
| `matplotlib` | wyświetlanie obrazów |
 
## Autor
 
Projekt wykonany w ramach zajęć – Jakub Kufieta Gr1
