#  File: Adjacency.py

#  Description: Converts an edge list into an adjacency matrix
#  Student Name: Jongho Yoo
#  Student UT EID: jy23294
#  Course Name: CS 313E
#  Unique Number: 85785

import sys


def edge_to_adjacency(edge_list):
    vertex_list = []
    for i in range(len(edge_list)):
        # add the vertexes into a list without duplicates
        if edge_list[i][0] not in vertex_list: 
            vertex_list.append(edge_list[i][0])
        if edge_list[i][1] not in vertex_list:
            vertex_list.append(edge_list[i][1])
    vertex_list = sorted(vertex_list) # order vertices in ascending order

    # first intialize adjacency matrix with 0s
    adj_matrix = []
    for i in range(len(vertex_list)):
        column = []
        for j in range(len(vertex_list)):
            column.append(0)
        adj_matrix.append(column)

    # fill out adj matrix with corresponding weight
    for edge in edge_list:
        vertex1 = edge[0]
        vertex2 = edge[1]
        weight = edge[2]

        index1 = vertex_list.index(vertex1)
        index2 = vertex_list.index(vertex2)
        adj_matrix[index1][index2] = weight # add weight to corresponding edges

    return adj_matrix
            

# remove formatting and convert to list of tokens
# do not change this method
def clean(text):
    text = text.strip()
    text = text.replace("[", "")
    text = text.replace("]", "")
    text = text.replace("”", "")
    text = text.replace(" ", "")
    text = text.split(",")
    return text


''' DRIVER CODE '''

# Debug flag - set to False before submitting
debug = False
if debug:
    in_data = open('adjacency.in')
else:
    in_data = sys.stdin

# get line of input, remove formatting, convert to list of tokens
input_text = in_data.readline()
input_text = clean(input_text)

# convert one string to 2D list of edge data
edges = []
for i in range(0, len(input_text), 3):
    newList = [input_text[i], input_text[i+1], int(input_text[i+2])]
    edges.append(newList)

# convert the 2D list to an adjacency matrix
adj_matrix = edge_to_adjacency(edges)

print('\n'.join([' '.join([str(cell) for cell in row]) for row in adj_matrix]))
