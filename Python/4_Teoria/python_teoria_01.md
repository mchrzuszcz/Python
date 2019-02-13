
# Python
## Teoria 1

## Program kursu

---

* wprowadzenie
* podstawowe typy danych i operatory
* wyrażenia warunkowe i pętle
* funkcje i moduły
* struktury danych
* klasy i obiekty
* operacje wejścia/wyjścia
* obsługa wyjątków

---

* obliczenia numeryczne
* debugowanie i profilowanie
* tworzenie graficznego interfejsu użytkownika
* dekoratory, funkcje lambda, generatory ...

## Materiały do zajęć

---

* dokumentacja: https://www.python.org/

---

* A. B. Downey, J. Elkner, C. Meyers, “Think Python. How to Think Like a Computer Scientist”: http://www.greenteapress.com/thinkpython/
* M. Pilgrim, “Dive into Python”: http://www.diveintopython.net/ -> [Zanurkuj_w_Pythonie.pdf](../5_Materialy_Pomocnicze/Zanurkuj_w_Pythonie.pdf)
* Swaroop CH "A Byte of Python": https://python.swaroopch.com/ (tłumaczenie: http://python.edu.pl/byteofpython/)

## Język kompilowany

---

* przykłady: C / C++, Pascal
* zalety: wydajność, błędy na etapie kompilacji, utrzymanie i rozwijanie kodu
* wady: czas pisania, kompilacja dużych projektów

kod źródłowy -> kompilator -> kod maszynowy -> wynik

## Język interpretowany

---

* przykłady: Python, Perl
* zalety: prosty, szybki i przyjemny
* wady: wydajność, debugowanie (brak kompilacji)


kod źródłowy -> interpreter -> wynik


## Python

---

> Python is powerful... and fast;
> plays well with others;
> runs everywhere;
> is friendly & easy to learn;
> is Open.

---

* otwarte oprogramowanie (*open source*)
* przenośny
    * Linux, Mac OS - prawdopodobnie już jest
    * Windows - instalator ze strony https://www.python.org
    * Anaconda - https://www.continuum.io/
* zwięzły i elegancki (prawie jak pseudokod)
* automatyczne zarządzanie pamięcią (*garbage collection*)
* bogata bilbioteka standardowa i niezliczona ilość bibliotek zewnętrznych
* struktury wysokiego poziomu


## Hello World! - w różnych językach

---

```py
# Python
print("Hello World!")
```

---

```cpp
// C++
#include <iostream>

int main()
{
    std::cout << "Hello World!";
}
```

---


```java
// Java
public class Hello {
    public static void main(String []args) {
        System.out.println("Hello World!");
    }
}
```

## Zastosowanie

---

