from src.GameModes.Decorators.GameModeDecorator import GameModeDecorator


class HintingDecorator(GameModeDecorator):
    __repetitive_wrong_guesses = 0

    def guess_is_correct(self, guess: str) -> bool:
        correct = super().guess_is_correct(guess)

        if not correct:
            self.__repetitive_wrong_guesses += 1
        else:
            self.__repetitive_wrong_guesses = 0

        if self.__should_give_hint():
            correct = True
            self.__repetitive_wrong_guesses = 0
            self.__give_hint()

        return correct

    def __should_give_hint(self) -> bool:
        return self.__repetitive_wrong_guesses >= 3

    def __give_hint(self):
        hint = self.__get_un_guessed_letter()

        if hint != '':
            print('A hint has been given!')
            super().add_good_guess(hint)

    def __get_un_guessed_letter(self) -> str:
        for letter in list(self.get_word()):
            if letter not in self.get_good_guesses():
                return letter

        return ''

    def reset(self) -> None:
        self.__repetitive_wrong_guesses = 0
        super().reset()
