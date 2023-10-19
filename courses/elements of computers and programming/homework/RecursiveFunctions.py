# File: RecursiveFunctions.py
# Student: Jongho Yoo
# UT EID: jy23294
# Course Name: CS303E
# 
# Date: April 6, 2023
# Description of Program: Recursive functions to satisfy the conditions

def sumItemsInList(L):
    """ Given a list of numbers, return the sum. """
    if L == []:
        return 0
    else:
        return L[0] + sumItemsInList(L[1:])
    
def countOccurrencesInList(key, L):
    """ Return the number of times key occurs in list L. """
    if not L:                 # same as L == []:
        return 0
    elif key == L[0]:
        return 1 + countOccurrencesInList(key, L[1:])
    else:
        return countOccurrencesInList(key, L[1:])
    
def addToN(n):
    """ Return the sum of the non-negative integers to n.
    E.g., addToN( 5 ) = 0 + 1 + 2 + 3 + 4 + 5. """
    if n == 0:
       return 0
    else:
        return n + addToN(n-1)
   
def findSumOfDigits(n):
    """ Return the sum of the digits in a non-negative integer. """
    if n < 10:
        return n
    else:
        return (n % 10) + findSumOfDigits(n // 10)

def integerToBinary(n):
    """ Given a nonnegative integer n, return the 
   binary representation as a string. """
    if n == 0:
        return '0'
    elif n == 1:
        return '1'
    else:
        return integerToBinary(n // 2) + str(n % 2)  

def integerToList(n):
    """ Given a nonnegative integer, return a list of the 
    digits (as strings). """
    if n < 10:
       return [str(n)]
    else:
        return integerToList(n // 10) + [str(n % 10)]

def isPalindrome(s):
    """ Return True if string s is a palindrome and False
    otherwise. Count the empty string as a palindrome. """
    if not s: # empty
        return True
    elif s[0] == s[-1]:
        return isPalindrome(s[1:-1])
    else:
        return False

def findFirstUppercase(s):
    """ Return the first uppercase letter in 
    string s, if any. Return None if there
    is none. """
    if not s: # if empty string
        return None
    elif ord(s[0]) <= 90 and ord(s[0]) >= 65:
        return s[0]
    else:
        return findFirstUppercase(s[1:])
    
# for this one, don't reverse the string.
def findLastUppercase(s):
    """ Return the last uppercase letter in 
    string s, if any. Return None if there
    is none. """
    if not s:
        return None
    elif ord(s[-1]) <= 90 and ord(s[0]) >= 65:
        return s[-1]
    else:
        return findLastUppercase(s[:-1])

def findFirstUppercaseIndexHelper(s, index):
    """ Helper function for findFirstUppercaseIndex.
    Return the index of the first uppercase letter;
    assume you are starting at index. Return -1 
    if there is none."""
    if not s:
        return -1
    elif ord(s[0]) <= 90 and ord(s[0]) >= 65:
        return index
    else:
        return findFirstUppercaseIndexHelper(s[1:], index + 1)
    
def findFirstUppercaseIndex(s):
    """ Return the index of the first uppercase letter in 
    string s, if any. Return -1 if there is none. This one 
    requires a helper function, which is the recursive 
    function. """
    return findFirstUppercaseIndexHelper(s, 0)