from unittest import TestCase

from src.ProgressStrategies.WordRevealer import WordRevealer


class TestWordRevealer(TestCase):
    def test_it_wil_reveal_the_whole_word(self):
        word = 'python'
        self.assertEqual(word, WordRevealer.reveal(word, list(word)))

    def test_it_will_reveal_part_of_the_word(self):
        self.assertEqual('_ytho_', WordRevealer.reveal('python', list('ytho')))

    def test_it_will_reveal_fill_multiple_of_the_same_letter(self):
        self.assertEqual('aa____dd__', WordRevealer.reveal('aabbccddee', list('ad')))
