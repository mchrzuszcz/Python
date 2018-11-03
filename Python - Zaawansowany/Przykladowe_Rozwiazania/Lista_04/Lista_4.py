#!/usr/bin/env python3

# Lista 4

# Zadanie 1

print("\nZadanie 1:\n")

slownik = {"chleb": 1, "cebula": 2, "szczypior": 3, "marchewka": 4, "boczek": 5}

print(slownik)

for key, value in slownik.items():
    print(key, value)

print(sum(slownik.values()) / len(slownik.values()))

slownik.update({"ogorek": 6})
print(slownik)

print(sum(slownik.values()) / len(slownik.values()))

del slownik["ogorek"]

print(slownik)

print(sum(slownik.values()) / len(slownik.values()))

# Zadanie 2

print("\nZadanie 2:\n")

def mniejsza(a, b):
    if (a < b):
        return a
    else:
        return b

# wyzej mozna ulepszyc

print(mniejsza(4, 3))

# Zadanie 3
print("\nZadanie 3:\n")

def mniejsza_args(*liczby):
    najmniejsza = liczby[0]
    for liczba in liczby:
        najmniejsza = mniejsza(najmniejsza,liczba)
    print(najmniejsza)

mniejsza_args(5, 1, 2, 3)

# Zadanie 4
print("\nZadanie 4:\n")

def fibonaci(n):
    a, b = 0, 1
    print("Wyraz numer:", 0, "Wartosc:", a)
    print("wyraz numer:", 1, "Wartosc:", b)
    for i in range(0, n - 1):
        a, b = b, a + b
        print("Wyraz numer:", i + 2, "Wartosc:", b)


print("Pierwsza wersja fibonacciego:")
fibonaci(10)

def fibonaci2(n):
    a = 0
    b = 1
    print("Wyraz ciagu {0} wynosi: {1}".format(0, a))
    print("Wyraz ciagu {0} wynosi: {1}".format(1, b))
    for i in range(2, n):
        a, b = b, a + b
        print("Wyraz ciagu {0} wynosi: {1}".format(i, b))

print("\nDruga wersja fibonacciego:")
fibonaci2(5)

def fibonaci3(n):
    if n == 0:
        return n
    if n == 1:
        return n
    f_prim = 0
    f = 1
    for i in range(2, n + 1):
        m = f + f_prim
        f_prim = f
        f = m
    return f


print("\nTrzecia wersja fibonacciego:")
print(fibonaci3(2))

# Zadanie 5
print("\nZadanie 5 w osobnym pliku.\n")

# Zadanie 6
print("\nZadanie 6:\n")

def argumenty(*pozycyjne, **kluczowe):
    for i, item in enumerate(pozycyjne):
        print "{} -> {}".format(i,item)
    for klucz,wartosc in kluczowe.iteritems():
        print "{} -> {}".format(klucz,wartosc)



