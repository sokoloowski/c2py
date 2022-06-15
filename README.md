# C2Py

Konwerter C do Pythona

[![pytest](https://github.com/agh-c2py/c2py/actions/workflows/pytest.yaml/badge.svg)](https://github.com/agh-c2py/c2py/actions/workflows/pytest.yaml)
[![GitHub top language](https://img.shields.io/github/languages/top/agh-c2py/c2py)](https://github.com/agh-c2py/c2py/search?l=python)
[![PEP8](https://img.shields.io/badge/code%20style-pep8-blue.svg)](https://www.python.org/dev/peps/pep-0008/)

## Dane studentów

- Kamila Skorupka (kskorupka@student.agh.edu.pl)
- Piotr Sokołowski (psokolowski@student.agh.edu.pl)

## Założenia programu

Naszym celem jest stworzenie konwertera kodu dla podjęzyka C do języka Python. Wynikiem działania naszego programu będzie plik zawierający wygenerowany kod. Planowanym językiem implementacji jest Python z wykorzystaniem parsera ~~[PLY](https://github.com/dabeaz/ply)~~ [ANTLR 4](https://github.com/antlr/antlr4/blob/master/doc/python-target.md).

## Opis tokenów

|      Token       |      Opis      |
| :--------------: | :------------: |
|       Auto       |      auto      |
|      Break       |     break      |
|       Case       |      case      |
|       Char       |      char      |
|      Const       |     const      |
|     Continue     |    continue    |
|     Default      |    default     |
|        Do        |       do       |
|      Double      |     double     |
|       Else       |      else      |
|       Enum       |      enum      |
|      Extern      |     extern     |
|      Float       |     float      |
|       For        |      for       |
|       Goto       |      goto      |
|        If        |       if       |
|      Inline      |     inline     |
|       Int        |      int       |
|       Long       |      long      |
|     Register     |    register    |
|     Restrict     |    restrict    |
|      Return      |     return     |
|      Short       |     short      |
|      Signed      |     signed     |
|      Sizeof      |     sizeof     |
|      Static      |     static     |
|      Struct      |     struct     |
|      Switch      |     switch     |
|     Typedef      |    typedef     |
|      Union       |     union      |
|     Unsigned     |    unsigned    |
|       Void       |      void      |
|     Volatile     |    volatile    |
|      While       |     while      |
|     Alignas      |    _Alignas    |
|     Alignof      |    _Alignof    |
|      Atomic      |    _Atomic     |
|       Bool       |     _Bool      |
|     Complex      |    _Complex    |
|     Generic      |    _Generic    |
|    Imaginary     |   _Imaginary   |
|     Noreturn     |   _Noreturn    |
|   StaticAssert   | _Static_assert |
|   ThreadLocal    | _Thread_local  |
|    LeftParen     |       (        |
|    RightParen    |       )        |
|   LeftBracket    |       [        |
|   RightBracket   |       ]        |
|    LeftBrace     |       {        |
|    RightBrace    |       }        |
|       Less       |       <        |
|    LessEqual     |       <=       |
|     Greater      |       >        |
|   GreaterEqual   |       >=       |
|    LeftShift     |       <<       |
|    RightShift    |       >>       |
|       Plus       |       +        |
|     PlusPlus     |       ++       |
|      Minus       |       -        |
|    MinusMinus    |       --       |
|       Star       |       *        |
|       Div        |       /        |
|       Mod        |       %        |
|       And        |       &        |
|        Or        |       \|       |
|      AndAnd      |       &&       |
|       OrOr       |      \|\|      |
|      Caret       |       ^        |
|       Not        |       !        |
|      Tilde       |       ~        |
|     Question     |       ?        |
|      Colon       |       :        |
|       Semi       |       ;        |
|      Comma       |       ,        |
|      Assign      |       =        |
|    StarAssign    |       *=       |
|    DivAssign     |       /=       |
|    ModAssign     |       %=       |
|    PlusAssign    |       +=       |
|   MinusAssign    |       -=       |
| LeftShiftAssign  |      <<=       |
| RightShiftAssign |      >>=       |
|    AndAssign     |       &=       |
|    XorAssign     |       ^=       |
|     OrAssign     |      \|=       |
|      Equal       |       ==       |
|     NotEqual     |       !=       |
|      Arrow       |       ->       |
|       Dot        |       .        |
|     Ellipsis     |      ...       |

## Gramatyka języka C

W oparciu o [oficjalną dokumentację języka C17](https://web.archive.org/web/20181230041359if_/http://www.open-std.org/jtc1/sc22/wg14/www/abq/c17_updated_proposed_fdis.pdf#page=353) przygotowaliśmy [opis gramatyki języka w notacji EBNF](https://github.com/agh-c2py/c2py/blob/main/docs/c17.ebnf). Korzystając z ogólnodostępnych narzędzi, przygotowaliśmy także [diagram składni języka](https://agh-c2py.github.io/c2py/).

## Opis i schemat struktury programu

Struktura naszego programu opiera się o:

### CLexer

Jest to skaner wygenerowany przez [ANTLR 4](https://github.com/antlr/antlr4/blob/master/doc/python-target.md).

### CParser

Jest to parser wygenerowany przez [ANTLR 4](https://github.com/antlr/antlr4/blob/master/doc/python-target.md).

### CVisitor

Tę klasę wykorzystaliśmy jako generator kodu. Klasa została wygenerowana przez [ANTLR 4](https://github.com/antlr/antlr4/blob/master/doc/python-target.md), którą następnie dopasowaliśmy do naszego projektu. Przyjęliśmy założenie, że funkcje/wyrażenia warunkowe/pętle zawierają klamry. Generator kodu napisaliśmy dla biblioteki "stdio.h", biorąc pod uwagę tylko funkcję "printf" jako funkcję wbudowaną.

## Informacje o stosowanych narzędziach i technologiach

Konwerter wykorzystuje bibliotekę `antlr4-python3-runtime` do obsługi skanera, parsera oraz generatora kodu. Inną wykorzystywaną przez nas biblioteką jest `autopep8`, która pozwala na sformatowanie kodu wyjściowego. Są one instalowane automatycznie razem z naszym narzędziem ([więcej informacji](#uruchomienie)).

## Informacje o zastosowanych metodach i algorytmach

W celu wygenerowania kodu wykorzystaliśmy klasę CVisitor. Wygenerowane przez [ANTLR 4](https://github.com/antlr/antlr4/blob/master/doc/python-target.md) metody dopasowaliśmy do naszego projektu. Domyślnie w każdej metodzie uruchamiany jest poniższy blok kodu:

```py
def visitToken(self, ctx:CParser.Token):
    res = ""
        for child in ctx.children:
            if child.getChildCount() == 0:
                res += child.getText()
            else:
                res += self.visit(child)
    return res
```

Metoda ta polega na odwiedzeniu najniższych liści wygenerowanego drzewa składniowego oraz pobranie jego wartości (tekstu). Mając już te wartości, możemy dopasować je do języka `Python`. Przykładowo:

```py
def visitPrimaryExpression(self, ctx:CParserPrimaryExpressionContext):
    res = ""
    for child in ctx.children:
        if child.getChildCount() == 0:
            prim_expr = child.getText()
            if prim_expr in ["true", "false"]:
                prim_expr[0] = prim_expr[0].upper()
            res += prim_expr
        else:
            res += self.visit(child)        
    return res
```

W metodzie tej zamieniamy wartości "true/false" na "True/False" (w języku Python wartości logiczne są z wielkiej litery). W podobny sposób dopasowywaliśmy inne tokeny na zasadzie "jeśli otrzymanym tokenem jest `token_1`, to zamień go na `ciag_instrukcji_1`".  
Metody, które w ten sposób zmieniliśmy, to:

- `visitPrimaryExpression`
- `visitPostfixExpression`
- `visitLogicalAndExpression`
- `visitLogicalOrExpression`
- `visitDeclaration`
- `visitTypeSpecifier`
- `visitCompoundStatement`
- `visitExpressionStatement`
- `visitSelectionStatement`
- `visitIterationStatement`
- `visitForCondition`
- `visitJumpStatement`
- `visitFunctionDefinition`  

Wyjątkiem jest metoda `visitCompilationUnit`, która łączy cały wygenerowany kod w całość - `compilationUnit` jest symbolem startowym.

## Krótka instrukcja obsługi

### Uruchomienie

Po [sklonowaniu](https://github.com/agh-c2py/c2py.git) lub [pobraniu i rozpakowaniu](https://github.com/agh-c2py/c2py/archive/refs/heads/main.zip) repozytorium, należy wejść do katalogu z plikami projektu. Następnie zainstalować i uruchomić główny plik poleceniem `python` lub `python3`, podając ścieżkę do kodu w języku C:

```bash
git clone https://github.com/agh-c2py/c2py.git
cd c2py
pip install .
python . "examples/helloworld.c"
```

Plik w języku Python zostanie zapisane w pliku `output/helloworld.c.py`. Uruchomienie pliku .py:

```bash
python output/helloworld.c.py
```

Pełne informacje o programie można wyświetlić korzystając z opcji `-h`:

```
python . -h
```

Polecenie to wyświetli następujący ekran pomocy:

```
usage: c2py [-h] [-o dir] [-f] path

C2Py is a tool to convert C code to Python code.

positional arguments:
  path                  path to source code in C

options:
  -h, --help            show this help message and exit
  -o dir, --output dir  specifies the output directory
  -f, --format          format the output using PEP8 code style
```

## Testy i przykłady

### Testy

W celu przetestowania naszej aplikacji zostały napisane testy automatyczne przy użyciu `pytest`. Znajdują się one w folderze `test`. Aby je uruchomić, należy wpisać polecenie w katalogu głównym projektu:

```bash
pytest
```

Testom poddajemy następujące przypadki:

- wyrażenia warunkowe  (`converter_if_statements.py`)  
- pętle (`converter_loop_test.py`)
- pusty program (`converter_test.py`)
- "Hello World!" (`converter_test.py`)
- program drukujący kilka linii (`converter_test.py`)
- program "Czy liczba jest pierwsza?" (`converter_test.py`)  

### Przykłady

Przykłady znajdują się w folderze `examples`:

- **errors** : programy, które zawierają błędy składniowe
- **if_statements** : programy z wykorzystaniem wyrażeń warunkowych
- **loops** : programy z wykorzystaniem pętli, w tym: `for`, `while` oraz `do while`

oraz dodatkowo:

- **empty.c** : pusta definicja funkcji `main`
- **helloworld.c** : program, który wyświetla napis `"Hello world!"`
- **if_primary_number.c** : program, który sprawdza, czy liczba jest pierwsza

## Możliwe rozszerzenia programu

W przyszłości planujemy rozszerzyć działanie programu o współpracę z plikami oraz rozszerzyć jego działanie dla niektórych funkcji z bibliotek "math.h".

## Ograniczenia programu

C2Py działa tylko dla prostych definicji funkcji z wykorzystaniem wyrażeń warunkowych, pętli oraz funkcji `printf`. Dodatkowo, działa on tylko dla biblioteki "stdio.h". Kolejnym ograniczeniem jest konieczność używania klamer przy instrukcjach warunkowych oraz pętlach ze względu na wcięcia, które należy brać pod uwagę w języku Python. Przyjęliśmy również uproszczenie, że każdą pętlę zamieniamy na pętlę `while`.
