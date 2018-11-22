#!/usr/bin/env python

import random
import turtle

# Zadanie 1
print("\nZadanie 1\n")

squares = [x**2 for x in range(10)]

print(squares)

for i, item in enumerate(squares):
    print("{0} -> {1}".format(i,item))

# Zadanie 2
print("\nZadanie 2\n")
print("Drukujemy wszystkie liczby parzyste mniejsze od 10")
i = 0
while i < 10:
    # 1 rozwiazanie
    #if not ((i % 2) != 0):    # reszta z dzielenia != 0 -> True
        #print(i) # drukuj liczby parzyste
    # 2 rozwiazanie
    if i % 2 == 0:
        print(i)
    # Ponizsza linia dla kazdego rozwiazania
    i += 1 # zwieksz i o jeden

# Zadanie 3
print("\nZadanie 3\n")
# lista zakupow
grocery = ['jajka', 'mleko', 'chleb', 'maslo', 'piwo']
# ilosc sztuk
n_items = {}
# zakazane produkty
prohibited = ['wodka', 'piwo', 'wino']

# w petli pytamy uzytkownika, ile sztuk danego produktu chce kupic
for product in grocery:
    # wydrukuj na ekranie komunikat: "Produkt [nazwa produktu]: sztuk = "
    # pobierz liczbe od uĹĽytkownika i zapisz w n_items
    liczba = 0
    if product in prohibited:
        print("Produkt {0}: sztuk = {1}".format(product, liczba))
    else:
        liczba = input("Produkt {0}: sztuk = ".format(product))
    n_items.update({product:liczba})
    # pomin„ produkty zakazane (i automatycznie przyjmij ilosc = 0)

# drukujemy liste zakupow
print(n_items)
# w petli wydrukuj: [lp]. [nazwa produktu]: [iloĹ›Ä‡]
# czyli np.: 1. jajka: 5 itd.
# [(index, (key, value)), ...]
for i, (key, value) in enumerate(n_items.items()):
    print("{0}. {1}: {2}".format(i, key, value))


print("Zadanie 4")
print("\nZadanie 4\n")
randomowa_liczba = random.randint(0,100)
print(randomowa_liczba)
status = True
while status == False:
    liczba_usera = int(input("Zagdnij liczbe w przedziale od 0 do 100: "))
    roznica = abs(randomowa_liczba-liczba_usera)
    if liczba_usera == randomowa_liczba:
        print("Odgadles liczbe! Wygrales!")
        status = True
    elif liczba_usera > randomowa_liczba:
        if roznica >= 50:
            print("Duzo mniejsza")
        elif roznica < 50 and roznica > 10:
            print("Mniejsza")
        else:
            print("Troche mniejsza")
    else:
        if roznica >= 50:
            print("Duzo wieksza")
        elif roznica < 50 and roznica > 10:
            print("Wieksza")
        else:
            print("Troche wieksza")

print("Zadanie 5")
print("\nZadanie 5\n")
length = input("Podaj dlugosc boku: ")
# 5.1
n_sides = 3

# 5.2
#n_sides = 6

# 5.3
#n_sides = input("Podaj liczbe bokow: ")

turtle.speed(20)

for i in range(n_sides):
    # 5.1
    turtle.forward(length)
    turtle.right(120)
    # 5.2
    #turtle.forward(length)
    #turtle.right(60)
    # 5.3
    #turtle.forward(length)
    #turtle.right(360/n_sides)

turtle.mainloop()