"""
Template Method tem a intenção de definir um algoritmo em um método, postergando alguns passos para as subclasses por herança. Template Method permite que subclasses redefinam certos passos de um algoritmo sem mudar a estrutura do mesmo.

IoC - Inversão de Controle
"""

from abc import ABC, abstractmethod


class Abstract(ABC):
    # NÃO É MÉTODO ABSTRATO
    def template_method(self):
        self.hook()
        self.operation_1()
        self.operation_2()

    def hook(self):
        pass

    @abstractmethod
    def operation_1(self):
        pass

    @abstractmethod
    def operation_2(self):
        pass


class ConcreteClass(Abstract):
    def hook(self):
        print("ConcreteClass.hook()")

    def operation_1(self):
        print("ConcreteClass.operation_1()")

    def operation_2(self):
        print("ConcreteClass.operation_2()")


if __name__ == "__main__":
    c1 = ConcreteClass()
    c1.template_method()
