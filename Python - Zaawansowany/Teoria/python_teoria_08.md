
# Python
## Teoria 8

---

* Błędy i wyjątki
* Operacje na plikach

## Błędy (*bug*)

---

> Without requirements or design, programming is the art of adding bugs to an empty text file.

> *Louis Srygley*

* błędy leksykalne i składniowe
* błędy typowania
* błędy semantyczne i logiczne
* błędy działania
* nieskończone obliczenia

## Błędy leksykalne (*syntax error*)

---

* pojedyncza jednostka leksykalna, której nie przewiduje definicja języka


```python
x = 1
x++ # operator ++ nie istnieje
```


      File "<ipython-input-1-c2b85b799f03>", line 2
        x++ # operator ++ nie istnieje
                                      ^
    SyntaxError: invalid syntax



## Błędy składniowe (*syntax error*)

---

* niepoprawnie zestawione poprawne jednostki leksykalne 


```python
if True                   # brakuje :
    print("Hello World")) # dodatkowy )
```


      File "<ipython-input-2-3cc3ffe6806b>", line 1
        if True                   # brakuje :
                                             ^
    SyntaxError: invalid syntax



## Błędy typowania

---

* wyrażenie nieadekwatne do typu


```python
x = 1

x[0] = 2 # x nie jest sekwencyjnym typem danych
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-3-4bf6b631916d> in <module>()
          1 x = 1
          2 
    ----> 3 x[0] = 2 # x nie jest sekwencyjnym typem danych
    

    TypeError: 'int' object does not support item assignment


## Błędy działania (*runtime error*)

---

* pojawiają się w trakcie działania programu (np. odczyt z pliku, który nie istnieje)


```python
def iloraz(a, b):
    """Zwraca a / b"""
    return a / b

iloraz(10, 0) # dzielenie przez 0
```


    ---------------------------------------------------------------------------

    ZeroDivisionError                         Traceback (most recent call last)

    <ipython-input-4-976842d0fc36> in <module>()
          3     return a / b
          4 
    ----> 5 iloraz(10, 0) # dzielenie przez 0
    

    <ipython-input-4-976842d0fc36> in iloraz(a, b)
          1 def iloraz(a, b):
          2     """Zwraca a / b"""
    ----> 3     return a / b
          4 
          5 iloraz(10, 0) # dzielenie przez 0


    ZeroDivisionError: division by zero


## Błędy semantyczne (*semantic error*)

---

* niezgodność oczekiwań ze stanem faktycznym


```python
def dzialanie(a, b, c):
    """Zwraca iloraz a przez sumę b i c."""
    return a / b + c # zamiast a / (b + c)
```

## Błędy logiczne

---

* program liczy nie to co trzeba (w tym też błędy semantyczne)
* najtrudniejsze do znalezienia


```python
def delta(a, b, c):
    """Liczy wyróżnik trójmianu kwadratowego."""
    return b - 4*a*c # zamiast b*b - 4*a*c
```

## Nieskończone pętle

---


```python
def loop(i = 0):
    while i < 10:
        i -= 1 # i zawsze będzie mniejsze od 10
```

## Therac-25

---

* maszyna do radioterapii nowotworów
* na skutek błędów programistycznych kilka osób zmarło na skutek napromieniowania
* błąd typu *race condition* - przy zbyt szybkim wprowadzaniu danych (przez operatora) parametry zabiegu nie były prawidłowo inicjowane

## Zapobieganie błędom

---

* pisanie czytelnego kodu
* *code review*
* debugowanie

## Czytelność kodu

---

* zrozumiałe nazwy zmiennych (nawet kosztem długości)
* komentowanie kodu źródłowego, który nie jest zrozumiały od razu
* tworzenie dokumentacji w trakcie pisania programu
* opisywanie przyjętych założeń (w komentarzach i/lub dokumentacji)

## *Code review*

---

* sprawdzenie kodu przez inną osobę - poniższy link przedstawia typową sytuację w pracy, zrozumiecie jak zobaczycie na własne oczy ;)

![](../Materialy_Pomocnicze/code_review.jpg)

## Debugowanie

---

> If debugging is the process of removing software bugs, then programming must be the process of putting them in. 

> *Edsger Dijkstra*

* systematyczne redukowanie błędów w kodzie
* kontrolowane wykonanie programu
* debugger

## \_\_debug\_\_

---


```python

