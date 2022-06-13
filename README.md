# C2Py

Konwerter C do Pythona

[![pytest](https://github.com/agh-c2py/c2py/actions/workflows/pytest.yaml/badge.svg)](https://github.com/agh-c2py/c2py/actions/workflows/pytest.yaml)
[![GitHub top language](https://img.shields.io/github/languages/top/agh-c2py/c2py)](https://github.com/agh-c2py/c2py/search?l=python)
[![PEP8](https://img.shields.io/badge/code%20style-pep8-blue.svg)](https://www.python.org/dev/peps/pep-0008/)

## Autorzy

- Kamila Skorupka (kskorupka@student.agh.edu.pl)
- Piotr Sokołowski (psokolowski@student.agh.edu.pl)

## Założenia programu

Naszym celem jest stworzenie konwertera kodu dla podjęzyka C do języka Python. Planowanym językiem implementacji jest Python z wykorzystaniem parsera ~~[PLY](https://github.com/dabeaz/ply)~~ [ANTLR 4](https://github.com/antlr/antlr4/blob/master/doc/python-target.md).

## Gramatyka języka C

W oparciu o [oficjalną dokumentację języka C17](https://web.archive.org/web/20181230041359if_/http://www.open-std.org/jtc1/sc22/wg14/www/abq/c17_updated_proposed_fdis.pdf#page=353) przygotowaliśmy [opis gramatyki języka w notacji EBNF](https://github.com/agh-c2py/c2py/blob/main/docs/c17.ebnf). Korzystając z ogólnodostępnych narzędzi, przygotowaliśmy także [diagram składni języka](https://agh-c2py.github.io/c2py/).

## Opis i schemat struktury programu

Struktura naszego programu opiera się o:

### CLexer

Jest to skaner wygenerowany przez [ANTLR 4](https://github.com/antlr/antlr4/blob/master/doc/python-target.md).

### CParser

Jest to parser wygenerowany przez [ANTLR 4](https://github.com/antlr/antlr4/blob/master/doc/python-target.md).

### CVisitor

Ten obiekt wykorzystaliśmy jako generator kodu. Obiekt został wygenerowany przez [ANTLR 4](https://github.com/antlr/antlr4/blob/master/doc/python-target.md), który następnie dopasowaliśmy do naszego projektu. Przyjęliśmy założenie, że funkcje/wyrażenia warunkowe/pętle zawierają klamry. Generator kodu napisaliśmy dla biblioteki "stdio.h", biorąc pod uwagę tylko funkcję "printf" jako funkcję wbudowaną.

## Informacje o stosowanych narzędziach i technologiach

Konwerter wykorzystuje bibliotekę `antlr4-python3-runtime`. Przed uruchomieniem programu, należy ją zainstalować:

```bash
pip install antlr4-python3-runtime
```

## Informacje o zastosowanych metodach i algorytmach

<span style="color:red;">_**Do uzupełnienia**_</span>

## Krótka instrukcja obsługi

### Uruchomienie

Po [sklonowaniu](https://github.com/agh-c2py/c2py.git) lub [pobraniu i rozpakowaniu](https://github.com/agh-c2py/c2py/archive/refs/heads/main.zip) repozytorium, należy wejść do katalogu z plikami projektu. Następnie zainstalować i uruchomić główny plik poleceniem `python` lub `python3`, podając ścieżkę do kodu w języku C:

```bash
git clone https://github.com/agh-c2py/c2py.git
cd c2py
pip install -e .
python . "examples/helloworld.c"
```

Plik w języku Python zostanie zapisane w pliku `output/helloworld.c.py`. Uruchomienie pliku .py:

```bash
python output/helloworld.c.py
```

## Testy i przykłady

W celu przetestowania naszej aplikacji zostały napisane testy automatyczne przy użyciu `pytest`. Znajdują się one w folderze `test`. Aby je uruchomić, należy wpisać polecenie w katalogu głównym projektu:

```bash
pytest
```  
  
<span style="color:red;">_**Należy opisać testy!!!**_ </span> 
  
Przykłady znajdują się w folderze `examples`:

- **errors** : programy, które zawierają błędy składniowe
- **if_statements** : programy z wykorzystaniem wyrażeń warunkowych
- **loops** : programy z wykorzystaniem pętli, w tym: _for_, _while_ oraz _do while_

oraz dodatkowo:

- **empty.c** : pusta definicja funkcji _main_
- **helloworld.c** : program, który wyświetla napis _"Hello world!"_
- **if_primary_number.c** : program, który sprawdza, czy liczba jest pierwsza

## Możliwe rozszerzenia programu

W przyszłości planujemy rozszerzyć działanie programu o współpracę z plikami oraz rozszerzyć jego działanie dla niektórych funkcji z bibliotek "math.h".

## Ograniczenia programu

C2Py działa tylko dla prostych definicji funkcji z wykorzystaniem wyrażeń warunkowych, pętli oraz funkcji "printf". Dodatkowo, działa on tylko dla biblioteki "stdio.h". Kolejnym ograniczeniem jest konieczność używania klamer przy instrukcjach warunkowych oraz pętlach ze względu na wcięcia, które należy brać pod uwagę w języku Python. Przyjęliśmy również uproszczenie, że każdą pętlę zamieniamy na pętlę _while_.