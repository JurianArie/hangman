from os import system

from src.GuessingStrategies.SimpleGuessingStrategy import SimpleGuessingStrategy
from src.HangMan import HangMan
from src.ProgressStrategies.SimpleProgressStrategy import SimpleProgressStrategy

word = input('Enter a word\n')

while not word.isalpha():
    print('Only letters are allowed')
    word = input('Enter a word\n')

system('clear')

progress_strategy = SimpleProgressStrategy(9)
guessing_strategy = SimpleGuessingStrategy(word)

HangMan(guessing_strategy, progress_strategy).play()
