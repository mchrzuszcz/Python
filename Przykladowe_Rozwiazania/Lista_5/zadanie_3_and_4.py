#!/usr/bin/env python

def collatz(c0,n):
    lista = []
    lista.append(c0)
    cn = c0
    for i in range(1,n):
        if cn % 2 == 0:
            cn = cn/2
        else:
            cn = 3*cn +1
        lista.append(cn)
    return lista

def collatz_pierwsza_1(c0,n):
    lista = []
    lista.append(c0)
    cn = c0
    for i in range(1,n):
        if cn % 2 == 0:
            cn = cn/2
        else:
            cn = 3*cn +1
        lista.append(cn)
        if cn == 1:
            break
    return lista

print("\nZadanie 3:\n")

lista_collatza = collatz(6,9)
for ele in lista_collatza:
    print ele

print("\nZadanie 4:\n")

lista_collatza_pierwsza = collatz_pierwsza_1(6,10)

for ele in lista_collatza_pierwsza:
    print ele