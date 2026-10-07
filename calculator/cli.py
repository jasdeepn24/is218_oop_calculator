from math import isfinite

from calculator.calculation import Calculation
from calculator.history import History
from calculator.operations import Operations


HELP = """Commands:
  add       Add two numbers
  subtract  Subtract the second number from the first
  multiply  Multiply two numbers
  divide    Divide the first number by the second
  history   Show this session's calculations
  clear     Clear calculation history
  help      Show available commands
  exit      Exit the calculator"""


def describe(calculation: Calculation, result: float) -> str:
    return (
        f"{calculation.operation.__name__}: "
        f"{calculation.a:g}, {calculation.b:g} = {result:g}"
    )


def show_history(history: History) -> None:
    entries = history.get_history()

    if not entries:
        print("No calculations in history.")
        return

    print("Calculation History\n")

    for number, (calculation, result) in enumerate(entries, start=1):
        print(f"{number}. {describe(calculation, result)}")


def read_number(prompt: str) -> float:
    number = float(input(prompt))

    if not isfinite(number):
        raise ValueError("A finite number is required.")

    return number


def run() -> None:
    history = History()

    operations = {
        "add": Operations.add,
        "subtract": Operations.subtract,
        "multiply": Operations.multiply,
        "divide": Operations.divide,
    }

    print('OOP Calculator\n\nType "help" for commands.')

    while True:
        try:
            command = input("> ").strip().lower()

            if command == "exit":
                break

            if command in operations:
                try:
                    a = read_number("First number: ")
                    b = read_number("Second number: ")

                    operation = operations[command]
                    calculation = Calculation(a, b, operation)
                    result = calculation.get_result()

                except (ValueError, ZeroDivisionError):
                    print("Invalid number or result. Please use valid finite numbers.")
                    continue

                history.add(calculation, result)
                print(f"Result: {result:g}")

            elif command == "history":
                show_history(history)

            elif command == "clear":
                history.clear()
                print("History cleared.")

            elif command == "help":
                print(HELP)

            else:
                print('Unknown command.\nType "help" for available commands.')

        except (EOFError, KeyboardInterrupt):
            print()
            break

    print("Goodbye!")