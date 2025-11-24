# Abstraction
# Hide the details and show what is required.

from abc import ABC, abstractmethod

class Father(ABC):

    @abstractmethod
    def loan(self):
        pass

class Child(Father):
    def loan(self):
        print("I will repay the loan.")

beta = Child()
beta.loan()