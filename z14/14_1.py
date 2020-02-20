#!/usr/bin/python3
# -*- coding: iso-8859-2 -*

# zad 14.1
# Przykładowy graf na liście sąsiedztwa / graph using Adjacency List


class Graph:

    # ustawiamy pusty graf / empty graph
    def __init__(self, g=None):
        if g is None:
            g = {}
        self.g = g

    # list of vertices
    def list_nodes(self):
        return list(self.g.keys())

    # list o edges
    def list_edges(self):
        return self.link_edges()

    def count_nodes(self):
        return len(self.list_nodes())

    def count_edges(self):
        return len(self.list_edges())

    # function creating edges
    def link_edges(self):
        edges = []
        for i in self.g:  # vertex
            for j in self.g[i]:  # neighbours
                if {i, j} not in edges:
                    edges.append({i, j})
        return edges

    # add new edge
    def add_edge(self, newEdge):
        (v1, v2) = tuple(set(newEdge))
        if v1 in self.g:
            self.g[v1].append(v2)
        else:
            self.g[v1] = [v2]

    # add new vertex
    def add_vertex(self, newVertex):
        if newVertex not in self.g:
            self.g[newVertex] = []

    def print_edges(self):
        result = "Edges: "
        for i in self.link_edges():
            result = result + str(i) + " "
        return result

    def print_vertex(self):
        result = "Vertex: "
        for i in self.g:
            result = result + str(i) + " "
        return result


if __name__ == "__main__":
    g = {"A": ["B", "C"], "B": ["C", "D"], "C": ["D"], "D": ["C"], "E": ["C"], "F": []}
    graph = Graph(g)
    print(graph.print_edges())
    print(graph.print_vertex())
    print("\n")

    print("Edges: ", graph.list_edges())
    print("Nodes: ",graph.list_nodes())
    print("Count edges: ", graph.count_edges())
    print("Count nodes: ", graph.count_nodes())
    print("\n")

    graph.add_vertex("G")
    graph.add_edge({"A", "G"})
    graph.add_edge({"B", "G"})
    print("Edges: ", graph.list_edges())
    print("Nodes: ",graph.list_nodes())
    print("Count edges: ", graph.count_edges())
    print("Count nodes: ", graph.count_nodes())