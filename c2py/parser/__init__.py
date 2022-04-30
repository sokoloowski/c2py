class Reader:
    def __init__(self, code: str):
        self.code = code
        self.pos = 0
        self.current_char = self.code[self.pos]

    def peek(self, pos=0) -> str | None:
        peek_pos = self.pos + 0 if pos < 0 else pos
        if peek_pos > len(self.code) - 1:
            return None
        return self.code[peek_pos]

    def consume(self) -> str | None:
        self.pos += 1
        if self.pos > len(self.code):
            return None
        return self.code[self.pos - 1]


class Lexer:
    pass


class Parser:
    pass
