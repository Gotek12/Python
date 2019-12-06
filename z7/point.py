#!/usr/bin/python3
# -*- coding: iso-8859-2 -*-

from math import sqrt


class Point:
    """Klasa reprezentuj±ca punkty na p³aszczy¼nie."""

    def __init__(self, x, y):  # konstuktor
        self.x = x
        self.y = y

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    def __repr__(self):        # zwraca string "Point(x, y)"
        return "Point({0}, {1})".format(self.x, self.y)

    def __eq__(self, other):    # obs³uga point1 == point2
        return (self.x == other.x) and (self.y == other.y)

    def __ne__(self, other):        # obs³uga point1 != point2
        return not self == other

    # Punkty jako wektory 2D.
    def __add__(self, other):   # v1 + v2
        return str(Point(self.x + other.x, self.y + other.y))

    def __sub__(self, other):   # v1 - v2
        return str(Point(self.x - other.x, self.y - other.y))

    def __mul__(self, other):   # v1 * v2, iloczyn skalarny
        return str(Point(self.x * other.x, self.y * other.y))

    def cross(self, other):         # v1 x v2, iloczyn wektorowy 2D
        return self.x * other.y - self.y * other.x

    def length(self):           # d³ugo¶æ wektora
        return sqrt(self.x**2 + self.y**2)