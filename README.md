# C2Py

Konwerter C do Pythona

[![pytest](https://github.com/agh-c2py/c2py/actions/workflows/pytest.yaml/badge.svg)](https://github.com/agh-c2py/c2py/actions/workflows/pytest.yaml)

## Autorzy

- Kamila Skorupka (kskorupka@student.agh.edu.pl)
- Piotr Sokołowski (psokolowski@student.agh.edu.pl)

## Założenia programu

Naszym celem jest stworzenie konwertera kodu w języku C do języka Python. Planowanym językiem implementacji jest Python z wykorzystaniem parsera ~~[PLY](https://github.com/dabeaz/ply)~~ [ANTLR 4](https://github.com/antlr/antlr4/blob/master/doc/python-target.md).

### Zależności

Konwerter wykorzystuje bibliotekę `antlr4-python3-runtime`. Przed uruchomieniem programu, należy ją zainstalować:

```bash
pip install antlr4-python3-runtime
```

### Uruchomienie

Po [sklonowaniu](https://github.com/agh-c2py/c2py.git) lub [pobraniu i rozpakowaniu](https://github.com/agh-c2py/c2py/archive/refs/heads/main.zip) repozytorium, należy wejść do katalogu z plikami projektu. Następnie, uruchomić główny plik poleceniem `python` lub `python3`, podając ścieżkę do kodu w języku C:

```bash
git clone https://github.com/agh-c2py/c2py.git
cd c2py
python . "examples/helloworld.c"
```

Drzewo wyprowadzenia zostanie zapisane w pliku `output/helloworld.c`.

## Gramatyka języka C

W oparciu o [oficjalną dokumentację języka C17](https://web.archive.org/web/20181230041359if_/http://www.open-std.org/jtc1/sc22/wg14/www/abq/c17_updated_proposed_fdis.pdf#page=353) przygotowaliśmy [opis gramatyki języka w notacji EBNF](https://github.com/agh-c2py/c2py/blob/main/docs/c17.ebnf). Korzystając z ogólnodostępnych narzędzi, przygotowaliśmy także [diagram składni języka](https://agh-c2py.github.io/c2py/).
