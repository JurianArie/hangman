from __future__ import annotations

from src.ProgressStrategies.Decorators.PayToWin import PayToWin
from src.ProgressStrategies.ProgressStrategyInterface import ProgressStrategyInterface


class ProgressStrategyBuilder:
    _progress_strategy: ProgressStrategyInterface

    def __init__(self, progress_strategy: ProgressStrategyInterface):
        self._progress_strategy = progress_strategy

    def pay_to_win(self) -> ProgressStrategyBuilder:
        self._progress_strategy = PayToWin(self._progress_strategy)

        return self

    def build(self) -> ProgressStrategyInterface:
        return self._progress_strategy
