#  File: Josephus.py
#  Student Name: Jongho Yoo
#  Student UT EID: jy23294

# Date Created: June 22, 2023
# Use circular linked list for the Josephus Problem


import sys


# This class represents one soldier.
class Link(object):
    # Constructor
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
    
    def __str__(self):
        return str(self.data)


class CircularList(object):
    # Constructor
    def __init__(self):
        self.head = None
        self.tail = None

    # Is the list empty
    def is_empty(self):
        return self.head is None  # Return true is empty, false if not empty

    # Append an item at the end of the list
    def insert(self, data):
        new_node = Link(data)
        if self.is_empty(): # if list is empty
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node  # first set previous tail pointer to new node
            self.tail = new_node       # set new node as new tail
            self.tail.next = self.head # set new node (tail) pointer to head to make it a circular linked list

    # Find the node with the given data (value)
    # or return None if the data is not there
    def find(self, data):
        current = self.head
 
        while current.data != data:
            if current.data == self.head: # completely traversed list without finding given data
                return None
            current = current.next
        return current
    
    # return length of linked list (number of nodes)
    def get_length(self):
        current = self.head
        count = 1

        while True:
            if current.next is None:
                break
            current = current.next
            if current == self.head:
                return count
            else:
                count += 1
        return count
        
    # Delete a Link with a given data (value) and return the node
    # or return None if the data is not there
    def delete(self, data):
        current = self.head
        previous = self.tail

        if self.is_empty(): # if list is empty, return None
            return None
        
        if self.get_length() == 1: # if list length is only 1, delete the data
            self.head = None
            self.tail = None

        while current.data != data: # traverse until data is found
            previous = current
            current = current.next
            if current == self.head: # if data in not in list, return None
                return None

        if current == self.head:
            self.head = current.next

        if current == self.tail:
            self.tail = previous

        previous.next = current.next # modify pointers to skip over (delete) current node
        return current

    # Delete the nth node starting from the start node
    # Return the data of the deleted node AND return the
    # next node after the deleted node in that order
    def delete_after(self, start, step):
        current = self.head

        while current != start:
            current = current.next
            
        for i in range(step - 1):
            current = current.next

        deleted_link = self.delete(current.data) # delete the current node
        return deleted_link, current.next   # output deleleted node and next node

    # Return a string representation of a Circular List
    # The format of the string will be the same as the __str__
    # format for normal Python lists
    def __str__(self):
        if self.is_empty():
            return '[]'

        current = self.head

        result = '['
        while True:
            result += str(current.data)
            if current.next is None:
                break
            current = current.next
            if current == self.head:
                break
            result += ', '
        result += ']'
        return result


# Input: Number of soldiers
# Outupt: Circular list with one link for each soldier
#         Data for first soldier is 1, etc.
def create_circular_list(num_soldiers):
    soldiers = CircularList()
    for i in range(1, num_soldiers + 1):
        soldiers.insert(i)
    return soldiers

# Input: circular list representing soldiers
#        data for the soldier to start with (1, 2...)
#        number of soldiers to count before identifying one to die
# Output: printed list of soldiers, in order they died
def process_Josephus(my_list, num_soldiers, start_data, step_count):
    current_soldier = my_list.find(start_data)

    if current_soldier is None:
        return None

    for i in range(num_soldiers):
        soldier, next_soldier = my_list.delete_after(current_soldier, step_count)
        print(soldier)

        current_soldier = next_soldier



##### DRIVER CODE #####

def main():
    debug = True
    if debug:
        in_data = open('josephus.in')
    else:
        in_data = sys.stdin

    # read the three numbers from the file
    line = in_data.readline().strip()
    num_soldiers = int(line)

    line = in_data.readline().strip()
    start_data = int(line)

    line = in_data.readline().strip()
    step_count = int(line)

    # Create cirular list
    my_list = create_circular_list(num_soldiers)

    # Kill off soldiers
    process_Josephus(my_list, num_soldiers, start_data, step_count)


if __name__ == "__main__":
    main()
