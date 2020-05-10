from src.GameModes.AbstractGameMode import AbstractGameMode


class WordsOnlyGameMode(AbstractGameMode):
    def guess_is_correct(self, guess: str) -> bool:
        guess = self._manipulate_guess(guess)

        if self.guess_has_been_tried(guess):
            return False

        self._guesses.append(guess)

        if guess == self.get_word():
            return self.set_guessed_correctly(True)

        return self.set_guessed_correctly(False)
