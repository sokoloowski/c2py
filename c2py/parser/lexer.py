def get_keywords() -> list[str]:
    """
    Get the list of keywords.
    """
    return [
        "auto", "break", "case", "char",
        "const", "continue", "default", "do",
        "double", "else", "enum", "extern",
        "float", "for", "goto", "if",
        "int", "long", "register", "return",
        "short", "signed", "sizeof", "static",
        "struct", "switch", "typedef", "union",
        "unsigned", "void", "volatile", "while"
    ]


def get_operators() -> list[str]:
    """
    Get the list of operators.
    """
    return [
        "++", "--", "()", "[]", ".", "->",
        "(type){list}", "+", "-", "!", "~",
        "(type)", "*", "&", "sizeof",
        "_Alignof", "*", "/", "%", "+", "-",
        "<<", ">>", "<", "<=", ">", ">=", "==",
        "!=", "&", "^", "|", "&&", "|", "?:",
        "=", "+=", "-=", "*=", "/=", "%=",
        "<<=", ">>=", "&=", "^=", "|=", ","
    ]
