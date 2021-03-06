from typing import List

from src.ProgressStrategies.AbstractProgressStrategy import AbstractProgressStrategy
from src.ProgressStrategies.WordRevealer import WordRevealer


class ClassicProgressStrategy(AbstractProgressStrategy):
    def __init__(self):
        super().__init__(7)

    def draw_progress(self, word: str, good_guesses: List[str]) -> str:
        progress = self.get_hang_man_stages()[self._triesLeft]

        return progress + '\n' + WordRevealer.reveal(word, good_guesses)

    def get_hang_man_stages(self):
        return {7: '''
      +---+
          |
          |
          |
          |
          |
    =========''', 6: '''
      +---+
      |   |
          |
          |
          |
          |
    =========''', 5: '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', 4: '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', 3: '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', 2: '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', 1: '''+---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', 0: '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    ========='''}
