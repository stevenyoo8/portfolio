#  File: ExpressionTree.py
#  Student Name: Jongho Yoo
#  Student UT EID: jy23294

# Description: Utilize binary tree to evaluate the expression
# Date: July 08, 2023


import sys

# list of valid operators
operators = ['+', '-', '*', '/', '//', '%', '**']


# Input: Elements of a simple expression
#        operator (String) and two operands (numbers)
# Output: result of evaluation of the expression
def operation(operator, n, m):
    expression = str(n) + operator + str(m)
    return eval(expression)


# Traditional Stack implementation containing list of data items
# Used to keep track of items in nested expressions.
class Stack (object):
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if (not self.is_empty()):
            return self.stack.pop()
        else:
            return None

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return self.size() == 0


# Node Class
# Purpose: Used by the Tree Class to represent one operand or operators
#          in a binary expression. It includes data (a character) and
#          two pointers, to the left and right child nodes.
class Node(object):
    def __init__(self, data = None, lChild = None, rChild = None):
        self.data = data
        self.lChild = lChild
        self.rChild = rChild


# Tree Class
# Purpose: To represent the string representation of operators and operands
#          of a binary expression so it can be evaluated.
class Tree (object):
    def __init__(self):
        self.root = Node(None)

    # Input: a string expression
    # Output: an expression tree
    def create_tree(self, expr):
        stack = Stack()
        current = self.root

        for token in expr.split():
            if token == '(':
                current.lChild = Node(None)
                stack.push(current)
                current = current.lChild
            elif token in operators:
                current.data = token
                stack.push(current)
                current.rChild = Node(None)
                current = current.rChild
            elif token == ')':
                if not stack.is_empty():
                    current = stack.pop()
            else: # if number
                if token is not None:
                    current.data = token
                    current = stack.pop()


    # Input: A node in an expression tree
    # Output: The result of evaluating the expression
    #         with this node as the root
    def evaluate(self, current):        
        if current.data in operators:
            return operation(current.data, self.evaluate(current.lChild), self.evaluate(current.rChild))
        elif current is None:
            return 0
        else:
            return float(current.data)
        

    # Starter Method for pre_order
    # Input: a node in an expression tree
    # Output: (string) the preorder notation of the expression
    #                  with this node a the root
    def pre_order(self, current):
        if current is None:
            return ""
        
        return (str(current.data) + " " +  self.pre_order(current.lChild) + self.pre_order(current.rChild))

    # Starter Method for post_order
    # Input: a node in an expression tree
    # Output: (string) the post order notation of the expression
    #                  with this node a the root
    def post_order(self, current):
        if current is None:
            return ""
        
        return (self.post_order(current.lChild) + self.post_order(current.rChild) + str(current.data) + " ")



''' ##### DRIVER CODE ##### '''

def main():

    debug = True
    if debug:
        in_data = open('expression.in')
    else:
        in_data = sys.stdin

    # read infix expression
    line = in_data.readline()
    expr = line.strip()

    tree = Tree()
    tree.create_tree(expr)

    # evaluate the expression and print the result
    print(expr, "=", str(tree.evaluate(tree.root)))

    # get the prefix version of the expression and print
    print("Prefix Expression:", tree.pre_order(tree.root).strip())

    # get the postfix version of the expression and print
    print("Postfix Expression:", tree.post_order(tree.root).strip())


if __name__ == "__main__":
    main()
