#!/usr/bin/env python


# Zadanie 2
def pobierz_dane():
    liczba_pierwsza_status = False
    while liczba_pierwsza_status == False:
        liczba_pierwsza = str(input("Podaj liczbe naturalna: "))
        if liczba_pierwsza.isdigit():
            liczba_pierwsza_status = True
            break
        else:
            print "Podana liczba nie jest liczba naturalna! Podaj liczbe naturalna!"
    return int(liczba_pierwsza)

def sprawdz_czy_liczba_pierwsza(liczba):
    liczba_pierwsza_status = True
    if liczba > 1:
        for num in range(2, liczba):
            if liczba % num == 0:
                liczba_pierwsza_status = False
                break
    return liczba_pierwsza_status

print "\nProgram do sprawdzania czy podana przez uzytkownika liczba jest liczba pierwsza.\n"
liczba_uzytkownika = pobierz_dane()

if sprawdz_czy_liczba_pierwsza(liczba_uzytkownika):
    print("Brawo! Podana liczba: {}, jest liczba pierwsza!".format(liczba_uzytkownika))
else:
    print("Porazka! Podana liczba: {}, nie jest liczba pierwsza!".format(liczba_uzytkownika))
