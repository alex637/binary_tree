__author__ = 'student'


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def add(self, data):
        node = Node(data)
        if self.root is None:
            self.root = node
            return
        curr_node = self.root
        while True:
            if data < curr_node.data:
                if curr_node.left is None:
                    curr_node.left = node
                    return
                else:
                    curr_node = curr_node.left
            elif data == curr_node.data:
                return
            else:
                if curr_node.right is None:
                    curr_node.right = node
                    return
                else:
                    curr_node = curr_node.right

    def print(self, node=None):
        if node is None:
            if self.root is None:
                return
            else:
                node = self.root
        if node.left is not None:
            Tree.print(self, node.left)
        print(node.data, end=' ')
        if node.right is not None:
            Tree.print(self, node.right)

"""
tree = Tree()
for x in [7, 3, 2, 1, 9, 5, 4, 6, 8]:
    tree.add(x)
tree.print()  # напечатает 1 2 3 4 5 6 7 8 9
"""
