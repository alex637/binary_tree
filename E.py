__author__ = 'student'


class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None
        self.left_height = 0
        self.right_height = 0


class Tree:
    def __init__(self):
        self.root = None
        self.height = 0

    def add(self, data):
        """
        Adds new node 'data' to the tree. Sets nodes' balance.
        :param data:
        :return: nothing
        """
        def upwards(child, parent):
            old_height = max(parent.left_height, parent.right_height)
            if parent.left == child:
                parent.left_height = max(child.left_height, child.right_height) + 1
            else:
                parent.right_height = max(child.left_height, child.right_height) + 1
            if max(parent.left_height, parent.right_height) > old_height and parent != self.root:
                upwards(parent, parent.parent)

        node = Node(data)
        if self.root is None:
            self.root = node
            return
        curr_node = self.root
        while True:
            if data < curr_node.data:
                if curr_node.left is None:
                    curr_node.left = node
                    curr_node.left.parent = curr_node
                    curr_node.left.left_height, curr_node.left.right_height = 0, 0
                    upwards(curr_node.left, curr_node)
                    return
                else:
                    curr_node = curr_node.left
            elif data == curr_node.data:
                return
            else:
                if curr_node.right is None:
                    curr_node.right = node
                    curr_node.right.parent = curr_node
                    curr_node.right.left_height, curr_node.right.right_height = 0, 0
                    upwards(curr_node.right, curr_node)
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
        print(node.data, node.left_height, node.right_height)
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

    def is_balanced(self):
        if self.root is None:
            return True
        q = [self.root]
        i = 0
        while i < len(q):
            if abs(q[i].left_height - q[i].right_height) > 1:
                return False
            if q[i].left:
                q.append(q[i].left)
            if q[i].right:
                q.append(q[i].right)
            i += 1
        else:
            return True


tree = Tree()
for x in list(map(int, input().strip().split())):
    tree.add(x)
if tree.is_balanced():
    print("YES")
else:
    print("NO")
