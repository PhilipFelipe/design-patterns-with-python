"""
Variação do Singleton, garante que o estado do objeto seja igual para todas as instâncias
"""


class StringReprMixin:
    def __str__(self):
        params = ", ".join([f"{k}={v}" for k, v in self.__dict__.items()])
        return f"{self.__class__.__name__}({params})"

    def __repr__(self) -> str:
        return self.__str__()


class SimpleMonoState(StringReprMixin):
    _state = {"x": 10, "y": 20}

    def __init__(self, name=None, surname=None):
        self.__dict__ = self._state

        if name is not None:
            self.name = name
        if surname is not None:
            self.surname = surname


if __name__ == "__main__":
    m1 = SimpleMonoState('Felipe')
    m2 = SimpleMonoState('Ana')
    print(m1)
    print(m2)
