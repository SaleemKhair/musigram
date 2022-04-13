import unittest
from diagram.model import Clock


class TestClock(unittest.TestCase):
  
    def setUp(self) -> None:
        self.clock = Clock(0, 0)
        self.clock.append(7)
        self.clock.append(9)
        self.clock.append(11)

    def test_get_set(self):
        clock_set = self.clock.get_set()
        assert clock_set == [7, 9, 11], 'incorrect set'

    def test_transpose(self):
        transposed_clock = self.clock.transpose(3)
        t_clock_set = transposed_clock.get_set()
        assert self.clock.get_set() == [7, 9, 11], 'side-effect on original'
        assert t_clock_set == [10, 0, 2], 'incorrect transpose'