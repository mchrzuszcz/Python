# Python

## Projekt - Gra Krowy i Byki

### Opis

Stwórz skrypt, który zagra z użytkownikiem w gre Krowy i Byki. Gra polega na tym, że skrypt:

1. Losuje 4-cyfrową liczbę.
2. Prosi użytkownika o podanie 4-cyfrowej liczby.
3. Skrypt sprawdza:  
    - każdą odgadniętą cyfrę w poprawnym miejscu i daje 1 krowę za prawidłowe odgadnięcie.
    - każdą odgadnięta cyfrę ale nie w poprawnym miejscu i daję za to 1 byka. 
4. Przy każdej próbie odgadnięcia informuje użytkownika o liczbie krów i byków.
5. Zlicza próby odgadnięcia liczby.
6. Kiedy użytkownik odgadnie wylosowaną liczbę, gra powinna się zakończyć.

Kroki od 2 do 5 włącznie powinny być powtarzane do momentu aż użytkownik nie odgadnie wylosowanej liczby.

<b>Przykład:</b>

Zakładamy że wylosowana liczba to: 9876.

```python
Witam w grze Krowy i Byki!
>>> Podaj liczbe: 1234
Krowy: 0, Byki: 0
>>> Podaj liczbe: 9811
Krowy: 2, Byki: 0
>>> Podaj liczbe: 9817
Krowy: 2, Byki: 1
>>> Podaj liczbe: 9876
Wygrales! Koniec Gry! Liczba prob: 4. 
```

<b>Powodzenia!</b>
