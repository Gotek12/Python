#!/usr/bin/python3
# -*- coding: iso-8859-2 -*
import random
import math
import heapq


# (a) różne liczby int od 0 do N-1 w kolejności losowej,
def randNum(n, r = 100):
    num = []
    for i in range(n):
        num.append(random.randint(0, r))
    return num


# (b) różne liczby int od 0 do N-1 prawie posortowane (liczby są blisko swojej prawidłowej pozycji),
#k - kazdy el jest oddalony o k od siebie
def randNumNearly(n, r, k):
    num = randNum(n, r)
    h = num[:k + 1]  # lista pierwszych k+1 elementow
    heapq.heapify(h)

    iMin = 0
    for i in range(k + 1, n):
        num[iMin] = heapq.heappop(h)
        heapq.heappush(h, num[i])
        iMin += 1
    while h:
        num[iMin] = heapq.heappop(h)
        iMin += 1
    return num


# (c) różne liczby int od 0 do N-1 prawie posortowane w odwrotnej kolejności,
def randNumNearlyRevers(n, r, k):
    num = randNumNearly(n, r, k)
    num.reverse()
    return num


# (d) N liczb float w kolejności losowej o rozkładzie gaussowskim,
def gaussianNum(size, sigma = 1, mu = 0):
    num = []
    for i in range(size):
        num.append(random.gauss(mu, sigma))
    return num


# (e) N liczb int w kolejności losowej, o wartościach powtarzających się, należących do zbioru k elementowego (k < N, np. k*k = N).
def randNumRepeat(n):
    num = randNum(n, math.sqrt(n))
    return num
