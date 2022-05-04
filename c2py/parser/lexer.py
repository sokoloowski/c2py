from .token import Token
from .reader import Reader


class Lexer:
    def __init__(self, code: str):
        self.reader = Reader(code)
        self.position = 0
        self.keywords = [
            "auto", "break", "case", "char",
            "const", "continue", "default", "do",
            "double", "else", "enum", "extern",
            "float", "for", "goto", "if",
            "int", "long", "register", "return",
            "short", "signed", "sizeof", "static",
            "struct", "switch", "typedef", "union",
            "unsigned", "void", "volatile", "while"
        ]
        self.operators = [
            "++", "--", "()", "[]", ".", "->",
            "(type){list}", "+", "-", "!", "~",
            "(type)", "*", "&", "sizeof",
            "_Alignof", "*", "/", "%", "+", "-",
            "<<", ">>", "<", "<=", ">", ">=", "==",
            "!=", "&", "^", "|", "&&", "|", "?:",
            "=", "+=", "-=", "*=", "/=", "%=",
            "<<=", ">>=", "&=", "^=", "|=", ","
        ]

    def peek(self, k: int = 0) -> tuple[Token, str]:
        i = 0
        j = 0
        res = ""
        while i == 0 and self.reader.peek(j).isspace():
            # skip white chars at the beginning
            j += 1
        while i < k:
            # skip first k tokens
            if self.reader.peek(j).isspace():
                i += 1
                while self.reader.peek(j).isspace():
                    # skip additional spaces between tokens
                    j += 1
            else:
                j += 1

        # Identifiers and keywords
        if self.reader.peek(j).isalpha():
            res += self.reader.peek(j)
            j += 1
            while self.reader.peek(j).isalnum():
                res += self.reader.peek(j)
                j += 1
            if res in self.keywords:
                return Token.KEYWORD, res
            else:
                return Token.IDENTIFIER, res

        # Strings
        if self.reader.peek(j) == '"':
            res += self.reader.peek(j)
            j += 1
            while self.reader.peek(j) != '"':
                res += self.reader.peek(j)
                j += 1
            res += self.reader.peek(j)
            return Token.STRING, res

        # TODO: other tokens

    def consume(self, k: int = 0):
        i = 0
        res = ""
        while i == 0 and self.reader.peek().isspace():
            # skip white chars at the beginning
            self.reader.consume()
        while i < k:
            # skip first k tokens
            if self.reader.peek().isspace():
                i += 1
                while self.reader.peek().isspace():
                    # skip additional spaces between tokens
                    self.reader.consume()
            else:
                self.reader.consume()

        # Identifiers and keywords
        if self.reader.peek().isalpha():
            res += self.reader.consume()
            while self.reader.peek().isalnum():
                res += self.reader.consume()
            if res in self.keywords:
                return Token.KEYWORD, res
            else:
                return Token.IDENTIFIER, res

        # Strings
        if self.reader.peek() == '"':
            res += self.reader.consume()
            while self.reader.peek() != '"':
                res += self.reader.consume()
            res += self.reader.consume()
            return Token.STRING, res

        # TODO: other tokens
