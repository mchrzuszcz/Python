import zadanie_1

celsius_temperatures = zadanie_1.read_file("Celcjusz.txt")
fahrenheit_temperatures = zadanie_1.read_file("Fahrenheit.txt")

fahrenheit_temperatures_size = len(fahrenheit_temperatures)
celsius_temperatures_size = len(celsius_temperatures)
if fahrenheit_temperatures_size != celsius_temperatures_size:
    print "Different count of temperatures. Fahrenheit: {}, Celsius: {}".format(fahrenheit_temperatures_size, celsius_temperatures_size)

count = 0
for i in range(len(fahrenheit_temperatures)):
    convertet_fahren_to_celsius = round(zadanie_1.convert_fahrenheit_to_celsius(float(fahrenheit_temperatures[i])), 1)
    if convertet_fahren_to_celsius != float(celsius_temperatures[i]):
        print "Different temperatures! Fahrenheit: {}, Celsius: {}".format(convertet_fahren_to_celsius, celsius_temperatures[i])
        count += 1

if count == 0:
    print "Temperatures are equal!"
else:
    print "{} are different that should be".format(count)


