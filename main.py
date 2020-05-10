from os import system

from src.GameModePreferences import GameModePreferences
from src.HangMan import HangMan
from src.ProgressPreferences import ProgressPreferences

wantsToPlay: bool = True
times_played: int = 0

while wantsToPlay:
    if times_played == 0 or input('Do you want to keep your settings? y/n:') != 'y':
        progress_strategy = ProgressPreferences().get_preference()
        game_mode = GameModePreferences().get_preference()

    word = input('Enter a word\n')

    while not word.isalpha():
        print('Only letters are allowed')
        word = input('Enter a word\n')

    system('clear')

    game_mode.set_word(word)

    hang_man = HangMan(game_mode, progress_strategy)
    hang_man.play()

    if input('Want to play again? y/n:') != 'y':
        wantsToPlay = False

    hang_man.reset()
    times_played += 1
