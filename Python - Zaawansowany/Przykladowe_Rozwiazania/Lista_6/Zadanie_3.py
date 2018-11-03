#!/usr/bin/env python

import math
import sys

def pobierz_argumenty(*args):
    liczba_argumentow = len(args)
    if liczba_argumentow != 3:
        print "Zla liczba argumentow {}! Skrypt powinien przyjac dokladnie 3 argumenty.".format(liczba_argumentow)
        exit(1)

def typ_rammiennosci_trojkata(*dlugosci_bokow):
    typ = ""
    if dlugosci_bokow.count(dlugosci_bokow[0]) == 3:
        typ = "rownoboczny"
    elif dlugosci_bokow.count(dlugosci_bokow[0]) == 2 or dlugosci_bokow.count(dlugosci_bokow[1]) == 2:
        typ = "rownoramienny"
    else:
        typ = "roznoramienny"
    return typ

def typ_katnosci_trojkata(*dlugosci_bokow):
    typ = ""
    index_najdluszy_bok = dlugosci_bokow.index(max(dlugosci_bokow))
    if index_najdluszy_bok == 0:
        index_krotszy_bok_1 = 1
        index_krotszy_bok_2 = 2
    elif index_najdluszy_bok == 1:
        index_krotszy_bok_1 = 0
        index_krotszy_bok_2 = 2
    else:
        index_krotszy_bok_1 = 0
        index_krotszy_bok_2 = 1
    kwadrat_najdluzszego_boku = dlugosci_bokow[index_najdluszy_bok]**2
    if dlugosci_bokow[index_krotszy_bok_1]**2 + dlugosci_bokow[index_krotszy_bok_2]**2 == kwadrat_najdluzszego_boku:
        typ = "prostokatny"
    if dlugosci_bokow[index_krotszy_bok_1]**2 + dlugosci_bokow[index_krotszy_bok_2]**2 < kwadrat_najdluzszego_boku:
        typ = "rozwartokatny"
    elif dlugosci_bokow[index_krotszy_bok_1]**2 + dlugosci_bokow[index_krotszy_bok_2]**2 > kwadrat_najdluzszego_boku:
        typ = "ostrokatny"
    return typ

def obwod_trojkata(*dlugosci_bokow):
    obwod = 0
    typ_ramiennosci = typ_rammiennosci_trojkata(*dlugosci_bokow)
    if typ_ramiennosci == "rownoboczny":
        obwod = 3*dlugosci_bokow[0]
    elif typ_ramiennosci == "rownoramienny":
        if dlugosci_bokow[0] == dlugosci_bokow[1]:
            obwod = 2*dlugosci_bokow[0] + dlugosci_bokow[2]
        elif dlugosci_bokow[0] == dlugosci_bokow[2]:
            obwod = 2*dlugosci_bokow[0] + dlugosci_bokow[1]
        else:
            obwod = 2*dlugosci_bokow[1] + dlugosci_bokow[0]
    else:
        obwod = dlugosci_bokow[0] + dlugosci_bokow[1] + dlugosci_bokow[2]
    return obwod

def pole_trojkata(*dlugosci_bokow):
    obwod = obwod_trojkata(*dlugosci_bokow)
    polowa_obwodu = float(obwod/2)
    pole = math.sqrt(polowa_obwodu*(polowa_obwodu-dlugosci_bokow[0])*(polowa_obwodu-dlugosci_bokow[1])*(polowa_obwodu-dlugosci_bokow[2]))
    return pole

def main():

    #dlugosci_bokow = [3,4,5] # prostokatny
    #dlugosci_bokow = [2,4,4] # rownoramienny
    #dlugosci_bokow = [4,4,4] # rownoboczny
    print sys.argv
    dlugosci_bokow = map(int, sys.argv[1:])
    print dlugosci_bokow

    pobierz_argumenty(*dlugosci_bokow)

    typ_ramiennosci = typ_rammiennosci_trojkata(*dlugosci_bokow)
    typ_katnosci = typ_katnosci_trojkata(*dlugosci_bokow)
    ob_trojkata = obwod_trojkata(*dlugosci_bokow)
    po_trojkata = pole_trojkata(*dlugosci_bokow)

    print "Typ ramiennosci trojkata: {}". format(typ_ramiennosci)
    print "Typ katnosci trojkata: {}".format(typ_katnosci)
    print "Obwod trojkata: {}".format(ob_trojkata)
    print "Pole trojkata: {}".format(po_trojkata)

if __name__ == '__main__':
    main()


