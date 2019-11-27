#!/usr/bin/python3
# -*- coding: iso-8859-2 -*-
import time
import random as ran
import math
from numba import njit, prange
import numpy as np

def calc_pi(n=100):
    """Obliczanie liczby pi metodą Monte Carlo.
    n oznacza liczbę losowanych punktów."""
    inside = 0
    for i in range(0, n):
        x = ran.random()
        y = ran.random()
        if math.sqrt(x**2 + y**2) <= 1:
            inside += 1
        pi = 4*(float(inside)/n)

    print("Pi Monte Carlo dla ", n, " kroków -> ", pi)


print("8.3")
print("Math.pi() -> ", math.pi)

# calc_pi(10000)
# calc_pi(10)

start_time = time.time()
calc_pi(999999)
stop_time = time.time() - start_time
print(stop_time, "s")

# calc_pi(9999999)