import pytest

from calculator.factory import CalculationFactory
from calculator.inputs import read_csv_values


def test_sources_share_calculation_policy(tmp_path):
    path = tmp_path / "values.csv"

    path.write_text(
        "value\n"
        "10\n"
        "20\n"
        "30\n"
        "40\n"
        "50\n"
    )

    for name in (
        "mean",
        "stddev",
    ):
        from_csv = CalculationFactory.create(
            name,
            *read_csv_values(path),
        ).get_result()

        manual = CalculationFactory.create(
            name,
            *[10, 20, 30, 40, 50],
        ).get_result()

        assert from_csv == pytest.approx(
            manual
        )


def test_missing_column(tmp_path):
    path = tmp_path / "values.csv"

    path.write_text(
        "other\n"
        "10\n"
        "20\n"
    )

    with pytest.raises(
        ValueError,
        match="column named value",
    ):
        read_csv_values(path)


def test_missing_observation_is_rejected(tmp_path):
    path = tmp_path / "values.csv"

    path.write_text(
        'value\n'
        '10\n'
        '""\n'
        '30\n'
    )

    values = read_csv_values(path)

    with pytest.raises(ValueError):
        CalculationFactory.create(
            "mean",
            *values,
        )