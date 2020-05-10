from src.GuessingStrategies.ClassicGuessingStrategy import ClassicGuessingStrategy
from src.GuessingStrategies.GuessingStrategyFactory import GuessingStrategyFactory
from src.GuessingStrategies.WordsOnlyGuessingStrategy import WordsOnlyGuessingStrategy
from src.ProgressStrategies.ClassicProgressStrategy import ClassicProgressStrategy
from src.ProgressStrategies.SimpleProgressStrategy import SimpleProgressStrategy


# TODO: test
class Preferences:
    @staticmethod
    def get_progress_preference():
        progress_options = {
            '0': SimpleProgressStrategy(9),
            '1': ClassicProgressStrategy(),
        }

        print('Which progress mode would you like?')
        print('0: simple')
        print('1: classic')

        progress_option = input('Enter mode:\n')

        if progress_option not in progress_options:
            # Default to the simple mode.
            progress_option = '0'

        return progress_options[progress_option]

    @staticmethod
    def get_guessing_strategy_preference():
        guessing_options = {
            '0': ClassicGuessingStrategy(''),
            '1': WordsOnlyGuessingStrategy(''),
            '2': GuessingStrategyFactory.case_sensitive_classic(''),
            '3': GuessingStrategyFactory.case_sensitive_words_only(''),
            '4': GuessingStrategyFactory.classic_with_hints(''),
            '5': GuessingStrategyFactory.words_only_with_hints(''),
        }

        print('Which guessing mode would you like?')
        print('0: classic')
        print('1: words only')
        print('2: case sensitive classic')
        print('3: case sensitive words only')
        print('4: classic with hints')
        print('5: words only with hints')

        guessing_option = input('Enter mode:\n')

        if guessing_option not in guessing_options:
            # Default to the simple mode.
            guessing_option = '0'

        return guessing_options[guessing_option]
