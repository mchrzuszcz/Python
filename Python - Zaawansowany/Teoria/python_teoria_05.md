

# Python
## Teoria 5

---

* *timeit*, czyli pythonowy stoper

## Dygresja o *__main__*

---


```python
import math

print(__name__)      # nazwa skryptu
print(math.__name__) # nazwa zaimportowanego modułu
```

    __main__
    math



```python
# instrukcje z main
# z zaimportowanych modułów
# nie zostaną wywołane

if __name__ == "__main__":
    print("Hello World!")
```

    Hello World!


## *timeit*

---


```python
def silnia(n):
    """Zwraca silnię liczby n."""
    if n < 2:
        return 1 # 0! = 1, 1! = 1
    return n*silnia(n - 1)
```


```python
from timeit import timeit

# timeit(funkcja, setup, number) -> czas wykonania funkcji w s
# funkcja - funkcja do wykonania
# setup - konfiguracja
# number - liczba powtórzeń
timeit("silnia(10)", setup="from __main__ import silnia", number=10)
```




    3.7365999560279306e-05




```python
timeit("silnia(100)", setup="from __main__ import silnia", number=10)
```




    0.0004746449994854629



## *timeit* z linii komend

---

```py
# silnia.py

def silnia(n):
    """Zwraca silnię liczby n."""
    if n < 2:
        return 1 # 0! = 1, 1! = 1
    return n*silnia(n - 1)
```

* możemy przetestować naszą funkcję z linii komend

```
$ python -m timeit -n10 'from silnia import silnia; silnia(10)'
10 loops, best of 3: 9.11 usec per loop
```


## Koty Ali

---

* Pierwszego dnia Ala dostała jednego kota. Każdego kolejnego dnia dostaje o jednego więcej niż dnia poprzedniego. Ile kotów ma Ala po *n* dniach?
    * pierwszy dzień: 1
    * drugi dzień: 1 + 1
    * trzeci dzień: 1 + 1 + 1
    ...

## Koty Ali - algorytm I

---


```python
def licz_koty_v1(n):
    """Zwraca liczbę kotów po n dniach."""
    n_cats = 0                     # Ala nie ma kota
    for dzien in range(1, n + 1):  # pętla po dniach
        for koty in range(dzien):  # liczba kotów = nr dnia
            n_cats += 1            # dodaj kota
    return n_cats                  # dwie pętle -> n*n operacji
```


```python
%timeit -n3 licz_koty_v1(10000) # liczba kotów po 10 dniach
```

    3 loops, best of 3: 4.43 s per loop


## Koty Ali - algorytm II

---


```python
def licz_koty_v2(n):
    """Zwraca liczbę kotów po n dniach."""
    n_cats = 0                     # Ala nie ma kota
    for dzien in range(1, n + 1):  # pętla po dniach
        n_cats += dzien            # dodaj koty (= nr dnia)
    return n_cats                  # jedna pętla -> n operacji
```


```python
%timeit -n3 licz_koty_v2(10000) # liczba kotów po 10 dniach
```

    3 loops, best of 3: 904 µs per loop


## Koty Ali - algorytm III

---


```python
def licz_koty_v3(n):
    """Zwraca liczbę kotów po n dniach."""
    return n * (n + 1) // 2 # jedna operacja
```


```python
%timeit -n3 licz_koty_v3(10000) # liczba kotów po 10 dniach
```

    3 loops, best of 3: 535 ns per loop


## Koty Ali - algorytm IV

---


```python
def licz_koty_v4(n):
    """Zwraca liczbę kotów po n dniach."""
    koty = list(range(n + 1)) # n zmiennych w pamięci
    return sum(koty)          # jedna pętla -> n operacji
```


```python
%timeit -n3 licz_koty_v4(10000) # liczba kotów po 10 dniach
```

    3 loops, best of 3: 411 µs per loop




