#!/usr/bin/python3
# -*- coding: iso-8859-2 -*

# zad 14.6


class Graph:

    def __init__(self, g=None):
        if g is None:
            g = []

        self.g = g
        self.dictionary = {}

    def create_dictionary(self):
        tmp = []
        for i in range(len(self.g)):
            for j in range(len(self.g[i])):
                if self.g[i][j] == 1:
                    tmp.append(j)
            self.dictionary[i] = tmp
            tmp = []
        return self.dictionary


g = [[1, 0, 0, 1],
    [0, 1, 1, 1],
    [0, 1, 1, 0],
    [1, 0, 0, 1]]

new_gr = Graph(g)
dic = new_gr.create_dictionary()

print(g)
print(dic)