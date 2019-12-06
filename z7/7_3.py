#!/usr/bin/python3
# -*- coding: iso-8859-2 -*
import math
from point import Point

class Rectangle:
    """Klasa reprezentująca prostokąty na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
    # Chcemy, aby x1 <= x2, y1 >= y2.
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

        if not x1 <= x2 and y1 >= y2:
           raise ValueError("Only x1 <= x2, y1 >= y2")


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

    def center2(self):
        return [(self.pt1.x/2 + self.pt2.x/2), (self.pt1.y/2 + self.pt2.y/2)]

    def area(self):            # pole powierzchni
        dl = math.sqrt(pow((self.pt2.x - self.pt1.x), 2) + pow((self.pt2.y - self.pt1.y), 2))
        return round(pow(dl, 2)/2, 2)

    def move(self, x, y):      # przesunięcie o (x, y)
        p1 = Point(self.pt1.x + x, self.pt1.y + y)
        p2 = Point(self.pt2.x + x, self.pt2.y + y)
        return "[" + str(p1) + ", " + str(p2) + "]"

    def move2(self, x, y):      # przesunięcie o (x, y)
        p1 = Point(self.pt1.x + x, self.pt1.y + y)
        p2 = Point(self.pt2.x + x, self.pt2.y + y)
        return [p1, p2]

    # https://4programmers.net/Forum/Java/187222-program_liczacy_pole_czesci_wspolnej_dwoch_prostokatow
    def intersection(self, other):   # część wspólna prostokątów
        x1 = max(self.pt1.x, other.pt1.x)
        y1 = max(self.pt1.y, other.pt1.y)
        p1 = Point(x1, y1)
        x2 = max(self.pt2.x, other.pt2.x)
        y2 = max(self.pt2.y, other.pt2.y)
        p2 = Point(x2, y2)

        return Rectangle(p1.x, p1.y, p2.x, p2.y)

    # https://stackoverflow.com/questions/25068538/intersection-and-difference-of-two-rectangles
    # https://www.geeksforgeeks.org/intersecting-rectangle-when-bottom-left-and-top-right-corners-of-two-rectangles-are-given/
    def overlap(self, other):
        if self.pt1.x > other.pt2.x or other.pt1.x > self.pt2.x:
            return False

        if self.pt1.y < other.pt2.y or other.pt1.y < self.pt2.y:
            return False

        return True

    def cover(self, other):    # prostąkąt nakrywający oba
        x1 = min(self.pt1.x, other.pt1.x)
        x2 = max(self.pt2.x, other.pt2.x)
        y1 = max(self.pt1.y, other.pt1.y)
        y2 = min(self.pt2.y, other.pt2.y)
        p1 = Point(x1, y1)
        p2 = Point(x2, y2)

        return "[" + str(p1) + ", " + str(p2) + "]"

    def make4(self):           # zwraca listę czterech mniejszych

        h = (self.pt1.y + self.pt2.y)/2

        L = []
        p1 = Rectangle(float(self.pt1.x), float(self.pt1.y), self.center2()[0], self.center2()[1])
        L.append(p1)
        p2 = Rectangle(float(self.pt1.x), h, self.center2()[0], float(self.pt2.y))
        L.append(p2)
        p3 = Rectangle(h, float(self.pt1.y), float(self.pt2.x), h)
        L.append(p3)
        p4 = Rectangle(self.center2()[0], self.center2()[1], float(self.pt2.x), float(self.pt2.y))
        L.append(p4)

        return L

# Kod testujący moduł.

import unittest

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
        self.assertEqual(self.r1.move(1, 2), "[(2, 4), (4, 6)]")

    def test_cover(self):
        self.assertEqual(self.r6.cover(self.r7), "[(1, 5), (6, 1)]")
        self.assertEqual(self.r8.cover(self.r9), "[(1, 4), (4, 1)]")

    def test_make4(self):
        self.assertEqual(str(self.r8.make4()[0]), "[(1.0, 4.0), (2.5, 2.5)]")
        self.assertEqual(str(self.r8.make4()[1]), "[(1.0, 2.5), (2.5, 1.0)]")
        self.assertEqual(str(self.r8.make4()[2]), "[(2.5, 4.0), (4.0, 2.5)]")
        self.assertEqual(str(self.r8.make4()[3]), "[(2.5, 2.5), (4.0, 1.0)]")

        # print(self.r10.make4())
        self.assertEqual(str(self.r10.make4()[0]), "[(1.0, 3.0), (2.0, 2.0)]")
        self.assertEqual(str(self.r10.make4()[1]), "[(1.0, 2.0), (2.0, 1.0)]")
        self.assertEqual(str(self.r10.make4()[2]), "[(2.0, 3.0), (3.0, 2.0)]")
        self.assertEqual(str(self.r10.make4()[3]), "[(2.0, 2.0), (3.0, 1.0)]")



if __name__ == "__main__":
    unittest.main()