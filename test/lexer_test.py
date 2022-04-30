from c2py.parser import Reader


def test_peek():
    reader = Reader("test")
    assert reader.peek() == "t"
    for i in range(len(reader.code)):
        assert reader.peek(i) == reader.code[i]
    assert reader.peek(len(reader.code)) is None


def test_consume():
    reader = Reader("test")
    assert reader.consume() == "t"
    assert reader.consume() == "e"
    assert reader.consume() == "s"
    assert reader.consume() == "t"
    assert reader.consume() is None
