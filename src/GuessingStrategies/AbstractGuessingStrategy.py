from abc import ABC, abstractmethod
from typing import List

from src.GuessingStrategies.GuessingInterfaceStrategy import GuessingInterfaceStrategy
from src.GuessingStrategies.WordChangers.CaseInsensitive import CaseInsensitive
from src.GuessingStrategies.WordChangers.WordChangerInterface import WordChangerInterface


class AbstractGuessingStrategy(GuessingInterfaceStrategy, ABC):
    _word: str
    _wordChanger: WordChangerInterface
    _guessedCorrectly: bool = False
    _correctlyGuessedLetters: List[str] = []
    _guesses: List[str] = []

    def __init__(self, word: str) -> None:
        self._word = word
        self._wordChanger = CaseInsensitive()

    @abstractmethod
    def guess_is_correct(self, guess: str) -> bool:
        pass

    def guess_has_been_tried(self, guess: str) -> bool:
        return self._manipulate_guess(guess) in self._guesses

    def all_letters_have_been_guessed(self) -> bool:
        unique_letters = list(set(self.get_word()))
        guessed = len(unique_letters) == len(self._correctlyGuessedLetters)

        return self.set_guessed_correctly(guessed)

    # Get the word and change it as needed.
    def get_word(self) -> str:
        return self._wordChanger.manipulate(self._word)

    def get_good_guesses(self) -> List[str]:
        return self._correctlyGuessedLetters

    def guessed_the_word(self) -> bool:
        return self._guessedCorrectly

    def set_guessed_correctly(self, guessed: bool) -> bool:
        self._guessedCorrectly = guessed

        return guessed

    def set_word(self, word: str):
        self._word = word

    # Allow the guess to be overwritten by children.
    def _manipulate_guess(self, guess: str) -> str:
        return self._wordChanger.manipulate(guess)

    def set_word_changer(self, word_changer: WordChangerInterface):
        self._wordChanger = word_changer
