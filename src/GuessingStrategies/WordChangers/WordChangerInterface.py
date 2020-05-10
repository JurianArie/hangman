from abc import ABC


class WordChangerInterface(ABC):
    @staticmethod
    def manipulate(word: str) -> str:
        pass
