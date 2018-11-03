#!/usr/bin/env python

import math

def pobierz_dane():
    a = input("Podaj wartosc wspolczynnika a: ")
    b = input("Podaj wartosc wspolczynnika b: ")
    c = input("Podaj wartosc wspolczynnika c: ")
    return a,b,c

def wylicz_delte(a,b,c):
    delta = b**2 - 4*a*c
    return delta

def wylicz_miejsca_zerowe(delta,a,b):
    if delta > 0:
        x1 = float(-b - math.sqrt(delta)) / float(2 * a)
        x2 = float(-b + math.sqrt(delta)) / float(2 * a)
        print "Rownanie kwadratowe posiada dwa rozwiazanie: x1 {}, x2 {}.".format(x1,x2)
    elif delta == 0:
        x0 = float(-b) / float(2*a)
        print "Rownanie kwadratowe posiada jedno rozwiazanie: x0 {}".format(x0)
    else:
        print "Rownanie kwadratowe nie posiada rozwiazan w zbiorze liczb rzeczywistych dla delta < 0."

def main():
    a,b,c = pobierz_dane()
    delta = wylicz_delte(a,b,c)
    wylicz_miejsca_zerowe(delta,a,b)

if __name__ == '__main__':
    main()




