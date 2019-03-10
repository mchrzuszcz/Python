
# Python
## Prework do 5 listy zadań 

## Moduł

---

Pamietasz jak w liście pierwszej importowaliśmy bibliotekę math? Dzisiaj zrobimy swój własny moduł, który będziemy mogli importować do każdego skryptu kiedy tylko będzie nam potrzebny!

Moduł to jest nic innego jak zwykły skrypt Python'a.

Tworzymy dwa pliki: modul.py oraz skrypt.py

Nasz plik modul.py wyglada nastepująco:

```python
#modul.py

def przykladowa_funkcja():
    print("Jestem funkcja z modulu")
    
```

A plik skrypt.py wygląda tak:

```python
#skrypt.py

import modul

modul.przykladowa_funkcja()
```

Po wywołaniu skryptu skrypt.py otrzymamy:

```Jestem funkcja z modulu```

W ten sposób możemy tworzyć pliki python'a które będą zbiorem przerożnych funkcji, klas, zmiennych i wielu innych składowych, które to w każdej chwili możemy wykorzystać w różnych skryptach na raz!  

Takie tworzenie modułów jest jednym z pryncypałów zasady DRY czyli DON'T REPEAT YOURSELF, odnosząca się do tego aby nie pisać tego samego kodu wielokrotnie - nie powtarzać go tylko żeby ten kod był reużywalny.

 To by było na tyle, **zapraszam** na zajęcia!