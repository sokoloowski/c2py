class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos]

    def peek(self, pos = 0) -> str:
        peek_pos = self.pos + 0 if pos < 0 else pos
        if peek_pos > len(self.text) - 1:
            return None
        return self.text[peek_pos]

    def consume(self) -> str:
        self.pos += 1
        if self.pos > len(self.text):
            return None
        return self.text[self.pos - 1]
