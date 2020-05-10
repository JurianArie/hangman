from unittest import TestCase

from src.GuessingStrategies.WordChangers.CaseSensitive import CaseSensitive


class TestCaseSensitive(TestCase):
    def test_manipulate(self):
        self.assertEqual('BlaA', CaseSensitive.manipulate('BlaA'))
        self.assertEqual('bla', CaseSensitive.manipulate('bla'))
