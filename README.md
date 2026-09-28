# is218_oop_calculator

# OOP Calculator

This is my IS218 OOP Calculator assignment. I built a Python calculator through six stages, starting with an Add object and gradually adding subtraction, history, an interactive command-line interface, error handling, and automated testing.

## Requirements

- Python 3.11 or newer
- Git

## Installation

Clone the repository and navigate into the project folder.

Create a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the required packages:

```bash
python -m pip install -r requirements.txt
```

On macOS or Linux, activate the virtual environment using source .venv/bin/activate. Make sure the virtual environment is active before installing dependencies or running tests.


## Running the Calculator

```bash
python -m calculator
```

Available commands:

- add: Add two numbers.
- subtract: Subtract the second number from the first.
- history: Display previous calculations.
- remove: Remove a calculation from history.
- help: Display available commands.
- exit: End the calculator session.

History is stored in memory and resets when the program closes.

## Running Tests

```bash
python -m pytest
```

The project uses pytest and pytest-cov to enforce 100% line and branch coverage.

GitHub Actions also runs these tests automatically on Python 3.11, 3.12, 3.13, and 3.14.

## Design

The Calculation class provides a shared structure for Add and Subtract. Both inherit the operands and implement their own get_result() method.

The History class stores calculation objects and manages adding, retrieving, and removing them.

The CLI connects everything and handles user commands and invalid input.






## Reflection

1. Where would Multiply belong?

If I wanted to add multiplication, I would create a new Multiply class in calculation.py that inherits from Calculation and implements its own get_result() method. I would also update the operations dictionary in cli.py, add multiply to the help menu, and write tests for the new operation. I wouldn't need to change the History class because it already works with Calculation objects, regardless of which operation they perform.



2. What contract could email and text-message notification objects share through send()?

Both EmailNotification and TextNotification could share a common contract requiring a send() method. Each class would implement that method differently depending on how it delivers the message. The rest of the program could call send() without needing to know whether the notification is an email or text message.


3. What design knowledge transfers to another language?

Concepts like classes, objects, inheritance, polymorphism, and encapsulation can transfer to other programming languages. The general idea of separating responsibilities also stays the same. However, I would still need to learn how another language handles things like syntax, types, constructors, inheritance, and exceptions. Knowing the concepts from Python would help me understand the structure, but it wouldn't mean I automatically know how to write them in another language.

