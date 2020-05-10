from src.GuessingStrategies.WordChangers.WordChangerInterface import WordChangerInterface


class CaseInsensitive(WordChangerInterface):
    @staticmethod
    def manipulate(word: str) -> str:
        return word.lower()
