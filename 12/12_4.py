#!/usr/bin/python3
# -*- coding: iso-8859-2 -*


def moda_sort(L, left, right):
    Lnew = L[left:right + 1]
    Lnew.sort()

    items = {}
    for i in Lnew:
        items.setdefault(i, 0)
        items[i] += 1

    maxi = max([i for i in items.values()])
    counter = 0
    d = []
    for i, j in items.items():
        if j == maxi:
            counter += 1
            d.append(i)

    if counter == len(items):
        print("Brak dominanty")
    else:
        print(d)


print("12.4")
liczby = [1, 2, 3, 3, 4, 4, 4, 5, 5, 6, 5]
moda_sort(liczby, 0, len(liczby))  # 4, 5

print("**********")
liczby = [1, 2, 3, 3, 5, 5, 6, 7, 8, 3]
moda_sort(liczby, 0, len(liczby))  # 3

print("**********")
liczby = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
moda_sort(liczby, 0, len(liczby))  # brak mody