# __debug__ - wbudowana stała
# równa True - jeśli uruchomione bez -O (optimize)

if __debug__:
    print("Jestem w trybie debugowania.")
else:
    print("Jestem w trybie normalnym.")
```

    Overwriting debug.py



```python
python debug.py
```

    Jestem w trybie debugowania.



```python
python -O debug.py
```

    Jestem w trybie normalnym.


## Przykład

---


```python
"""Wyznacza pierwsze wyrazy ciągu Fibonacciego."""

fib = [0, 1]

for i in range(10):
    if not __debug__:
        print("i =", i)
        print("fib =", fib)
        print("fib[i-2] =", fib[i-2])
        print("fib[i-1] =", fib[i-1])
        print()
    
    fib.append(fib[i-2] + fib[i-1])

print(fib) # [0, 1, 1, 2, 3, 5, 8, 13, ...]
```

```python
python fib.py
```

    [0, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 5]


## Przykład - *debug mode*

---


```python
python -O fib.py
```

    i = 0
    fib = [0, 1]
    fib[i-2] = 0
    fib[i-1] = 1
    
    i = 1
    fib = [0, 1, 1]
    fib[i-2] = 1
    fib[i-1] = 0
    
    i = 2
    fib = [0, 1, 1, 1]
    fib[i-2] = 0
    fib[i-1] = 1
    
    i = 3
    fib = [0, 1, 1, 1, 1]
    fib[i-2] = 1
    fib[i-1] = 1
    
    i = 4
    fib = [0, 1, 1, 1, 1, 2]
    fib[i-2] = 1
    fib[i-1] = 1
    
    i = 5
    fib = [0, 1, 1, 1, 1, 2, 2]
    fib[i-2] = 1
    fib[i-1] = 1
    
    i = 6
    fib = [0, 1, 1, 1, 1, 2, 2, 2]
    fib[i-2] = 1
    fib[i-1] = 2
    
    i = 7
    fib = [0, 1, 1, 1, 1, 2, 2, 2, 3]
    fib[i-2] = 2
    fib[i-1] = 2
    
    i = 8
    fib = [0, 1, 1, 1, 1, 2, 2, 2, 3, 4]
    fib[i-2] = 2
    fib[i-1] = 2
    
    i = 9
    fib = [0, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4]
    fib[i-2] = 2
    fib[i-1] = 3
    
    [0, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 5]


## Wbudowany debugger

---


```python

import pdb # wbudowany debugger

pdb.set_trace() # zacznij debugować

fib = [0, 1]

for i in range(10):
    fib.append(fib[i-2] + fib[i-1])

print(fib) # [0, 1, 1, 2, 3, 5, 8, 13, ...]
```


## pdb

---

* *n* - następna instrukcja
* *s* - wejdź w funkcję
* *r* - wyjdź z funkcji
* *p* - wydrukuj zmienną
* *q* - przerwij
* *enter* - powtórz ostatnią komendę
* ...

## Wyjątki (*exceptions*)

---

* błędy działania (*runtime error*)
* wykryte podczas wykonywania są nazywane wyjątkami
* programista może decydować co robić z wyjątkami

## Przykład - iloraz

---


```python
def iloraz(a, b):
    """Zwraca a / b"""
    return a / b
```


```python
iloraz(10, 2)
```




    5.0




```python
iloraz(10, 0)
```


    ---------------------------------------------------------------------------

    ZeroDivisionError                         Traceback (most recent call last)

    <ipython-input-17-0a93c896245e> in <module>()
    ----> 1 iloraz(10, 0)
    

    <ipython-input-15-a5a78f530c06> in iloraz(a, b)
          1 def iloraz(a, b):
          2     """Zwraca a / b"""
    ----> 3     return a / b
    

    ZeroDivisionError: division by zero


## Iloraz - zabezpiecznie *if*

---


```python
def iloraz(a, b):
    """Zwraca a / b lub zero, jeśli b = 0."""
    if b == 0: # można tak, ale lepiej korzystać z wyjątków
        return 0
    return a / b
