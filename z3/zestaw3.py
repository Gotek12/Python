#!/usr/bin/python3
# -*- coding: iso-8859-2 -*-
import sys

# 3.1
# a
x = 2;
y = 3;
if (x > y):
    result = x;
else:
    result = y;
# taki kod zadzia�a, ale wed�ug pep8 nale�y zastosowa� inne podej�cie
# r�wnie� dopuszcza nawiasy, ale dla tak kr�tkiego warunku s� one niepotrzebne
# �rednik�w te� nie trzeba stosowa�, ale je�li chcieliby�my zrobi� tak x = 2; y = 2 to nale�y je stosowa�, aby kod by� bardziej zrozumia�y

# b
# for i in "qwerty": if ord(i) < 100: print i
# nie zadzia�a na python3 ze wzgl�du na print bez nawias�w
# wiele blok�w kodu w jednej linijce jest niezgodne z pep8
# tak napisany kod powoduje, �e warunek if nie widzi zmiennej i

# c
# for i in "axby": print ord(i) if ord(i) < 100 else i
# dla pythona3 brak () w print a, sk�adniowo mo�na tak napisa� funkcj� ale jest mniej czytelna ni� rozbicie jej na wiele linii

# 3.2
# L = [3, 5, 4] ; L = L.sort()
# bia�y znak przed �rednikiem jest b��dem
# funkcja sort() sortuje el wewn�trz, a nie go zwraca wi�c zamiast L=L.sort() nale�y zrobi� L.sort()

# x, y = 1, 2, 3
# za du�o liczb po prawej stronie '=' lub za ma�o kontener�w na zmienne po lewej

# X = 1, 2, 3; X[1] = 4
# x = 1,2,3 konstrukcja tworzy krotk�(tuple) wi�c operacja x[1] jest niemo�liwa bo krotki si� nie zmienia

# X = [1, 2, 3] ; X[3] = 4
# w tym przypadku wychodzimy poza zakres gdy� zaczynamy iterowa� od 0, a nie od 1

# X = "abc"; X.append("d")
# string nie ma operacji append()

# map(pow, range(8))
# mapujemy na pow, kt�ry przyjmuje 2 argumenty
# je�li chcemy korzysta� z range nale�y go przekonwertowa� na list� list(range(8))
# ale zn�w b�dzie problem, gdy� b�dziemy mieli operacje int i lista

# 3.3
print("\n3.3")
for i in range(0, 31):
    if i % 3 != 0:
        print(i, end=' ')
# wynik: 1 2 4 5 7 8 10 11 13 14 16 17 19 20 22 23 25 26 28 29

# 3.4
print("\n3.4")
while 1:
    try:
        x = input("Wpisz liczbe: ")
        if x == "stop":
            break
        x = float(x)
    except ValueError as ex:
        print("To nie jest liczba -> ", ex)
        continue
    print(float(x), pow(float(x), 3))
# wynik np dla 6 -> 6.0 216.0
# wynik np aaa -> To nie jest liczba

# 3.5
q = int(input("Podaj dl miarki (int)> "))
miarka = ""
kropki = "..."
kreska = "|"
for i in range(0, q):
    miarka += (kreska + kropki)
    if i == q - 1:
        miarka += (kreska + "\n")

for i in range(0, q + 1):
    miarka += str(i)
    if i >= 99:
        miarka += " "
    elif i >= 9:
        miarka += "  "
    else:
        miarka += "   "
print(miarka)

# 3.6
print("\n3.6")
x = int(input("Podaj x "))
y = int(input("Podaj y "))
print("Generuje kratkownice ", x, "x", y)
kratkownica = ""
for i in range(0, x + 1):
    for j in range(0, y):
        kratkownica += "+---"
        if j == y - 1:
            kratkownica += "+"
    kratkownica += "\n"
    if i != x:
        for k in range(0, y):
            kratkownica += "|   "
            if k == y - 1:
                kratkownica += "|"
        kratkownica += "\n"
print(kratkownica)

# 3.8
print("\n3.8")
s1 = ['a', 'b', 'c', 'd']
s2 = ('b', 'd', 'e', 'f')
wynik = []

# znajdywanie tych samych el
for i in s1:
    if i in s2:
        wynik.append(i)

print("El wsp�lne dla 2 sekwencji", wynik)
# 2 sposob
print("El wsp�lne dla 2 sekwencji", list(set(s1) & set(s2)))
# wynik: ['b', 'd']

print("El wyst�puj�c w 2 sekwencjach ->", list(set(s1) | set(s2)))
# wynik: ['b', 'a', 'd', 'e', 'c', 'f']

# 3.9
print("\n3.9")
listaSek = [[], [4], (1, 2), [3, 4], (5, 6, 7)]
newL = []
for i in range(len(listaSek)):
    newL.append(sum(listaSek[i]))
print(newL)
# wynik: [0, 4, 3, 7, 18]

# 3.10
print("\n3.10")


def roman2int(roman):
    # 1 spos�b na s�ownik
    slowniczek = {
        "M": 1000,
        "D": 500,
        "C": 100,
        "L": 50,
        "X": 10,
        "V": 5,
        "I": 1
    }
    # 2 spos�b na s�ownik
    slowniczek2 = {}
    slowniczek2["M"] = 1000
    slowniczek2["D"] = 500
    slowniczek2["C"] = 100
    slowniczek2["L"] = 50
    slowniczek2["X"] = 10
    slowniczek2["V"] = 5
    slowniczek2["I"] = 1

    value = 0
    for i in range(len(roman)):
        if i > 0 and slowniczek[roman[i]] > slowniczek[roman[i - 1]]:
            value += slowniczek[roman[i]] - 2 * slowniczek[roman[i - 1]]
        else:
            value += slowniczek[roman[i]]
    return value

print("Przyk�adowe liczby")
print("MMMM -> ", roman2int('MMMM'))  # 4000
print("III -> ", roman2int('III'))  # 3
print("MD -> ", roman2int('MD'))  # 1500
print("DCC -> ", roman2int('DCC'))  # 700
print("XIV -> ", roman2int('XIV'))  # 14