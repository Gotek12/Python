#!/usr/bin/python3
# -*- coding: iso-8859-2 -*-

'''
Problem takiego r�wnania jest taki, �e mo�emy z niego uzyska� warto�� elementu x, y, ale r�wnie� brak rozwi�zania lub wz�r na prost�.
Wszystko zale�y od tego jaki elementy a, b, c si� zeruje.
Wszystkie warunki znajduj� si� w poni�szej implementacji
'''

def solve1(a, b, c):
    """Rozwi�zywanie r�wnania liniowego a x + b y + c = 0."""
    if a == 0 and b == 0 and c == 0:
        print("a == 0 i b == 0 i c == 0 -> 0 = 0")

    elif c == 0:
        if a == 0:
            print("a == 0 i b != 0 i c == 0 -> y = 0")
        elif b == 0:
            print("a != 0 i b == 0 i c == 0 -> x = 0")
        elif a != 0 and b != 0:
            print("a != 0 i b != 0 i c == 0 -> mamy prost� y =", -a/b, "x")

    elif c != 0:
        if a != 0 and b != 0:
            p1 = -c/b
            p2 = -c/a
            print("a != 0 i b != 0 i c != 0 -> prosta przecinaj�ca si� w punktach ( 0,", p1,") i (", p2, ",0 ) co daje prost� y =", p1/-p2,"x +",p1)

        if a == 0 and b == 0:
            print("a == 0 i c == 0 -> 0 =", c, " brak rozwi�zania")
        elif a == 0:
            y = -c/b
            print("c != 0 i a == 0 -> y =", y)
        elif b == 0:
            x = -c/a
            print("c != 0 i b == 0 -> x =", x)

print("Mamy r�wnanie liniowe w postaci: a * x + b * y + c = 0")
# a = input("Podaj a > ")
# b = input("Podaj b > ")
# c = input("Podaj c > ")
# solve1(a, b, c)

# a == 0 i b == 0 i c == 0
solve1(0, 0, 0)
# a == 0 i c == 0
solve1(0, 0, 12)
# c != 0 i a == 0
solve1(0, 1, 2)
# c != 0 i b == 0
solve1(1, 0, 2)
# a != 0 i b != 0 i c != 0
solve1(1, 2, 3)
# a != 0 i b != 0 i c == 0
solve1(1, 2, 0)
# a == 0 i b != 0 i c == 0
solve1(0, 2, 0)
# a != 0 i b == 0 i c == 0
solve1(2, 0, 0)