#!/usr/bin/env python

import matplotlib.pyplot as plt

class Samochod(object):

    def __init__(self, max_predkosc, spalanie):
        self.max_predkosc = max_predkosc
        self.spalanie = spalanie
        self.wszystkie_predkosci = []
        self.wszystkie_trasy = {}
        self.iterator_trasy = 0
        self.obecna_predkosc = 0
        self.pokonany_dystans = 0
        self.czas_podrozy = 0

    def przyspiesz(self, o_ile):
        self.obecna_predkosc += o_ile
        if self.obecna_predkosc > self.max_predkosc:
            self.obecna_predkosc = self.max_predkosc
        if self.obecna_predkosc > 0:
            self.wszystkie_predkosci.append(self.obecna_predkosc)

    def zwolnij(self, o_ile):
        self.obecna_predkosc -= o_ile
        if self.obecna_predkosc < 0:
            self.obecna_predkosc = 0
        if self.obecna_predkosc > 0:
            self.wszystkie_predkosci.append(self.obecna_predkosc)

    def hamuj(self):
        self.obecna_predkosc = 0

    def turbo(self):
        self.obecna_predkosc = self.max_predkosc
        self.wszystkie_predkosci.append(self.obecna_predkosc)

    def jedz(self, dystans):
        self.czas_podrozy += float(dystans)/float(self.obecna_predkosc)
        self.pokonany_dystans += dystans
        self.iterator_trasy += 1
        self.dodaj_trase()

    def wylicz_srednia_predkosc(self):
        srednia_predkoc = float(sum(self.wszystkie_predkosci))/float(len(self.wszystkie_predkosci))
        return srednia_predkoc

    def wylicz_srednie_spalanie(self):
        srednie_spalanie = (float(self.pokonany_dystans)/100.0) * self.spalanie
        return srednie_spalanie

    def dodaj_trase(self):
        klucz_trasy = "trasa_{}".format(self.iterator_trasy)
        self.wszystkie_trasy.update({klucz_trasy: {"dystans": self.pokonany_dystans, "czas": self.czas_podrozy, "predkosc": self.obecna_predkosc}})

    def podroz(self):
        srednia_predkosc = self.wylicz_srednia_predkosc()
        srednie_spalanie = self.wylicz_srednie_spalanie()
        print("Samochod przejechal {} km, ze srednia predkoscia {} hm/h, co zajelo {} h i spalilo {} litrow benzyny.".format(self.pokonany_dystans, srednia_predkosc, self.czas_podrozy, srednie_spalanie))

    # Zadanie 2

    def rysuj_wykres_dystans_czas(self):
        x = [wartosc['czas'] for wartosc in self.wszystkie_trasy.values()]
        y = [wartosc['dystans'] for wartosc in self.wszystkie_trasy.values()]
        plt.xlabel('Czas podrozy[h]')
        plt.ylabel('Pokonany dystans [km]')
        plt.title('Stosunek dystansu od czasu')
        plt.grid(True)
        plt.plot(x, y)
        plt.show()

    def rysuj_wykres_predkosc_czas(self):
        x = [wartosc['czas'] for wartosc in self.wszystkie_trasy.values()]
        y = [wartosc['predkosc'] for wartosc in self.wszystkie_trasy.values()]
        plt.xlabel('Czas podrozy[h]')
        plt.ylabel('Predkosc [km/h]')
        plt.title('Stosunek predkosc od czasu')
        plt.grid(True)
        plt.plot(x, y)
        plt.show()

# Zadanie 1

samochod = Samochod(200,10)
samochod.przyspiesz(100)
samochod.jedz(100) # dystans = 100km, czas = 1h
samochod.turbo()
samochod.jedz(100) # dystans = 100 + 100km, czas = 1 + 0.5h
samochod.podroz()

# Zadanie 2
samochod.rysuj_wykres_dystans_czas()
samochod.rysuj_wykres_predkosc_czas()