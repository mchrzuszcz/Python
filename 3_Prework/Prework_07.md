
# Python
## Prework do 7 listy zadań 

## Operacje na pliku - czytanie i pisanie

W pewnym momencie na pewno zaczniesz sie zastanawiać jak zapisać dane do pliku, a następnie jak je wczytać do skryptu. Służy do tego funkcja _open_ oraz wyrażenie _with_.

Wzór: 

```python
with open(nazwa_pliku, tryb) as dowolna_nazwa_obiektu_pliku:
    dowolna_nazwa_obiektu_pliku.funkcja_obiektu_pliku
```

Przykłady:

```python
with open("tekst.txt", "w") as f:
    f.write("przykladowy tekst do zapisu")
```

```python
with open("tekst.txt", "r") as f:
    dane = f.read()
    
>>> print(dane)
przykladowy tekst do zapisu
```

Podstawowe tryby: r - czytanie (read), w - pisanie (write), a - dodawanie do pliku (add/append)


## argparse - czyli lepszy sys.argv

Biblioteka argparse jest rozwinięciem funkcjonalności argumentów dla skryptu. Dzięk tej bibliotece możemy nazywać argumenty i definiować dla nich pomoc tzw. help, definiować czy są wymagane czy opcjonalne, jakie mogą przyjmować wartości i wiele wiele innych!

Przykład:

```python

import argparse

def arg_parser():
    parser = argparse.ArgumentParser() # tutaj tworzymy instancje obiektu ArgumentParser
    # ponizej tworzymy argument i odpowiednio nadajemy mu nazwe --mode, potem opisujemy jego krotka pomoc (help), 
    # definiujemy jego możliwe wartosci za pomocą argumentu choices dla funkcji add_argument
    # Wartosc domyslna rowna 0, typ argumentu rowny int oraz ze parametr nie jest wymagany -> Required=False
    parser.add_argument('--mode', help="Mode how to read file, 0 - (default choice) read whole file, 1 - omit lines with # at the beginning, 2 - line numbering", choices=[0,1,2], default=0, type=int, required=False)
    return parser.parse_args() # tutaj parsujemy argumenty i zwracamy z funkcji obiekt praser 

```

To by było na tyle, **zapraszam** na zajęcia!
