from random import randrange

from src.GuessingStrategies.ClassicGuessingStrategy import ClassicGuessingStrategy
from src.GuessingStrategies.GuessingInterfaceStrategy import GuessingInterfaceStrategy
from src.GuessingStrategies.GuessingStrategyFactory import GuessingStrategyFactory
from src.GuessingStrategies.WordsOnlyGuessingStrategy import WordsOnlyGuessingStrategy
from src.ProgressStrategies.AbstractProgressStrategy import AbstractProgressStrategy
from src.ProgressStrategies.ClassicProgressStrategy import ClassicProgressStrategy
from src.ProgressStrategies.SimpleProgressStrategy import SimpleProgressStrategy


# TODO: test
class Preferences:
    @staticmethod
    def get_progress_preference() -> AbstractProgressStrategy:
        progress_options = {
            '0': SimpleProgressStrategy(9),
            '1': ClassicProgressStrategy(),
        }

        print('Which progress mode would you like?')
        print('0: simple')
        print('1: classic')

        progress_option = input('Enter mode:\n')

        if progress_option not in progress_options:
            # Default to the first mode.
            progress_option = '0'

        return progress_options[progress_option]

    @staticmethod
    def get_guessing_strategy_preference() -> GuessingInterfaceStrategy:
        guessing_options = {
            '0': ClassicGuessingStrategy(''),
            '1': WordsOnlyGuessingStrategy(''),
            '2': GuessingStrategyFactory.case_sensitive_classic(''),
            '3': GuessingStrategyFactory.case_sensitive_words_only(''),
            '4': GuessingStrategyFactory.classic_with_hints(''),
            '5': GuessingStrategyFactory.words_only_with_hints(''),
            '6': GuessingStrategyFactory.case_sensitive_classic_with_hints(''),
            '7': GuessingStrategyFactory.case_sensitive_words_only_with_hints(''),
            '8': 'random',
        }

        guessing_option_names = {
            '0': 'classic',
            '1': 'words only',
            '2': 'case sensitive classic',
            '3': 'case sensitive words only',
            '4': 'classic with hints',
            '5': 'words only with hints',
            '6': 'case sensitive classic with hints',
            '7': 'case sensitive words only with hints',
            '8': 'random',
        }

        print('Which guessing mode would you like?')
        for i in range(len(guessing_option_names)):
            i = str(i)
            print(i + ': ' + guessing_option_names[str(i)])

        guessing_option = input('Enter mode:\n')

        if guessing_option not in guessing_options:
            # Default to the first mode.
            guessing_option = '0'

        if guessing_option_names[guessing_option] == 'random':
            random_choice = str(randrange(0, len(guessing_options) - 1))

            guessing_option = random_choice
            print('The random mode is: %s' % guessing_option_names[random_choice])

        return guessing_options[guessing_option]
