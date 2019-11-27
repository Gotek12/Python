#!/usr/bin/python3
# -*- coding: iso-8859-2 -*-
import time

# rekurencja
def P(i, j):
    if i == 0.0 and j == 0.0:
        return 0.5
    if i > 0.0 and j == 0.0:
        return 0.0
    if i == 0.0 and j > 0.0:
        return 1.0
    if i > 0.0 and j > 0.0:
        return 0.5 * (P(i - 1.0, j) + P(i, j - 1))

# dynamicznie
P2_tab = {}
def P2(i, j):
    if(i, j) in P2_tab:
        return P2_tab[(i, j)]
    else:
        if i == 0.0 and j == 0.0:
            suma = 0.5
        if i > 0.0 and j == 0.0:
            suma = 0.0
        if i == 0.0 and j > 0.0:
            suma = 1.0
        if i > 0.0 and j > 0.0:
            suma = 0.5 * (P2(i - 1.0, j) + P2(i, j - 1))
        P2_tab[(i, j)] = suma
        return suma


print(P(2.0, 3.0))
print(P2(2.0, 3.0))

print(P(5.0, 4.0))
print(P2(5.0, 4.0))

t1 = time.time()
print(P(17.0, 11.0))
print("Czas P(17.0, 11.0) rekurencyjnnie ->", time.time()-t1)

t2 = time.time()
print(P2(17.0, 11.0))
print("Czas P2(17.0, 11.0) dynamicznie ->", time.time()-t2)
