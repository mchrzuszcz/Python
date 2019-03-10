
# Python
## Prework do 6 listy zadań 

## sys.argv

---

Możliwe że podczas swojej pracy nad skryptami python'a odnosleś/odnioslaś w pewnym momencie wrażenie, że dobrzy byłoby sterować działaniem skryptu z poziomu jego uruchomienia.  

Załóżmy, że tworzymy skrypt, który czyta dane z pliku, no i super, ale co jeśli nazwa pliku sie zmieni? Albo lokalizacja pliku sie zmieni?

Pewnie odpowiesz, że "to sie łatwo da zmienić w kodzie". A ja powiem, spoko tylko po co? Po co otwierac plik i zmieniać coś w nim? Najgorzej jeszcze jak skrypt dostanie osoba, która nie zna sie na programowaniu w pythonie i nie będzie wiedziała gdzie taką nazwę zmienić ale będzie chciała skorzystać ze skryptu.

W takiej sytuacji korzystamy z argumentów skryptu, cos na wzór argumentów funkcji.  

Najprostrzym narzędziem do odwołania się do argumentów wywołania skryptu służy lista argv z biblioteki sys.  

Przykładowy skrypt:

```python
# skrypt.py
import sys
print(sys.argv)
``` 

Wywołanie skryptu:

```python skrypt.py 1 2 "trzy" "czwarty_argument" "cokolwiek"```

Efekt:

['skrypt.py','1','2','trzy','czwarty_argument','cokolwiek']

sys.argv zwraca nam liste której elementami są argumenty przekazane podczas wywołania skryptu oraz nazwa skryptu, która zawsze znajduję się jako zerowy element listy sys.argv.

 To by było na tyle, **zapraszam** na zajęcia!