#!/usr/bin/python3
# -*- coding: iso-8859-2 -*

# zad 14.4


class Graph:

    def __init__(self, g=None, n=10):
        if g is None:
            g = []
        self.g = g
        self.n = n

    def make_grid(self):
        # for i in range(self.n):
        #     self.g[i] = []
        #
        # print(self.g)
        for x in range(self.n):
            for y in range(int(self.n/2)):
                self.g.append([x, y])

        for i in self.g:
            self.neighbors(i)

    def neighbors(self, node):
        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        result = []
        for dir in dirs:
            neighbor = [node[0] + dir[0], node[1] + dir[1]]
            if neighbor in self.g:
                result.append(neighbor)

        print(result)
        return result

if __name__ == "__main__":
    graph = Graph()
    graph.make_grid()


## zadanie 4.3