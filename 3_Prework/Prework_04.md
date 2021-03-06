
# Python
## Prework do 4 listy zadań 

## Funkcja

---

Funkcja? Zestaw kodu, który powinnien wykonywać konkretną, zdefniowana czynność np. dodawać dwie cyfry.

```python
def dodaj_dwie_liczby(a,b):
    print("Dodaje dwie liczby: {} oraz {}".format(a,b))
    print("Wynik: {}".format(a+b))

>>> dodaj_dwie_liczby(1,1)
Dodaje dwie liczby: 1 oraz 1
Wynik: 2

```

Wzór składni funkcji:

```python
def nazwa_funkcji(parametr_1, parametr_n):
    kod funkcji
```

Funkcje powinny być pisane w sposób _single responsibility_ co oznacza, że funkcja powinna wykonywać jedną konkretną czynność. Oznacza to że jeśli funkcja dodaje dwie liczby to wykonuje tylko akcje dodawania, nie powinna mieć opcji odejmowania, dzielenia itd. Umożliwia to utrzymanie tzw. czytelności kodu.

## Argumenty Pozycyjne (args)

---

Argumenty są to wartości przekazywane do funkcji jako zmienne. 

Wzór:

```python
def funkcja(TUTAJ_DEFINIUJEMY_ARGUMENTY):
    pass
    
funkcja(TUTAJ_PRZEKAZUJEMY_WARTOSCI_JAKO_ARGUMENTY_FUNKCJI)

```

Argumenty pozycyjne to te, które sa definiowane/przekazywane względem pozycji.

```python
def funkcja(param_1, param_2):   
        [pozycja 1], [pozycja 2]
```



## Argumenty Kluczowe (kwargs)

---

Przykład:

```python
def funkcja(klucz="WARTOSC_DOMYSLNA_KLUCZA"):
    print(klucz)
    
>>> funkcja(klucz="WARTOSC")
WARTOSC
>>> funkcja()
WARTOSC_DOMYSLNA_KLUCZA

```

Argumenty kluczowe to te, które sa definiowane/przekazywane względem nazwy tak jak klucz w słowniku.

To by było na tyle, **zapraszam** na zajęcia!
