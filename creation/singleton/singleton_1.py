"""
Garantir que uma classe tenha somente uma instância e fornecer um ponto global de acesso para a mesma.
"""


from ast import main
from os import name


class AppSettings:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        """Init será chamado todas as vezes"""
        self.name = "Adrian"


if __name__ == "__main__":
    as1 = AppSettings()
    as1.name = "Felipe"
    as2 = AppSettings()
    as3 = AppSettings()
    print(as1)
    print(as2)
    print(as3.name)
