from abc import ABC, abstractmethod
from typing import List


class AbstractGuessingStrategy(ABC):
    word: str
    guessedCorrectly: bool = False
    correctlyGuessedLetters: List[str] = []
    guesses: List[str] = []

    def __init__(self, word: str) -> None:
        self.word = word.lower()

    @abstractmethod
    def guess_is_correct(self, guess: str) -> bool:
        pass

    def guess_has_been_tried(self, guess: str) -> bool:
        return guess.lower() in self.guesses

    def all_letters_have_been_guessed(self) -> bool:
        unique_letters = list(set(self.word))
        guessed = len(unique_letters) == len(self.correctlyGuessedLetters)

        return self.set_guessed_correctly(guessed)

    def get_word(self) -> str:
        return self.word

    def get_good_guesses(self) -> List[str]:
        return self.correctlyGuessedLetters

    def guessed_the_word(self) -> bool:
        return self.guessedCorrectly

    def set_guessed_correctly(self, guessed: bool) -> bool:
        self.guessedCorrectly = guessed

        return guessed
