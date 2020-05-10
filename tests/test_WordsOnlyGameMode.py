from unittest import TestCase

from src.GameModes.WordsOnlyGameMode import WordsOnlyGameMode


class TestWordsOnlyGameMode(TestCase):
    def test_guess_is_correct(self):
        guesser = WordsOnlyGameMode('guess')
        self.assertFalse(guesser.guess_is_correct('g'))
        self.assertFalse(guesser.guess_is_correct('u'))
        self.assertFalse(guesser.guess_is_correct('e'))
        self.assertFalse(guesser.guess_is_correct('s'))

        self.assertFalse(guesser.guessed_the_word())

        self.assertTrue(guesser.guess_is_correct('guess'))
        self.assertTrue(guesser.guessed_the_word())

    def test_it_is_case_insensitive(self):
        guesser = WordsOnlyGameMode('blA')
        self.assertEqual('bla', guesser.get_word())
        self.assertTrue(guesser.guess_is_correct('Bla'))
        self.assertTrue(guesser.guessed_the_word())
