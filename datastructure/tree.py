import random


class Node(object):
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left_child = None
        self.right_child = None

class BinaryTree(object):
    def __init__(self):
        self.root = None

    def insert_as_left_child(self, parent, data):
        node = Node(data)
        parent.left_child = node
        return node

    def insert_as_right_child(self, parent, data):
        node = Node(data)
        parent.right_child = node
        return node

    def insert_as_root(self, data):
        node = Node(data)
        self.root = node

    def breadth_first_trans(self, func):
        node = self.root
        current_siblings = [node] # current level
        next_siblings = [] # next level
        while True:
            if len(current_siblings) == 0 and len(next_siblings) == 0:
                break
            if len(current_siblings) == 0:
                current_siblings = next_siblings[:]
                next_siblings = []
                print # new line
            node = current_siblings.pop(0)
            func(node)
            if node.left_child:
                next_siblings.append(node.left_child)
            if node.right_child:
                next_siblings.append(node.right_child)

    def _print_func(self, x):
        print x.data,

    def print_tree(self):
        self.breadth_first_trans(self._print_func)

    def _preorder(self, node, func):
        if node is None:
            return
        func(node)
        self._preorder(node.left_child, func)
        self._preorder(node.right_child, func)

    def preorder_trans(self, func):
        self._preorder(self.root, func)

    def _inorder(self, node, func):
        if node is None:
            return
        self._inorder(node.left_child, func)
        func(node)
        self._inorder(node.right_child, func)

    def inorder_trans(self, func):
        self._inorder(self.root, func)

    def _postorder(self, node, func):
        if node is None:
            return
        self._postorder(node.left_child, func)
        self._postorder(node.right_child, func)
        func(node)

    def postorder_trans(self, func):
        self._postorder(self.root, func)
        
        
if __name__ == "__main__":
    #nodes = random.sample(range(100), 21)
    # use a fixed array to ease the analysis
    nodes = [32, 66, 94, 97, 50, 18, 70, 12, 7, 81, 20, 24, 9, 10, 84, 15, 56, 51, 86, 33, 75]
    print nodes
    tree = BinaryTree()
    root = nodes.pop(0)
    tree.insert_as_root(root)
    nodes = [[nodes[i], nodes[i+1]] for i in range(0, len(nodes)-1, 2)]

    parents = [tree.root]

    for node in nodes:
        parent = parents.pop(0)
        parents.append(tree.insert_as_left_child(parent, node[0]))
        parents.append(tree.insert_as_right_child(parent, node[1]))
    print "depth first traverse: "
    tree.print_tree()
    
    print "\n\nPreorder traverse:"
    tree.preorder_trans(tree._print_func)

    print "\n\nInorder traverse:"
    tree.inorder_trans(tree._print_func)

    print "\n\nPostorder traverse:"
    tree.postorder_trans(tree._print_func)
