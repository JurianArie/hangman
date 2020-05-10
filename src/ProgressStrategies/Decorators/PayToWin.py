from src.ProgressStrategies.Decorators.ProgressStrategyDecorator import ProgressStrategyDecorator


class PayToWin(ProgressStrategyDecorator):
    __bought_lives: int = 0
    __initial_price: int = 1

    def should_decrease(self, guess_was_correct: bool) -> bool:
        if guess_was_correct:
            return False

        if self.get_tries_left() - 1 <= 0:
            print('You can buy another live for $%s' % self.get_price_for_new_life())
            if input('Would you like to buy it? y/n:') == 'y':
                self.__bought_lives += 1
                super().increase_tries_left()

                return False

        return True

    def get_price_for_new_life(self):
        if not self.__bought_lives:
            return self.__initial_price

        return self.__bought_lives * 2

    def reset(self) -> None:
        self.__bought_lives = 0
        self.__initial_price = 1
        super().reset()
