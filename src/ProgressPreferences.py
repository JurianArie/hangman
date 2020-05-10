from src.ProgressStrategies.ClassicProgressStrategy import ClassicProgressStrategy
from src.ProgressStrategies.ProgressStrategyBuilder import ProgressStrategyBuilder
from src.ProgressStrategies.ProgressStrategyInterface import ProgressStrategyInterface
from src.ProgressStrategies.SimpleProgressStrategy import SimpleProgressStrategy

# TODO: test
PROGRESS_OPTIONS = {
    '0': ProgressStrategyBuilder(SimpleProgressStrategy(9)),
    '1': ProgressStrategyBuilder(ClassicProgressStrategy()),
}


class ProgressPreferences:
    def get_preference(self) -> ProgressStrategyInterface:
        print('Which progress mode would you like?')
        print('0: simple')
        print('1: classic')

        progress_option = input('Enter mode:\n')

        if progress_option not in PROGRESS_OPTIONS:
            # Default to the first mode.
            progress_option = '0'

        progress_strategy_builder = PROGRESS_OPTIONS[progress_option]

        if input('Enable pay to win? y/n:') == 'y':
            progress_strategy_builder.pay_to_win()

        return progress_strategy_builder.build()
