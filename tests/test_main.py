import runpy

import pytest


def test_main(monkeypatch, capsys):
    def raise_eof(_):
        raise EOFError

    monkeypatch.setattr("builtins.input", raise_eof)

    runpy.run_module("calculator", run_name="__main__")

    assert "Goodbye!" in capsys.readouterr().out