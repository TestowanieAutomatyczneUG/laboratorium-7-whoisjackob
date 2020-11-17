import unittest

from src.sample.Roman import *

class RomanNumeralsTest(unittest.TestCase):

    def setUp(self):
        self.tmp = Roman()

    def test_1_is_a_single_i(self):
        self.assertEqual(self.tmp.roman(1), "I")

    def test_2_is_two_i_s(self):
        self.assertEqual(self.tmp.roman(2), "II")

    def test_3_is_three_i_s(self):
        self.assertEqual(self.tmp.roman(3), "III")
