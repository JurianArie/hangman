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
