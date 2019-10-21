#!/usr/bin/python3
# -*- coding: iso-8859-2 -*-

import random as ran
import math


def calc_pi(n=100):
    """Obliczanie liczby pi metod� Monte Carlo.
    n oznacza liczb� losowanych punkt�w."""
    inside = 0
    for i in range(0, n):
        x = ran.random()
        y = ran.random()
        if math.sqrt(x**2 + y**2) <= 1:
            inside += 1
        pi = 4*(float(inside)/n)

    print("Pi Monte Carlo dla ", n, " krok�w -> ", pi)


print("8.3")
print("Math.pi() -> ", math.pi)
calc_pi(10000)