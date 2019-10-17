#!/usr/bin/python
# -*- coding: iso-8859-2 -*-

import unittest
from math import sqrt
from times import Time as T
import sys
# korzystamy z python 2
# ale również zadziała na python3
# 6.1

print('Ver of python -> ', sys.version_info[0])
class TestTime(unittest.TestCase):
    def setUp(self):
        self.t123 = T(123)
        self.t1 = T(1)
        self.t2 = T(2)
        self.t3 = T(3)
        self.t33 = T(1) + T(2)

    def test_print(self):
        self.assertEqual(str(T(12345)), "03:25:45")
        self.assertEqual(str(self.t1), "00:00:01")
        self.assertEqual(repr(self.t123), "Time(123)")

    def test_add(self):
        self.assertNotEqual(self.t1 + self.t3, self.t1)
        self.assertEqual(self.t1, self.t1)
        self.assertEqual(self.t33, self.t3)

    def test_cmp(self):
        self.assertTrue(self.t33 == self.t33)
        self.assertTrue(self.t33 == self.t3)
        self.assertFalse(self.t123 == self.t1)
        self.assertTrue(self.t1 != self.t2)
        self.assertTrue(self.t123 > self.t1)
        self.assertFalse(self.t123 <= self.t1)

    def test_int(self):
        self.assertTrue(int(self.t1), 1)
        self.assertTrue(int(self.t123), 123)
        self.assertTrue(int(T(12345)), 12345)

    def tearDown(self): pass


if __name__ == "__main__":
    unittest.main()     # wszystkie testy"""