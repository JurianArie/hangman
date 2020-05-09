from typing import List


class WordRevealer:
    @staticmethod
    def reveal(word: str, good_guesses: List[str]) -> str:
        letters = list(word)
        progress = ''

        for letter in letters:
            if letter in good_guesses:
                progress += letter
            else:
                progress += '_'

        return progress
