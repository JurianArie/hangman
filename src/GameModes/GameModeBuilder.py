from __future__ import annotations

from src.GameModes.Decorators.CaseSensitiveDecorator import CaseSensitiveDecorator
from src.GameModes.Decorators.HintingDecorator import HintingDecorator
from src.GameModes.GameModeInterface import GameModeInterface


class GameModeBuilder:
    _guesser: GameModeInterface

    def __init__(self, guesser: GameModeInterface):
        self._guesser = guesser

    def with_hints(self) -> GameModeBuilder:
        self._guesser = HintingDecorator(self._guesser)

        return self

    def case_sensitive(self) -> GameModeBuilder:
        self._guesser = CaseSensitiveDecorator(self._guesser)

        return self

    def build(self) -> GameModeInterface:
        return self._guesser
