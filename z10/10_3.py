#!/usr/bin/python3
# -*- coding: iso-8859-2 -*


class Stack:

    def __init__(self, size=10):
        self.items = size * [None]  # utworzenie tablicy
        self.n = 0  # liczba elementów na stosie
        self.size = size
        self.itemsTest = size * [0]

    def top(self):
        return self.items[self.n - 1]

    def is_empty(self):
        return self.n == 0

    def is_full(self):
        return self.size == self.n

    def push(self, data):
        if self.size >= data >= 1 and self.itemsTest[data - 1] == 0:
            self.itemsTest[data - 1] = 1
            self.items[self.n] = data
            self.n += 1

    def pop(self):
        if self.is_empty():
            print("Pusty stos")
        else:
            self.itemsTest[self.top() - 1] = 0
            data = self.items[self.n - 1]
            self.items[self.n - 1] = None  # usuwam referencję
            self.n -= 1
            return data


stos = Stack(5)
stos.push(1)
stos.push(1)
stos.push(5)
stos.push(4)
stos.push(3)
stos.push(3)
stos.push(2)
stos.pop()
stos.pop()
stos.pop()
stos.pop()
stos.pop()
print(stos.top())

stos.push(5)
print(stos.top())

stos.push(1)
print(stos.top())

stos.push(2)
print(stos.top())

stos.pop()
stos.pop()
stos.pop()
stos.pop()
print(stos.top())
