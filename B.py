__author__ = 'student'


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.count = 1


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
                curr_node.count += 1
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
        for i in range(node.count):
            print(node.data, end=' ')
        if node.right is not None:
            Tree.print(self, node.right)

tree = Tree()
for x in list(map(int, input().strip().split())):
    tree.add(x)
tree.print()
