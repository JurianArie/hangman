from os import system

from src.HangMan import HangMan
from src.Preferences import Preferences

progress_strategy = Preferences.get_progress_preference()
guessing_strategy = Preferences.get_guessing_strategy_preference()

word = input('Enter a word\n')

while not word.isalpha():
    print('Only letters are allowed')
    word = input('Enter a word\n')

system('clear')

HangMan(guessing_strategy(word), progress_strategy).play()
