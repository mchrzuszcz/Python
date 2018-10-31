#!/usr/bin/env python

import zadanie_1


def collect_data_from_user(temp_name="Celcjuszach"):
    while True:
        n = input("Ile temperatur (w {}) chcesz wygenerowac? Podaj liczbe calkowita: ".format(temp_name))
        if str(n).isdigit():
            break
        print("Podana wartosc: {}, nie jest liczba calkowita!".format(n))
    return n

n = collect_data_from_user()
random_temperatures = zadanie_1.random_celsius_temp(n)
print random_temperatures
zadanie_1.save_to_file(random_temperatures)