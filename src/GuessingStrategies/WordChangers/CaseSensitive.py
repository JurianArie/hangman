from src.GuessingStrategies.WordChangers.WordChangerInterface import WordChangerInterface


class CaseSensitive(WordChangerInterface):
    @staticmethod
    def manipulate(word: str) -> str:
        return word
