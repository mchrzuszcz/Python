
# Python
## Prework do 3 listy zadań 

## Pętla - For

---

Niezwykle prosty mechanim a bardzo przydatny. Pozwala nam przechodzic czyli "iterować" po każdem elemencie danego zbioru np. listy.  

Dla przykładu zdefiniujmy sobie prostą liste i wykorzystajmy pętle for które pozwoli nam wypisać wszystkie elementy tej listy:

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

Teraz dodamy bardzo prostą i fajną funkcję *enumerate* do naszej pętli for żeby oprócz literek wyświetlić też pozycje czyli indeks każdej litery. Temat indeksowania powinieneś poznać na poprzedniej lekcji więc to będzie bułka z masłem. 

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

Drugi typ pętli, równie prosty jak for. Pętli while nie powinno sie używać na zbiorach jak np. lista, a raczej w przypadkach kiedy chcemy aby wykonywała się jakaś akcja dopóki zdefiniowany warunek jest spełniony.   

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

If

## Lista składana z ang. (*list comprehension*)

---

Lista skladana

## Słownik

---

Slownik