```


```python
iloraz(10, 2)
```




    5.0




```python
iloraz(10, 0)
```




    0



## Iloraz - *wyjątek*

---


```python
def iloraz(a, b):
    """Zwraca a / b lub zero, jeśli b = 0."""
    try:    # spróbuj
        return a / b
    except: # jeśli error to
        return 0
```


```python
iloraz(10, 2)
```




    5.0




```python
iloraz(10, 0)
```




    0



## Przykład - pobierz liczbę całkowitą

---


```python
while True:
    try:    # spróbuj rzutować na int
        x = int(input("Podaj liczbę: "))
        break
    except: # jeśli się nie uda to
        print("Spróbuj jeszcze raz.")
```

    Podaj liczbę: a
    Spróbuj jeszcze raz.
    Podaj liczbę: 1.0
    Spróbuj jeszcze raz.
    Podaj liczbę: 1


## Typy wyjątków

---

* pełna lista wbudowanych wyjątków [link](https://docs.python.org/3/library/exceptions.html#bltin-exceptions)


```python
while True:
    try:
        x = int(input("Podaj liczbę: "))
        break
    except ValueError: # jeśli błąd wartości
        print("Spróbuj jeszcze raz.")
```

    Podaj liczbę: a
    Spróbuj jeszcze raz.
    Podaj liczbę: 1.0
    Spróbuj jeszcze raz.
    Podaj liczbę: 1


## Komunikat wyjątku

---


```python
while True:
    try:
        x = int(input("Podaj liczbę: "))
        break
    except ValueError as err: # err = komunikat błędu
        print("Spróbuj jeszcze raz, bo", err)
```

    Podaj liczbę: a
    Spróbuj jeszcze raz, bo invalid literal for int() with base 10: 'a'
    Podaj liczbę: 1.0
    Spróbuj jeszcze raz, bo invalid literal for int() with base 10: '1.0'
    Podaj liczbę: 1


## Przykład

---


```python
# więcej o plikach za chwilę

import sys

def read_data():
    try:
        plik = open('data.txt') # otwórz plik
        linia = plik.readline() # wczytaj linię
        dane = int(linia)       # rzutuj linię na int
    except IOError as err:      # IOError
        print("Błąd I/O:", err)
    except ValueError as err:   # ValueError
        print("Złe dane:", err)
    except:                     # InnyError
        print("Coś poszło nie tak...")
        sys.exit(0)
```

## Przykład - test

---


```python
read_data()
```

    Błąd I/O: [Errno 2] No such file or directory: 'data.txt'



```python
Python
```

    Writing data.txt



```python
read_data()
```

    Złe dane: invalid literal for int() with base 10: 'Python'


## *try...finally*

---


```python
def iloraz(a, b):
    """Zwraca a / b."""
    try:
        return a / b
    finally: # wykonaj mimo zgłoszonego wyjątku
        print("Posprzątam bez względu na wyjątki.")
```


```python
iloraz(10, 5)
```

    Posprzątam bez względu na wyjątki.





    2.0




```python
iloraz(10, 0)
```

    Posprzątam bez względu na wyjątki.



    ---------------------------------------------------------------------------

    ZeroDivisionError                         Traceback (most recent call last)

    <ipython-input-33-0a93c896245e> in <module>()
    ----> 1 iloraz(10, 0)
    

    <ipython-input-31-2179acde9974> in iloraz(a, b)
          2     """Zwraca a / b."""
          3     try:
    ----> 4         return a / b
          5     finally: # wykonaj mimo zgłoszonego wyjątku
          6         print("Posprzątam bez względu na wyjątki.")


    ZeroDivisionError: division by zero


## *try...except...finally*

---


```python
def iloraz(a, b):
    """Zwraca a / b lub zero, jeśli b = 0."""
    try:
        return a / b
    except:
        print("Użytkownik nie zna matematyki.")
    finally: # wykona zawsze bez względu na wyni try
        print("Posprzątam bez względu na wyjątki.")
```


```python
iloraz(10, 5)
```

    Posprzątam bez względu na wyjątki.





    2.0




```python
iloraz(10, 0)
```

    Użytkownik nie zna matematyki.
    Posprzątam bez względu na wyjątki.


## Zgłaszanie wyjątków

---


```python
def iloraz(a, b):
    """Zwraca a / b."""
    if b == 0:
        raise NameError("Dzielenie przez zero.")
    return a / b
