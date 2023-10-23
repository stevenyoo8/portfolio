# GraphInspection.py

import sys


class Stack(object):
    def __init__(self):
        self.stack = []

    # add an item to the top of the stack
    def push(self, item):
        self.stack.append(item)

    # remove an item from the top of the stack
    def pop(self):
        return self.stack.pop()

    # check the item on the top of the stack
    def peek(self):
        return self.stack[-1]

    # check if the stack is empty
    def is_empty(self):
        return (len(self.stack) == 0)

    # return the number of elements in the stack
    def size(self):
        return (len(self.stack))

    def clear(self):
        self.stack = []

    def __str__(self):
        return self.stack


# You can use this class as needed.
# Do not change.
class Queue(object):
    def __init__(self):
        self.queue = []

    # add an item to the end of the queue
    def enqueue(self, item):
        self.queue.append(item)

    # remove an item from the beginning of the queue
    def dequeue(self):
        return self.queue.pop(0)

    def current(self):
        return self.queue[0]

    # check if the queue is empty
    def is_empty(self):
        return (len(self.queue) == 0)

    # return the size of the queue
    def size(self):
        return (len(self.queue))


# Represents a veretex in a graph.
# Do not change.
class Vertex(object):
    def __init__(self, label, weight=1):
        self.label = label
        self.weight = weight
        self.visited = False

    # determine if a vertex was visited
    def was_visited(self):
        return self.visited

    # determine the label of the vertex
    def get_label(self):
        return self.label

    # string representation of the vertex
    def __str__(self):
        return str(self.label)


# Represents a directed graph of vertices and edges.
# It uses a 1D list of vertices and a 2D list for an adjacency matrix.
# Change only the methods specified in comments and instructions.
class Graph(object):
    def __init__(self):
        self.Vertices = []  # a list of vertex objects
        self.adjMat = []  # adjacency matrix of edges

    # check if a vertex is already in the graph
    def has_vertex(self, label):
        nVert = len(self.Vertices)
        for i in range(nVert):
            if (label == (self.Vertices[i]).get_label()):
                return True
        return False

    # given a label get the index of a vertex
    def get_index(self, label):
        nVert = len(self.Vertices)
        for i in range(nVert):
            if (label == (self.Vertices[i]).get_label()):
                return i
        return -1

    # add a Vertex with a given label to the graph
    def add_vertex(self, label):
        if (self.has_vertex(label)):
            return

        # add vertex to the list of vertices
        self.Vertices.append(Vertex(label))

        # add a new column in the adjacency matrix
        nVert = len(self.Vertices)
        for i in range(nVert - 1):
            (self.adjMat[i]).append(0)

        # add a new row for the new vertex
        new_row = []
        for i in range(nVert):
            new_row.append(0)
        self.adjMat.append(new_row)

    # add weighted directed edge to graph
    def add_directed_edge(self, start, finish, weight=1):
        self.adjMat[start][finish] = weight

    # add weighted undirected edge to graph
    def add_undirected_edge(self, start, finish, weight=1):
        self.adjMat[start][finish] = weight
        self.adjMat[finish][start] = weight

   # for debugging, get text of adjacency matrix with vertex labels
    def print_graph(self):
        num_vertices = len(self.Vertices)
        print(" ", end=" ")
        for i in range(num_vertices):
            print(self.Vertices[i], end=" ")
        print()
        for i in range(num_vertices):
            print(self.Vertices[i], end=" ")
            for j in range(num_vertices):
                print(self.adjMat[i][j], end=" ")
            print()
        print()


''''''''''''''''''''
''' DRIVER CODE '''

# Debug flag - set to False before submitting
debug = True
if debug:
    in_data = open('graph1.in')
else:
    in_data = sys.stdin

# create a Graph object
theGraph = Graph()

# read the number of vertices
line = in_data.readline()
line = line.strip()
num_vertices = int(line)

# read the vertices and insert them into the graph
for i in range(num_vertices):
    line = in_data.readline()
    vertex = line.strip()
    theGraph.add_vertex(vertex)

# read the number of edges
line = in_data.readline()
line = line.strip()
num_edges = int(line)

# read the edges and insert them into the graph
for i in range(num_edges):
    line = in_data.readline()
    line = line.strip()
    edge = line.split()
    # print(edge)
    start = theGraph.get_index(edge[0])
    finish = theGraph.get_index(edge[1])
    weight = int(edge[2])
    # print(start, finish)

    theGraph.add_directed_edge(start, finish, weight)

if debug:
    theGraph.print_graph()

print("The graph is weighted:", theGraph.is_weighted())
print("The graph is directed:", theGraph.is_directed())

'''

    # is graph weighted?
    def is_weighted(self):
        for i in range(len(self.adjMat)):
            for j in range(len(self.adjMat)):
                if self.adjMat[i][j] > 1:
                    return True
        return False

    # is graph directed?
    def is_directed(self):
        for i in range(len(self.adjMat)):
            for j in range(len(self.adjMat)):
                if self.adjMat[i][j] != self.adjMat[j][i]:
                    return True
        return False

 
'''
