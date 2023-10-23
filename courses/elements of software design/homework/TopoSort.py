#  File: TopoSort.py
#  Student Name:
#  Student UT EID:
#  Partner Name: [DELETE if you did not work with a partner.]
#  Partner UT EID: [DELETE if you did not work with a partner.]

import sys

# You can use this class as needed.
# Do not change.


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
    def __init__(self, label):
        self.label = label
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

    ''' has_cycle() methods '''

    # helper method for dfs()
    # return an unvisited vertex adjacent to vertex v (index)
    def get_adj_unvisited_vertex(self, v):
        nVert = len(self.Vertices)
        for i in range(nVert):
            if (self.adjMat[v][i] > 0) and (
                    not (self.Vertices[i]).was_visited()):
                return i
        return -1

    # helper method for dfs()
    # return list of adjacent vertices to vertex v (index)
    def get_adj_vertexes(self, v): # gives outgoing vertices
        verts = []
        nVert = len(self.Vertices)
        for i in range(nVert):
            if (self.adjMat[v][i] > 0):
                verts.append(i)
        return verts
    
    def get_incoming(self, v): # gives incoming vertices
        verts = []
        nVert = len(self.Vertices)
        for i in range(nVert):
            if (self.adjMat[i][v] > 0):
                verts.append(i)
        return verts

    # helper method for dfs()
    # returns list of verticies to or from vertex v (index)
    def get_adj_back_forth_vertex(self, v):
        verts = []
        nVert = len(self.Vertices)
        for i in range(nVert):
            if self.adjMat[v][i] > 0 or self.adjMat[i][v] > 0:
                verts.append(i)
        return verts

    # needed for has_cycle()
    # do the depth first search in a graph from vertex v (index)
    # also determine if there is a cycle for a given path
    # return True if there is a cycle, False otherwise
    def dfs(self, v):
        # create the Stack
        theStack = Stack()

        # cycle check
        cyclic = False

        # mark the vertex v as visited and push it on the stack
        (self.Vertices[v]).visited = True
        # print(self.Vertices[v])
        theStack.push(v)

        # visit the other vertices according to depth
        while (not theStack.is_empty()) and not cyclic:
            # get an adjacent unvisited vertex
            u = self.get_adj_unvisited_vertex(theStack.peek())
            # print(u)
            # print(theStack.__str__())
            adjacents = self.get_adj_vertexes(u)
            # print(adjacents)
            if v in adjacents:
                # print(v)
                final_adjacents = self.get_adj_back_forth_vertex(v)
                # print(final_adjacents)
                # print(u)
                if u in final_adjacents:
                    cyclic = True
            if (u == -1):
                u = theStack.pop()
            else:
                (self.Vertices[u]).visited = True
                # print(self.Vertices[u])
                theStack.push(u)
                # if cyclic:
                #     theStack.clear()

        # the stack is empty, let us reset the flags
        nVert = len(self.Vertices)
        for i in range(nVert):
            (self.Vertices[i]).visited = False

        return cyclic
        # determine if a directed graph has a cycle
        # this function should return a boolean and not print the result

    ###
    # determine if the graph has a cycle
    # return true if a cycle exists, false otherwise
    def has_cycle(self):
        for v in range(len(self.Vertices)):
            if not self.Vertices[v].was_visited():
                if self.dfs(v):
                    return True
        return False

    ###
    # helper method for toposort()
    def dfs_toposort(self, v, stack):
        self.Vertices[v].visited = True
        for u in self.get_adj_vertexes(v):
            if not self.Vertices[u].was_visited():
                self.dfs_toposort(u, stack)
        stack.push(v)
    
    def toposort(self):
        if self.has_cycle():
            return []  # Graph has a cycle, return empty list

        # Prepare lists
        results = []
        in_degree = {v: 0 for v in self.Vertices}
        queue = Queue()

        # Calculate in-degree for each vertex
        for v in self.Vertices:
            for u in self.get_adj_vertexes(self.get_index(v.get_label())):
                in_degree[self.Vertices[u]] += 1

        # Enqueue vertices with in-degree 0
        for v in self.Vertices:
            if in_degree[v] == 0:
                queue.enqueue(v)

        # Perform topological sorting
        while not queue.is_empty():
            currentV = queue.dequeue()
            results.append(currentV.get_label())

            for u in self.get_adj_vertexes(self.get_index(currentV.get_label())):
                in_degree[self.Vertices[u]] -= 1
                if in_degree[self.Vertices[u]] == 0:
                    queue.enqueue(self.Vertices[u])

        return results

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


''' ##### DRIVER CODE #####
    ##### Do not change, except for the debug flag '''

# Debug flag - set to False before submitting
debug = True
if debug:
    in_data = open('topo.in')
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
    start = theGraph.get_index(edge[0])
    finish = theGraph.get_index(edge[1])
    theGraph.add_directed_edge(start, finish, 1)

if debug:
    theGraph.print_graph()

# test if a directed graph has a cycle
if (theGraph.has_cycle()):
    print("The Graph has a cycle.")
else:
    print("The Graph does not have a cycle.")

# test topological sort
if (not theGraph.has_cycle()):
    vertex_list = theGraph.toposort()
    print("\nList of vertices after toposort:")
    print(vertex_list)
