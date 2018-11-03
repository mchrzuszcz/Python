# Języki skryptowe - Python
# Lista 1

---

Zad 1.

Użyj trybu interaktywnego jako kalkulatora, aby wyliczyć następujące wyrażenia:

* suma liczb: 2, 3, 5, -8
* średnia liczb: 2, 3, 5, -8

*wskazówka:*

```py
import math
dir(math)
```

* math.sin(x), gdzie x = 2 / 3 * math.pi

* math.sin(x), gdzie x = 2 / 3 * math.pi - math.pi

---

Zad 2.

W trybie interaktywnym wykonaj następującą serię poleceń:

```py
2 * 2
_ * 3
_ * 4
_ * 5
```

Jakie jest znaczenie zmiennej `_`? Czy ułatwiłoby to wyliczenie punktu 2 z zadania 1?

---

Zad 3.

Zbadaj działanie funkcji wbudowanej `round`, np.

```py
help(round)
round(2.5)
round(2.51)
round(-2.5)
round(-2.51)
```

---

Zad 4.

Zdefiniuj dwie zmienne typu tekstowego i jedną całkowitą, np.

```py
a = "jeden"
b = "dwa"
c = 3
```

Wykonaj następujące polecenia:

```py
a * b
a + b
a * c
a + c
a + str(c)
```

---

Zad 5.

Napisz skrypt, który wykona następujące czynności:

* zmiennej `a` przypisze wartość `5`
* zmiennej `b` przypisze wartość `3`
* zmiennej `P` przypisze wartość `a*b`
* wypisze na ekranie "Pole prostokąta o bokach `a` i `b` wynosi `P`." (gdzie w miejsce zmiennych zostaną wstawione odpowiednie wartości).

Uruchom program w konsoli. Następnie edytuj skrypt zmieniając długości boków i uruchom go raz jeszcze.

*wskazówka:*

```py
Wykorzystaj funkcje str.format().
```