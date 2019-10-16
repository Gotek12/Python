#!/usr/bin/python3
# -*- coding: iso-8859-2 -*-

#5.3
from polys import *
import unittest


class TestPolynomials(unittest.TestCase):
    def setUp(self):
        self.p1 = [0, 1]  # W(x) = x
        self.p2 = [0, 0, 1]  # W(x) = x*x

    def test_add_poly(self):
        self.assertEqual(add_poly(self.p1, self.p2), [0, 1, 1])
        self.assertEqual(add_poly(self.p2, self.p1), [0, 1, 1])
        self.assertEqual(add_poly(self.p2, self.p2), [0, 0, 2])

    def test_sub_poly(self):
        self.assertEqual(sub_poly(self.p2, self.p2), [0, 0, 0])
        self.assertEqual(sub_poly(self.p2, self.p1), [0, -1, 1])
        self.assertEqual(sub_poly(self.p1, self.p2), [0, 1, -1])


if __name__ == '__main__':
    unittest.main()