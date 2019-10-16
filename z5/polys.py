#!/usr/bin/python3
# -*- coding: iso-8859-2 -*-


def add_poly(poly1, poly2):
    # listTmp = [poly1, poly2]
    # return [sum(x) for x in zip(*listTmp)]
    if len(poly1) > len(poly2):
        tmp = poly1
        poly1 = poly2
        poly2 = tmp
    return [poly1[i % len(poly1)] + poly2[i] for i in range(len(poly2))]


def sub_poly(poly1, poly2):
    if len(poly1) > len(poly2):
        tmp = len(poly1) - len(poly2)
        for i in range(tmp):
            poly2.append(0)

    if len(poly1) < len(poly2):
        tmp = len(poly2) - len(poly1)
        for i in range(tmp):
            poly1.append(0)

    return [poly1 - poly2 for poly1, poly2 in zip(poly1, poly2)]


def mul_poly(poly1, poly2): pass


def is_zero(poly): pass  # bool, [0], [0,0], itp.


def cmp_poly(poly1, poly2): pass  # bool, porównywanie


def eval_poly(poly, x0): pass  # poly(x0), algorytm Hornera


def combine_poly(poly1, poly2): pass  # poly1(poly2(x)), trudne!


def pow_poly(poly, n): pass  # poly(x) ** n


def diff_poly(poly): pass  # pochodna wielomianu
