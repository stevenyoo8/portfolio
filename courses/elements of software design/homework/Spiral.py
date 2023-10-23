#  File: Spiral.py
#  Student Name: Jongho Yoo
#  Student UT EID: jy23294

#  Description: Create a number spiral and find the sum of adjacent numbers of a given number

import sys

# Input: n
# Output: size of spiral
def get_dimension(in_data):
    # read first line: gives size/dimension of spiral
    line = in_data.readline()
    # coerce to integer
    size = int(line.strip())

    # pass result   
    return size


# Input: n is an odd integer between 1 and 100
# Output: returns a 2-D list representing a spiral
#         if n is even add one to n
def create_spiral(n):
    # if n is even add one to n
    if n % 2 == 0:
        n += 1
    
    # intialize spiral
    spiral = []

    # add columns to spiral (make it 2D), initialize with 0s
    for i in range(n):
        column = []
        for j in range(n):
            column.append(0)
        spiral.append(column)

    # num to input into spiral (start at 1)
    num = 1
    # max/last num in spiral with given dimension
    last_num = n ** 2

    # center of spiral to start at
    x = n // 2 # indicates list index within entire list (column)
    y = n // 2 # indicates element index within a list (row)

    # initialize step size
    step_size = 1

    # fill out spiral
    while num <= last_num:
        # input num and move right
        for i in range(0, step_size):
            spiral[y][x] = num # insert num into position in spiral
            x += 1 # move right
            num += 1 # next num
        
        # input num and move down
        for i in range(0, step_size):
            spiral[y][x] = num
            y += 1 # move down
            num += 1

        # increase step size
        step_size += 1

        # input num and move left
        for i in range(0, step_size):
            spiral[y][x] = num
            x -= 1
            num += 1       

        # input num and move up
        for i in range(0, step_size):
            spiral[y][x] = num
            y -= 1
            num += 1
        
        # last row to input (move right)
        if last_num - step_size == num:
            step_size += 1
            for i in range(0, step_size):
                spiral[y][x] = num
                x += 1
                num += 1
            
        step_size += 1

    return spiral

# Input: handle to input file
#        the number spiral
# Output: printed adjacent sums
def print_adjacent_sums(in_data, spiral):
    # input will be list of strings, one string per line
    lines = in_data.readlines()

    for i in range(len(lines)):
        value = lines[i].strip() # remove whitespace and new line character
        try:
            value = int(value)
            adj_sum = sum_adjacent_numbers(spiral, value)
            print(adj_sum)    
        except ValueError:
            print("Invalid Input")

# Input: the number spiral
#        the number to find the adjacent sum for
# Output: integer that is the sum of the
#         numbers adjacent to n in the spiral
#         if n is outside the range return 0
def sum_adjacent_numbers(spiral, n):
    # find location (index) of number
    for i, j in enumerate(spiral):
        if n in j:
            position = [i, j.index(n)]

    # x and y positions
    x, y = position

    # size of spiral x and y cannot exceed
    size = len(spiral)

    # define boundary adjacent numbers cannot be in
    boundary = range(0, size)

    # initialize adjacent sum
    adj_sum = 0

    # add all values around num that exist in the spiral
    if (x + 1) in boundary and y in boundary:
        adj_sum += spiral[x + 1][y]
    if (x + 1) in boundary and (y - 1) in boundary:
        adj_sum += spiral[x + 1][y - 1]
    if x in boundary and (y - 1) in boundary:
        adj_sum += spiral[x][y - 1]
    if (x - 1) in boundary and (y - 1) in boundary:
        adj_sum += spiral[x - 1][y - 1]
    if (x - 1) in boundary and y in boundary:
        adj_sum += spiral[x - 1][y]
    if (x - 1) in boundary and (y + 1) in boundary:
        adj_sum += spiral[x - 1][y + 1]
    if x in boundary and (y + 1) in boundary:
        adj_sum += spiral[x][y + 1]
    if (x + 1) in boundary and (y + 1) in boundary:
        adj_sum += spiral[x + 1][y + 1]

    return adj_sum

# print spiral if needed
def print_spiral(spiral):
    for i in range(0, len(spiral)):
        for j in range(0, len(spiral[0])):
            row_format = '{:>4}'
            print(row_format.format(spiral[i][j]), end='')
        print()



''' ##### DRIVER CODE ##### '''

def main():

    # debug flag
    debug = True
    if debug:
        in_data = open('spiral.in')
    else:
        in_data = sys.stdin

    # process the lines of input
    size = get_dimension(in_data)

    # create the spiral
    spiral = [[]]
    spiral = create_spiral(size)
    # print_spiral(spiral)

    # process adjacent sums
    print_adjacent_sums(in_data, spiral)

    in_data.close()


if __name__ == "__main__":
    main()
