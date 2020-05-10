from random import randrange

from src.GameModes.ClassicGameMode import ClassicGameMode
from src.GameModes.GameModeBuilder import GameModeBuilder
from src.GameModes.GameModeInterface import GameModeInterface
from src.GameModes.WordsOnlyGameMode import WordsOnlyGameMode

GAME_MODE_NAMES = {
    '0': 'classic',
    '1': 'words only',
    '2': 'random',
}

GAME_MODES = {
    '0': GameModeBuilder(ClassicGameMode('')),
    '1': GameModeBuilder(WordsOnlyGameMode('')),
    '2': 'random',
}


class GameModePreferences:
    def get_preference(self) -> GameModeInterface:
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
    def get_builder_with_random_options() -> GameModeBuilder:
        random_choice = str(randrange(0, len(GAME_MODES) - 1))
        game_mode_name = GAME_MODE_NAMES[random_choice]
        game_mode_builder = GAME_MODES[random_choice]

        if randrange(100) < 50:  # 50/50
            game_mode_builder.with_hints()
            game_mode_name += ' with hints'

        if randrange(100) < 50:  # 50/50
            game_mode_builder.case_sensitive()
            game_mode_name = 'case sensitive ' + game_mode_name

        print('The random mode is: %s' % game_mode_name)

        return game_mode_builder
