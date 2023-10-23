# this function is recursive because it calls itself
def fact(n):
    if n <= 1: # base case
        print("1")
        return
    else:      # recursive case
        num = n * fact(n-1) # call its own function
        print(num)
        return

# mutally recursive: A calls B and B calls A
def isNonnegativeEven(n):
    print("In isNonnegativeEven(", n, ")")
    if n < 0:
        print(False)
        return
    elif n == 0:
        print(True)
        return
    else:
        isNonnegativeOdd(n - 1)
        return

def isNonnegativeOdd(n):
    print("In isNonnegativeOdd(", n, ")")
    if n < 1:
        print(False)
        return
    elif n == 1:
        print(True)
        return
    else:
        isNonnegativeEven(n - 1)
        return
    
def countItemsInList(L):
    if not L:
        return 0
    else:
        return 1 + countItemsInList(L[1:])
 
def countItems2(lst, k):
    if not lst:
        print("1 + " * k, "+ 0 =")
        return 0
    else:
        print(" 1 + " * k, "1 + countItems(", lst[1:], ") =")
        return 1 + countItems2(lst[1:], k + 1)

# lst = [4, 5, 2, 5, 9, 2, 8]
# countItems2(lst, 0)

# -------------------------------------------------------------------------------------------------------------- #
# sum of list
def sumItemsInList(L):
    if not L: # if list empty
        return 0
    else:
        return L[0] + sumItemsInList(L[1:])

# occurrences of key in list
def countOccurancesInList(key, L):
    if not L:
        return 0
    elif key == L[0]:
        return 1 + countOccurancesInList(key, L[1:])
    else:
        return countOccurancesInList(key, L[1:])

# reverse a list
def reverseList(L):
    if not L:
        return []
    else:
        return reverseList(L[1:]) + [L[0]]

# greatest common factor
def gcd(a, b):
    print("Computing gcd(", a, ",", b, ")")
    if a < b:
        return gcd(a, b-a)
    elif b < a:
        return gcd(a-b, b)
    else: # a = b
        print("Found gcd: ", a)
        return a
    
# binary search function
def binarySearch(lst, key): # this is our helper function
    low = 0
    high = len(lst) - 1
    while high >= low:
        mid = (low + high) // 2
        if key < lst[mid]:
            high = mid - 1
        elif key == lst[mid]:
            return mid
        else: # key > lst[mid]
            low = mid + 1
    return (-low - 1)

def binarySearchRecursive(lst, key):
    if lst == []:
        return False
    mid = (len(lst) - 1) // 2
    if key == lst[mid]:
        return True
    elif key < lst[mid]:
        return binarySearchRecursive(lst[:mid], key)
    else:
        return binarySearchRecursive(lst[mid + 1], key)
    
def binarySearchHelper(lst, key, low, high):
    if low > high:
        return -low - 1
    
    mid = (low + high) // 2
    if key == lst[mid]:
        return mid
    elif key < lst[mid]:
        return binarySearchHelper(lst, key, low, mid - 1)
    else:
        return binarySearchHelper(lst, key, mid + 1, high)
    
def binarySearchRecursive2(lst, key):
    low = 0
    high = len(lst) - 1
    return binarySearchHelper(lst, key, low, high)

# -------------------------------------------------------------------------------------------------------------- #

# fibonacci
def fib(n):
    """ Return nth Fibonacci number . """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n -1) + fib(n -2)

def fibCountCalls(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return 1 + fibCountCalls(n - 1) + fibCountCalls(n - 2)

import time
def fibCaller():
    while True:
        n = int (input(" Input an integer(negative to exit): "))
        if n < 0:
            break
        # Time the call
        tStart = time.clock(); ans = fib(n); tEnd = time.clock()
        interval = tEnd - tStart
        intervalStr = format(interval , "9.4f")
        # How many recursive calls?
        calls = fibCountCalls(n)
        print (" fib (" + str(n) +") = " + str(ans) , end = "")
        print (" with " + str(calls) + " recursive calls")
        print (" time = " + intervalStr + " seconds to execute")

# recursive to find fibonacci faster by going forward, not backwards
def fibHelper(k , limit , ans , ansSub1):
    if k >= limit:
        return ans
    else :
        return fibHelper(k +1 , limit , ans + ansSub1 , ans)
    
def fibBetter(n):
    return fibHelper(1 , n , 1, 0)

def fibBetterCaller():
    while True:
        n = int(input("Input an integer(negative to exit): "))
        if n < 0:
            break
        # Time the call
        tStart = time.clock(); ans = fibBetter(n); tEnd = time.clock()
        interval = tEnd - tStart
        intervalStr = format(interval , "9.4f")
        # How many recursive calls?
        calls = fibBetter(n)
        print (" fib (" + str(n) + ") = " + str(ans) , end = "")
        print (" with " + str(calls) + " recursive calls")
        print (" time = " + intervalStr + " seconds to execute")

### iterative form has no limit. Recursive form has a limit 900 < x < 1000 because when you do recursions, you
### have to store each value in memory and it eventually runs out. Runtime stack will overflow when we reach the
### “recursion depth.”

# closed form solution
def closedForm(n):
    import math
    value = ((1 / math.sqrt(5)) * (((1 + math.sqrt(5)) / 2) ** 2)) - ((1 / math.sqrt(5)) * (((1 - math.sqrt(5)) / 2) ** 2))

# -------------------------------------------------------------------------------------------------------------- #

# Towers of Hanoi. Hard to do iteratively, better to do with recursion
def makeMove(peg1, peg2):
    print("Move desk from " + peg1 + " to " + peg2)

def towersofHanoi(n, A, B, C):
    if n == 1:
        makeMove(A, C)
    else:
        towersofHanoi(n-1, A, C, B)
        makeMove(A, C)
        towersofHanoi(n-1, B, A, C)

towersofHanoi(4, "A", "B", "C")