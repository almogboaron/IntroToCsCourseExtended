from printree import *  # for Binary_search_tree's __repr__


class Tree_node():
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return "(" + str(self.key) + ":" + str(self.val) + ")"


class Binary_search_tree():

    def __init__(self):
        self.root = None

    def __repr__(self):  # no need to understand the implementation of this one
        out = ""
        for row in printree(self.root):  # need printree.py file
            out = out + row + "\n"
        return out

    def lookup(self, key):
        ''' return node with key, uses recursion '''

        def lookup_rec(node, key):
            if node == None:
                return None
            elif key == node.key:
                return node
            elif key < node.key:
                return lookup_rec(node.left, key)
            else:
                return lookup_rec(node.right, key)

        return lookup_rec(self.root, key)

    def insert(self, key, val):
        ''' insert node with key,val into tree, uses recursion '''

        def insert_rec(node, key, val):
            if key == node.key:
                node.val = val  # update the val for this key
            elif key < node.key:
                if node.left == None:
                    node.left = Tree_node(key, val)
                else:
                    insert_rec(node.left, key, val)
            else:  # key > node.key:
                if node.right == None:
                    node.right = Tree_node(key, val)
                else:
                    insert_rec(node.right, key, val)
            return

        if self.root == None:  # empty tree
            self.root = Tree_node(key, val)
        else:
            insert_rec(self.root, key, val)

    def minimum(self):
        ''' return node with minimal key '''
        if self.root == None:
            return None
        node = self.root
        left = node.left
        while left != None:
            node = left
            left = node.left
        return node

    def depth(self):
        ''' return depth of tree, uses recursion'''

        def depth_rec(node):
            if node == None:
                return -1
            else:
                return 1 + max(depth_rec(node.left), depth_rec(node.right))

        return depth_rec(self.root)

    def size(self):
        ''' return number of nodes in tree, uses recursion '''

        def size_rec(node):
            if node == None:
                return 0
            else:
                return 1 + size_rec(node.left) + size_rec(node.right)

        return size_rec(self.root)


def test():
    bin_tree = Binary_search_tree()
    print("MIN ", bin_tree.minimum())
    print("DEPTH ", bin_tree.depth())
    print("SIZE ", bin_tree.size())
    print(bin_tree)
    bin_tree.insert(2, "a")
    print(bin_tree)
    bin_tree.insert(4, "b")
    print(bin_tree.lookup(4))
    print(bin_tree)
    bin_tree.insert(2, "c")
    print(bin_tree)
    bin_tree.insert(3, "d")
    print(bin_tree)
    bin_tree.insert(1, "e")
    print(bin_tree)
    bin_tree.insert(0, "f")
    bin_tree.insert(5, "g")
    bin_tree.insert(7, "h")
    bin_tree.insert(6, "i")
    print(bin_tree)
    print(bin_tree.lookup(1))
    print(bin_tree.lookup(2))
    print(bin_tree.lookup(9))
    print("MIN ", bin_tree.minimum())
    print("DEPTH ", bin_tree.depth())
    print("SIZE ", bin_tree.size())




