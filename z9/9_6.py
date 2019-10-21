#!/usr/bin/python3
# -*- coding: iso-8859-2 -*


class Node:
    """Klasa reprezentująca węzeł drzewa binarnego."""

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

    def insert(self, node):
        if self.data < node.data:  # na prawo
            if self.right:
                self.right.insert(node)
            else:
                self.right = node
        elif self.data > node.data:  # na lewo
            if self.left:
                self.left.insert(node)
            else:
                self.left = node
        else:
            pass  # ignoruję duplikaty

    def count(self):
        counter = 1
        if self.left:
            counter += self.left.count()
        if self.right:
            counter += self.right.count()
        return counter


class BinaryTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def size(self):
        return self.size

    def isEmpty(self):
        return self.root is None

    def insert(self, value):
        if self.root:
            self.root.insert(Node(value))
        else:
            self.root = Node(value)

    def count_total(self, node):
        suma = node.data
        if node.left != None:
            suma += self.count_total(node.left)
        if node.right != None:
            suma += self.count_total(node.right)
        return suma

    def count_leafes(self, node):
        count = 0
        if node.left == None and node.right == None:
            count += 1
        if node.left != None:
            count += self.count_leafes(node.left)
        if node.right != None:
            count += self.count_leafes(node.right)

        return count


tree = BinaryTree()
tree.insert(1)
tree.insert(2)
tree.insert(3)
tree.insert(4)
tree.insert(5)
tree.insert(6)
tree.insert(7)
print(tree.count_total(tree.root))  # 28
print(tree.count_leafes(tree.root))  # 1

tree2 = BinaryTree()
tree2.insert(18)
tree2.insert(20)
tree2.insert(13)
tree2.insert(21)
print(tree2.count_total(tree2.root))  # 72
print(tree2.count_leafes(tree2.root))  # 2

tree3 = BinaryTree()
tree3.insert(30)
tree3.insert(15)
tree3.insert(40)
tree3.insert(7)
tree3.insert(20)
tree3.insert(45)

print(tree3.count_total(tree3.root))  # 157
print(tree3.count_leafes(tree3.root))  # 3
# https://www.cs.usfca.edu/~galles/visualization/BST.html
