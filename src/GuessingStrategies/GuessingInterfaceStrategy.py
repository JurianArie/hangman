from abc import ABC
from typing import List


class GuessingInterfaceStrategy(ABC):
    def guess_is_correct(self, guess: str) -> bool:
        pass

    def guess_has_been_tried(self, guess: str) -> bool:
        pass

    def all_letters_have_been_guessed(self) -> bool:
        pass

    def get_word(self) -> str:
        pass

    def get_good_guesses(self) -> List[str]:
        pass

    def guessed_the_word(self) -> bool:
        pass

    def set_guessed_correctly(self, guessed: bool) -> bool:
        pass

    def set_word(self, word: str):
        pass

    def _manipulate_guess(self, guess: str) -> str:
        pass
