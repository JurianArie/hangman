from abc import ABC, abstractmethod
from typing import List


class AbstractProgressStrategy(ABC):
    _triesLeft: int

    def __init__(self, max_ties: int):
        self._triesLeft = max_ties
        super().__init__()

    @abstractmethod
    def draw_progress(self, word: str, good_guesses: List[str]) -> str:
        pass

    def decrease_tries_left(self) -> None:
        self._triesLeft = self._triesLeft - 1

    def get_tries_left(self) -> int:
        return self._triesLeft
