from src.GuessingStrategies.ClassicGuessingStrategy import ClassicGuessingStrategy
from src.GuessingStrategies.Decorators.CaseSensitiveDecorator import CaseSensitiveDecorator
from src.GuessingStrategies.WordsOnlyGuessingStrategy import WordsOnlyGuessingStrategy


class GuessingStrategyFactory:
    @staticmethod
    def case_sensitive_words_only(word: str):
        return CaseSensitiveDecorator(WordsOnlyGuessingStrategy(word))

    @staticmethod
    def case_sensitive_classic(word: str):
        return CaseSensitiveDecorator(ClassicGuessingStrategy(word))
