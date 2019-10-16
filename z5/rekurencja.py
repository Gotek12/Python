#!/usr/bin/python
# -*- coding: iso-8859-2 -*-
def factorial(n):
    value = 1;
    for i in range(1, n+1):
        value *= i;
    return value

def fibo(n):
    x, y = 0, 1
    for i in range(0, n):
        x, y = y, x + y
    return x