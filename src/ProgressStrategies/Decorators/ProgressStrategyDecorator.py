from abc import ABC
from typing import List

from src.ProgressStrategies.ProgressStrategyInterface import ProgressStrategyInterface


class ProgressStrategyDecorator(ProgressStrategyInterface, ABC):
    _progress_strategy: ProgressStrategyInterface

    def __init__(self, progress_strategy: ProgressStrategyInterface):
        self._progress_strategy = progress_strategy

    def draw_progress(self, word: str, good_guesses: List[str]) -> str:
        return self._progress_strategy.draw_progress(word, good_guesses)

    def decrease_tries_left(self) -> None:
        return self._progress_strategy.decrease_tries_left()

    def increase_tries_left(self) -> None:
        return self._progress_strategy.increase_tries_left()

    def get_tries_left(self) -> int:
        return self._progress_strategy.get_tries_left()

    def should_decrease(self, guess_was_correct: bool) -> bool:
        return self._progress_strategy.should_decrease(guess_was_correct)

    def reset(self) -> None:
        return self._progress_strategy.reset()

