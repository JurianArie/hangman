from abc import ABC, abstractmethod
from typing import List


class AbstractGuessingStrategy(ABC):
    _word: str
    _guessedCorrectly: bool = False
    _correctlyGuessedLetters: List[str] = []
    _guesses: List[str] = []

    def __init__(self, word: str) -> None:
        self._word = word.lower()

    @abstractmethod
    def guess_is_correct(self, guess: str) -> bool:
        pass

    def guess_has_been_tried(self, guess: str) -> bool:
        return guess.lower() in self._guesses

    def all_letters_have_been_guessed(self) -> bool:
        unique_letters = list(set(self._word))
        guessed = len(unique_letters) == len(self._correctlyGuessedLetters)

        return self.set_guessed_correctly(guessed)

    def get_word(self) -> str:
        return self._word

    def get_good_guesses(self) -> List[str]:
        return self._correctlyGuessedLetters

    def guessed_the_word(self) -> bool:
        return self._guessedCorrectly

    def set_guessed_correctly(self, guessed: bool) -> bool:
        self._guessedCorrectly = guessed

        return guessed
