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


# The Binary Search Tree class
class BST(object):
    def __init__(self, int_list=None):
        self.root = None
        if int_list is not None:
            for num in int_list:
                self.insert(num)

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.insert_helper(self.root, data)

    def insert_helper(self, node, data):
        # Compare the new value with the parent node
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self.insert_helper(node.left, data)
        elif data > node.data:
            if node.right is None:
                node.right = Node(data)
            else:
                self.insert_helper(node.right, data)

    def getSpaces(self, num):
        spaces = ""
        for i in range(num):
            spaces += "    "
        return spaces

    # Print the tree
    # def printTree(self):
    #     if (self.root is None):
    #         return
    #     else:
    #         self.printTreeHelper(self.root)

    # def printTreeHelper(self, node, level=0):
    #     if node.right:
    #         self.printTreeHelper(node.right, level+1)
    #     print(self.getSpaces(level), node.data, "-----")
    #     if node.left:
    #         self.printTreeHelper(node.left, level+1)

    # Returns True if two BSTs are similar
    def is_similar(self, compTree):
        return self.is_similar_helper(self.root, compTree.root)

    def is_similar_helper(self, tree1_node, tree2_node):
        if tree1_node is None and tree2_node is None: # base: traversed entire tree with no differences
            return True
        if tree1_node is None or tree2_node is None: # base: one node is none, the other is not none. Differs
            return False

        return (tree1_node.data == tree2_node.data and self.is_similar_helper(tree1_node.left, tree2_node.left) and self.is_similar_helper(tree1_node.right, tree2_node.right))

    # Returns True if a BST is a complete tree
    def is_complete(self):
        if self.root is None: # empty tree is complete
            return True

        queue = Queue()
        queue.enqueue(self.root)
        found_empty_node = False

        while not queue.is_empty():
            current_node = queue.dequeue()

            if current_node is not None:
                if found_empty_node: # if a node is missing, incomplete tree
                    return False

                queue.enqueue(current_node.left)
                queue.enqueue(current_node.right)
            else: # current_node is None
                found_empty_node = True

        return True


''' DRIVER CODE '''
# Don't change code below, except for the debug flag.

# Debug flag - set to False before submitting
debug = False
if debug:
    in_data = open('bst_util.in')
else:
    in_data = sys.stdin

# read number of trees
numTrees = int(in_data.readline())
trees = []

# build list of trees
for i in range(numTrees):
    line = in_data.readline()
    line = line.strip()
    line = line.split()
    tree_input = list(map(int, line)) 	# converts elements into ints
    trees.append(BST(tree_input))
    # if debug:
    #     trees[i].printTree()

# run utility methods
num_similar = 0
num_complete = 0
for i in range(numTrees):
    for j in range(i + 1, numTrees):
        if (i != j and trees[i].is_similar(trees[j])):
            num_similar += 1
    if (trees[i].is_complete()):
        num_complete += 1

print(num_similar)
print(num_complete)
