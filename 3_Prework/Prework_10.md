
# Python
## Prework do 10 listy zadań 

## Global - zmienne globalne

Zmienne globalne to takie, które są dostępne z każdego poziomu skryptu, nawet wewnątrz funkcji.

Przykład:

```python
zmienna_globalna=0

def funkcja():
    global zmienna_globalna
    print(zmienna_globalna)
    
def funkcja1():
    zmienna_globalna = 2 # ale jednak lokalna
    print(zmienna_globalna)
    
print(zmienna_globalna)
funkcja()
funkcja1()
print(zmienna_globalna)
``` 

To by było na tyle, **zapraszam** na zajęcia!