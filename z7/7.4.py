#!/usr/bin/python3
# -*- coding: iso-8859-2 -*
import math
from point import Point

class Triangle:
    """Klasa reprezentująca trójkąty na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2, x3, y3):
        # Należy zabezpieczyć przed sytuacją, gdy punkty są współliniowe.
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)
        self.pt3 = Point(x3, y3)

        # http://matematyka.pisz.pl/forum/86269.html
        ab = (self.pt2.y -  self.pt1.y)/(self.pt2.x - self.pt1.x)
        ac = (self.pt3.y -  self.pt1.y)/(self.pt3.x - self.pt1.x)
        if ab == ac:
           raise ValueError("Punkty są współliniowe")

    def __str__(self):          # "[(x1, y1), (x2, y2), (x3, y3)]"
        return "[" + str(self.pt1) + ", " + str(self.pt2) + ", " + str(self.pt3) + "]"

    def __repr__(self):        # "Triangle(x1, y1, x2, y2, x3, y3)"
        return "Triangle({0}, {1}, {2}, {3}, {4}, {5})".format(self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y, self.pt3.x, self.pt3.y)

    def __eq__(self, other):    # obsługa tr1 == tr2
        return self.pt1 == other.pt1 and self.pt2 == other.pt2 and self.pt3 == other.pt3

    def __ne__(self, other):        # obsługa tr1 != tr2
        return not self == other

    def center(self):           # zwraca środek trójkąta
        return "[" + str((self.pt1.x/2 + self.pt2.x/2 + self.pt3.x/2)) + ", " + str((self.pt1.y/2 + self.pt2.y/2 + self.pt3.y/2)) + "]"

    def area(self):             # pole powierzchni
        return abs( (self.pt2.x - self.pt1.x)*(self.pt3.y - self.pt1.y) - (self.pt2.y - self.pt1.y)*(self.pt3.x - self.pt1.x) )/2

    def move(self, x, y):  # przesunięcie o (x, y)
        p1 = Point(self.pt1.x + x, self.pt1.y + y)
        p2 = Point(self.pt2.x + x, self.pt2.y + y)
        p3 = Point(self.pt3.x + x, self.pt3.y + y)
        return "[" + str(p1) + ", " + str(p2) + ", " + str(p3) + "]"

    def make4(self):           # zwraca listę czterech mniejszych

        s1 = Point((self.pt1.x + self.pt2.x)/2, (self.pt1.y + self.pt2.y)/2)
        s2 = Point((self.pt1.x + self.pt3.x) / 2, (self.pt1.y + self.pt3.y) / 2)
        s3 = Point((self.pt2.x + self.pt3.x) / 2, (self.pt2.y + self.pt3.y) / 2)

        L = []
        p1 = Triangle(float(self.pt1.x), float(self.pt1.y), s1.x, s1.y, s2.x, s2.y)
        L.append(p1)
        p2 = Triangle(s3.x, s3.y, s1.x, s1.y, s2.x, s2.y)
        L.append(p2)
        p3 = Triangle(s1.x, s1.y, float(self.pt2.x), float(self.pt2.y), s3.x, s3.y)
        L.append(p3)
        p4 = Triangle(s2.x, s2.y, s3.x, s3.y, float(self.pt3.x), float(self.pt3.y))
        L.append(p4)
        return L

# Kod testujący moduł.

import unittest

class TestTriangle(unittest.TestCase):
    def setUp(self): pass

    def test_print(self): pass

    def test_eq(self): pass

    def test_nq(self): pass

    def test_center(self): pass

    def test_pole(self): pass

    def move(self): pass

    def test_make4(self): pass


if __name__ == "__main__":
    unittest.main()