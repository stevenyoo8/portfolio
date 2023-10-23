# Binary Tree inspection.py

import sys

# a queue class, tested and working


class Queue(object):
    def __init__(self):
        self.queue = []

    # add an item to the end of the queue
    def enqueue(self, item):
        self.queue.append(item)

    # remove an item from the beginning of the queue
    def dequeue(self):
        return self.queue.pop(0)

    # checks the item at the top of the Queue
    def peek(self):
        return self.queue[0]

    # check if the queue is empty
    def is_empty(self):
        return len(self.queue) == 0

    # return the size of the queue
    def size(self):
        return len(self.queue)


# Node class that defines items in the Tree
class Node(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


# The Binary Tree class
class BinaryTree(object):
    def __init__(self, int_list=None):
        self.root = None
        if int_list is not None:
            for num in int_list:
                self.insert(num)

    def insert(self, data):

        if self.root is None:
            self.root = Node(data)
            return
        else:
            queue = Queue()
            queue.enqueue(self.root)
            while not queue.is_empty():
                current = queue.dequeue()
                if not current.left:
                    current.left = Node(data)
                    return
                else:
                    queue.enqueue(current.left)
                if not current.right:
                    current.right = Node(data)
                    return
                else:
                    queue.enqueue(current.right)

    def getSpaces(self, num):
        spaces = ""
        for i in range(num):
            spaces += "    "
        return spaces

    # Print the tree
    def printTree(self):
        if (self.root is None):
            return
        else:
            self.printTreeHelper(self.root)

    def printTreeHelper(self, node, level=0):
        if node.right:
            self.printTreeHelper(node.right, level+1)
        print(self.getSpaces(level), node.data, "-----")
        if node.left:
            self.printTreeHelper(node.left, level+1)

    def is_BST(self):
        return (self.is_BST_helper(self.root))

    def is_BST_helper(self, current):

        left = right = True
        if current.left is not None:
            print("processing left:", current.left.data)
            if current.left.data > current.data:
                return False
            else:
                left = self.is_BST_helper(current.left)
        if left:
            if current.right is not None:
                print("processing right:", current.right.data)
                if current.right.data < current.data:
                    return False
                else:
                    right = self.is_BST_helper(current.right)

        return left and right


''' DRIVER CODE '''
# Don't change code below, except for the debug flag.

# Debug flag - set to False before submitting
debug = True
if debug:
    in_data = open('binary_tree.in')
else:
    in_data = sys.stdin

# input data from file
line = in_data.readline()
line = line.strip()
line = line.split()
tree_input = list(map(int, line)) 	# converts elements into ints

# create and build the tree
tree = BinaryTree(tree_input)

# if debug, print the tree
if debug:
    tree.printTree()

# Inspect the tree
print("This tree is a BST: ", tree.is_BST())


'''
    # Returns True if a binary tree is also a BST
    def is_BST(self):
        return self.is_BST_helper(self.root)

    def is_BST_helper(self, current):

        left = right = True
        if current.left is not None:
            print("processing:", current.left.data)
            if current.left.data > current.data:
                return False
            else:
                left = self.is_BST_helper(current.left)
        if current.right is not None:
            print("processing:,", current.right.data)
            if current.right.data < current.data:
                return False
            else:
                right = self.is_BST_helper(current.right)

        return left and right
'''
