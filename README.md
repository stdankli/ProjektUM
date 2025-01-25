# Rozpoznawanie cyfr z rysunku przy użyciu Flask i TensorFlow

## Opis

Aplikacja umożliwia użytkownikowi rysowanie cyfr na wirtualnym płótnie (canvas) w przeglądarce, a następnie przesyła obraz do serwera Flask, który korzysta z wytrenowanych modeli TensorFlow do rozpoznawania cyfr.

Aplikacja obsługuje trzy różne modele rozpoznawania cyfr:

- **M\_Koloch**
- **M\_Klimeczek**
- **M\_Dorosh**

Po rozpoznaniu aplikacja zwraca cyfrę przewidzianą przez wybrany model.

---

## Funkcjonalności

- Rysowanie cyfr na canvasie w przeglądarce.
- Wybór modelu, który ma być użyty do rozpoznania cyfry.
- Wysyłanie danych obrazu do serwera w formacie Base64.
- Rozpoznawanie cyfr przy użyciu modeli TensorFlow.
- Wyświetlanie wyniku w przeglądarce za pomocą popup okienka.

---

## Wymagania

### Backend

- Python 3.x
- Flask
- TensorFlow
- NumPy
- Pillow

### Frontend

- Przeglądarka obsługująca JavaScript

---

## Struktura projektu

```
/project_root
|
├── run.py               # Główny plik aplikacji Flask
├── M_Koloch.h5          # Model M_Koloch
├── M_Klimeczek2.h5      # Model M_Klimeczek
├── M_Dorosh.h5          # Model M_Dorosh
├── templates/
│   └── index.html       # Plik HTML z frontendem aplikacji
└── static/
    └── css/
        └── style.css    # Plik CSS do stylizacji
```

---

## Uruchomienie

1. Upewnij się, że masz zainstalowane wszystkie wymagane biblioteki. Możesz to zrobić za pomocą polecenia:
   ```bash
   pip install flask tensorflow numpy pillow
   ```
2. Uruchom aplikację Flask za pomocą polecenia:
   ```bash
   python run.py
   ```
3. Otwórz przeglądarkę i przejdź pod adres:
   ```
   http://127.0.0.1:5000
   ```
4. Rysuj cyfrę na canvasie.
5. Wybierz model do rozpoznania (przycisk: Koloch, Klimeczek lub Dorosh).
6. Poczekaj na wynik – rozpoznana cyfra pojawi się w alercie przeglądarki.

---

## Technologie użyte w projekcie

- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS, JavaScript
- **Uczenie maszynowe:** TensorFlow

### Autorzy:
- Michael Koloch
- Daniel Klimeczek
- Anastazja Dorosh
