from src.GameModes.GameModeInterface import GameModeInterface
from src.ProgressStrategies.AbstractProgressStrategy import AbstractProgressStrategy


class HangMan:
    _gameMode: GameModeInterface
    _progressStrategy: AbstractProgressStrategy

    def __init__(
            self,
            game_mode: GameModeInterface,
            progress_strategy: AbstractProgressStrategy,
    ) -> None:
        self._gameMode = game_mode
        self._progressStrategy = progress_strategy

    def play(self) -> None:
        while self.has_tries_left():
            guess = input('Make a new guess\n')

            if not guess.isalpha():
                print('Only letters are allowed')
                continue

            # Don't allow the same word/letter to entered twice.
            if self._gameMode.guess_has_been_tried(guess):
                print('You\'ve already tried that')
                continue

            # Only decrease the tries left on a wrong guess.
            if not self._gameMode.guess_is_correct(guess):
                self._progressStrategy.decrease_tries_left()

            if self._gameMode.guessed_the_word():
                break

            self.draw_progress()

            self.print_tries_left()

        self.print_result()

    def draw_progress(self):
        word = self._gameMode.get_word()
        good_guess = self._gameMode.get_good_guesses()

        print(self._progressStrategy.draw_progress(word, good_guess))

    def print_result(self):
        if self._gameMode.guessed_the_word():
            print('You won!')
        else:
            print('You lost! The word was: %s' % self._gameMode.get_word())

    def print_tries_left(self):
        if self.has_tries_left():
            print('tries left: %s' % self._progressStrategy.get_tries_left())

    def has_tries_left(self) -> bool:
        return self._progressStrategy.get_tries_left() > 0
