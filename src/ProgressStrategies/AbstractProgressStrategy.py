from abc import ABC, abstractmethod
from typing import List


class AbstractProgressStrategy(ABC):
    triesLeft: int

    def __init__(self, max_ties: int):
        self.triesLeft = max_ties
        super().__init__()

    @abstractmethod
    def draw_progress(self, word: str, good_guesses: List[str]) -> str:
        pass

    def decrease_tries_left(self) -> None:
        self.triesLeft = self.triesLeft - 1

    def get_tries_left(self) -> int:
        return self.triesLeft
