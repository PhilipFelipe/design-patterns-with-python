from __future__ import annotations
from abc import ABC, abstractmethod


class SoundBox:
    def __init__(self):
        self.mode: PlayMode = RadioMode(self)
        self.playing = 0

    def change_mode(self, mode: PlayMode) -> None:
        self.playing = 0
        self.mode = mode
        print("Changing to mode:", self.mode.__class__.__name__)

    def press_next(self) -> None:
        self.mode.press_next()
        print(self)

    def press_prev(self) -> None:
        self.mode.press_prev()
        print(self)

    def __str__(self) -> str:
        s = f"Playing: {self.mode.sound.playing}.\nMode: {self.mode.__class__.__name__}"
        return s


class PlayMode(ABC):
    def __init__(self, sound: SoundBox) -> None:
        self.sound = sound

    @abstractmethod
    def press_next(self) -> None:
        pass

    @abstractmethod
    def press_prev(self) -> None:
        pass


class RadioMode(PlayMode):
    def press_next(self) -> None:
        self.sound.playing += 1000

    def press_prev(self) -> None:
        self.sound.playing -= 1000 if self.sound.playing > 0 else 0


class MusicMode(PlayMode):
    def press_next(self) -> None:
        self.sound.playing += 1

    def press_prev(self) -> None:
        self.sound.playing -= 1 if self.sound.playing > 0 else 0


if __name__ == "__main__":
    sound = SoundBox()
    sound.press_next()
    sound.press_next()
    sound.press_next()
    sound.press_next()
    sound.press_prev()
    sound.press_prev()
    sound.press_prev()
    sound.press_prev()

    new_mode = MusicMode(sound)
    sound.change_mode(new_mode)
    sound.press_next()
    sound.press_next()
    sound.press_next()
    sound.press_prev()
    sound.press_prev()
