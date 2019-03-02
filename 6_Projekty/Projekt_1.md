# Python
## Projekt 1 - Mieszkaniowy łowca okazji

W tym projekcie Twoim zadaniem będzie napisać skrypt, który będzie szybszy od manualnych home brokerów i będzie miał za zadanie sprawdzać mieszkania na portalach OLX oraz OTODOM dla lokalizacji Wrocław i zapisywac informacje na ich temat do pliku csv.

Dzięki takim skryptom biznesmani wyszukują super okazji na rynku nieruchomosci! Serio!

**Informacje, które ma wyszukać skrypt dla każdej z witryn (OLX oraz OTODOM):**
* Tytuł ogłoszenia
* Cena mieszkania
* Dzielnica Wrocławia
* Wynajem/Sprzedaż
* Link do ogłoszenia
* W przypadku sprzedaży czy cena jest do negocjacji

**Biblioteki potrzebne do wykonania tego projektu:**
* beautifulsoup4
* requests

**Linki do strony z mieszkaniami:**  
- OLX: https://www.olx.pl/nieruchomosci/mieszkania/wroclaw  
- OTODOM: https://www.otodom.pl/sprzedaz/mieszkanie/wroclaw

**Struktura całej aplikacji ma wyglądać następująco:**

- oddzielny plik (moduł) który będzie zawierał klasę OLXParser
- oddzielny plik (moduł) który będzie zawierał klasę OTODOMParser
- plik głowny main który będzie importował powyższe moduły, inicjalizował instancje klas a następnie wywoływał odpowiednie funkcje, żeby zebrać informacje na temat mieszkań.

**Podpowiedź:**

Jeśli napotkasz problem z polskimi znakami, że python nie może ich zdekodować to użyj prosze funkcji:  

_przykladowy_string.encode("utf-8")_

**Dodatkowo:**

Skrypt może mieć dodatkowy moduł, który będzie odpowiedzialny za zapis zebranych danych na temat mieszkań do pliku csv.

**UWAGA:**

Dla ułatwienia zadania skrypt ma czytać mieszkania tylko z pierwszej strony linku, jego zadaniem nie powinno być chodzenie po stronach serwisu.  

Gdy skończysz projekt porównaj go z przykładowym rozwiązaniem.

**Powodzenia!**