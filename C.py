__author__ = 'student'


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        # self.count = 1
        self.height = None


class Tree:
    def __init__(self):
        self.root = None
        self.height = 0

    def add(self, data):
        """
        Adds new node 'data' to the tree. Sets new tree.height
        :param data:
        :return: nothing
        """
        node = Node(data)
        if self.root is None:
            self.root = node
            self.root.height = 1
            self.height = 1
            return
        curr_node = self.root
        while True:
            if data < curr_node.data:
                if curr_node.left is None:
                    curr_node.left = node
                    curr_node.left.height = curr_node.height + 1
                    if curr_node.left.height > self.height:
                        self.height = curr_node.left.height
                    return
                else:
                    curr_node = curr_node.left
            elif data == curr_node.data:
                # curr_node.count += 1
                return
            else:
                if curr_node.right is None:
                    curr_node.right = node
                    curr_node.right.height = curr_node.height + 1
                    if curr_node.right.height > self.height:
                        self.height = curr_node.right.height
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
        # for i in range(node.count):
        #     print(node.data, end=' ')
        if node.right is not None:
            Tree.print(self, node.right)

    def find_leaves(self, node=None):
        if node is None:
            if self.root is None:
                return
            else:
                node = self.root
        if node.left is None and node.right is None:
            return [node.data]
        leaves = []
        if node.left:
            leaves += self.find_leaves(node.left)
        if node.right:
            leaves += self.find_leaves(node.right)
        return leaves


tree = Tree()
for x in list(map(int, input().strip().split())):
    tree.add(x)
print(tree.height)
