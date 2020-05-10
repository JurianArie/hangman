from src.ProgressStrategies.AbstractProgressStrategy import AbstractProgressStrategy
from src.ProgressStrategies.ClassicProgressStrategy import ClassicProgressStrategy
from src.ProgressStrategies.SimpleProgressStrategy import SimpleProgressStrategy

# TODO: test
PROGRESS_OPTIONS = {
    '0': SimpleProgressStrategy(9),
    '1': ClassicProgressStrategy(),
}


class ProgressPreferences:
    def get_preference(self) -> AbstractProgressStrategy:
        print('Which progress mode would you like?')
        print('0: simple')
        print('1: classic')

        progress_option = input('Enter mode:\n')

        if progress_option not in PROGRESS_OPTIONS:
            # Default to the first mode.
            progress_option = '0'

        return PROGRESS_OPTIONS[progress_option]
