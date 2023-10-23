# File: MyListFunctions.py
# Student: Jongho Yoo
# UT EID: jy23294
# Course Name: CS303E
# 
# Date: 3/21/2023
# Description of Program: Create a library of function for lists

def myAppend(lst, x):
    # Return a new list that is like lst but with 
    # the element x at the right end
    return lst + [x]

def myExtend(lst, lst2):
    # Return a new list that contains the elements of
    # lst1 followed by the elements of lst2 in order.
    return lst + lst2

def myMax(lst):
    # Return the element with the highest value.
    # If lst is empty, print "Empty list: no max value"
    # and return None.  You can assume that the list
    # elements can be compared.
    alphabetLower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    alphabetUpper = []
    for i in range(len(alphabetLower)):
        upperChr = chr(ord(alphabetLower[i]) - 32)
        alphabetUpper += upperChr

    if len(lst) == 0:
        print("Empty list: no max value")
        return None
    else:
        newList = []
        for i in range(len(lst)):
            if (lst[i] in alphabetLower) or (lst[i] in alphabetUpper):
                letterNum = ord(lst[i])
                newList = newList + [letterNum]
            else:
                num = lst[i]
                newList = newList + [num]
                
    maxIndex = 0
    maxNum = 0
    for i in range(len(newList)):
        if newList[i] > maxNum:
            maxIndex = i
    return lst[maxIndex]

def mySum(lst):
    # Return the sum of the elements in lst.  Assume
    # that the elements are numbers.
    sum = 0
    for i in range(len(lst)):
        sum += lst[i]
    return sum

def myCount(lst, x):
    # Return the number of times element x appears
    # in lst.
    count = 0
    for i in range(len(lst)):
        if lst[i] == x:
            count += 1
    return count

def myInsert(lst, i, x):
    # Return a new list like lst except that x has been
    # inserted at the ith position.  I.e., the list is now
    # one element longer than before. Print "Invalid index" if
    # i is negative or is greater than the length of lst and 
    # return None.
    if i < 0 or i > len(lst):
        print("Invalid Index")
        return None
    else:
        newList = []
        for a in range(len(lst)):
            num = lst[a]
            if a == i:
                newList = newList + [x]
                newList = newList + [num]
            else: 
                newList = newList + [num]
    return newList

def myPop(lst, i):
    # Return two results: 
    # 1. a new list that is like lst but with the ith 
    #    element removed;
    # 2. the value that was removed.
    # Print "Invalid index" if i is negative or is greater than
    # or equal to len(lst), and return lst unchanged, and None
    if i < 0 or i >= len(lst):
        print("Invalid Index")
        return lst, None
    else:
        newList = []
        for a in range(len(lst)):
            num = lst[a]
            if a == i:
                continue
            else: 
                newList = newList + [num]
        return newList, lst[i]
    
def myFind(lst, x):
    # Return the index of the first (leftmost) occurrence of 
    # x in lst, if any.  Return -1 if x does not occur in lst.
    if x not in lst:
        return -1
    else:
        for i in range(len(lst)):
            value = lst[i]
            if value == x:
                return i

def myRFind(lst, x):
    # Return the index of the last (rightmost) occurrence of 
    # x in lst, if any.  Return -1 if ch does not occur in lst.
    if x not in lst:
        return -1
    else:
        for i in range(len(lst) -1, -1, -1):
            value = lst[i]
            if value == x:
                return i
            
def myFindAll(lst, x):
    # Return a list of indices of occurrences of x in lst, if any.
    # Return the empty list if there are none.
    newList = []
    if x not in lst:
        return newList
    else:
        for i in range(len(lst)):
            value = lst[i]
            if value == x:
                newList += [i]
        return newList

def myReverse(lst):
    # Return a new list like lst but with the characters
    # in the reverse order. 
    newList = []
    for i in range(len(lst) -1, -1, -1):
        num = lst[i]
        newList += [num]
    return newList

def myRemove(lst, x):
    # Return a new list with the first occurrence of x
    # removed.  If there is none, return lst.
    if x not in lst:
        return lst
    else:
        newList = []
        removed = False
        for i in range(len(lst)):
            if lst[i] == x and not removed:
                removed = True
            else:
                num = lst[i]
                newList += [num]
        return newList

def myRemoveAll(lst, x):
    # Return a new list with all occurrences of x
    # removed.  If there are none, return lst.
    if x not in lst:
        return lst
    else:
        newList = []
        for i in range(len(lst)):
            if lst[i] == x:
                continue
            else:
                num = lst[i]
                newList += [num]
        return newList

def mySlice(lst, i, j):
    # A limited version of the slice operations on lists.
    # If i and j are in [0..len(lst)], return the list 
    # [ lst[i], lst[i+1], ... lst[j-1] ].  I.e., 
    # the slice lst[i:j].  Print an error message if either
    # i or j is not in [0..len(lst)].  Notice that this is 
    # similar but not identical to the way Python slice behaves. 
    if i < 0 or j > len(lst):
        print("Illegal index value")
        return
    elif i == 0 and j == len(lst):
        return lst
    else:
        newList = []
        diff = j - i - 1
        count = 0
        while count < diff:
            for a in range(i, j):
                num = lst[a]
                newList += [num]
                count += 1
        return newList