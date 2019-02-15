#!/usr/bin/env python

import math
import sys
import turtle


def sprawdz_argumenty(*args):
    liczba_argumentow = len(args)
    if liczba_argumentow != 4:
        print("Zla liczba argumentow {} ! Skrypt powinien przyjac dokladnie 3 argumenty.".format(liczba_argumentow))
        exit(1)

def czy_da_sie_zbudowac_trojkat(a,b,c):
    if a + b <= c or a + c <= b or b + c <= a:
        return False
    return True

def typ_rammiennosci_trojkata(*dlugosci_bokow):
    typ = ""
    if dlugosci_bokow.count(dlugosci_bokow[0]) == 3:
        typ = "rownoboczny"
    elif dlugosci_bokow.count(dlugosci_bokow[0]) == 2 or dlugosci_bokow.count(dlugosci_bokow[1]) == 2:
        typ = "rownoramienny"
    else:
        typ = "roznoramienny"
    return typ

def typ_katnosci_trojkata(a,b,c):
    a, b, c = sorted([a,b,c])
    kwadrat_najdluzszego_boku = c**2
    if a**2 + b**2 == kwadrat_najdluzszego_boku:
        typ = "prostokatny"
    if a**2 + b**2 < kwadrat_najdluzszego_boku:
        typ = "rozwartokatny"
    elif a**2 + b**2 > kwadrat_najdluzszego_boku:
        typ = "ostrokatny"
    return typ

def obwod_trojkata(*dlugosci_bokow):
    return sum(dlugosci_bokow)

def pole_trojkata(*dlugosci_bokow):
    obwod = obwod_trojkata(*dlugosci_bokow)
    polowa_obwodu = float(obwod/2)
    pole = math.sqrt(polowa_obwodu*(polowa_obwodu-dlugosci_bokow[0])*(polowa_obwodu-dlugosci_bokow[1])*(polowa_obwodu-dlugosci_bokow[2]))
    return pole

def rysuj_trojkat(a,b,c):

    turtle.speed(20)
    turtle.pencolor("red")
    turtle.forward(a*50)
    kat_do_obrotu = math.degrees(math.acos((a ** 2 + c ** 2 - b ** 2) / (2.0 * a * c)))
    turtle.left(180-kat_do_obrotu)
    if c != a:
        turtle.pencolor("green")
    turtle.forward(c*50)
    kat_do_obrotu = math.degrees(math.acos((b ** 2 + c ** 2 - a ** 2) / (2.0 * b * c)))
    turtle.left(180-kat_do_obrotu)
    if b != a and b != c:
        turtle.pencolor("blue")
    elif b == a:
        turtle.pencolor("red")
    turtle.forward(b*50)
    turtle.mainloop()

def main():

    #dlugosci_bokow = [3,4,5] # prostokatny
    #dlugosci_bokow = [2,4,4] # rownoramienny
    #dlugosci_bokow = [4,4,4] # rownoboczny

    print(sys.argv)
    sprawdz_argumenty(*sys.argv)
    dlugosci_bokow = list(map(int, sys.argv[1:]))
    print(dlugosci_bokow)

    if not czy_da_sie_zbudowac_trojkat(*dlugosci_bokow):
        print("Nie da sie zbudowac trojkata z podanych odcinkow!")
        exit(1)

    typ_ramiennosci = typ_rammiennosci_trojkata(*dlugosci_bokow)
    typ_katnosci = typ_katnosci_trojkata(*dlugosci_bokow)
    ob_trojkata = obwod_trojkata(*dlugosci_bokow)
    po_trojkata = pole_trojkata(*dlugosci_bokow)

    print("Typ ramiennosci trojkata: {}". format(typ_ramiennosci))
    print("Typ katnosci trojkata: {}".format(typ_katnosci))
    print("Obwod trojkata: {}".format(ob_trojkata))
    print("Pole trojkata: {}".format(po_trojkata))
    print("Rysuje trojkat...")
    rysuj_trojkat(*dlugosci_bokow)

if __name__ == '__main__':
    main()