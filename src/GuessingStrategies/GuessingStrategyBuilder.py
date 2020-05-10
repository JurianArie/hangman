from __future__ import annotations

from src.GuessingStrategies.Decorators.CaseSensitiveDecorator import CaseSensitiveDecorator
from src.GuessingStrategies.Decorators.HintingDecorator import HintingDecorator
from src.GuessingStrategies.GuessingInterfaceStrategy import GuessingInterfaceStrategy


class GuessingStrategyBuilder:
    _guesser: GuessingInterfaceStrategy

    def __init__(self, guesser: GuessingInterfaceStrategy):
        self._guesser = guesser

    def with_hints(self) -> GuessingStrategyBuilder:
        self._guesser = HintingDecorator(self._guesser)

        return self

    def case_sensitive(self) -> GuessingStrategyBuilder:
        self._guesser = CaseSensitiveDecorator(self._guesser)

        return self

    def build(self) -> GuessingInterfaceStrategy:
        return self._guesser
