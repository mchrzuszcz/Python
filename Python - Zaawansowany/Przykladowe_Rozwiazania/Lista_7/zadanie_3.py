import zadanie_1

celsius_temperatures = zadanie_1.read_file()

fahrenheit_temperatures = []
for celcius_temp in celsius_temperatures:
    fahrenheit_temp = zadanie_1.convert_celsius_to_fahrenheit(float(celcius_temp))
    fahrenheit_temperatures.append(fahrenheit_temp)

zadanie_1.save_to_file(fahrenheit_temperatures, "Fahrenheit.txt")