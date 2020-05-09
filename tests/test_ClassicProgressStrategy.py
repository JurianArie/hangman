from unittest import TestCase

from src.ProgressStrategies.ClassicProgressStrategy import ClassicProgressStrategy


class TestClassicProgressStrategy(TestCase):
    def it_starts_with_seven_tries(self):
        self.assertEqual(7, ClassicProgressStrategy().get_tries_left())

    def test_draw_progress(self):
        classic = ClassicProgressStrategy()
        self.assertEqual(classic.draw_progress('word', list('w')), classic.get_hang_mans()[7] + '\nw___')
        classic.decrease_tries_left()
        self.assertEqual(classic.draw_progress('word', list('wr')), classic.get_hang_mans()[6] + '\nw_r_')
        classic.decrease_tries_left()
        classic.decrease_tries_left()
        self.assertEqual(classic.draw_progress('word', list('wr')), classic.get_hang_mans()[4] + '\nw_r_')
