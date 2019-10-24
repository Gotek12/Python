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
# taki kod zadziała, ale według pep8 należy zastosować inne podejście
# również dopuszcza nawiasy, ale dla tak krótkiego warunku są one niepotrzebne
# średników też nie trzeba stosować, ale jeśli chcielibyśmy zrobić tak x = 2; y = 2 to należy je stosować, aby kod był bardziej zrozumiały

# b
# for i in "qwerty": if ord(i) < 100: print i
# nie zadziała na python3 ze względu na print bez nawiasów
# wiele bloków kodu w jednej linijce jest niezgodne z pep8
# tak napisany kod powoduje, że warunek if nie widzi zmiennej i

# c
# for i in "axby": print ord(i) if ord(i) < 100 else i
# dla pythona3 brak () w print a, składniowo można tak napisać funkcję ale jest mniej czytelna niż rozbicie jej na wiele linii

# 3.2
# L = [3, 5, 4] ; L = L.sort()
# biały znak przed średnikiem jest błędem
# funkcja sort() sortuje el wewnątrz, a nie go zwraca więc zamiast L=L.sort() należy zrobić L.sort()

# x, y = 1, 2, 3
# za dużo liczb po prawej stronie '=' lub za mało kontenerów na zmienne po lewej

# X = 1, 2, 3; X[1] = 4
# x = 1,2,3 konstrukcja tworzy krotkę(tuple) więc operacja x[1] jest niemożliwa bo krotki się nie zmienia

# X = [1, 2, 3] ; X[3] = 4
# w tym przypadku wychodzimy poza zakres gdyż zaczynamy iterować od 0, a nie od 1

# X = "abc"; X.append("d")
# string nie ma operacji append()

# map(pow, range(8))
# mapujemy na pow, który przyjmuje 2 argumenty
# jeśli chcemy korzystać z range należy go przekonwertować na listę list(range(8))
# ale znów będzie problem, gdyż będziemy mieli operacje int i lista

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

print("El wspólne dla 2 sekwencji", wynik)
# 2 sposob
print("El wspólne dla 2 sekwencji", list(set(s1) & set(s2)))
# wynik: ['b', 'd']

print("El występując w 2 sekwencjach ->", list(set(s1) | set(s2)))
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
    # 1 sposób na słownik
    slowniczek = {
        "M": 1000,
        "D": 500,
        "C": 100,
        "L": 50,
        "X": 10,
        "V": 5,
        "I": 1
    }
    # 2 sposób na słownik
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

print("Przykładowe liczby")
print("MMMM -> ", roman2int('MMMM'))  # 4000
print("III -> ", roman2int('III'))  # 3
print("MD -> ", roman2int('MD'))  # 1500
print("DCC -> ", roman2int('DCC'))  # 700
print("XIV -> ", roman2int('XIV'))  # 14