from src.GuessingStrategies.Decorators.GuessingStrategyDecorator import GuessingStrategyDecorator
from src.GuessingStrategies.GuessingInterfaceStrategy import GuessingInterfaceStrategy
from src.GuessingStrategies.WordChangers.CaseSensitive import CaseSensitive


class CaseSensitiveDecorator(GuessingStrategyDecorator):
    def __init__(self, guessing_strategy: GuessingInterfaceStrategy):
        super().__init__(guessing_strategy)
        super().set_word_changer(CaseSensitive())
