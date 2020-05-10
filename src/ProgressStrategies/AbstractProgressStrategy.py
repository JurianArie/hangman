from abc import ABC, abstractmethod
from typing import List

from src.ProgressStrategies.ProgressStrategyInterface import ProgressStrategyInterface


class AbstractProgressStrategy(ProgressStrategyInterface, ABC):
    _triesLeft: int

    def __init__(self, max_ties: int):
        self._triesLeft = max_ties

    @abstractmethod
    def draw_progress(self, word: str, good_guesses: List[str]) -> str:
        pass

    def decrease_tries_left(self) -> None:
        self._triesLeft = self._triesLeft - 1

    def increase_tries_left(self) -> None:
        self._triesLeft = self._triesLeft + 1

    def get_tries_left(self) -> int:
        return self._triesLeft

    def should_decrease(self, guess_was_correct: bool) -> bool:
        return not guess_was_correct
