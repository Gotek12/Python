#!/usr/bin/python3
# -*- coding: iso-8859-2 -*


class Node:
    """Klasa reprezentująca węzeł listy jednokierunkowej."""

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)   # bardzo ogólnie


class SingleList:
    """Klasa reprezentująca całą listę jednokierunkową."""

    def __init__(self):
        self.length = 0         # nie trzeba obliczać za każdym razem
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.length == 0

    def count(self):      # tworzymy interfejs do odczytu
        return self.length

    def insert_head(self, node):
        if self.length == 0:
            self.head = self.tail = node
        else:                   # dajemy na koniec listy
            node.next = self.head
            self.head = node
        self.length += 1

    def insert_tail(self, node):   # klasy O(N)
        if self.length == 0:
            self.head = self.tail = node
        else:                   # dajemy na koniec listy
            self.tail.next = node
            self.tail = node
        self.length += 1

    def remove_head(self):          # klasy O(1)
        if self.length == 0:
            raise ValueError("pusta lista")

        node = self.head
        self.head = self.head.next
        node.next = None   # czyszczenie łącza
        self.length -= 1
        if self.length == 0:   # zabezpieczenie
            self.tail = None
        return node   # zwracamy usuwany node

    def remove_tail(self):
        if self.length == 0:
            raise ValueError("pusta lista")

        node = self.head
        while node.next is not None:
            prev = node
            node = node.next
        if self.length != 1:
            prev.next = None

        self.length -= 1
        return node

    def print_list(self):
        if self.length == 0:
            print("[ ]")
        else:
            node = self.head
            while node.next is not None:
                print(node.data, end = ' ')
                node = node.next
            print(node.data, end =' ')

    def merge(self, other):
        pass  # klasy O(1)

    # Węzły z listy other są przepinane do listy self na jej koniec.

    def clear(self):
        self.length = 0
        self.head = None
        self.tail = None


alist = SingleList()
alist.insert_head(Node(11))         # [11]
alist.insert_head(Node(22))         # [22, 11]
alist.insert_tail(Node(33))         # [22, 11, 33]
print("length", alist.length)  # odczyt atrybutu
print("length", alist.count()) # wykorzystujemy interfejs
print("remove tail", alist.remove_tail())
print("length", alist.count())
while not alist.is_empty():   # kolejność 22, 11
    print("remove head", alist.remove_head())

alist.print_list()
alist.insert_head(Node(12))  # 12
alist.insert_head(Node(1))  # 1, 12
alist.insert_tail(Node(102))  # 1, 12, 102
alist.insert_tail(Node(8))  # 1, 12, 102, 8
print("length", alist.count())
alist.print_list()
alist.clear()
print()
alist.print_list()
print("length", alist.count())

alist.insert_head(Node(12))  # 12
alist.insert_head(Node(1))  # 1, 12
alist.insert_tail(Node(102))  # 1, 12, 102
alist.insert_tail(Node(8))  # 1, 12, 102, 8
print("length", alist.count())
alist.print_list()
print("\n")
alist.remove_tail()  # 1, 12, 102
alist.print_list()
print("\n")
alist.remove_head()  # 12, 102
alist.print_list()
print("\n")
alist.remove_tail()  # 12
alist.print_list()

print("\n")
alist.remove_tail()
alist.print_list()

alist.insert_tail(Node(123))
alist.insert_head(Node(1231))
print("\n")
print("length", alist.count())
alist.print_list()

