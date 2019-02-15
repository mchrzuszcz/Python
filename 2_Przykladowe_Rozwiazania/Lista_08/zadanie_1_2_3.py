#!/usr/bin/env python

import sys

def generuj_ciag_skladana(n):
    ciag = [float(i)/float(i + 1) for i in range(n)]
    return ciag

def generuj_ciag_generator(n):
    ciag = (float(i)/float(i + 1) for i in range(n))
    return ciag

def zapisz_do_pliku(zawartosc, nazwa_pliku):
    with open(nazwa_pliku, "w") as f:
        if isinstance(zawartosc,list):
            for element in zawartosc:
                f.write("{}\n".format(element))
        else:
            f.write(zawartosc)

def main():
    # Zadanie 1
    n = int(sys.argv[1])
    ciag_1 = generuj_ciag_skladana(n)
    zapisz_do_pliku(ciag_1, "zadanie_1.txt")
    # Zadanie 2
    ciag_2 = generuj_ciag_generator(n)
    print "Zarezerwowana pamiec przez liste skladana: {}.".format(sys.getsizeof(ciag_1))
    print "Zarezerwowana pamiec przez generator: {}.".format(sys.getsizeof(ciag_2))
    print "Zawartosc listy skladanej: {}".format(ciag_1)
    print "Zawartosc generatora: {}.".format(ciag_2)
    print "Uzycie generatora:"
    print next(ciag_2)
    print next(ciag_2)
    print next(ciag_2)
    # Zadanie 2 - wyjasnienie
    # Na przyklad kiedy chcesz przeiterowac cala liste, python w przypadku listy skladanej rezerwuje pamiec odrazu dla wszystkich elementow listy.
    # W przypadku generatora python nie trzyma wszystkich elementow w pamieci tylko "generuje" kolejny element zbioru na zadanie.

if __name__ == '__main__':
    main()