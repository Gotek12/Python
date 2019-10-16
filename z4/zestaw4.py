#!/usr/bin/python3
# -*- coding: iso-8859-2 -*-

# 4.2
def fmiarka():
    q = int(input("Podaj dl miarki (int)> "))
    miarka = ""
    kropki = "..."
    kreska = "|"
    for i in range(0, q):
        miarka += kreska + kropki
        if i == q-1:
            miarka += kreska + "\n"

    for i in range(0, q+1):
        miarka += str(i)
        if i >= 99:
            miarka += " "
        elif i >= 9:
            miarka += "  "
        else:
            miarka += "   "
    return miarka


def fkratownica():
    x = int(input("Podaj x "))
    y = int(input("Podaj y "))
    print("Generuje kratkownice ", x, "x", y)
    kratkownica = ""
    for i in range(0, x+1):
        for j in range(0, y):
            kratkownica += "+---"
            if j == y-1:
                kratkownica += "+"
        kratkownica += "\n"
        if i != x:
            for k in range(0, y):
                kratkownica += "|   "
                if k == y-1:
                    kratkownica += "|"
            kratkownica += "\n"
    return kratkownica


print("4.2")
print(fmiarka())
print(fkratownica())

# 4.3
print("\n4.3")
def factorial(n):
    value = 1;
    for i in range(1, n+1):
        value *= i;
    return value


print("6! ->", factorial(6))  # 720
print("12! ->", factorial(12))  # 479001600
# wynik: 6 -> 720, 12 -> 479001600

# 4.4
print("\n4.4")
def fibo(n):
    x, y = 0, 1
    for i in range(0, n):
        x, y = y, x + y
    return x


print(fibo(6)) #8
print(fibo(14)) #377
# wynik: 6 -> 8, 14 -> 377

# 4.5
print("\n4.5")
L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l = 1
r = 4

print("Odwracanie iteracyjnie: ")
def odwracanie(L, l, r):
    for i in range(int((l+r)/2)):
        a = L[l]
        L[l] = L[r]
        L[r] = a
        r = r - 1
        l = l + 1
    return L


print(odwracanie(L, l, r))
L2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


print("Odwracanie rekurencyjnie: ")
def odwracanieR(L2, l, r):
    if l >= r:
        return
    L2[l], L2[r] = L2[r], L2[l]
    odwracanieR(L2, l+1, r-1)


odwracanieR(L2, l, r)
print(L2)
# wynik: [1, 5, 4, 3, 2, 6, 7, 8, 9, 10]

# 4.6
print("\n4.6")
sequence = [ [[23], [1,4,5,6]], [4], [1,2], [3,4], [5,(6,7)]]  # 71


def sum_seq(sequence):
    suma = 0
    for i in sequence:
        # sprawdzamy czy istnieje zagnieżdżenie
        if isinstance(i, (list, tuple)):
            suma += sum_seq(i)
        else:
            suma += i
    return suma


print(sum_seq(sequence))
# wynik: 71

# 4.7
print("\n4.7")
seq = [1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]


def flatten(seq):
    suma = []
    for i in seq:
        if isinstance(i, (list, tuple)):
            suma.extend(flatten(i))  # dodaj kontent do istniejącej listy
            # print(suma)
        else:
            suma.append(i)
    return suma


print(flatten(seq))
# wynik: [1, 2, 3, 4, 5, 6, 7, 8, 9]