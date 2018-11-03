#!/usr/bin/env python

def objetosc_prostopadloscianu(a, b=None, c=None):
    if b == None and c == None:
        b = a
        c = a
    objetosc = a * b * c
    return objetosc

print objetosc_prostopadloscianu(1,2,3)
print objetosc_prostopadloscianu(2)

