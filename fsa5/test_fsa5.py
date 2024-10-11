import unittest

from fsa5.fsa5_main import FSA


class TestFSA(unittest.TestCase):
    def test(self):
        input_data = [1, 0, 1, 0, 0, 0, 0, 1, 1]
        fsa = FSA.instance()
        self.assertEqual([0, 0, 0, 0, 1, 0, 1, 0, 0], fsa.process(input_data))