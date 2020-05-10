from abc import ABC
from typing import List


class ProgressStrategyInterface(ABC):
    def draw_progress(self, word: str, good_guesses: List[str]) -> str:
        pass

    def decrease_tries_left(self) -> None:
        pass

    def increase_tries_left(self) -> None:
        pass

    def get_tries_left(self) -> int:
        pass

    def should_decrease(self, guess_was_correct: bool) -> bool:
        pass

    def reset(self) -> None:
        pass
