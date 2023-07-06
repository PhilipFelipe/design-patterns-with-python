class Singleton(type):
    _instances: dict = {}

    def __call__(cls, *args, **kwargs):
        """Call da metaclass é sempre executado primeiro"""
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class AppSettings(metaclass=Singleton):
    def __init__(self):
        """Com o metaclass o problemaa do init é resolvido"""
        self.name = "Adrian"


class Teste(metaclass=Singleton):
    def __init__(self):
        pass


if __name__ == "__main__":
    as1 = AppSettings()
    as1.name = "Lucas"
    print(as1.name)

    as2 = AppSettings()
    print(as2.name)

    as3 = AppSettings()
    print(as3.name)

    print(as1 == as2 == as3)

    t1 = Teste()
    t2 = Teste()
    print(t1 == t2)
