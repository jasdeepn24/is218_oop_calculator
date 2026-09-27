from abc import ABC, abstractmethod

class Calculation(ABC):
    def __init__(self, a, b: float) -> None:
        self.a = a
        self.b = b

    @abstractmethod
    def get_result(self) -> float:
        """Return the result of the calculation."""

class Add(Calculation):
    def get_result(self) -> float:
        return self.a + self.b
    

class Subtract(Calculation):
    def get_result(self) -> float:
        return self.a - self.b
    
    