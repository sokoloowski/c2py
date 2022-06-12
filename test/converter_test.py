from .helper import run_example


def test_empty() -> None:
    assert run_example("empty") == ""


def test_helloworld() -> None:
    assert run_example("helloworld") == "Hello, world!\n\n"


def test_primary() -> None:
    assert run_example("if_primary_number") == "11 is primary\n"
