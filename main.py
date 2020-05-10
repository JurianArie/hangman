from os import system

from src.GameModePreferences import GameModePreferences
from src.HangMan import HangMan
from src.ProgressPreferences import ProgressPreferences

progress_strategy = ProgressPreferences().get_preference()
game_mode = GameModePreferences().get_preference()

word = input('Enter a word\n')

while not word.isalpha():
    print('Only letters are allowed')
    word = input('Enter a word\n')

system('clear')

game_mode.set_word(word)

HangMan(game_mode, progress_strategy).play()
