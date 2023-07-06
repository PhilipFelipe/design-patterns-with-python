from abc import ABC, abstractmethod


class Veiculo(ABC):
    @abstractmethod
    def buscar_cliente(self) -> None:
        pass


class CarroLuxo(Veiculo):
    def buscar_cliente(self) -> None:
        print("Carro de luxo está buscando o cliente...")


class CarroPopular(Veiculo):
    def buscar_cliente(self) -> None:
        print("Carro popular está buscando o cliente...")


class MotoPopular(Veiculo):
    def buscar_cliente(self) -> None:
        print("Moto popular está buscando o cliente...")


class MotoLuxo(Veiculo):
    def buscar_cliente(self) -> None:
        print("Moto de luxo está buscando o cliente...")


class VeiculoFactory(ABC):
    def __init__(self, tipo):
        self.carro = self.get_carro(tipo)

    @staticmethod
    @abstractmethod
    def get_carro(tipo: str) -> Veiculo:
        pass

    def buscar_cliente(self):
        self.carro.buscar_cliente()


class ZonaNorteVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro(tipo: str) -> Veiculo:
        if tipo == "luxo":
            return CarroLuxo()
        if tipo == "popular":
            return CarroPopular()
        if tipo == "motoluxo":
            return MotoLuxo()
        if tipo == "motopopular":
            return MotoPopular()

        raise TypeError("Tipo de carro não existe!")


class ZonaSulVeiculoFactory(VeiculoFactory):
    @staticmethod
    def get_carro(tipo: str) -> Veiculo:
        if tipo == "popular":
            return CarroPopular()
        raise TypeError("Tipo de carro não existe!")


if __name__ == "__main__":
    from random import choice

    veiculos_dispoinveis_zona_norte = ["luxo", "popular", "motoluxo", "motopopular"]
    veiculos_dispoinveis_zona_sul = ["popular"]
    print("ZONA NORTE")
    for i in range(10):
        carro = ZonaNorteVeiculoFactory(choice(veiculos_dispoinveis_zona_norte))
        carro.buscar_cliente()

    print("ZONA SUL")
    for i in range(10):
        carro_2 = ZonaSulVeiculoFactory(choice(veiculos_dispoinveis_zona_sul))
        carro_2.buscar_cliente()
