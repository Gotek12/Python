#!/usr/bin/python3
# -*- coding: iso-8859-2 -*
# problem skoczka
import time

n = int(input("Podaj wielko�� szachownicy: "))
print("Ustawiono wielko�� szachownicy ", n, "x", n)
xS = int(input("Podaj po�o�enie x na szachownicy: "))
yS = int(input("Podaj po�o�enie y na szachownicy: "))
print("Badamy problem skoczka zaczynaj�cego od po�o�enia ", xS, "x", yS)


# sprawdza czy koordynaty s� mo�liwe
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

    # lista mo�liwych ruch�wc dla skoczka
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

    # je�li dojdziemy do ko�ca planszy
    if step == n**2:
        return True

    # p�tla badaj�ca ka�dy mo�liwy ruch (8 mo�liwych)
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
print("Czy istnieje rozwi�zanie: ", findSolutions())
end_time = time.time() - start_time
print("Czas oblicze� to: ", end_time, "s")
# np 8x8 pozycja 0x0 ok
# 5x5 pozycja 2x2 ok
# 6x6 pozycja 2x2 ok
# 10x10 pozycja 0x0 ok