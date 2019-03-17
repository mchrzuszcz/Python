
# Python
## Prework do 2 listy zadań 

## Łańcuch znaków z ang. (*string*)

---

Zmienna typu *str* przechowuje tak naprawdę ciąg znaków, liter bądź cyfr, w którym każdy znak ma określoną pozycję. Pozycje natomiast liczymy nie od 1 jak to mamy w zwyczaju ale od 0. 
 
 Czyli upraszczając, w programowaniu liczmy od 0 i zapamiętajmy to sobie bo jest to bardzo ważne i bardzo się nam to przyda w przyszłości.


```python
s = "Python"

s[0] # str[i] -> i-ty znak w ciągu
```

    'P'

```python
s[1] # pierwszy to drugi? TAK!
```

    'y'
    
```python
s[2]
```

    't'

| Litera: | P | y | t | h | o | n |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|Pozycja/Index:| 0 | 1 | 2 | 3 | 4 | 5 | 

## Lista z ang. (*list*)

---

* zbiór zmiennych, liczba, danych itd. dowolnego typu
* dynamiczny rozmiar, można ją modyfikować w każdym momencie
* tworzymy ją poprzez:
    * nawiasy kwadratowe
    * rzutowanie *list(jakis_zbior)* (czyli konstruktor klasy *list*)
    * lista składana (*list comprehension*) o tym na kolejnych zajęciach

## Lista - przykład

---

```python
lista = [1, 2, 'a', "Python"]
```


```python
len(lista) # długość listy
```

    4

```python
lista[0] # pierwszy element listy
```
    1
```python
lista[-1] # ostatni element listy
```
    'Python'
## Krotka z ang. (*tuple*)

---

* zbiór zmiennych, liczba, danych itd. dowolnego typu
* stały rozmiar - nie można jej zmieniac, tzn. dodawać usuwać elementów
* tworzymy ją poprzez:
    * nawiasy okrągłe
    * ciąg elementów oddzielonych przecinkiem
    * rzutowanie *tuple(jakis_zbior)*

## Krotka - przykład



```python
krotka = (1, 2, 3, "Python") # jak lista, ale () zamiast []

print(krotka)
```

    (1, 2, 3, 'Python')



```python
krotka = 1, 2, 3, "Python" # brak nawiasów = tuple

print(krotka)
```

    (1, 2, 3, 'Python')



```python
lista = list("Python") # lista ze stringa

krotka = tuple(lista)  # krotka z listy

print(lista)
print(krotka)
```

    ['P', 'y', 't', 'h', 'o', 'n']
    ('P', 'y', 't', 'h', 'o', 'n')


## Lista vs Krotka

---

* krotka ma stały rozmiar a lista jest dynamiczna
* krotka jest "niezmienna" (*immutable*) w przeciwieństwie do listy (*mutable*)
* więcej o *mutable* vs *immutable* w folderze [4_Teoria](../4_Teoria/python_teoria_02.md)
* jeśli sekwencja obiektów jest stała w czasie działania programu, lepiej używać krotek
    * szybsze
    * bezpieczniejsze
    * mogą być kluczami w słowniku *(o słownikach na kolejnych zajęciach)*
    
## Range

---

* uwaga: w Pythonie 2 *range()* jest funkcją wbudowaną; w Pythonie 3 jest to typ danych (klasa)
* reprezentuje (niezmienniczą) sekwencję liczb
* zajmuje mniej pamięci niż *list* lub *tuple* (przechowuje tylko informację o początku, końcu i kroku)

## Range

---


```python
x = range(10) # od 0 do 10

print(x) # w Pythonie 2 zobaczylibyśmy [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


## Range

---


```python
cyfry = range(0, 10)       # range(początek = 0, koniec) 
parzyste = range(2, 10, 2) # range(początek, koniec, krok)
nieparzyste = range(1, 10, 2)

print(cyfry)
print(parzyste)
print(nieparzyste)
```

    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    [2, 4, 6, 8]
    [1, 3, 5, 7, 9]


## Sekwencyjne typy danych

---

* *list* - dynamiczny ciąg zmiennych dowolnego typu
* *tuple* - niezmienniczy ciąg zmiennych dowolnego typu
* *range* - niezmienniczy ciąg liczba całkowitych
* *str* - niezmienniczy ciąg znaków
* (dla kompletności) są jeszcze binarne sekwencyjne typy danych: *bytes*, *bytearray*, *memoryview*

## Indeksowanie

---

Indeksowanie dla powtórki (bo to  bardzo ważne!) zaczyna się od 0 a kończy na *n-1*, gdzie *n* - długość ciągu.   

Długość ciągu w przykładzie poniżej to po prostu ilość liter w słowie "Python" czyli 6, a stosując wzór n-1 gdzie n jest równe 6 to 6-1 równa sie 5 :)  

Sprawdź czy się zgadza!


```python
s = "Python"

n = len(s) # długość łańcucha s

print(n)
```

    6

```python
s[n-1] # ostatni element
```

    'n'

```python
s[n] # poza zakresem
```


    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    <ipython-input-7-1dea7ae0782c> in <module>()
    ----> 1 s[n] # poza zakresem
    

    IndexError: string index out of range
    
| Litera: | P | y | t | h | o | n |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
|Pozycja/Index:| 0 | 1 | 2 | 3 | 4 | 5 | 
