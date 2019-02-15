# Języki skryptowe - Python
# Lista 6

---

Każda funkcja powinna być opisana *docstringiem*.

---

Zad 1.

Napisz skrypt, który wygeneruje listę zawierającą 100 pierwszych wyrazów
ciągu geometrycznego (dla zadanych *a1* i *q* - pierwszy wyraz ciągu i iloraz).

Następnie wydrukuje na ekranie ten ciąg oraz jego podciąg zawierający tylko
parzyste wyrazy.

---

Zad 2.

Napisz funkcję, która sprawdza, czy podana liczba jest liczbą pierwszą. Funkcja
powinna zwracać *True* lub *False*.

Napisz skrypt, który sprawdzi, czy podana przez użytkownika liczba jest liczbą pierwszą.

*Uwaga: program powinien pytać do skutku, aż użytkownik poda liczbę naturalną. Wsk.* `str.isdigit()`

---

Zad 3.

Napisz skrypt, który wymaga trzech argumentów z linii komend (wsk. `sys.argv`), czyli

```
python moj_skrypt.py arg1 arg2 arg3
```

które są długościami boków trójkąta (można założyć, że podane argumenty są liczbami). Na tej podstawie skrypt powinien wydrukować na ekranie następujące informacje:

* czy z podanych liczb da się zbudować trójkąt (jeśli nie to wypisz stosowny komunikat i przerwij działanie programu)
* obwód trójkąta
* pole trójkąta
* informację czy trójkąt jest równoboczny, równoramienny czy różnoboczny
* informację czy trójkąt jest prostokątny, ostrokątny czy rozwartokątny
* napisz funkcje, która wyrysuje zadany trójkąt używając biblioteki turtle (Wsk. `Twierdzenie Cosinusów`)

**Uwaga:** W przypadku złej liczby argumentów program powinien wyświetlić odpowiedni komunikat i zakończyć działanie.

**Przydatne linki do Twierdzenia Cosinusów:**
- https://en.wikipedia.org/wiki/Law_of_cosines