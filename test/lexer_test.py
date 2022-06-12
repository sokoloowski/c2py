import os
import random
import string
from antlr4 import *
from ..CLexer import CLexer

def generate_file_name() -> str:
    return "".join(random.choices(string.ascii_letters, k=8)) + ".c"

def hello_world() -> list[str]:
    return [
        "int", "main", "(", "void", ")",
        "{",
            "printf", "(", "\"Hello, World!\"", ")", ";",
            "return", "0", ";",
        "}"
    ]

def parse(whitechar: str) -> None:
    tmp_file = generate_file_name()
    with open(tmp_file, "w") as f:
        f.write(whitechar.join(hello_world()))
    lexer = CLexer(FileStream(tmp_file))
    tokens = lexer.getAllTokens()
    for i, e in enumerate(hello_world()):
        assert e == tokens[i].text
        print(e)
    os.remove(tmp_file)

def test_helloworld_unix_new_lines():
    for i in range(10):
        parse("\n" * (i + 1))

def test_helloworld_windows_new_lines():
    for i in range(10):
        parse("\r\n" * (i + 1))

def test_helloworld_spaces():
    for i in range(10):
        parse(" " * (i + 1))
