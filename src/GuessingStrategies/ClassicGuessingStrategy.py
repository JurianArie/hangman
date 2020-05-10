from src.GuessingStrategies.AbstractGuessingStrategy import AbstractGuessingStrategy


class ClassicGuessingStrategy(AbstractGuessingStrategy):
    def guess_is_correct(self, guess: str) -> bool:
        guess = self._manipulate_guess(guess)

        if self.guess_has_been_tried(guess):
            return False

        self._guesses.append(guess)

        if len(guess) == 1 and guess in self.get_word():
            self._correctlyGuessedLetters.append(guess)

            # Always return true.
            return self.all_letters_have_been_guessed() or True
        elif guess == self.get_word():
            return self.set_guessed_correctly(True)

        return self.set_guessed_correctly(False)
