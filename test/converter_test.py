from .helper import run_example


def test_empty() -> None:
    assert run_example("empty") == ""


def test_helloworld() -> None:
    assert run_example("helloworld") == "Hello, world!\n"


def test_multiple_lines() -> None:
    text = ["First", "Second", "Third"]
    expected = "\n".join([i + " line" for i in text]) + "\n"
    assert run_example("print_few_lines") == expected

def test_primary() -> None:
    assert run_example("if_primary_number") == "11 is primary"