```


```python
iloraz(10, 5)
```




    2.0




```python
iloraz(10, 0)
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-39-0a93c896245e> in <module>()
    ----> 1 iloraz(10, 0)
    

    <ipython-input-37-0c4a0fa13db9> in iloraz(a, b)
          2     """Zwraca a / b."""
          3     if b == 0:
    ----> 4         raise NameError("Dzielenie przez zero.")
          5     return a / b


    NameError: Dzielenie przez zero.


## Zgłaszanie wyjątków test

---


```python
try:
    iloraz(10, 0)
except NameError as err:
    print("Błąd:", err)
```

    Błąd: Dzielenie przez zero.


## Własne wyjątki

---

* możliwe jest definiowanie własnych wyjątków
* o tym w przyszłości, jak już poznamy klasy

## *assert*

---

```py
# assert expression jest równoważne
if __debug__:
    if not expression: raise AssertionError
```


```python

import sys

assert sys.argv[1] != "Python"

print("Assert test.")
```



## *assert* - test

---


```python
python assert.py 1
```

    Assert test.



```python
python assert.py Python
```

    Traceback (most recent call last):
      File "assert.py", line 4, in <module>
        assert sys.argv[1] != "Python"
    AssertionError



```python
python -O assert.py Python
```

    Assert test.


## Operacje na plikach

---

* do otwierania plików służy funkcja wbudowana *open*
* przyjmuje wiele argumentów, przy czym dwa najważniejsze to: *file* i *mode*

```py
open(file, mode)
```

* *file* - nazwa pliku (lub pełna ścieżka, jeśli nie w katalogu roboczym)
* *mode* - tryb

## Tryby pracy nad plikiem

---

| Tryb | Opis                                                 |
|:----:|:----------------------------------------------------:|
| r    | tylko do oczytu (domyślnie)                          |
| w    | tylko do zapisu (istniejący plik zostanie nadpisany) |
| x    | tylko do zapisu (plik nie może istnieć)              |
| a    | tylko do zapisu (od końca pliku)                     |
| +    | aktualizowanie pliku (odczyt i zapis)                |
| t    | tryb tekstowy (domyślnie)                            |
| b    | tryb binarny                                         |

* np. `open(file, r+b)` otwiera plik do odczytu, z możliwością zapisu, w trybie binarnym

## Zapis do pliku

---


```python
# otwórz plik do zapisu
# usuń zawartość jeśli plik istnieje
file = open("test", 'w')

file.write("0123456789") # zapisz do pliku

file.close() # zamknij plik
```


```python
file.write("jeszcze coś") # plik już jest zamknięty
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-46-456f9e28996a> in <module>()
    ----> 1 file.write("jeszcze coś") # plik już jest zamknięty
    

    ValueError: I/O operation on closed file.


## Dopisywanie do pliku

---


```python
# otwórz plik do zapisu
# ustaw się na końcu pliku
file = open("test", 'a')

file.write("abcdefghij") # zapisz do pliku

file.close() # zamknij plik
```

## Odczyt pliku

---


```python
file = open("test", "r") # otwórz tylko do odczytu

zawartosc = file.read() # wczytaj całą zawartość pliku

file.close()

print(zawartosc)
```

    0123456789abcdefghij


## *r+* vs *a*

---


```python
# a (append) - zaczyna dopisywać na koniec pliku
# r+ - zaczyna zapisywać od początku (nadpisując dane)

file = open("test", "r+") # odczyt z możliwością zapisu

file.write("." * 5) # zapisz 5 kropek

file.close()
```


```python
# Bash
cat test
```

    .....56789abcdefghij

## *w+* vs *r+*

---


```python
# r+ - zaczyna zapisywać od początku (nadpisując dane)
# w+ - najpierw czyści plik (jeśli istnieje)

file = open("test", "w+") # zapis z możliwością odczytu

file.write("." * 5) # zapisz 5 kropek

file.close()
```


```python
# Bash
cat test
```

    .....

## *w* vs *w+*

---


```python
file = open("test", "w") # tylko zapis

file.write("." * 5) # zapisz 5 kropek

zawartosc = file.read()

