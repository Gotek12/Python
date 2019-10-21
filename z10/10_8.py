#!/usr/bin/python3
# -*- coding: iso-8859-2 -*
import random


class RandomQueue:
    def __init__(self, n = 10):
        self.data = n * [None]
        self.size = 0
        self.maxi = n

    def insert(self, data):
        if self.is_full():
            raise Exception("Kolejka jest pelna")

        self.data[self.size] = data
        self.size += 1

    def remove(self):
        if self.is_empty():
            raise Exception("Kolejka jest pusta")

        losuj = random.randint(0, self.size-1)

        tmp = self.data[losuj]
        self.data[losuj] = self.data[self.size - 1]
        self.data[self.size - 1] = tmp

        self.data.pop()

        self.size -= 1
        return tmp

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.maxi

    def __str__(self):
        return str(self.data)


queue = RandomQueue(5)
queue.insert(1)
queue.insert(2)
queue.insert(3)
queue.insert(4)
queue.insert(5)
#queue.insert(6)
print(queue)
print(queue.remove())
print(queue)
print(queue.remove())
print(queue)
print(queue.remove())
print(queue)
print(queue.remove())
print(queue)
print(queue.remove())
print(queue)
