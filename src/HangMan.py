from src.GuessingStrategies.AbstractGuessingStrategy import AbstractGuessingStrategy
from src.ProgressStrategies.AbstractProgressStrategy import AbstractProgressStrategy


class HangMan:
    progressStrategy: AbstractProgressStrategy
    guessingStrategy: AbstractGuessingStrategy

    def __init__(
            self,
            guessing_strategy: AbstractGuessingStrategy,
            progress_strategy: AbstractProgressStrategy,
    ) -> None:
        self.guessingStrategy = guessing_strategy
        self.progressStrategy = progress_strategy

    def play(self) -> None:
        while self.has_tries_left():
            guess = input('Make a new guess\n')

            if not guess.isalpha():
                print('Only letters are allowed')
                continue

            if self.guessingStrategy.guess_has_been_tried(guess):
                print('You\'ve already tried that')
                continue

            if self.guessingStrategy.guess_is_correct(guess) and self.guessingStrategy.guessed_the_word():
                break

            self.progressStrategy.decrease_tries_left()

            self.draw_progress()

            self.print_tries_left()

        self.print_result()

    def draw_progress(self):
        word = self.guessingStrategy.get_word()
        good_guess = self.guessingStrategy.get_good_guesses()

        print(self.progressStrategy.draw_progress(word, good_guess))

    def print_result(self):
        if self.guessingStrategy.guessed_the_word():
            print('You won!')
        else:
            print('You lost! The word was: %s' % self.guessingStrategy.get_word())

    def print_tries_left(self):
        if self.has_tries_left():
            print('tries left: %s' % self.progressStrategy.get_tries_left())

    def has_tries_left(self) -> bool:
        return self.progressStrategy.get_tries_left() > 0
