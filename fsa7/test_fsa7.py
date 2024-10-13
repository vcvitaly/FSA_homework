import unittest

from fsa7.fsa7_main import FSA


class TestFSA(unittest.TestCase):
    def test_equal(self):
        input_data = [1, 1, 0, 0, 1, 1, 0, 0]
        fsa = FSA.instance()
        self.assertEqual([0, 0, 0, 0], fsa.process(input_data))

    def test_not_equal(self):
        input_data = [1, 0, 0, 0, 1, 1, 0, 0]
        fsa = FSA.instance()
        self.assertEqual([1, 1, 1, 1], fsa.process(input_data))

    def test_half_equal(self):
        input_data = [1, 1, 0, 0, 1, 0, 0, 0]
        fsa = FSA.instance()
        self.assertEqual([0, 0, 1, 1], fsa.process(input_data))