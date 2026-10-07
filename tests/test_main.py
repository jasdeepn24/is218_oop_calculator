import runpy


def test_main(monkeypatch, capsys):
    answers = iter(["exit"])

    monkeypatch.setattr(
        "builtins.input",
        lambda prompt: next(answers),
    )

    runpy.run_module(
        "calculator",
        run_name="__main__",
    )

    assert "Goodbye!" in capsys.readouterr().out


def test_main_can_be_imported():
    import importlib

    module = importlib.import_module("calculator.__main__")

    assert hasattr(module, "run")