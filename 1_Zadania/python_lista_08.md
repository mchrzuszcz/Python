# Języki skryptowe - Python
# Lista 8

---

Zad 1.

Napisz skrypt, który tworzy listę (wykorzystaj *list comprehension* ) zawierającą *n* pierwszych wyrazów ciągu: *an = n/(n + 1)*, gdzie *n* jest parametrem podanym z linii komend.

Następnie w pętli zapisuje wszystkie wyrazy ciągu do pliku.

Rozbij skrypt na funkcje.

---

Zad 2.

Dodaj do pierwszego zadania funkcje, która wykorzystuje *generator expression* zamiast *list comprehension*.

---

Zad 3.

Wykorzystując *sys.getsizeof* porównaj zużycie pamięci przez wygenerowane ciagi z pierwszych zadań dla różnych wartości *n*. Wyjaśnij otrzymane wyniki.

---

Zad 4.

Plik [studenci_python.txt](../5_Materialy_Pomocnicze/studenci_python.txt) zawiera listę studentów uczęszczających na wykład z Pythona.

Plik [studenci_cpp.txt](../5_Materialy_Pomocnicze/studenci_cpp.txt) zawiera listę studentów uczęszczających na wykład z C++.

Napisz skrypt, który wydrukuję listę studentów uczęszczających na oba wykłady.

---

Zadanie 5

Napisz skrypt, który dla zadanego *n* generuje *n* pierwszych wyrazów ciągu "look-and-say".

Więcej informacji na temat algorytmu -> [look_and_say.](../5_Materialy_Pomocnicze/look_and_say.md)

Skrypt powininen składać się z przynajmniej dwóch funkcji: look_and_say oraz main. Funkcja look_and_say powinna przyjmować 1 argument, którym będzie liczba którą funkcja ma "przeczytać". 
