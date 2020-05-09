from typing import List

from src.ProgressStrategies.AbstractProgressStrategy import AbstractProgressStrategy
from src.ProgressStrategies.WordRevealer import WordRevealer


class SimpleProgressStrategy(AbstractProgressStrategy):
    def __init__(self, max_ties: int) -> None:
        super().__init__(max_ties)

    def draw_progress(self, word: str, good_guesses: List[str]) -> str:
        return WordRevealer.reveal(word, good_guesses)
