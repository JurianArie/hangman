from os import system

from src.GuessingStrategies.ClassicGuessingStrategy import ClassicGuessingStrategy
from src.HangMan import HangMan
from src.Preferences import Preferences

progress_strategy = Preferences.get_progress_preference()

word = input('Enter a word\n')

while not word.isalpha():
    print('Only letters are allowed')
    word = input('Enter a word\n')

system('clear')

guessing_strategy = ClassicGuessingStrategy(word)

HangMan(guessing_strategy, progress_strategy).play()
