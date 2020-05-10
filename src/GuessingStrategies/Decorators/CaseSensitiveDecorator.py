from src.GuessingStrategies.AbstractGuessingStrategy import AbstractGuessingStrategy
from src.GuessingStrategies.Decorators.GuessingStrategyDecorator import GuessingStrategyDecorator
from src.GuessingStrategies.WordChangers.CaseSensitive import CaseSensitive


class CaseSensitiveDecorator(GuessingStrategyDecorator):
    def __init__(self, guessing_strategy: AbstractGuessingStrategy):
        guessing_strategy.set_word_changer(CaseSensitive())
        super().__init__(guessing_strategy)
