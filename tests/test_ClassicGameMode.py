from unittest import TestCase

from src.GameModes.ClassicGameMode import ClassicGameMode


class TestClassicGameMode(TestCase):
    def test_guess_is_correct(self):
        guesser = ClassicGameMode('python')
        self.assertTrue(guesser.guess_is_correct('python'))
        self.assertTrue(guesser.guessed_the_word())
        self.assertFalse(guesser.all_letters_have_been_guessed())

        self.assertFalse(guesser.guess_is_correct('blabla'))
        self.assertFalse(guesser.guess_is_correct(''))
        self.assertFalse(guesser.guessed_the_word())

    def test_it_is_case_insensitive(self):
        guesser = ClassicGameMode('Word')
        self.assertEqual('word', guesser.get_word())
        self.assertTrue(guesser.guess_is_correct('wOrD'))
        self.assertTrue(guesser.guessed_the_word())

    def test_it_checks_previous_tries(self):
        guesser = ClassicGameMode('impossible')
        self.assertFalse(guesser.guess_is_correct('python'))
        self.assertFalse(guesser.guess_is_correct('python'))
        self.assertTrue(guesser.guess_has_been_tried('pytHon'))

    def test_it_will_check_letters(self):
        guesser = ClassicGameMode('hang')
        self.assertTrue(guesser.guess_is_correct('h'))
        self.assertFalse(guesser.guess_is_correct('i'))
        self.assertTrue(guesser.guess_is_correct('a'))
        self.assertTrue(guesser.guess_is_correct('n'))
        self.assertEqual(list('han'), guesser.get_good_guesses())

        self.assertTrue(guesser.guess_is_correct('g'))
        self.assertTrue(guesser.guessed_the_word())
        self.assertTrue(guesser.all_letters_have_been_guessed())
