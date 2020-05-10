from src.GuessingStrategies.ClassicGuessingStrategy import ClassicGuessingStrategy
from src.GuessingStrategies.Decorators.CaseSensitiveDecorator import CaseSensitiveDecorator
from src.GuessingStrategies.Decorators.HintingDecorator import HintingDecorator
from src.GuessingStrategies.WordsOnlyGuessingStrategy import WordsOnlyGuessingStrategy


class GuessingStrategyFactory:
    @staticmethod
    def case_sensitive_words_only(word: str):
        return CaseSensitiveDecorator(WordsOnlyGuessingStrategy(word))

    @staticmethod
    def case_sensitive_classic(word: str):
        return CaseSensitiveDecorator(ClassicGuessingStrategy(word))

    @staticmethod
    def words_only_with_hints(word: str):
        return HintingDecorator(WordsOnlyGuessingStrategy(word))

    @staticmethod
    def classic_with_hints(word: str):
        return HintingDecorator(ClassicGuessingStrategy(word))

    @staticmethod
    def case_sensitive_words_only_with_hints(word: str):
        return HintingDecorator(
            CaseSensitiveDecorator(WordsOnlyGuessingStrategy(word))
        )

    @staticmethod
    def case_sensitive_classic_with_hints(word: str):
        return HintingDecorator(
            CaseSensitiveDecorator(ClassicGuessingStrategy(word))
        )
