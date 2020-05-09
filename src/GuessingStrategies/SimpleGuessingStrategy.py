from src.GuessingStrategies.AbstractGuessingStrategy import AbstractGuessingStrategy


class SimpleGuessingStrategy(AbstractGuessingStrategy):
    def __init__(self, word: str):
        super().__init__(word)

    def guess_is_correct(self, guess: str) -> bool:
        guess = guess.lower()

        if self.guess_has_been_tried(guess):
            return False

        self.guesses.append(guess)

        if len(guess) == 1 and guess in self.word:
            self.correctlyGuessedLetters.append(guess)
        elif guess == self.word:
            return self.set_guessed_correctly(True)

        return self.all_letters_have_been_guessed()
