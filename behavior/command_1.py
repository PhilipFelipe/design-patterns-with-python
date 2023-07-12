"""
Command tem intenção de encapsular uma solicitação como um objeto, desta forma permitindo parametrizar outros objetos com diferentes solicitações, enfileirar ou fazer o registro (log) e até mesmo implementar recursos de cancelamento de operações.

É formado por um cliente, um invoker e um receiver. O cliente cria um objeto command e o configura com o receiver. O invoker armazena o command e o passa para o receiver executar. O receiver executa a ação solicitada pelo command.
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Dict


class Light:
    """Receiver - Luz Inteligente"""

    def __init__(self, name: str, room_name: str) -> None:
        self.name = name
        self.room_name = room_name
        self.color = "Default"

    def on(self):
        print(f"Light '{self.name}' in '{self.room_name}' is now ON!")

    def off(self):
        print(f"Light '{self.name}' in '{self.room_name}' is now OFF!")

    def change_color(self, color: str):
        self.color = color
        print(
            f"Light '{self.name}' in '{self.room_name}' is now with color '{self.color}'!"
        )


class ICommand(ABC):
    """Interface de comando"""

    @abstractmethod
    def execute(self) -> None:
        pass

    @abstractmethod
    def undo(self) -> None:
        pass


class LightOnCommand(ICommand):
    """Comando concreto"""

    def __init__(self, light: Light) -> None:
        self.light = light

    def execute(self) -> None:
        self.light.on()

    def undo(self) -> None:
        self.light.off()


class LightChangeColorCommand(ICommand):
    def __init__(self, light: Light, color: str) -> None:
        self.light = light
        self.color = color
        self.old_color = light.color

    def execute(self) -> None:
        self._old_color = self.light.color
        self.light.change_color(self.color)

    def undo(self) -> None:
        self.light.change_color(self._old_color)


class RemoteController:
    """Invoker"""

    def __init__(self) -> None:
        self._buttons: Dict[str, ICommand] = {}

    def button_add_command(self, name: str, command: ICommand) -> None:
        self._buttons[name] = command

    def button_execute(self, name: str) -> None:
        if name in self._buttons:
            self._buttons[name].execute()

    def button_undo(self, name: str) -> None:
        if name in self._buttons:
            self._buttons[name].undo()


if __name__ == "__main__":
    bedroom_light = Light("Bedroom Light", "Bedroom")
    bathroom_light = Light("Bathroom Light", "Bedroom")

    bedroom_light_on = LightOnCommand(bedroom_light)
    bathroom_light_on = LightOnCommand(bathroom_light)
    bedroom_light_blue = LightChangeColorCommand(bedroom_light, "Blue")
    bedroom_light_red = LightChangeColorCommand(bedroom_light, "Red")

    remote = RemoteController()
    remote.button_add_command("first_button", bedroom_light_on)
    remote.button_add_command("second_button", bathroom_light_on)
    remote.button_add_command("third_button", bedroom_light_blue)
    remote.button_add_command("fourth_button", bedroom_light_red)

    remote.button_execute("first_button")
    remote.button_undo("first_button")

    remote.button_execute("second_button")
    remote.button_undo("second_button")

    remote.button_execute("third_button")
    remote.button_undo("third_button")

    remote.button_execute("fourth_button")
    remote.button_undo("fourth_button")
