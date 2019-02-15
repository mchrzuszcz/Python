# Języki skryptowe - Python
# Lista 7

Wzory do konwersji: [Celcius to Fahrenheit - RapidTables](https://www.rapidtables.com/convert/temperature/how-celsius-to-fahrenheit.html)

---

Zad 1.

Stwórz moduł, który zawiera niżej wymienione funkcje:

* konwersja Celsjusz -> Fahrenheit
* konwersja Fahrenheit -> Celsjusz
* generowanie losowych temperatur w Celsjuszach

---

Zad 2.

Napisz skrypt, który wykorzystuje moduł z pierwszego zadania, aby utworzyć plik `celsjusz.txt`, w którym zapisze *n* losowo wygenerowanych temperatur.

*Uwaga: niech n będzie pobierane z linii komend; program powinien stosownie reagować, gdy podany przez użytkownika argument nie jest liczbą całkowitą;*

---

Zad 3.

Napisz skrypt, który wykorzystuje moduł z pierwszego zadania. Nastepnie wczytać plik `celsjusz.txt`, po czym utworzyć odpowiadający mu plik `fahrenheit.txt`, w którym zapisze przekonwertowane temperatury.

---

Zad 4.

Napisz skrypt, który wykorzystuje moduł z pierwszego zadania, aby sprawdzić, czy pliki `celsjusz.txt` i `fahrenheit.txt` zawierają rzeczywiście te same temperatury, ale w innych skalach np. w Kelvinach.

---

Zad 5.

Napisz program `read.py`, który przyjmuje argumenty z linii komend:

```
read.py file [mode]
```

gdzie `file` jest argumentem obowiązkowym, a `[mode]` opcjonalnym.

Program powinien drukować na ekranie podany plik w zadanym trybie:

* mode=0 (domyślnie) - drukuje cały plik
* mode=1 - pomija linie zaczynające się od # (komentarze)
* mode=2 - numeruje linie, czyli

```
1. pierwsza linia z pliku
2. druga linia z pliku
...
```

<b>Plik z przykładowym tekstem do wyświetlenia:</b> [tekst.txt](../5_Materialy_Pomocnicze/tekst.txt)  

<b>Wskazówka: </b> Wykorzystaj biblioteke argparse.
   
<b>Uwaga</b>: program powinien zwracać stosowny komunikat i zakończyć prace, gdy argument obowiązkowy nie zostanie podany.
