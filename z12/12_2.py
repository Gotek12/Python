#!/usr/bin/python3
# -*- coding: iso-8859-2 -*


def binarne_rek(L, left, right, y):
    """Wyszukiwanie binarne w wersji rekurencyjnej."""

    while left < right:

        dive = int((left + right) / 2)
        if y > L[dive]:
            return binarne_rek(L, dive + 1, right, y)
        elif y < L[dive]:
            return binarne_rek(L, left, dive - 1, y)
        else:
            return dive
    return -1  # brak takiej liczby w drzewie


print("12.2")
# test
liczby = [53, 107, 129, 174, 237, 238, 297, 338, 341, 353, 386, 387, 387, 460, 515, 566,580, 630, 653, 656, 659, 703,
          713, 714, 760, 768, 832, 839, 861, 883, 969, 970]

findPosistion = binarne_rek(liczby, 0, len(liczby), 53)  # 0
print(liczby[findPosistion], "jest na pozycji ", findPosistion)

print("********")
findPosistion = binarne_rek(liczby, 0, len(liczby), 970)  # 31
print(liczby[findPosistion], "jest na pozycji ", findPosistion)

print("********")
findPosistion = binarne_rek(liczby, 0, len(liczby), 387)  # 11
print(liczby[findPosistion], "jest na pozycji ", findPosistion)

print("********")
findPosistion = binarne_rek(liczby, 0, len(liczby), -12)  # -1
print(-12, "jest na pozycji ", findPosistion)

print("********")
findPosistion = binarne_rek(liczby, 0, len(liczby), 3870)  # -1
print(3870, "jest na pozycji ", findPosistion)
