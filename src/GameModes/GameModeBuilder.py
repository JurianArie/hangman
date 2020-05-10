from __future__ import annotations

from src.GameModes.Decorators.CaseSensitiveDecorator import CaseSensitiveDecorator
from src.GameModes.Decorators.HintingDecorator import HintingDecorator
from src.GameModes.GameModeInterface import GameModeInterface


class GameModeBuilder:
    __game_mode: GameModeInterface

    def __init__(self, guesser: GameModeInterface):
        self.__game_mode = guesser

    def with_hints(self) -> GameModeBuilder:
        self.__game_mode = HintingDecorator(self.__game_mode)

        return self

    def case_sensitive(self) -> GameModeBuilder:
        self.__game_mode = CaseSensitiveDecorator(self.__game_mode)

        return self

    def build(self) -> GameModeInterface:
        return self.__game_mode
