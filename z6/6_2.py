#!/usr/bin/python3
# -*- coding: iso-8859-2 -*-

import unittest
from point import Point as Point
from math import sqrt


# 6.2
class TestPoint(unittest.TestCase):
    def setUp(self):
        self.p1 = Point(1, 2)
        self.p2 = Point(2, 3)
        self.p3 = Point(0, 0)
        self.p4 = Point(-12, 3)

    def test_print(self):
        self.assertEqual(str(self.p1), "(1, 2)")
        self.assertEqual(str(self.p2), "(2, 3)")
        self.assertEqual(str(self.p3), "(0, 0)")
        self.assertEqual(str(self.p4), "(-12, 3)")
        self.assertEqual(repr(self.p1), "Point(1, 2)")
        self.assertEqual(repr(self.p2), "Point(2, 3)")
        self.assertEqual(repr(self.p3), "Point(0, 0)")
        self.assertEqual(repr(self.p4), "Point(-12, 3)")

    def test_eq(self):
        self.assertTrue(self.p1 == self.p1)
        self.assertFalse(self.p1 == self.p2)

    def test_nq(self):
        self.assertFalse(self.p1 != self.p1)
        self.assertTrue(self.p1 != self.p2)

    def test_add(self):
        self.assertEqual(self.p1 + self.p1, "(2, 4)")
        self.assertEqual(self.p2 + self.p1, "(3, 5)")
        self.assertEqual(self.p3 + self.p4, "(-12, 3)")

    def test_sub(self):
        self.assertEqual(self.p1 - self.p1, "(0, 0)")
        self.assertEqual(self.p2 - self.p1, "(1, 1)")
        self.assertEqual(self.p3 - self.p4, "(12, -3)")

    def test_mul(self):
        self.assertEqual(self.p1 * self.p1, "(1, 4)")
        self.assertEqual(self.p2 * self.p1, "(2, 6)")
        self.assertEqual(self.p3 * self.p4, "(0, 0)")

    def test_cross(self):
        self.assertEqual(self.p1.cross(self.p2), -1)
        self.assertEqual(self.p3.cross(self.p2), 0)

    def test_length(self):
        self.assertEqual(self.p1.length(), sqrt(5))
        self.assertEqual(Point(4,3).length(), 5)
        self.assertNotEqual(Point(4, 3).length(), 52)
        self.assertEqual(self.p3.length(), 0)


if __name__ == "__main__":
    unittest.main()