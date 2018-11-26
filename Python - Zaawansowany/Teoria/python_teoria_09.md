
# Python
## Teoria 9

---

* typy sekwencyjne: *set* i *frozenset*
* generatory
* omówienie zadań z listy 6

## Typy sekwencyjne 

---

* do tej pory poznaliśmy cztery typy sekwencyjne:
    * *str* - typ tekstowy
    * *list* - *mutowalna* sekwencja
    * *tuple* - *niemutowalna* sekwencja
    * *range* - *niemutowalna* sekwencja liczb

## Sekwencja *set*

---

* *set* jest *mutowalną* sekwencją
* różnice względem *list*
    * nie może zawierać duplikatów
    * jest nieuporządkowana
    * może zawierać tylko *hashowalne* obiekty

## Definiowanie *set*

---


```python
zbior = {1, 4, 6, 2, 1} # nawiasy klamrowe

type(zbior)
```




    set




```python
print(zbior)
```

    {1, 2, 4, 6}



```python
zbior[0] # nie ma indeksowania zbiorów
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-3-119e4f5506a9> in <module>()
    ----> 1 zbior[0] # nie ma indeksowania zbiorów
    

    TypeError: 'set' object does not support indexing


## *set* z *list*

---


```python
lista = [1, 4, 6, 2, 1]

zbior = set(lista) # stwórz zbiór na bazie listy

print(zbior)
```

    {1, 2, 4, 6}


## Dodawanie elementów do zbioru

---


```python
zbior = {1, 2, 3}

print(zbior)
```

    {1, 2, 3}



```python
zbior.add(4) # dodaj 4

print(zbior)
```

    {1, 2, 3, 4}



```python
zbior.add(4) # jeszcze raz dodaj 4

print(zbior) # nie ma duplikatów
```

    {1, 2, 3, 4}


## Elementy *niehashowalne*

---


```python
zbior = {1, 2, 3}

lista = [4, 5] # lista jest niehashowalna

# zbiór nie może przechowywać 
# elementów niehashowalnych
zbior.add(lista)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-8-c1da28ad9f1d> in <module>()
          5 # zbiór nie może przechowywać
          6 # elementów niehashowalnych
    ----> 7 zbior.add(lista)
    

    TypeError: unhashable type: 'list'


## Sekwencje hashowalne

---


```python
zbior = {1, 2, 3}

krotka = (4, 5) # krotka jest hashowalna

# więc można dodać krotkę
# do zbioru
zbior.add(krotka)

print(zbior)
```

    {(4, 5), 1, 2, 3}


## Usuwanie elementów ze zbioru

---


```python
zbior = {1, 2, 3}

zbior.remove(1) # usuń 1

print(zbior)
```

    {2, 3}



```python
# zwróci błąd jeśli element nie istnieje
zbior.remove(1)
```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    <ipython-input-11-15d16e079b36> in <module>()
          1 # zwróci błąd jeśli element nie istnieje
    ----> 2 zbior.remove(1)
    

    KeyError: 1


## Bezpieczne usuwanie?

---


```python
zbior = {1, 2, 3}

# aby uniknąć błędów i przerwania programu
# można sprawdzić, czy na pewno element
# znajduje się w zbiorze
if 1 in zbior:
    zbior.remove(1)
```


```python
# lub skorzystać z try...except
try:
    zbior.remove(1)
except:
    pass
```


```python
# lub skorzystać z discard
zbior.discard(1)
```

## Zastosowanie zbiorów

---


```python
# usuwanie duplikatów z listy

lista = [2, 1, 2, 3, 4, 3, 2, 1, 5, 5, 2]

lista = list(set(lista))

# uwaga - tracimy kolejność
print(lista)
```

    [1, 2, 3, 4, 5]


## Część wspólna zbiorów

---


```python
A = {1, 2, 3, 4, 5}
B = {3, 4, 5, 6, 7}

A.intersection(B) # część wspólna A i B
```




    {3, 4, 5}




```python
# lub krócej
A & B
```




    {3, 4, 5}



## Część wspólna list

---


```python
A = [1, 2, 3, 4, 5]
B = [3, 4, 5, 6, 7]

# rzutuje A i B na zbiory
# wyznacza ich część wspólną
# rzutuje na listę
wspolna = list(set(A) & set(B))

print(wspolna)
```

    [3, 4, 5]


## *frozenset*

---

* jak *set* ale *niemutowalny*, czyli nie można modyfikować zawartości


```python
zamrozony_zbior = frozenset([1, 2, 3, 4, 5])

type(zamrozony_zbior)
```




    frozenset




