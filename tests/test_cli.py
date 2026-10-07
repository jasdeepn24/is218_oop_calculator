from calculator.cli import HELP, describe, read_number, run, show_history
from calculator.calculation import Calculation
from calculator.history import History
from calculator.operations import Operations


def test_describe():
    calculation = Calculation(10, 5, Operations.add)
    result = calculation.get_result()

    assert describe(calculation, result) == "add: 10, 5 = 15"


def test_show_empty_history(capsys):
    history = History()

    show_history(history)

    assert "No calculations in history." in capsys.readouterr().out


def test_show_history(capsys):
    history = History()

    calculation = Calculation(10, 5, Operations.add)
    result = calculation.get_result()
    history.add(calculation, result)

    show_history(history)

    output = capsys.readouterr().out

    assert "Calculation History" in output
    assert "1. add: 10, 5 = 15" in output


def test_read_number(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "12.5")

    assert read_number("Number: ") == 12.5


def test_read_number_rejects_infinity(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "inf")

    try:
        read_number("Number: ")
        assert False
    except ValueError:
        assert True


def test_help_text():
    assert "add" in HELP
    assert "subtract" in HELP
    assert "multiply" in HELP
    assert "divide" in HELP
    assert "history" in HELP
    assert "clear" in HELP


def test_run_add(monkeypatch, capsys):
    responses = iter(["add", "2", "3", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(responses))

    run()

    output = capsys.readouterr().out

    assert "Result: 5" in output
    assert "Goodbye!" in output


def test_run_subtract(monkeypatch, capsys):
    responses = iter(["subtract", "10", "4", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(responses))

    run()

    assert "Result: 6" in capsys.readouterr().out


def test_run_multiply(monkeypatch, capsys):
    responses = iter(["multiply", "4", "5", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(responses))

    run()

    assert "Result: 20" in capsys.readouterr().out


def test_run_divide(monkeypatch, capsys):
    responses = iter(["divide", "10", "4", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(responses))

    run()

    assert "Result: 2.5" in capsys.readouterr().out


def test_run_history(monkeypatch, capsys):
    responses = iter(["add", "2", "3", "history", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(responses))

    run()

    output = capsys.readouterr().out

    assert "Calculation History" in output
    assert "add: 2, 3 = 5" in output


def test_run_empty_history(monkeypatch, capsys):
    responses = iter(["history", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(responses))

    run()

    assert "No calculations in history." in capsys.readouterr().out


def test_run_clear(monkeypatch, capsys):
    responses = iter(["add", "2", "3", "clear", "history", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(responses))

    run()

    output = capsys.readouterr().out

    assert "History cleared." in output
    assert "No calculations in history." in output


def test_run_help(monkeypatch, capsys):
    responses = iter(["help", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(responses))

    run()

    assert "Commands:" in capsys.readouterr().out


def test_run_unknown_command(monkeypatch, capsys):
    responses = iter(["pizza", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(responses))

    run()

    assert "Unknown command." in capsys.readouterr().out


def test_run_invalid_number(monkeypatch, capsys):
    responses = iter(["add", "hello", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(responses))

    run()

    assert "Invalid number or result." in capsys.readouterr().out


def test_run_division_by_zero(monkeypatch, capsys):
    responses = iter(["divide", "10", "0", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(responses))

    run()

    assert "Invalid number or result." in capsys.readouterr().out


def test_run_eof(monkeypatch, capsys):
    def raise_eof(_):
        raise EOFError

    monkeypatch.setattr("builtins.input", raise_eof)

    run()

    assert "Goodbye!" in capsys.readouterr().out


def test_run_keyboard_interrupt(monkeypatch, capsys):
    def raise_interrupt(_):
        raise KeyboardInterrupt

    monkeypatch.setattr("builtins.input", raise_interrupt)

    run()

    assert "Goodbye!" in capsys.readouterr().out