"""
Mediator é um padrão de projeto comportamental que tem a intenção de definir um objeto que encapsula a forma como um conjunto de objetos interage. O Mediator promove o baixo acoplamento ao evitar que os objetos se refiram uns aos outros explicitamente e permite variar suas interações independentemente.
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Colleague(ABC):
    def __init__(self):
        self.name: str

    @abstractmethod
    def broadcast(self, msg: str) -> None:
        pass

    @abstractmethod
    def direct(self, msg: str) -> None:
        pass


class Person(Colleague):
    def __init__(self, name: str, mediator: Mediator) -> None:
        self.name = name
        self._mediator = mediator

    def broadcast(self, msg: str) -> None:
        self._mediator.broadcast(msg, self)

    def send_direct(self, receiver: str, msg: str) -> None:
        self._mediator.direct(msg, self, receiver)

    def direct(self, msg: str) -> None:
        print(msg)


class Mediator(ABC):
    @abstractmethod
    def broadcast(self, msg: str, colleague: Colleague) -> None:
        pass

    @abstractmethod
    def direct(self, msg: str, sender: Colleague, receiver: str) -> str:
        pass


class Chatroom(Mediator):
    def __init__(self) -> None:
        self._colleagues: List[Colleague] = []

    def is_colleague(self, colleague: Colleague) -> bool:
        return colleague in self._colleagues

    def add(self, colleague: Colleague) -> None:
        if not self.is_colleague(colleague):
            self._colleagues.append(colleague)

    def remove(self, colleague: Colleague) -> None:
        if self.is_colleague(colleague):
            self._colleagues.remove(colleague)

    def broadcast(self, msg: str, colleague: Colleague) -> None:
        if not self.is_colleague(colleague):
            return
        print(f"{colleague.name} disse: {msg}")

    def direct(self, msg: str, sender: Colleague, receiver: str) -> None:
        if not self.is_colleague(sender):
            return
        receiver_obj: List[Colleague] = [
            colleague for colleague in self._colleagues if colleague.name == receiver
        ]

        if not receiver_obj:
            return

        receiver_obj[0].direct(f"{sender.name} para {receiver_obj[0].name}: {msg}")


if __name__ == "__main__":
    chat = Chatroom()

    felipe = Person("Felipe", chat)
    lucas = Person("Lucas", chat)
    ana = Person("Ana", chat)

    chat.add(felipe)
    chat.add(lucas)
    chat.add(ana)

    felipe.broadcast("Salveee")
    ana.broadcast("Oiie")
    lucas.broadcast("Mó legal esse chatroom!")

    print()
    felipe.send_direct("Ana", "Oi Ninha")
    ana.send_direct("Felipe", "Oi lipe")
