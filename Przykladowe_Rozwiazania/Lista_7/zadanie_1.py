#!/usr/bin/env python

import random

def convert_celsius_to_fahrenheit(temp_in_celcius):
    temp_in_fahrenheit = float(temp_in_celcius*1.8) + 32
    return round(temp_in_fahrenheit,2)

def convert_fahrenheit_to_celsius(temp_in_fahrenheit):
    temp_in_celsius = float(temp_in_fahrenheit - 32)/1.8
    return round(temp_in_celsius,2)

def convert_celsius_to_kelvin(temp_in_celsius):
    temp_in_kelvin = temp_in_celsius + 273.15
    return round(temp_in_kelvin,2)

def convert_fahrenheit_to_kelvin(temp_in_fahrenheit):
    temp_in_kelvin = (temp_in_fahrenheit + 459.67)*5/9
    return round(temp_in_kelvin,2)

def random_celsius_temp(n=1):
    rand_celsius_list = []
    for i in range(0,n):
        rand_celsius = random.uniform(-50.0, 50.0)
        rand_celsius = round(rand_celsius,2)
        rand_celsius_list.append(rand_celsius)
    return rand_celsius_list

def save_to_file(content, file_name="Celcjusz.txt"):
    with open(file_name, "w") as f:
        if isinstance(content, list):
            for element in content:
                f.write("{}\n".format(str(element)))
        else:
            f.write(str(content))

def read_file(file_name="Celcjusz.txt"):
    content= []
    with open(file_name, "r") as f:
        for line in f:
            content.append(line)
    return content

