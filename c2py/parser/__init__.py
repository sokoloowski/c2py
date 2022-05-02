class Reader:
    def __init__(self, code: str):
        self.code = list(code)
        self.position = 0

    def is_eof(self) -> bool:
        return len(self.code) <= 0

    def peek(self, k: int = 0) -> str | None:
        if k < 0 or self.position + k >= len(self.code):
            return None
        return self.code[self.position + k]

    def consume(self, k: int = 0) -> str | None:
        if k < 0 or self.position + k >= len(self.code):
            return None
        ch = self.code[self.position + k]
        self.position += k + 1
        return ch


class Lexer:
    def __init__(self):
        pass

    def peek(self, k: int = 0):
        pass

    def consume(self, k: int = 0):
        pass


class Parser:
    def __init__(self):
        pass

    def parse(self):
        pass
