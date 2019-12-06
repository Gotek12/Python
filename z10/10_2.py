#!/usr/bin/python3
# -*- coding: iso-8859-2 -*


class Stack:

    def __init__(self, size=10):
        self.items = size * [None]  # utworzenie tablicy
        self.n = 0  # liczba elementów na stosie
        self.size = size

    def top(self):
        return self.items[self.n - 1]

    def is_empty(self):
        return self.n == 0

    def is_full(self):
        return self.size == self.n

    def push(self, data):
        if self.is_full():
            raise Exception("Stos pełny")
        self.items[self.n] = data
        self.n += 1
        return data

    def pop(self):
        if self.is_empty():
            raise Exception("Pusty stos")

        self.n -= 1
        data = self.items[self.n]
        self.items[self.n] = None  # usuwam referencję
        return data


print("10.2")
stos = Stack(4)
# stos.pop()
stos.push(1)
print(stos.top())
stos.push(1)
stos.push(1)
print(stos.top())
stos.push(2)
#stos.push(1)
