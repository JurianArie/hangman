from src.GuessingStrategies.ClassicGuessingStrategy import ClassicGuessingStrategy
from src.GuessingStrategies.Decorators.CaseSensitiveDecorator import CaseSensitiveDecorator
from src.GuessingStrategies.Decorators.HintingDecorator import HintingDecorator
from src.GuessingStrategies.GuessingInterfaceStrategy import GuessingInterfaceStrategy
from src.GuessingStrategies.WordsOnlyGuessingStrategy import WordsOnlyGuessingStrategy


class GuessingStrategyFactory:
    @staticmethod
    def case_sensitive_words_only(word: str) -> GuessingInterfaceStrategy:
        return CaseSensitiveDecorator(WordsOnlyGuessingStrategy(word))

    @staticmethod
    def case_sensitive_classic(word: str) -> GuessingInterfaceStrategy:
        return CaseSensitiveDecorator(ClassicGuessingStrategy(word))

    @staticmethod
    def words_only_with_hints(word: str) -> GuessingInterfaceStrategy:
        return HintingDecorator(WordsOnlyGuessingStrategy(word))

    @staticmethod
    def classic_with_hints(word: str) -> GuessingInterfaceStrategy:
        return HintingDecorator(ClassicGuessingStrategy(word))

    @staticmethod
    def case_sensitive_words_only_with_hints(word: str) -> GuessingInterfaceStrategy:
        return HintingDecorator(
            CaseSensitiveDecorator(WordsOnlyGuessingStrategy(word))
        )

    @staticmethod
    def case_sensitive_classic_with_hints(word: str) -> GuessingInterfaceStrategy:
        return HintingDecorator(
            CaseSensitiveDecorator(ClassicGuessingStrategy(word))
        )
