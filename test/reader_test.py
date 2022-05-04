from c2py.parser.reader import Reader


def test_peek():
    reader = Reader("test")
    assert reader.peek() == "t"
    for i in range(len(reader.code)):
        assert reader.peek(i) == reader.code[i]
    assert reader.peek(len(reader.code)) is None


def test_consume():
    reader = Reader("test")
    assert reader.consume() == "t"  # test -> est
    assert reader.consume(1) == "s"  # est -> t
    assert reader.consume() == "t"  # t -> None
    assert reader.consume() is None
