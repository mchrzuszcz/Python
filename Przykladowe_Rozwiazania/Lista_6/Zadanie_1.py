#!/usr/bin/env python

# Zadanie 1
# a1 - pierwszy wyraz ciagu
# q - iloraz
# Przyklad 1,3,9,27. Iloraz: 3

def pobierz_dane():
    a1 = input("Podaj pierwszy wyraz ciagu: ")
    q = input("Podaj iloraz ciagu: ")
    return a1, q

def generuj_ciag_geometryczny(a1, q, n=100):
    ciag_geometryczny = []
    ciag_geometryczny.append(a1)
    liczba = a1
    for i in range(1, n):
        liczba = liczba * q
        ciag_geometryczny.append(liczba)
    return ciag_geometryczny

def znajdz_liczby_parzyste(lista_liczb):
    lista_parzysta = []
    for i in lista_liczb:
        if i % 2 == 0:
            lista_parzysta.append(i)
    return lista_parzysta

a1, q = pobierz_dane()
print a1,q
ciag_geometryczny = generuj_ciag_geometryczny(a1,q,4)
print ciag_geometryczny
lista_parzysta = znajdz_liczby_parzyste(ciag_geometryczny)
print lista_parzysta
