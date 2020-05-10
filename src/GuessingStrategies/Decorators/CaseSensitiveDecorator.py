from src.GuessingStrategies.AbstractGuessingStrategy import AbstractGuessingStrategy
from src.GuessingStrategies.Decorators.GuessingStrategyDecorator import GuessingStrategyDecorator
from src.GuessingStrategies.WordChangers.CaseSensitive import CaseSensitive


class CaseSensitiveDecorator(GuessingStrategyDecorator):
    def __init__(self, guessing_strategy: AbstractGuessingStrategy):
        super().__init__(guessing_strategy)
        self._guessingStrategy.set_word_changer(CaseSensitive())
