from .helper import run_example, generate_list


def test_for_loop() -> None:
    assert run_example("loops/for") == generate_list(10, "\n")


def test_while_loop() -> None:
    assert run_example("loops/while") == generate_list(10, "\n")


def test_do_while_loop() -> None:
    assert run_example("loops/do-while") == generate_list(10, "\n")
