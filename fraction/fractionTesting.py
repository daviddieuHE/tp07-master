import unittest

from fraction.fraction import Fraction

class agrsTest(unittest.TestCase):

    def test_pass(self):
        self.assertTrue(Fraction(4, 1))