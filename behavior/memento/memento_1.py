"""
GoF - Memento é um padrão de projeto comportamental que tem a intenção de permitir que vocÊ salve e restaure um estado anterior de um objeto originator sem revelar detalhes da sua implementação e sem violar o encapsulamento.

Originator é o objeto que deseja salvar seu estado.
Memento é usado para salvar o estado do Originator.
Caretaker é usada para armazenar mementos.
Caretaker é também usado com o Padrão Command.
"""

from __future__ import annotations
from typing import Any, List, Dict
from copy import deepcopy


class Memento:
    def __init__(self, state: Dict) -> None:
        self._state: Dict
        super().__setattr__("_state", state)

    def get_state(self) -> Dict:
        return self._state

    def __setattr__(self, __name: str, __value: Any) -> None:
        raise AttributeError("Memento is read-only")


class ImageEditor:
    def __init__(self, name: str, width: int, height: int) -> None:
        self.name = name
        self.width = width
        self.height = height

    def save_state(self) -> Memento:
        return Memento(deepcopy(self.__dict__))

    def restore(self, memento: Memento) -> None:
        self.__dict__ = memento.get_state()

    def __str__(self) -> str:
        return f"{self.__class__.__name__}{(self.__dict__)}"


class Caretaker:
    def __init__(self, originator: ImageEditor) -> None:
        self._originator = originator
        self._mementos: List[Memento] = []

    def backup(self) -> None:
        self._mementos.append(self._originator.save_state())

    def restore(self) -> None:
        if not self._mementos:
            return
        self._originator.restore(self._mementos.pop())


if __name__ == "__main__":
    img = ImageEditor("foto.jpg", 800, 600)
    ct = Caretaker(img)
    ct.backup()

    img.name = "foto_2.jpg"
    img.width = 1280
    img.height = 720
    ct.backup()

    img.name = "foto_3.jpg"
    img.width = 1920
    img.height = 1080
    ct.backup()

    img.name = "foto_4.jpg"
    img.width = 600
    img.height = 600
    print(img)

    ct.restore()
    print(img)

    ct.restore()
    print(img)

    ct.restore()
    print(img)

    ct.restore()
    print(img)

    ct.restore()
    print(img)

    ct.restore()
    print(img)

    ct.restore()
    print(img)
