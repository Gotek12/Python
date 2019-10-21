#!/usr/bin/python3
# -*- coding: iso-8859-2 -*-
import math


def heron(a, b, c):
    """Obliczanie pola powierzchni tr�jk�ta za pomoc� wzoru
    Herona. D�ugo�ci bok�w tr�jk�ta wynosz� a, b, c."""
    try:
        if not a + b > c or not a + c > b or not b + c > a:
            raise ValueError

        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) + (s - b) + (s - c))
        print(area)
    except ValueError:
        print("B��dne warto�ci - tr�jk�t nie istnieje")


print("8.4")
heron(1, 10, 12) # b��dna waro��
heron(3, 4, 5)
heron(7, 24, 25)
heron(5, 5, 2)