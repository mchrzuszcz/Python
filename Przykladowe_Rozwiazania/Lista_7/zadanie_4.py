#!/usr/bin/env python

import zadanie_1

celsius_temperatures = zadanie_1.read_file("Celcjusz.txt")
fahrenheit_temperatures = zadanie_1.read_file("Fahrenheit.txt")

celsius_temperatures = map(float, celsius_temperatures)
fahrenheit_temperatures = map(float, fahrenheit_temperatures)

fahrenheit_temperatures_size = len(fahrenheit_temperatures)
celsius_temperatures_size = len(celsius_temperatures)

if fahrenheit_temperatures_size != celsius_temperatures_size:
    print "Different count of temperatures. Fahrenheit: {}, Celsius: {}".format(fahrenheit_temperatures_size, celsius_temperatures_size)
    exit(1)

celsius_in_kelvin = []
fahrenheit_in_kelvin = []

for i in range(celsius_temperatures_size):
    c_kelvin = zadanie_1.convert_celsius_to_kelvin(celsius_temperatures[i])
    f_kelvin = zadanie_1.convert_fahrenheit_to_kelvin(fahrenheit_temperatures[i])
    celsius_in_kelvin.append(c_kelvin)
    fahrenheit_in_kelvin.append(f_kelvin)

equal_temperatures = []
not_equal_temperatures = []

for i in range(len(celsius_in_kelvin)):
    if celsius_in_kelvin[i] == fahrenheit_in_kelvin[i]:
        equal_temperatures.append(i)
    else:
        not_equal_temperatures.append(i)

print "Equal temperatures on index: {}".format(equal_temperatures)
print "Not equal temperatures on index: {}".format(not_equal_temperatures)

print "Celsius temperatures: {}".format(celsius_temperatures)
print "Fahrenheit temperatures: {}".format(fahrenheit_temperatures)

print "Celsius in Kelvin: {}".format(celsius_in_kelvin)
print "Fahrenheit in Kelvin: {}".format(fahrenheit_in_kelvin)

