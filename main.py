from os import system

from src.GuessingPreferences import GuessingPreferences
from src.HangMan import HangMan
from src.ProgressPreferences import ProgressPreferences

progress_strategy = ProgressPreferences().get_preference()
guessing_strategy = GuessingPreferences().get_preference()

word = input('Enter a word\n')

while not word.isalpha():
    print('Only letters are allowed')
    word = input('Enter a word\n')

system('clear')

guessing_strategy.set_word(word)

HangMan(guessing_strategy, progress_strategy).play()
