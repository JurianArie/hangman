from unittest import TestCase

from src.GameModes.WordChangers.CaseInsensitive import CaseInsensitive


class TestCaseInsensitive(TestCase):
    def test_manipulate(self):
        self.assertEqual('blaa', CaseInsensitive.manipulate('BlaA'))
        self.assertEqual('bla', CaseInsensitive.manipulate('bla'))