* internet: Yahoo, Google, ...
* gry: Battlefield 2, Civilization 4, ...
* grafika: Walt Disney, Blender 3D, ...
* finanse: Altis Investment Management, Bellco Credit Union, ...
* nauka: NASA, Los Alamos National Laboratory, ...
* interfejs programistyczny aplikacji (*Application Programming Interface = API*): tensorflow (Google's machine learning), Amazon, Facebook, Youtube, ...

## Python 2 vs Python 3

---

* *Short version: Python 2.x is legacy, Python 3.x is the present and future of the language* (https://wiki.python.org/moin/Python2orPython3)
* Python 3 jest gotowy, jednak nie wszystkie zewnętrzne biblioteki są już z nim kompatybilne

## Python 2 vs Python 3

---

* Niektóre zmiany są kosmetyczne

```py
# Python 2

print "Hello World!"

# Python 3

print("Hello World!")
```

## Python 2 vs Python 3

---

* Niektóre niebezpieczne

```py
# Python 2

3 / 2.0 # = 1.5
3 / 2   # = 1

# Python 3

3 / 2.0 # = 1.5
3 / 2   # = 1.5
3 // 2  # = 1
```

## Python 2 vs Python 3

---

* A niektóre gruntowne: iteratory
* Niektóre elementy Pythona 3 można zaimportować w Pythonie 2

```
Python 2.7.12 (default, Jul  1 2016, 15:12:24) 
[GCC 5.4.0 20160609] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> 3 / 2
1
>>> from __future__ import division
>>> 3 / 2
1.5
>>> 
```

* Więcej informacji: https://wiki.python.org/moin/Python2orPython3

* Na kursie omawiany będzie Python 2

## Tryb interaktywny

---

```
$ python
Python 2.7.15 
Type "help", "copyright", "credits" or "license" for more information.
>>> oceny_uwr = {2.0: "niedostateczny", 3.0: "dostateczny",
...              3.5: "dostateczny plus", 4.0: "dobry",
...              4.5: "dobry plus", 5.0: "bardzo dobry"}
>>> for ocena in sorted(oceny_uwr, reverse=True):
...     print(ocena, oceny_uwr[ocena])
... 
5.0 bardzo dobry
4.5 dobry plus
4.0 dobry
3.5 dostateczny plus
3.0 dostateczny
2.0 niedostateczny
>>> 
```

## Tryb skryptowy - linux

---

```
$ cat skala_ocen.py 
#!/usr/bin/env python

oceny_uwr = {2.0: "niedostateczny", 3.0: "dostateczny",
             3.5: "dostateczny plus", 4.0: "dobry",
             4.5: "dobry plus", 5.0: "bardzo dobry"}

for ocena in sorted(oceny_uwr, reverse=True):
    print(ocena, oceny_uwr[ocena])
    
$ python skala_ocen.py 
5.0 bardzo dobry
4.5 dobry plus
4.0 dobry
3.5 dostateczny plus
3.0 dostateczny
2.0 niedostateczny
```

## Tryb skryptowy - linux

---

```
$ ./skala_ocen.py
bash: ./skala_ocen.py: Permission denied

$ chmod +x skala_ocen.py 

$ ./skala_ocen.py 
5.0 bardzo dobry
4.5 dobry plus
4.0 dobry
3.5 dostateczny plus
3.0 dostateczny
2.0 niedostateczny
```

## Czytelność kodu

---

* przejrzysty kod
* zrozumiałe nazwy zmiennych
* komentarzy nigdy za wiele
* dzielenie linii nie boli
* konsekwencja w konwencji
* najlepiej trzymać się standardu PEP 8: https://www.python.org/dev/peps/pep-0008/
* ale bez przesady - przede wszystkim kod ma być czytelny

## Czytelność kodu - good way

---


```python
import random

# skala ocen obowiązująca na Uniwersytecie Wrocławskim
oceny_uwr = {2.0: "niedostateczny", 3.0: "dostateczny",
             3.5: "dostateczny plus", 4.0: "dobry",
             4.5: "dobry plus", 5.0: "bardzo dobry"}

# lista studentów uczęszczających na zajęcia z Pythona
lista_studentow = ["Kasia", "Basia", "Józek", "Marek"]

# przez lenistwo prowadzącego oceny wystawiane losowo
for student in lista_studentow:
    # losowa ocena
    ocena = random.choice(list(oceny_uwr))
    # przypisanie oceny
    print(student, " -> ", oceny_uwr[ocena])
```

    Kasia  ->  dobry plus
    Basia  ->  dobry plus
    Józek  ->  dostateczny plus
    Marek  ->  niedostateczny


## Czytelność kodu - wrong way

---


```python
import random
o = {2.0: "niedostateczny", 3.0: "dostateczny", 3.5: "dostateczny plus", 4.0: "dobry", 4.5: "dobry plus", 5.0: "bardzo dobry"}
s = ["Kasia", \
     "Basia", "Józek",
     "Marek"]
for i in range(len(s)): x = random.randint(2, len(o) - 1); print(s[i], " -> ", o[x])
```

    Kasia  ->  dostateczny
    Basia  ->  niedostateczny
    Józek  ->  dostateczny
    Marek  ->  bardzo dobry


## Podstawowe typy danych 

---

* typ całkowity (*int*)
* typ zmiennoprzecinkowy (*float*)
* typ logiczny (*bool*)
* typ tekstowy (*str*)
* zmienne są typowane dynamicznie


```python
x = 1   # [zmienna] [operator przypisania] [wartość]
y = 1.0
z = True

# drukuj typy zmiennych x, y i z (oddzielone przecinkiem)
print(type(x), type(y), type(z))
```

    (<type 'int'>, <type 'float'>, <type 'bool'>)


## Operacje na liczbach

---


```python
2 + 2 # suma dwóch liczb całkowitych -> liczba całkowita
```




    4




```python
2 + 2.0 # wynikiem tej sumy jest liczba zmiennoprzecinkowa
```




    4.0




```python
5 - 2
```




    3




```python
-5 * 2 
```




    -10




```python
5 / 2 # w Pythonie 2 dzielenie zawsze zwraca liczbę całkowitą
```




    2




```python
5 // 2 # chyba że użyjemy // -> dla pythona 3 zeby zwrócił liczbę całkowitą, w innym przypadku zwróci zmiennoprzecinkową
```




    2



## Operacje na liczbach

---


```python
5 % 2 # reszta z dzielenia (operator modulo)
```




    1




```python
int(2.5) # jawne rzutowanie na int
```




    2




```python
float(1) # jawne rzutowanie na float
```




    1.0




## Operacje na liczbach

---


```python
abs(-10) # moduł
```




    10




```python
abs(-2.5)
```




    2.5



## Operacje na liczbach


```python
pow(2, 3) # pow(a, b) = a^b
```




    8




```python
pow(2, 3.0) # zwróć uwagę na typy
```




    8.0




```python
2 ** 3 # inna wersja a^b
```




    8




## Moduł math

---


```python
import math # import [moduł]

dir (math) # lista dostępnych funkcji
```




    ['__doc__',
     '__file__',
     '__loader__',
     '__name__',
     '__package__',
     '__spec__',
     'acos',
     'acosh',
     'asin',
     'asinh',
     'atan',
     'atan2',
     'atanh',
     'ceil',
     'copysign',
     'cos',
     'cosh',
     'degrees',
     'e',
     'erf',
     'erfc',
     'exp',
     'expm1',
     'fabs',
     'factorial',
     'floor',
     'fmod',
     'frexp',
     'fsum',
     'gamma',
     'gcd',
     'hypot',
     'inf',
     'isclose',
     'isfinite',
     'isinf',
     'isnan',
     'ldexp',
     'lgamma',
     'log',
     'log10',
     'log1p',
     'log2',
     'modf',
     'nan',
     'pi',
     'pow',
     'radians',
     'sin',
     'sinh',
     'sqrt',
     'tan',
     'tanh',
     'trunc']



## Moduł math

---


```python
help(math.floor) # dokumentacja funkcji floor z math
```

    Help on built-in function floor in module math:
    
    floor(...)
        floor(x)
        
        Return the floor of x as an Integral.
        This is the largest integer <= x.
    



```python
help(math.ceil) # zwróć uwagę na: moduł.funkcja
```

    Help on built-in function ceil in module math:
    
    ceil(...)
        ceil(x)
        
        Return the ceiling of x as an Integral.
        This is the smallest integer >= x.
    


## Moduł math

---


```python
int(2.8) # rzutowanie float na int "ucina wszystko po kropce"
```




    2




```python
math.floor(2.8) # tak jak funkcja math.floor
```




    2




```python
math.ceil(2.8) # funkcja math.ceil zaokrągla w górę
```




    3




```python
math.ceil(2.1) # zawsze w górę (patrz definicja)
```




    3



## Typ tekstowy bez *unicode*

---

```py
Python 2.7.12 (default, Jul  1 2016, 15:12:24) 
[GCC 5.4.0 20160609] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> s = "zażółć gęślą jaźń"
>>> s
'za\xc5\xbc\xc3\xb3\xc5\x82\xc4\x87 g\xc4\x99\xc5\x9bl\xc4\x85 ja\xc5\xba\xc5\x84'
>>> 
```

## Typ tekstowy

---

* Literał łańcuchowy można wprowadzić przez:
    * pojedynczy cudzysłów
    ```py
    s = 'zażółć gęślą jaźń'
    ```
    * podwójny cudzysłów
    ```py
    s = "zażółć gęślą jaźń"
    ```
    * potrójny cudzysłów
    ```py
    s = '''zażółć gęślą jaźń'''
    s = """zażółć gęślą jaźń"""
    ```

## Znak ucieczki

---

* zmienia interpretację znaku
* w Pythonie (i prawie zawsze) jest to "\"


```python
print("Ala powiedziała: "Mam kota." ...") # cudzysłów kończy literał
```


      File "<ipython-input-44-2bf66ab2182a>", line 1
        print("Ala powiedziała: "Mam kota." ...") # cudzysłów kończy literał
                                   ^
    SyntaxError: invalid syntax




```python
print("Ala powiedziała: \"Mam kota.\" ...") # chyba że "uciekniemy"
```

    Ala powiedziała: "Mam kota." ...



```python
print('Ala powiedziała: "Mam kota." ...') # kombinacja ' i "
```

    Ala powiedziała: "Mam kota." ...



```python
print("Ala powiedziała: 'Mam kota.' ...") # działa w obie strony
```

    Ala powiedziała: 'Mam kota.' ...


## Wybrane sekewncje specjalne

---

* `\n` - nowa linia
* `\t` - tabulacja

```python
print("\\n wstawia nową linię.\nNowa linia.") # zwróć uwagę na \\n
```

    \n wstawia nową linię.
    Nowa linia.



```python
print("\tTabulacja też się przydaje.") # brak spacji po \t
```

    	Tabulacja też się przydaje.



## Długie łancuchy

---


```python
tekst = "Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker"

print(tekst)
```

    Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker


## Długie łancuchy

---


```python
tekst = "Lorem Ipsum jest tekstem stosowanym jako przykładowy \
        wypełniacz w przemyśle poligraficznym. Został po raz \
        pierwszy użyty w XV w. przez nieznanego drukarza do \
        wypełnienia tekstem próbnej książki. Pięć wieków później \
        zaczął być używany przemyśle elektronicznym, \
        pozostając praktycznie niezmienionym. Spopularyzował się \
        w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, \
        zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym \
        różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do \
        realizacji druków na komputerach osobistych, jak Aldus PageMaker"

print(tekst)
```

    Lorem Ipsum jest tekstem stosowanym jako przykładowy         wypełniacz w przemyśle poligraficznym. Został po raz         pierwszy użyty w XV w. przez nieznanego drukarza do         wypełnienia tekstem próbnej książki. Pięć wieków później         zaczął być używany przemyśle elektronicznym,         pozostając praktycznie niezmienionym. Spopularyzował się         w latach 60. XX w. wraz z publikacją arkuszy Letrasetu,         zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym         różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do         realizacji druków na komputerach osobistych, jak Aldus PageMaker


## Długie łancuchy

---


```python
tekst = "Lorem Ipsum jest tekstem stosowanym jako przykładowy " \
        "wypełniacz w przemyśle poligraficznym. Został po raz " \
        "pierwszy użyty w XV w. przez nieznanego drukarza do " \
        "wypełnienia tekstem próbnej książki. Pięć wieków później " \
        "zaczął być używany przemyśle elektronicznym, " \
        "pozostając praktycznie niezmienionym. Spopularyzował się " \
        "w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, " \
        "zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym " \
        "różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do " \
        "realizacji druków na komputerach osobistych, jak Aldus PageMaker "

print(tekst) # "slowo" "slowo" = "slowo" + "slowo"
```

    Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker 


## Długie łancuchy

---


```python
tekst = "Lorem Ipsum jest tekstem stosowanym jako przykładowy\n" \
        "wypełniacz w przemyśle poligraficznym. Został po raz\n" \
        "pierwszy użyty w XV w. przez nieznanego drukarza do\n" \
        "wypełnienia tekstem próbnej książki. Pięć wieków później\n" \
        "zaczął być używany przemyśle elektronicznym,\n" \
        "pozostając praktycznie niezmienionym. Spopularyzował się\n" \
        "w latach 60. XX w. wraz z publikacją arkuszy Letrasetu,\n" \
        "zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym\n" \
        "różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do\n" \
        "realizacji druków na komputerach osobistych, jak Aldus PageMaker\n"

print(tekst)
```

    Lorem Ipsum jest tekstem stosowanym jako przykładowy
    wypełniacz w przemyśle poligraficznym. Został po raz
    pierwszy użyty w XV w. przez nieznanego drukarza do
    wypełnienia tekstem próbnej książki. Pięć wieków później
    zaczął być używany przemyśle elektronicznym,
    pozostając praktycznie niezmienionym. Spopularyzował się
    w latach 60. XX w. wraz z publikacją arkuszy Letrasetu,
    zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym
    różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do
    realizacji druków na komputerach osobistych, jak Aldus PageMaker
    


## Długie łancuchy

---


```python
tekst = """Lorem Ipsum jest tekstem stosowanym jako przykładowy
wypełniacz w przemyśle poligraficznym. Został po raz
pierwszy użyty w XV w. przez nieznanego drukarza do
wypełnienia tekstem próbnej książki. Pięć wieków później
zaczął być używany przemyśle elektronicznym,
pozostając praktycznie niezmienionym. Spopularyzował się
w latach 60. XX w. wraz z publikacją arkuszy Letrasetu,
zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym
różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do
realizacji druków na komputerach osobistych, jak Aldus PageMaker
"""

print(tekst)
```

    Lorem Ipsum jest tekstem stosowanym jako przykładowy
    wypełniacz w przemyśle poligraficznym. Został po raz
    pierwszy użyty w XV w. przez nieznanego drukarza do
    wypełnienia tekstem próbnej książki. Pięć wieków później
    zaczął być używany przemyśle elektronicznym,
    pozostając praktycznie niezmienionym. Spopularyzował się
    w latach 60. XX w. wraz z publikacją arkuszy Letrasetu,
    zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym
    różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do
    realizacji druków na komputerach osobistych, jak Aldus PageMaker
    
## Przykładowy program

```python
import turtle # biblioteka do rysowania

pen = turtle.Turtle() 

n_steps = 90 # w ilu krokach robimy 360 stopni

for i in range(n_steps):
    
    pen.forward(100) # rysuj 100 do przodu
    pen.right(45)    # obróć się w prawo o 45 stopni
    pen.forward(50)  # rysuj 50 do przodu
    pen.left(90)     # obróć się w lewo o 90 stopni
    pen.forward(100) # rysuj do przodu o 100
    pen.right(45)    # obróź się w prawo o 45 stopni
    
    pen.penup() # podnieś długopis (nie rysuj przy przemieszczeniu)
    pen.setposition(0, 0) # wróć na środek
    pen.pendown() # rysujemy dalej
    
    pen.right(360/n_steps) # obróć się w prawo o n_stepną część 360
```

