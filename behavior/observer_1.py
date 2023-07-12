"""
O padrão Observer tem a intenção de definir uma dependência um-para-muitos entre objetos, de maneira que quando um objeto muda de estado, todos os seus dependentes são notificados e atualizados automaticamente.
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, Dict


class IObservable(ABC):
    """Observable"""

    @property
    @abstractmethod
    def state(self) -> Dict:
        pass

    @abstractmethod
    def add_observer(self, observer: IObserver) -> None:
        pass

    @abstractmethod
    def remove_observer(self, observer: IObserver) -> None:
        pass

    @abstractmethod
    def notify_observers(self) -> None:
        pass


class WheaterStation(IObservable):
    """Observable"""

    def __init__(self):
        self._observers: List[IObserver] = []
        self._state: Dict = {}

    @property
    def state(self) -> Dict:
        return self._state

    @state.setter
    def state(self, state_update: Dict) -> None:
        new_state: Dict = {**self._state, **state_update}
        if new_state != self._state:
            self._state = new_state
            self.notify_observers()

    def reset_state(self) -> None:
        self._state = {}
        self.notify_observers()

    def add_observer(self, observer: IObserver) -> None:
        self._observers.append(observer)

    def remove_observer(self, observer: IObserver) -> None:
        if observer not in self._observers:
            return
        self._observers.remove(observer)

    def notify_observers(self) -> None:
        for observer in self._observers:
            observer.update()


class IObserver(ABC):
    @abstractmethod
    def update(self) -> None:
        pass


class Smartphone(IObserver):
    def __init__(self, name: str, observable: IObservable) -> None:
        self.name = name
        self.observable = observable

    def update(self) -> None:
        observable_name = self.observable.__class__.__name__
        print(
            f"{self.name} o objeto {observable_name} acabou de atualizar seu estado para => {self.observable.state}"
        )


if __name__ == "__main__":
    wheater_station = WheaterStation()
    smartphone = Smartphone("iPhone", wheater_station)
    smartphone_2 = Smartphone("Galaxy S21", wheater_station)

    wheater_station.add_observer(smartphone)
    wheater_station.add_observer(smartphone_2)

    wheater_station.state = {"temperature": "30"}
    wheater_station.state = {"temperature": "32", "humidity": "90%"}

    wheater_station.remove_observer(smartphone_2)

    wheater_station.reset_state()
