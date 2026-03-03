from abc import ABC, abstractmethod
class Food(ABC):
    @abstractmethod
    def prepare(self):
        pass
class Pizza(Food):
    def prepare(self):
        print("Preparing pizza...")
class Burger(Food):
    def prepare(self):
        print("Preparing burger...")
pizza = Pizza()
pizza.prepare()
burger = Burger()
burger.prepare()