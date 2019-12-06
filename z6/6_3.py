#!/usr/bin/python3
# -*- coding: iso-8859-2 -*
import math
from point import Point
import unittest


class Rectangle:

    #lewy dolny i prawy górny
    def __init__(self, x1, y1, x2, y2):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):        # "[(x1, y1), (x2, y2)]"
        return "[" + str(self.pt1) + ", " + str(self.pt2) + "]"

    def __repr__(self):        # "Rectangle(x1, y1, x2, y2)"
        return "Rectangle({0}, {1}, {2}, {3})".format(self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y)

    def __eq__(self, other):   # obsługa rect1 == rect2
        return self.pt1 == other.pt1 and self.pt2 == other.pt2

    def __ne__(self, other):      # obsługa rect1 != rect2
        return not self == other

    def center(self):          # zwraca środek prostokąta
        return "[" + str((self.pt1.x/2 + self.pt2.x/2)) + ", " + str((self.pt1.y/2 + self.pt2.y/2)) + "]"

    def area(self):            # pole powierzchni
        dl = math.sqrt(pow((self.pt2.x - self.pt1.x), 2) + pow((self.pt2.y - self.pt1.y), 2))
        return round(pow(dl, 2)/2, 2)

    def move(self, x, y):      # przesunięcie o (x, y)
        p1 = Point(self.pt1.x + x, self.pt1.y + y)
        p2 = Point(self.pt2.x + x, self.pt2.y + y)
        return Rectangle(p1.x, p1.y, p2.x, p2.y)


class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.r1 = Rectangle(1, 2, 3, 4)
        self.r2 = Rectangle(1, 2, 3, 4)
        self.r3 = Rectangle(7, 3, -3, 5)
        self.r4 = Rectangle(0, 10, 10, 0)
        self.r5 = Rectangle(5, 5, 15, 0)
        self.r6 = Rectangle(1, 2, 2, 1)
        self.r7 = Rectangle(3, 5, 6, 2)
        self.r8 = Rectangle(1, 4, 4, 1)
        self.r9 = Rectangle(1, 4, 2, 2)
        self.r10 = Rectangle(1, 3, 3, 1)

    def test_print(self):
        self.assertEqual(str(self.r1), "[(1, 2), (3, 4)]")
        self.assertEqual(repr(self.r1), "Rectangle(1, 2, 3, 4)")

    def test_eq(self):
        self.assertTrue(self.r1 == self.r1)
        self.assertTrue(self.r1 == self.r2)

    def test_nq(self):
        self.assertFalse(self.r1 != self.r1)

    def test_center(self):
        self.assertEqual(self.r3.center(), "[2.0, 4.0]")

    def test_pole(self):
        self.assertEqual(self.r1.area(), 4.0)

    def move(self):
        self.assertEqual(str(self.r1.move(1, 2)), "[(2, 4), (4, 6)]")

if __name__ == "__main__":
    unittest.main()