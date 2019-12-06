#!/usr/bin/python3
# -*- coding: iso-8859-2 -*
# problem skoczka
import time

n = int(input("Podaj wielkość szachownicy: "))
print("Ustawiono wielkość szachownicy ", n, "x", n)
xS = int(input("Podaj położenie x na szachownicy: "))
yS = int(input("Podaj położenie y na szachownicy: "))
print("Badamy problem skoczka zaczynającego od położenia ", xS, "x", yS)


# sprawdza czy koordynaty są możliwe
def isValid(x, y, chessboard):
    if 0 <= x < n and 0 <= y < n and chessboard[x][y] == -1:
        return True
    return False


def findSolutions():
    global n, xS, yS
    # generowanie pustej planszy
    chessboard = [[-1 for i in range(n)] for j in range(n)]

    # test poczatkowej pozycji
    if not (0 <= xS < n and 0 <= yS < n):
        raise ValueError("Niepoprawne koordynanty")

    # for r in chessboard:
    #    print(r)

    # lista możliwych ruchówc dla skoczka
    xPoz = [2, 1, -1, -2, -2, -1, 1, 2]
    yPoz = [1, 2, 2, 1, -1, -2, -2, -1]
    chessboard[xS][yS] = 0  # pozycja startowa
    step = 1

    if not find(chessboard, xS, yS, xPoz, yPoz, step):
        return False
    else:
        return True


def find(chessboard, x, y, xPoz, yPoz, step):
    global n

    # jeśli dojdziemy do końca planszy
    if step == n**2:
        return True

    # pętla badająca każdy możliwy ruch (8 możliwych)
    for i in range(8):
        xNew = x + xPoz[i]
        yNew = y + yPoz[i]

        if isValid(xNew, yNew, chessboard):
            chessboard[xNew][yNew] = step
            if find(chessboard, xNew, yNew, xPoz, yPoz, step + 1):
                return True

            chessboard[xNew][yNew] = -1
    return False


start_time = time.time()
print("Czy istnieje rozwiązanie: ", findSolutions())
end_time = time.time() - start_time
print("Czas obliczeń to: ", end_time, "s")
# np 8x8 pozycja 0x0 ok
# 5x5 pozycja 2x2 ok
# 6x6 pozycja 2x2 ok
# 10x10 pozycja 0x0 ok