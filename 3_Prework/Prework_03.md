
# Python
## Prework do 3 listy zadań 

## Pętla - For

---

Niezwykle prosty mechanizm a bardzo przydatny. Pozwala nam przechodzić czyli "iterować" po każdym elemencie danego zbioru np. listy.  

Dla przykładu zdefiniujmy sobie prostą liste i wykorzystajmy pętle _for_ która pozwoli nam wypisać wszystkie elementy tej listy:

```python
lista = ['a', 'b', 'c', 'd']

for litera in lista: # czyli w wolnym tlumaczeniu: Dla każdej litery w liscie
    print(litera)    # wypisujemy ją na ekran
```

    a
    b
    c
    d

Proste prawda? :)

## Pętla - For - enumerate

---

Teraz dodamy bardzo prostą i fajną funkcję *enumerate* do naszej pętli _for_ żeby oprócz literek wyświetlić też pozycje czyli indeks każdej litery. Temat indeksowania powinieneś poznać na poprzedniej lekcji więc to będzie bułka z masłem. 

```python
lista = ['a', 'b', 'c', 'd']

for pozycja,litera in enumerate(lista): # czyli w wolnym tlumaczeniu: Dla każdej litery w liscie
    print(pozycja, litera)    # wypisujemy ją na ekran
```

    0, a
    1, b
    2, c
    3, d

## Pętla - While

---

Drugi typ pętli, równie prosty jak _for_. Pętli _while_ nie powinno sie używać na zbiorach jak np. lista, a raczej w przypadkach kiedy chcemy aby wykonywała się jakaś akcja dopóki zdefiniowany warunek jest spełniony.   

Nie przejmuj się, to jest bardzo proste, przykład:

```python
i = 0

# ponizej po slowie while oznaczajacego pętle mamy warunek ktory musi byc spelniony aby pętla sie wykonywała
while i < 5: # wykonuj dopóki i < 5, w innych słowach wykonuj dopóki i jest mniejsze od 5
    i = i + 1   # gdybysmy nie dodali tej linijki to mielibyśmy nieskończoną pętlę
    print(i)
```

    1 
    2 
    3 
    4 
    5 

Wzór: 

```py
while warunek:
    instrukcje
```

Ale proste!

## Wyrażenie if

---

Wyrażenie _if_ jest jedną z najłatwiejszych rzeczy w programowaniu a niezwykle przydatną :) otóż załóżmy że chcemy sprawdzić czy podana liczba jest większa od 0?  

Jak to zrobić? Już pokazuję!

 ```py
i = 0
if i > 0:
    print("Zmienna i jest większa od zera!")
else:
    print("Zmienna i jest mniejsza od zera")
```

Kiedy warunek zostanie spełniony zobaczymy napis: _"Zmienna i jest większa od zera!"_ natomist jeśli nasza liczba nie spęłni warunku czyli będzie równa 0 bądź mniejsza to zobaczymy napis: _"Zmienna i jest mniejsza od zera"_.


## Słownik z ang. (*dictionary*) w skrócie *dict*

---

Ostatni z najbardziej podstawowych zbiorów ale nadzwyczaj użyteczny. Słownik jest zbiorem, którego elementami jest para "klucz": "wartosc_klucza", już tłumaczę na przykładzie o co chodzi.

 ```py
>>> slownik = {"unikanlna_nazwa_klucza":"wartosc_klucza", "unikanlna_nazwa_klucza_2": "wartosc_klucza_2"}
>>> print(slownik)
{'unikanlna_nazwa_klucza_2': 'wartosc_klucza_2', 'unikanlna_nazwa_klucza': 'wartosc_klucza'}
>>> print(slownik["unikanlna_nazwa_klucza"])
wartosc_klucza
>>> print(slownik["unikanlna_nazwa_klucza_2"])
wartosc_klucza_2
```

Warto dodać i zapamiętać, że słownik jest zbiorem mutowalnym - czyli można go modyfikować, a także jest zbiorem nieuporządkowanym - to bardzo ważne!.  

Co oznacza nieuporządkowany? Otóż oznacza to że gdy go wyświetlamy funkcją print jego elementy to mogą się one zamienić kolejnością czyli np. pierwsza para może być wyświetlona jako ostatnia:

 ```py
>>> slownik = {"unikanlna_nazwa_klucza":"wartosc_klucza", "unikanlna_nazwa_klucza_2": "wartosc_klucza_2"}
>>> print(slownik)
{'unikanlna_nazwa_klucza_2': 'wartosc_klucza_2', 'unikanlna_nazwa_klucza': 'wartosc_klucza'}
>>> print(slownik)
{'unikanlna_nazwa_klucza': 'wartosc_klucza', 'unikanlna_nazwa_klucza_2': 'wartosc_klucza_2'}
```

Więc skoro słownik jest zbiorem nieuporządkowanym to znaczy, że nie powinniśmy się odwoływać do jego elementów po indeksie ale po nazwie klucza np. slownik["unikanlna_nazwa_klucza_2"].

Jak dodać coś do słownika? Możemy użyć funkcji wbudowanej update() dla dodania kilku par `klucz:wartosc` na raz:

```python
>>> slownik = {"klucz0":0}
>>> slownik.update({"klucz1":1, "klucz2":2})
>>> slownik
{"klucz0":0,"klucz1":1, "klucz2":2}
```

Jak dodać pojedyńczą parę?

```python
>>> slownik["nowy_klucz"] = "wartość_nowego_klucza"
{"klucz0":0,"klucz1":1, "klucz2":2, "nowy_klucz": "wartość_nowego_klucza"}
```

## Lista składana z ang. (*list comprehension*)

---

Lista skladana to nic innego jak krótsze zapisanie dodawania poszczególnych elementów do zdefiniowanej listy za pomocą pętli for.

**Wzór:**

[ wyrażenie for element in list if warunek ]

**Przykład:**

 ```py
 >>> lista = [ i for i in range(10) ]
 >>> print(lista)
 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
 ```
 
 ## Pobieranie wartości od użytkownika - funcja input()

---

Dzięki funkcji input() jesteśmy w stanie pobrać od użytkownika dowolny ciąg znaków, który może być liczbą, słowem czy nazwą pliku wraz z formatem.

```python
>>> x = input("Podaj wartosc x: ")
Podaj wartosc x: 5
>>> print(x)
5

```

 To by było na tyle, **zapraszam** na zajęcia!