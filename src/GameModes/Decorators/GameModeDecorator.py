from abc import ABC
from typing import List

from src.GameModes.GameModeInterface import GameModeInterface
from src.GameModes.WordChangers.WordChangerInterface import WordChangerInterface


class GameModeDecorator(GameModeInterface, ABC):
    _game_mode: GameModeInterface

    def __init__(self, game_mode: GameModeInterface):
        self._game_mode = game_mode

    def guess_is_correct(self, guess: str) -> bool:
        return self._game_mode.guess_is_correct(guess)

    def guess_is_allowed(self, guess: str) -> bool:
        return self._game_mode.guess_is_allowed(guess)

    def guess_has_been_tried(self, guess: str) -> bool:
        return self._game_mode.guess_has_been_tried(guess)

    def all_letters_have_been_guessed(self) -> bool:
        return self._game_mode.all_letters_have_been_guessed()

    def get_word(self) -> str:
        return self._game_mode.get_word()

    def get_good_guesses(self) -> List[str]:
        return self._game_mode.get_good_guesses()

    def add_good_guess(self, letter: str) -> None:
        return self._game_mode.add_good_guess(letter)

    def guessed_the_word(self) -> bool:
        return self._game_mode.guessed_the_word()

    def set_guessed_correctly(self, guessed: bool) -> bool:
        return self._game_mode.set_guessed_correctly(guessed)

    def set_word(self, word: str):
        return self._game_mode.set_word(word)

    def set_word_changer(self, word_changer: WordChangerInterface) -> None:
        self._game_mode.set_word_changer(word_changer)

    def reset(self) -> None:
        self._game_mode.reset()

