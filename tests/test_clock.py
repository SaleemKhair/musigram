import unittest
from musigram.model import Clock


class TestClock(unittest.TestCase):
  
    def setUp(self) -> None:
        self.clock = Clock(0, 0)
        self.clock.append(7)
        self.clock.append(9)
        self.clock.append(11)

        self.transpositionally_relative = Clock(0, 0)
        self.transpositionally_relative.append(8)
        self.transpositionally_relative.append(10)
        self.transpositionally_relative.append(0)

        self.inversionally_relateive = Clock(0, 0)
        self.inversionally_relateive.append(8)
        self.inversionally_relateive.append(6)
        self.inversionally_relateive.append(4)


    def test_get_set(self):
        clock_set = self.clock.get_set()
        assert clock_set == [7, 9, 11], 'incorrect set'

    def test_transpose(self):
        transposed_clock = self.clock.transpose(3)
        t_clock_set = transposed_clock.get_set()
        assert self.clock.get_set() == [7, 9, 11], 'side-effect on original'
        assert t_clock_set == [10, 0, 2], 'incorrect transpose'
    
    def test_invert(self):
        inverted_clock = self.clock.invert(3)
        i_clock_set = inverted_clock.get_set()
        assert self.clock.get_set() == [7, 9, 11], 'side-effect on original'
        assert i_clock_set == [8, 6, 4], 'incorrect invert'

    def test_is_inversionally_relateive(self):
        assert self.clock.is_inversionally_relateive(self.inversionally_relateive)

    def test_is_transpositionally_relative(self):
        assert self.clock.is_transpositionally_relative(self.transpositionally_relative)