file.close()

print(zawartosc)
```


    ---------------------------------------------------------------------------

    UnsupportedOperation                      Traceback (most recent call last)

    <ipython-input-53-6fb740cd3fea> in <module>()
          3 file.write("." * 5) # zapisz 5 kropek
          4 
    ----> 5 zawartosc = file.read()
          6 
          7 file.close()


    UnsupportedOperation: not readable


## *w* vs *w+*

---


```python
file = open("test", "w+") # zapis z możliwościa odczytu

file.write("." * 5) # zapisz 5 kropek

zawartosc = file.read()

file.close()

print(zawartosc) # nie wydrukuje bo jesteśmy na końcu pliku
```

    


## *seek*

---


```python
file = open("test", "w+") # zapis z możliwościa odczytu

file.write("." * 5) # zapisz 5 kropek

file.seek(0) # ustaw położenie

zawartosc = file.read()

file.close()

print(zawartosc) # nie wydrukuje bo jesteśmy na końcu pliku
```

    .....


## *tell*

---


```
# Bash
cat test
```

    .....


```python
file = open("test", "a+") # dodawanie z możliwością odczytu

file.tell() # pozycja w pliku
```




    5




```python
file.write("12345") # dopisz 12345

file.tell()
```




    10




```python
# Bash
cat test
```

    .....12345

## *seek* and *read*

---


```python
# Bash
cat test
```

    .....12345


```python
# seek(offset, punkt_odniesienia)
# po = 0, 1, 2 (początek pliku, bieżąca pozycja, koniec pliku)
# w trybie tekstowym tylko 0 jest dozwolone

file.seek(6, 0) # o 6 znaków od początku 

file.read(1)
```




    '2'




```python
file.tell() # read(n) przesuwa o n
```




    7



## Uwaga

---

* wygodnie jest wczytać cały plik do pamięci
    * *read()* - zawartość jako pojedynczy string
    * *readlines()* - zawartość jako lista (linia -> element)
* jednak w przypadku dużych plików może to byś katastrofalne, wtedy lepiej
    * *read(n)* - wczytaj *n* bajtów
    * *readline()* - wczytaj linię

## Otwieranie plików a wyjątki

---

```py
try:
    file = open("złe_dane")
    data = file.read() # zgłasza wyjątek
finally: # porządek nawet w przypadku wyjątku
    print("Czyszczę śmieci.")
    file.close()
```

## *with* statement

---

* gwarantuje, że jeśli wywołane zostało `__enter__()` (np. otwarcie pliku)
* to zostanie wywołane `__exit()__` (np. zamknięcie pliku)
* nawet jeśli po drodze wystąpi wyjątek 

## *with open*

---

```py
with open("plik_z_danymi") as file:
    data = file.read()
```

* gwarantuje, że plik zostanie zawsze poprawnie zamknięty
* wygodniejsze niż *try...finally...*

## Comma-separated values (CSV)

---

* forma przechowywania danych w plikach tesktowych
* każde pole oddzielone jest przecinkiem
* plik csv

```
imię, nazwisko, ocena
Kasia, Kowalska, 4
Jan, Nowak, 4
```

* tabela

| imię  | nazwisko | ocena |
|:-----:|:--------:|:-----:|
| Kasia | Kowalska | 4     |
| Jan   | Nowak    | 4     |

## Moduł *csv*

---


```python
import csv

data = [["imie", "nazwisko", "ocena"],
        ["Kasia", "Kowalska", 4],
        ["Jan", "Nowak", 4]]

with open("oceny.csv", "w") as csvfile:
    writer = csv.writer(csvfile) # tworzymy "pisarza" csv
    for wpis in data:
        writer.writerow(wpis)    
```


```python
# Bash
cat oceny.csv
```

    imie,nazwisko,ocena
    Kasia,Kowalska,4
    Jan,Nowak,4


## Wczytywanie danych

---


```python
import csv

with open('oceny.csv', 'r') as csvfile:
    reader = csv.reader(csvfile) # tworzymy "czytelnika" csv
    for wpis in reader:
        print(wpis)
```

    ['imie', 'nazwisko', 'ocena']
    ['Kasia', 'Kowalska', '4']
    ['Jan', 'Nowak', '4']
