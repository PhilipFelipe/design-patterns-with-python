from re import T


def singleton(the_class):
    """Esta função decoradora é responsável por criar uma instância única"""
    instances = {}

    def get_class(*args, **kwargs):
        if the_class not in instances:
            instances[the_class] = the_class(*args, **kwargs)
        print(instances[the_class])
        return instances[the_class]

    return get_class


@singleton
class AppSettings:
    def __init__(self):
        """Com o decorator singleton o problema do init é resolvido"""
        self.name = "Adrian"


@singleton
class Teste:
    def __init__(self):
        pass


if __name__ == "__main__":
    as1 = AppSettings()
    as1.name = "Felipe"
    as2 = AppSettings()
    print(as1.name)
    print(as2.name)

    t1 = Teste()
    t2 = Teste()
    print(t1 == t2)
