import runpy


def test_main(capsys):
    runpy.run_module("calculator", run_name="__main__")

    assert capsys.readouterr().out.strip() == "5.0"