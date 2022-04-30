class Reader:
    def __init__(self, code: str):
        self.code = list(code)

    def is_eof(self) -> bool:
        return len(self.code) <= 0

    def peek(self, k: int = 0) -> str | None:
        if k > len(self.code) - 1:
            return None
        return self.code[k]

    def consume(self, k: int = 0) -> str | None:
        if k > len(self.code) - 1:
            return None
        ch = self.code.pop(k)
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
