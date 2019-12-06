#!/usr/bin/python3
# -*- coding: iso-8859-2 -*


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def setRoot(self, data):
        self.root = Node(data)

    def insert(self, data):
        if self.root is None:
            self.setRoot(data)
        else:
            self.insertNode(self.root, data)

    def insertNode(self, currentNode, data):
        if data <= currentNode.data:
            if currentNode.left:
                self.insertNode(currentNode.left, data)
            else:
                currentNode.left = Node(data)
        elif data > currentNode.data:
            if currentNode.right:
                self.insertNode(currentNode.right, data)
            else:
                currentNode.right = Node(data)

    def bst_max(self, top):
        current = top
        while current.right is not None:
            current = current.right

        return current.data

    def bst_min(self, top):
        current = top
        while current.left is not None:
            current = current.left

        return current.data


print("9.7")

bst = BST()
bst.insert(2)
bst.insert(1)
bst.insert(3)
bst.insert(6)
bst.insert(7)

print("Max value w bst -> ", bst.bst_max(bst.root))  # 7
print("Min value w bst -> ", bst.bst_min(bst.root))  # 1

bst2 = BST()
bst2.insert(20)
bst2.insert(8)
bst2.insert(22)
bst2.insert(4)
bst2.insert(12)
bst2.insert(10)
bst2.insert(14)

print("Max value w bst -> ", bst2.bst_max(bst2.root))  # 22
print("Min value w bst -> ", bst2.bst_min(bst2.root))  # 4
