from unittest import TestCase


class TestAbstractProgressStrategy(TestCase):
    def test_it_will_get_the_correct_tries_left(self):
        dummy = DummyProgressStrategy(9)
        self.assertEqual(9, dummy.get_tries_left())
        dummy.decrease_tries_left()
        self.assertEqual(8, dummy.get_tries_left())


from typing import List

from src.ProgressStrategies.AbstractProgressStrategy import AbstractProgressStrategy


class DummyProgressStrategy(AbstractProgressStrategy):
    def draw_progress(self, word: str, good_guesses: List[str]) -> str:
        return ''
