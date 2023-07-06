"""
Builder é um padrão de projeto criacional que permite a você construir objetos complexos passo a passo. O padrão permite que você produza diferentes tipos e representações de um objeto usando o mesmo código de construção.
"""


from abc import ABC, abstractmethod


class StringReprMixin:
    def __str__(self):
        params = ", ".join([f"{k}={v}" for k, v in self.__dict__.items()])
        return f"{self.__class__.__name__}({params})"

    def __repr__(self) -> str:
        return self.__str__()


class User(StringReprMixin):
    def __init__(self):
        self.username = None
        self.lastname = None
        self.age = None
        self.phone_numbers = []
        self.addresses = []


class IUserBuilder(ABC):
    @property
    @abstractmethod
    def result(self):
        pass

    @abstractmethod
    def add_first_name(self, first_name):
        pass

    @abstractmethod
    def add_last_name(self, last_name):
        pass

    @abstractmethod
    def add_age(self, age):
        pass

    @abstractmethod
    def add_phone_number(self, phone):
        pass

    @abstractmethod
    def add_address(self, address):
        pass


class UserBuilder(IUserBuilder):
    def __init__(self):
        self.reset()

    def reset(self):
        self._result = User()

    @property
    def result(self):
        return_data = self._result
        self.reset()
        return return_data

    def add_first_name(self, first_name):
        self._result.username = first_name
        return self

    def add_last_name(self, last_name):
        self._result.lastname = last_name
        return self

    def add_age(self, age):
        self._result.age = age
        return self

    def add_phone_number(self, phone):
        self._result.phone_numbers.append(phone)
        return self

    def add_address(self, address):
        self._result.addresses.append(address)
        return self


class UserDirector:
    def __init__(self, builder):
        self._builder: UserBuilder = builder

    def with_age(self, first_name, last_name, age):
        self._builder.add_first_name(first_name)
        self._builder.add_last_name(last_name)
        self._builder.add_age(age)
        return self._builder.result

    def with_address(self, first_name, last_name, address):
        """Usando 'method chaining' nas funções do builder"""
        self._builder.add_first_name(first_name)\
            .add_last_name(last_name)\
            .add_address(address)
        return self._builder.result


if __name__ == "__main__":
    user_builder = UserBuilder()
    user_director = UserDirector(user_builder)
    user1 = user_director.with_age("Adrian", "Brito", 25)
    user2 = user_director.with_address("Carlos", "Mota", "Av. São Paulo")
    print(user1)
    print(user2)
