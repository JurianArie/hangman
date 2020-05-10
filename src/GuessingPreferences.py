from random import randrange

from src.GuessingStrategies.ClassicGuessingStrategy import ClassicGuessingStrategy
from src.GuessingStrategies.GuessingInterfaceStrategy import GuessingInterfaceStrategy
from src.GuessingStrategies.GuessingStrategyBuilder import GuessingStrategyBuilder
from src.GuessingStrategies.WordsOnlyGuessingStrategy import WordsOnlyGuessingStrategy

GAME_MODE_NAMES = {
    '0': 'classic',
    '1': 'words only',
    '2': 'random',
}

GAME_MODES = {
    '0': GuessingStrategyBuilder(ClassicGuessingStrategy('')),
    '1': GuessingStrategyBuilder(WordsOnlyGuessingStrategy('')),
    '2': 'random',
}


class GuessingPreferences:
    def get_preference(self) -> GuessingInterfaceStrategy:
        print('What game mode would you like?')
        for i in range(len(GAME_MODE_NAMES)):
            i = str(i)
            print(i + ': ' + GAME_MODE_NAMES[str(i)])

        game_mode_option = input('Enter mode:\n')

        if game_mode_option not in GAME_MODES:
            # Default to the first mode.
            game_mode_option = '0'

        return self.get_builder(game_mode_option).build()

    """
        
    """
    def get_builder(self, game_mode_option):
        if GAME_MODE_NAMES[game_mode_option] == 'random':
            return self.get_builder_with_random_options()

        game_mode_builder = GAME_MODES[game_mode_option]

        if input('With hints? y/n:') == 'y':
            game_mode_builder.with_hints()

        if input('Case sensitive? y/n:') == 'y':
            game_mode_builder.case_sensitive()

        return game_mode_builder

    @staticmethod
    def get_builder_with_random_options() -> GuessingStrategyBuilder:
        random_choice = str(randrange(0, len(GAME_MODES) - 1))
        guessing_strategy_builder = GAME_MODES[random_choice]
        mode_name = GAME_MODE_NAMES[random_choice]

        if randrange(100) < 50:  # 50/50
            guessing_strategy_builder.with_hints()
            mode_name += ' with hints'

        if randrange(100) < 50:  # 50/50
            guessing_strategy_builder.case_sensitive()
            mode_name = 'case sensitive ' + mode_name

        print('The random mode is: %s' % mode_name)

        return guessing_strategy_builder
