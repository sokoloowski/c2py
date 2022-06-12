from .helper import run_example

def test_empty():
    assert run_example("empty") == ""

def test_helloworld():
    assert run_example("helloworld") == "Hello, world!\n\n"

def test_primary():
    assert run_example("if_primary_number") == "11 is primary\n"
