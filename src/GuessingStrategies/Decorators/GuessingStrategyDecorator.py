from abc import ABC
from typing import List

from src.GuessingStrategies.GuessingInterfaceStrategy import GuessingInterfaceStrategy


class GuessingStrategyDecorator(GuessingInterfaceStrategy, ABC):
    _guessingStrategy: GuessingInterfaceStrategy

    def __init__(self, guessing_strategy: GuessingInterfaceStrategy):
        self._guessingStrategy = guessing_strategy

    def guess_is_correct(self, guess: str) -> bool:
        return self._guessingStrategy.guess_is_correct(guess)

    def guess_has_been_tried(self, guess: str) -> bool:
        return self._guessingStrategy.guess_has_been_tried(guess)

    def all_letters_have_been_guessed(self) -> bool:
        return self._guessingStrategy.all_letters_have_been_guessed()

    def get_word(self) -> str:
        return self._guessingStrategy.get_word()

    def get_good_guesses(self) -> List[str]:
        return self._guessingStrategy.get_good_guesses()

    def add_good_guess(self, letter: str) -> None:
        return self._guessingStrategy.add_good_guess(letter)

    def guessed_the_word(self) -> bool:
        return self._guessingStrategy.guessed_the_word()

    def set_guessed_correctly(self, guessed: bool) -> bool:
        return self._guessingStrategy.set_guessed_correctly(guessed)

    def set_word(self, word: str):
        return self._guessingStrategy.set_word(word)
