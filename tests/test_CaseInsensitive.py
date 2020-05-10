from unittest import TestCase

from src.GuessingStrategies.WordChangers.CaseInsensitive import CaseInsensitive


class TestCaseInsensitive(TestCase):
    def test_manipulate(self):
        self.assertEqual('blaa', CaseInsensitive.manipulate('BlaA'))
        self.assertEqual('bla', CaseInsensitive.manipulate('bla'))
