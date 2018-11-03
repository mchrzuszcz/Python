#!/usr/bin/env python

def generuj_ciag_look_and_say(ciag):
    cyfra=ciag[0]
    counter=0
    nowy_ciag=""
    for liczba in ciag:
        if liczba == cyfra:
            counter += 1
        else:
            nowy_ciag="{}{}{}".format(nowy_ciag,counter,cyfra)
            cyfra = liczba
            counter = 1
    nowy_ciag = "{}{}{}".format(nowy_ciag, counter, cyfra)
    return nowy_ciag

def main():
    n=5
    ciag="1"
    print "{} wyraz ciagu look and say: {}".format(1, ciag)
    for i in range(n-1):
        ciag = generuj_ciag_look_and_say(ciag)
        print "{} wyraz ciagu look and say: {}".format(i+2, ciag)

if __name__ == '__main__':
    main()