```python
zamrozony_zbior.add(1) # nie można dodawać / usuwać
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-20-c3b7844219a4> in <module>()
    ----> 1 zamrozony_zbior.add(1) # nie można dodawać / usuwać
    

    AttributeError: 'frozenset' object has no attribute 'add'


## Generatory

---

* funkcja, która zachowuje się jak iterator (czyli można np. wykorzystać ją w pętli)
* zamiast tworzyć całą listę obiektów, które będą przechowywane w pamięci
* oszczędza czas i pamięć


## Ciąg geometryczny

---


```python
def geometryczny(a1, q, n):
    """Generuje n wyrazów ciągu geometrycznego."""
    
    ciag = [a1]
    
    for _ in range(n-1): # n-1 bo pierwszy już jest
        ciag.append(ciag[-1]*q) # następny = poprzedni * iloraz
        
    return ciag
```


```python
ciag = geometryczny(1, 3, 10)

print(ciag)
```

    [1, 3, 9, 27, 81, 243, 729, 2187, 6561, 19683]


## Ciąg geometryczny - generator

---


```python
def gen_geometryczny(a1, q, n):
    """Generuje n wyrazów ciągu geometrycznego."""
    
    for _ in range(n):
        yield a1 # zwróć obecną wartość a1
        a1 *= q  # i czekaj na kolejną iterację
```

## Generator a lista

---


```python
ciag1 = geometryczny(1, 3, 10)     # zwraca listę 
ciag2 = gen_geometryczny(1, 3, 10) # zwraca generator
```


```python
print(ciag1)
```

    [1, 3, 9, 27, 81, 243, 729, 2187, 6561, 19683]



```python
print(ciag2)
```

    <generator object gen_geometryczny at 0x7f9bac1ec678>


## Generator jak iterator

---


```python
next(ciag2) # pierwszy element
```




    1




```python
next(ciag2) # kolejny element itd
```




    3




```python
# a najczęściej w pętli
for i in gen_geometryczny(1, 3, 10):
    print(i, end=', ')
```

    1, 3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 


## Lista czy generator

---

* generator będzie z reguły szybszy
* generator może być nieskończony
* jednak nie można wykonywać operacji na "elementach", np. sortowania
* lista może być efektywniejsza, jeśli planujemy więcej pętli

## "Wyczerpanie" generatora

---


```python
ciag = gen_geometryczny(1, 3, 20) # generuje 20 wyrazów
```


```python
for i in range(10): # wydrukuj 10 pierwszych
    print(next(ciag), end=' ')
```

    1 3 9 27 81 243 729 2187 6561 19683 


```python
for element in ciag: # nie zaczyna od pierwszego!
    print(element, end=' ')
```

    59049 177147 531441 1594323 4782969 14348907 43046721 129140163 387420489 1162261467 


## Powtórka: listy składane (*list comprehensions*)

---


```python
# chcemy stworzyć listę zawierającą
# kwadraty wszystkich cyfr

kwadraty = []

for x in range(10):
    kwadraty.append(x**2)
    
print(kwadraty)
```

    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]



```python
# a korzystając z listy skladanej

kwadraty = [x**2 for x in range(10)]

print(kwadraty)
```

    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


## Append vs lista składana

---


```python
def create_list(n=100000):
    """Tworzy listę kwadratów pierwszych n liczb naturalnych"""
    
    kwadraty = []
    
    for x in range(n):
        kwadraty.append(x**2)
        
    return kwadraty

def list_comprehension(n=100000):
    """Tworzy listę kwadratów pierwszych n liczb naturalnych"""
    
    return [x**2 for x in range(n)]
```

## Czas

---


```python
timeit -n3 x = create_list() # lista tworzona przez append
```

    3 loops, best of 3: 48.3 ms per loop



```python
timeit -n3 y = list_comprehension() # lista składana
```

    3 loops, best of 3: 42.5 ms per loop



```python
create_list() == list_comprehension() # wynik ten sam
```




    True



## Przykład

---


```python
def force(m, a):
    """Zwraca wartość siły [N].
    
    Liczy siłę jaką należy zadziałać na ciało
    o masie m [kg], aby nadać mu przyspieszenie a [m/s^2].
    """
    return m*a

wagi = [10, 20, 30, 40, 50] # kg
przyspieszenia = [1, 2, 3, 4, 5] # m/s^2
```


```python
# stwórz tablicę z wartościami sił 

sily = [force(m, a) for m, a in zip(wagi, przyspieszenia)]

print(sily)
```

    [10, 40, 90, 160, 250]


## Generator "jak lista składana"

---


```python
# lista składana
list_comprehension = [x**2 for x in range(10)]

# generator expression
generator = (x**2 for x in range(10))
```


```python
for x in generator:
    print(x, end=' ')
```

    0 1 4 9 16 25 36 49 64 81 


```python
# lub prościej

for x in (x**2 for x in range(10)):
    print(x, end=' ')
```

    0 1 4 9 16 25 36 49 64 81 

## Uwagi na koniec

---

* unikaj tworzenia list przez *append*, jeśli można wykorzystać *list comprehension*
* unikaj tworzenia list jeśli jest to zbędne (użyj generatorów)
* unikaj *generator function* na rzecz *generator expression*