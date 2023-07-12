"""
Template Method tem a intenção de definir um algoritmo em um método, postergando alguns passos para as subclasses por herança. Template Method permite que subclasses redefinam certos passos de um algoritmo sem mudar a estrutura do mesmo.

IoC - Inversão de Controle
"""

from abc import ABC, abstractmethod


class Pizza(ABC):
    """Abstract class"""

    def prepare(self):
        """template method"""
        self.add_ingredients()  # Abstract
        self.cook()  # Abstract
        self.cut()  # Concrete
        self.serve()  # Concrete

    def cut(self):
        print(f"{self.__class__.__name__}: Cutting pizza")

    def serve(self):
        print(f"{self.__class__.__name__}: Serving pizza")

    @abstractmethod
    def add_ingredients(self):
        pass

    @abstractmethod
    def cook(self):
        pass


class StylishPizza(Pizza):
    def add_ingredients(self):
        print("StylishPizza: Adding ingredients")

    def cook(self):
        print("StylishPizza: Cooking. Time: 45 minutes")


if __name__ == "__main__":
    pizza = StylishPizza()
    pizza.prepare()
