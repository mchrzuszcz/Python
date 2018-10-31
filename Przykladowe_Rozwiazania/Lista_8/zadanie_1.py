#!/usr/bin/env python

import sys

def generuj_ciag(n):
    ciag = [ float(i)/float(i + 1) for i in range(n)]
    return ciag

def zapisz_do_pliku(zawartosc, nazwa_pliku):
    with open(nazwa_pliku, "w") as f:
        if isinstance(zawartosc,list):
            for element in zawartosc:
                f.write("{}\n".format(element))
        else:
            f.write(zawartosc)

def main():

    n = int(sys.argv[1])
    ciag = generuj_ciag(n)
    zapisz_do_pliku(ciag, "zadanie_1.txt")


if __name__ == '__main__':
    main()