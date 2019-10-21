#!/usr/bin/python3
# -*- coding: iso-8859-2 -*


def median(L, left, right):
    Lnew = L[left:right+1]
    Lnew.sort()

    n = len(Lnew)
    if n % 2 == 0:
        return float((Lnew[int(n / 2 - 1)] + Lnew[int(n / 2)]) / 2.0)
    else:
        return Lnew[int(n / 2)]


print("12.3")
liczby = [6, 4, 2, 4, 4]
print(median(liczby, 0, len(liczby)))  # 4

liczby = [1, 1, 5, 6, 6, 8, 10]
print(median(liczby, 0, len(liczby)))  # 6

liczby = [1, 1, 5, 6, 6, 8, 10, 23, 45, 12, 17]
print(median(liczby, 0, 7))  # 6