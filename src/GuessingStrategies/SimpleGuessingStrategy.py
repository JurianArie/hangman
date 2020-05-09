from src.GuessingStrategies.AbstractGuessingStrategy import AbstractGuessingStrategy


class SimpleGuessingStrategy(AbstractGuessingStrategy):
    def __init__(self, word: str):
        super().__init__(word)

    def guess_is_correct(self, guess: str) -> bool:
        self.set_guessed_correctly(False)
        guess = guess.lower()

        if self.guess_has_been_tried(guess):
            return False

        self._guesses.append(guess)

        if len(guess) == 1 and guess in self._word:
            self._correctlyGuessedLetters.append(guess)

            # Always return true.
            return self.all_letters_have_been_guessed() or True
        elif guess == self._word:
            return self.set_guessed_correctly(True)

        return self.all_letters_have_been_guessed()
