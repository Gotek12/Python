#!/usr/bin/python3
# -*- coding: iso-8859-2 -*-
import math


def reduction(x, y):
   maxi = math.gcd(x, y)
   x /= maxi
   y /= maxi
   return [x, y]


def add_frac(frac1, frac2):
    # max = fractions.gcd(frac1[1], frac2[1])
    # max = (frac1[1]*frac2[1]) / max
    # num =  frac1[0] * (max/frac1[1]) + frac2[0] * (max/frac2[1])
    # common = fractions.gcd(num, max)
    # max = int(max/common)
    # num = int(num/common)
    # return num/max
    return reduction((frac1[0] * frac2[1] + frac1[1] * frac2[0]), (frac1[1] * frac2[1]))


def sub_frac(frac1, frac2):
    return reduction((frac1[0] * frac2[1] - frac1[1] * frac2[0]), (frac1[1] * frac2[1]))


def mul_frac(frac1, frac2):
    return reduction((frac1[0] * frac2[0]), (frac1[1] * frac2[1]))


def div_frac(frac1, frac2):
    return reduction((frac1[0] * frac2[1]), (frac1[1] * frac2[0]))


def is_positive(frac):
    if frac[0] > 0 and frac[1] > 0 or frac[0] < 0 and frac[1] < 0:
        return True
    else:
        return False


def is_zero(frac):
    if frac[0] == 0:
        return True
    return False


def cmp_frac(frac1, frac2):
    if (frac1[0] / frac1[1]) == (frac2[0] / frac2[1]):
        return 0
    elif (frac1[0] / frac1[1]) > (frac2[0] / frac2[1]):
        return -1
    else:
        return 1


def frac2float(frac):
    return float(frac[0]/frac[1])