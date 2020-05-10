from unittest import TestCase

from src.GameModes.WordChangers.CaseSensitive import CaseSensitive


class TestCaseSensitive(TestCase):
    def test_manipulate(self):
        self.assertEqual('BlaA', CaseSensitive.manipulate('BlaA'))
        self.assertEqual('bla', CaseSensitive.manipulate('bla'))
