from c2py.Lexer import Lexer

def test_peek():
    lexer = Lexer("test")
    assert lexer.peek() == "t"
    for i in range(len(lexer.text)):
        assert lexer.peek(i) == lexer.text[i]
    assert lexer.peek(len(lexer.text)) == None

def test_consume():
    lexer = Lexer("test")
    assert lexer.consume() == "t"
    assert lexer.consume() == "e"
    assert lexer.consume() == "s"
    assert lexer.consume() == "t"
    assert lexer.consume() == None