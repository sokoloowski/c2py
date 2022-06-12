from .helper import run_example


def test_extended_if_statement() -> None:
    assert run_example("if_statements/extended_if_statement") == "4\n"


def test_if_elif_else() -> None:
    assert run_example("if_statements/if_elif_else") == "false\n"


def test_if_statement_with_logical_expression() -> None:
    assert run_example("if_statements/if_statement_with_logical_expression") == "true\n"


def test_simple_if_else() -> None:
    assert run_example("if_statements/simple_if_else") == "true\n"


def test_simple_if() -> None:
    assert run_example("if_statements/simple_if") == "true\n"
