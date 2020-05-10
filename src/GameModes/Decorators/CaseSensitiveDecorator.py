from src.GameModes.Decorators.GameModeDecorator import GameModeDecorator
from src.GameModes.GameModeInterface import GameModeInterface
from src.GameModes.WordChangers.CaseSensitive import CaseSensitive


class CaseSensitiveDecorator(GameModeDecorator):
    def __init__(self, game_mode: GameModeInterface):
        super().__init__(game_mode)
        super().set_word_changer(CaseSensitive())
