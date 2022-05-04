from c2py.parser.lexer import Lexer
from c2py.parser.token import Token
import lorem


def test_peek():
    expected = [
        (Token.KEYWORD, "auto"),
        (Token.KEYWORD, "int"),
        (Token.IDENTIFIER, "asdf"),
        (Token.STRING, f'"{lorem.sentence()}"')
    ]
    test_string = "   "  # some spaces to test skipping white chars
    for i, j in expected:
        test_string += j + "   "
    lexer = Lexer(test_string)
    for i in range(len(expected)):
        actual = lexer.peek(i)
        assert actual == (expected[i][0], expected[i][1])


def test_consume():
    expected = [
        (Token.KEYWORD, "auto"),
        (Token.KEYWORD, "int"),
        (Token.IDENTIFIER, "asdf"),
        (Token.STRING, f'"{lorem.sentence()}"')
    ]
    test_string = "   "  # some spaces to test skipping white chars
    for i, j in expected:
        test_string += j + "   "
    lexer = Lexer(test_string)
    for i in range(len(expected)):
        actual = lexer.consume()
        assert actual == (expected[i][0], expected[i][1])
