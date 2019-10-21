#!/usr/bin/python3
# -*- coding: iso-8859-2 -*-

# 5.2
from fracs import *
import unittest

class TestFractions(unittest.TestCase):
    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        # self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])
        self.assertEqual(add_frac([1, 500], [2, 1500]), [1, 300])

    def test_sub_frac(self):
        self.assertEqual(sub_frac([1, 4], [1, 3]), [-1, 12])

    def test_mul_frac(self):
        self.assertEqual(mul_frac([1, 12], [3, 3]), [1, 12])

    def test_div_frac(self):
        self.assertEqual(div_frac([1, 12], [1, 12]), [1, 1])

    def test_is_positive(self):
        self.assertEqual(is_positive([1, 2]), True)
        self.assertEqual(is_positive([-1, 2]), False)
        self.assertEqual(is_positive([-1, -2]), True)
        self.assertEqual(is_positive([1, -2]), False)

    def test_is_zero(self):
        self.assertEqual(is_zero([0,-231]), True)

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac([1, 2], [3, 6]), 0)
        self.assertEqual(cmp_frac([-1, 2], [3, 6]), 1)
        self.assertEqual(cmp_frac([1, 2], [3, -6]), -1)

    def test_frac2float(self):
        self.assertEqual(frac2float([1, 4]), 0.25)


if __name__ == '__main__':
    unittest.main()
