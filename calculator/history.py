from calculator.calculation import Calculation


class History:
    def __init__(self):
        self._entries = []

    def add(self, calculation, result) -> None:
        if not isinstance(calculation, Calculation):
            raise TypeError("History accepts Calculation objects only.")

        self._entries.append((calculation, result))

    def get_history(self):
        return self._entries.copy()

    def clear(self) -> None:
        self._entries.clear()