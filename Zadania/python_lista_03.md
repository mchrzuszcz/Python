# Języki skryptowe - Python
# Lista 3

---

Zad 1

Wykorzystaj listę składaną (*list comprehension*), aby stworzyć sekwencję kwadratów liczb naturalnych mniejszych od 100. Następnie (korzystając z *enumerate*) wydrukuj na ekranie:

```
1 -> 1
2 -> 4
3 -> 9
.
.
.
```

---

Zad 2.

Przeanalizuj poniższy kod:


```py
#!/usr/bin/env python

i = 0

# drukujemy wszystkie liczby parzyste mniejsze od 10
while i < 10:
    if i % 2:    # reszta z dzielenia != 0 -> True
        continue # pomiń liczby nieparzyste
    else:
        print(i) # drukuj liczby parzyste

    i += 1 # zwiększ i o jeden
```

* Czy skrypt będzie działał zgodnie z założeniami? Jeśli nie, to napraw go.

---

Zad 3.

Uzupełnij skrypt o brakujące fragmenty:


```py

#!/usr/bin/env python

# lista zakupów
grocery = ['jajka', 'mleko', 'chleb', 'maslo', 'piwo']
# ilość sztuk
n_items = {}
# zakazane produkty
prohibited = ['wódka', 'piwo', 'wino']

# w pętli pytamy użytkownika, ile sztuk danego produktu chce kupić
for product in grocery:
    # wydrukuj na ekranie komunikat: "Produkt [nazwa produktu]: sztuk = "
    # pobierz liczbę od użytkownika i zapisz w n_items dla danego produktu
    # pomiń produkty zakazane (i automatycznie przyjmij ilość = 0)

# w pętli wydrukuj: [lp]. [nazwa produktu]: [ilość]
# czyli np.: 1. jajka: 5 itd.
```

---

Zad 4.

Napisz skrypt, który:

- losuje liczbę całkowitą mniejszą od 100 (`help(random.randint)`)
- pyta użytkownika o odgadnięcie liczby
- informuje użytkownika, czy podana przez niego liczba jest:
    - dużo mniejsza (różnica > 50)
    - mniejsza (różnica > 10)
    - trochę mniejsza
    - trochę większa
    - większa (różnica > 10)
    - dużo większa (różnica > 50)
- program się kończy, gdy użytkownik odgadnie wylosowaną liczbę


---

Zad 5.

Poniższy skrypt narysuje kwadrat:

```py
#!/usr/bin/env python

import turtle

length = eval(input("Podaj dł\lugosc boku: "))
n_sides = 4 # ilosc boków

turtle.speed(20) # ustal predkosc zolwia

# powtorz n_sides razy
for i in range(n_sides):
    turtle.forward(length) # narysuj linie o danej dlugosci
    turtle.right(90)       # obroc sie w prawo o dany kat

turtle.mainloop() # nie zamykaj okna po narysowaniu
```

5.1 zmodyfikuj go tak, aby narysował trójkąt równoboczny
5.2 zmodyfikuj go tak, aby narysował sześciokąt foremny
5.3 zmodyfikuj go tak, aby narysował wielokąt foremny, którego liczba boków podana jest przez użytkownika

