#!/usr/bin/env python3

# Lista 4

# Zadanie 1

print("Zadanie 1: \n\n")

slownik = {"chleb": 1, "cebula": 2, "szczypior": 3, "marchewka": 4, "boczek": 5}

print(slownik)

for key, value in slownik.items():
    print(key, value)

slownik.update({"ogorke": 6})
print(slownik)

print(sum(slownik.values()))

print(sum(slownik.values()) / len(slownik.values()))

del slownik["ogorke"]

print(slownik)


def testowy(a, b):
    print(a, b)


testowy(2, 3)

# Zadanie 2

print("Zadanie 2: \n\n")


def mniejsza(a, b):
    if (a < b):
        return a
    else:
        return b


# wyzej mozna ulepszyc


print(mniejsza(4, 3))

# Zadanie 3
print("Zadanie 3: \n\n")


def mniejsza_args(*args):
    for arg in args:
        print(arg)


mniejsza_args(1, 2, 3)

# Zadanie 4
print("Zadanie 4: \n\n")


def fibonaci(n):
    a, b = 0, 1
    print("Wyraz numer:", 0, "Wartosc:", a)
    print("wyraz numer:", 1, "Wartosc:", b)
    for i in range(0, n - 1):
        a, b = b, a + b
        print("Wyraz numer:", i + 2, "Wartosc:", b)


print("Fib")
fibonaci(10)


# Nowy fib

def nowy_fib(n):
    a = 0
    b = 1
    print("Wyraz ciagu {0} wynosi: {1}".format(0, a))
    print("Wyraz ciagu {0} wynosi: {1}".format(1, b))
    for i in range(2, n):
        a, b = b, a + b
        print("Wyraz ciagu {0} wynosi: {1}".format(i, b))


print("Nowy Fib")
nowy_fib(5)


# Prosty fib

def prosty_fib(n):
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


print("Prosty Fib")
print(prosty_fib(2))

# Zadanie 5
print("Zadanie 5: \n\n")

pierwszy_input = input("Give me sth!: ")
print(pierwszy_input)

# Zadanie 6
print("Zadanie 6: \n\n")


def wymusza(*args):
    if len(args) < 3:
        print("za malo")
        return False


# lub

def kluczowe(klient, produkt, cena):
    print(klient, produkt, cena)


kluczowe(klient="Jasiek", produkt="Chleb", cena=5)

# Zadanie 7
print("Zadanie 7: \n\n")


def sklep_z_serami(rodzaj, *argumenty, **klucze):
    print("-- Czy macie", rodzaj, '?')
    print("-- Przykro mi,", rodzaj, "wĹ‚aĹ›nie siÄ™ skoĹ„czyĹ‚.")
    for arg in argumenty: print(arg)
    print('-' * 40)
    for kl in klucze.keys(): print(kl, ':', klucze[kl])


# argument kluczowy to te z klucz:wartosc np. klient=John to jest kluczowy, pozycyjny to ten ktory jest okreslany wedlug pozycji

sklep_z_serami('Limburger', "Jest bardzo dojrzaly, prosze pana.",
               "Jest naprawde bardzo, BARDZO dojrzaly, prosze pana.", klient='John Cleese',
               wlasciciel='Michael Palin', skecz='Skecz ze sklepem z serami')

