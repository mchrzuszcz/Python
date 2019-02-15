# Zadanie 5

# Format
# For integers, when binary, octal, or hexadecimal output is used, this option adds the prefix respective '0b', '0o', or '0x' to the output value.
# Wiecej informacji w dokumentacji pythona: https://docs.python.org/3.4/library/string.html

def rgb2hex(r, g, b):
    hex = "#{:02x}{:02x}{:02x}".format(r, g, b)
    return hex


def hex2rgb(kod_hex):
    rgb = tuple(map(ord, kod_hex[1:].decode('hex')))
    return rgb


# Dla lepszego zrozumienia

# Decode
# O standardach do dekodowania/enkodowania -> https://docs.python.org/3/library/codecs.html#standard-encodings
# Wiecej o decode -> https://docs.python.org/3/howto/unicode.html


# Wiecej o ord -> https://docs.python.org/2/library/functions.html#ord
print("ord teraz")
print(ord("1"))

# Przyklad - Wyjasnienie funkcji map

def myfunc(a):
    return len(a)

x = map(myfunc, ('jablko', 'banan', 'wisnia'))

print(x)

# Konwersja obiektu map na liste, dla lepszej czytelnosci:
print(list(x))