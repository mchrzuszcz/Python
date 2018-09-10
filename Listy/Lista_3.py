#!/usr/bin/env python3
import random


#Zadanie 2

print("Zadanie 2")

squares = [x**2 for x in range(10)]

print(squares)

for i, item in enumerate(squares):
    print("{0} -> {1}".format(i,item))



# zadanie 3
print("Zadanie 3")
print("drukujemy wszystkie liczby parzyste mniejsze od 10")
i = 0
while i < 10:
#    if not ((i % 2) != 0):    # reszta z dzielenia != 0 -> True
#        print(i) # drukuj liczby parzyste

    if i % 2 ==0:
        print(i)
    i += 1 # zwiÄ™ksz i o jeden


print("Zadanie 4")
# lista zakupow
grocery = ['jajka', 'mleko', 'chleb', 'maslo', 'piwo']
# ilosc sztuk  - MALA MODYFIKACJA TUTAJ ZAMIAST LISTY DALEM SLOWNIK
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


print("Zadanie 5")
#randomowa_liczba = random.randint(0,100)
randomowa_liczba = 90
status = True
print(randomowa_liczba)
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