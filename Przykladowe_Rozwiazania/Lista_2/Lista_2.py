#!/usr/bin/env python

import sys

# Zad 1
print("\nZadanie 1\n")

tupla = (0,1,2,3,4, "piec", "szesc", "siedem", "osiem", "dziewiec")
print(tupla[:3])
print(tupla[-2:])
print(tupla[1::2])
print(len(tupla))
print(len(tupla[-1]))

# Zad 2
print("\nZadanie 2\n")

studenci = ["Kasia", "Basia", "Marek", "Darek"]
print(studenci)
studenci.append("Jozek")
print(studenci)
studenci.extend(["Ania","Basia"])
print(studenci)
studenci.sort()
print(studenci)
print(studenci[3])
print(studenci[:2])
print(studenci[-2:])
studenci.remove("Basia")
studenci.remove("Basia")
print(studenci)
print(len(studenci))
studenci = tuple(studenci)
print(type(studenci))


# Zad 3
print("\nZadanie 3\n")

lista = list(range(3,100,3))
print(lista[1],lista[2],lista[-1])
print(lista[5],lista[8])
del lista[5::3]
print(lista[5],lista[8])
print(sum(lista))
print(sum(lista)/len(lista))

# Zad 4
print("\nZadanie 4\n")

krotka = ("a","b","c","d")
print(krotka)
print("".join(krotka))
print(" ".join(krotka))
print(", ".join(krotka))
print("\t".join(str(([0]*100))))
print("\t".join(str(0) for i in range(100)))

# Zad 5
print("\nZadanie 5\n")
slubowanie = """
Wstepujac do wspolnoty akademickiej Uniwersytetu Wroclawskiego, slubuje uroczyscie:
- zdobywal wiedze i umiejetnosci,
- postepowal zgodnie z prawem, tradycja i dobrymi obyczajami akademickimi,
- dbal o dobre imie Uniwersytetu Wroclawskiego i godnosc studenta.
"""

print(slubowanie)
slubowanie
print(slubowanie.count(" i "))
print(slubowanie.count("i"))
print("Uniwersytet" in slubowanie)
print(len(slubowanie.split(" ")))

print(slubowanie.split("\n"))
print(len(slubowanie.split("\n")))

print(slubowanie.splitlines())
print(len(slubowanie.splitlines()))


# Zadanie 6
print("\nZadanie 6\n")
print(sys.getsizeof(0))
print(sys.getsizeof(1))
print(sys.getsizeof(2**100))
print(sys.getsizeof(True))
print(sys.getsizeof(False))
print("boole")
print(bool(0))
print(bool(1))
print("isinstance")
print(isinstance(0,int))
print(isinstance(0,float))
print(isinstance(0.0,float))
print(isinstance(True,int))
print(isinstance(True,int))

# Zadanie 7
print("\nZadanie 7\n")
x = 2
y = x

print(x, y, id(x), id(y))
y = 3
print(x, y, id(x), id(y))

x = [1,2]
y = x
print(x, y, id(x), id(y))
y[1] = 3
print(x, y, id(x), id(y))

# Zadanie 8
print("\nZadanie 8\n")
x = (a, b, c) = (1, 2, 3)
print(x)
print(a)
print(b)
print(c)

x = a, b, c = 1, 2, 3


print(x)
print(a)
print(b)
print(c)