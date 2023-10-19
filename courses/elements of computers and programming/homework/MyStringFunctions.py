# File: MyStringFunctions.py
# Student: Jongho Yoo
# UT EID: jy23294               
# Course Name: CS303E
# 
# Date: Mar 1, 2023
# Description of Program: Define a library of functions on strings

def myAppend(s, ch):
    # Return a new string that is like s but with 
    # character ch added at the end
    return s + ch

def myCount(s, ch):
    # Return the number of times character ch appears
    # in s.
    count = 0
    for i in s:
        if i == ch:
            count += 1
    return count 

def myExtend(s1, s2):
    # Return a new string that contains the elements of
    # s1 followed by the elements of s2, in the same
    # order they appear in s2.
    return s1 + s2

def myMin(s):
    # Return the character in s with the lowest ASCII code.
    # If s is empty, print "Empty string: no min value"
    # and return None.
    if s == "":
        print("Empty string: no min value")
        return
    else:
        return min(s)

def myInsert(s, i, ch):
    # Return a new string like s except that ch has been
    # inserted at the ith position. I.e., the string is now
    # one character longer than before. Print "Invalid index" if
    # i is greater than the length of s and return None.
    newString = ""
    if i > len(s):
        print("Invalid Index")
        return
    else:
        for a in range(len(s)):
            chr = s[a]
            if a == i:
                newString += ch
                newString += chr
            else:
                newString += chr
    return newString
        
def myPop(s, i):
    # Return two results: 
    # 1. a new string that is like s but with the ith 
    #    element removed;
    # 2. the value that was removed.
    # Print "Invalid index" if i is greater than or 
    # equal to len(s), and return s unchanged and None
    newString = ""
    if i >= len(s):
        print("Invalid Index")
        return s, None
    else:
        for a in range(len(s)):
            chr = s[a]
            if a == i:
                continue
            else:
                newString += chr
    return newString, s[i]

def myFind(s, ch):
    # Return the index of the first (leftmost) occurrence of 
    # ch in s, if any. Return -1 if ch does not occur in s.
    if ch not in s:
        return -1
    else:
        for i in range(len(s)):
            chr = s[i]
            if chr == ch:
                return i

def myRFind(s, ch):
    # Return the index of the last (rightmost) occurrence of 
    # ch in s, if any. Return -1 if ch does not occur in s.
    if ch not in s:
        return -1
    else: 
        for i in range(len(s) -1, -1, -1):
            chr = s[i]
            if chr == ch:
                return i

def myRemove(s, ch):
    # Return a new string with the first occurrence of ch 
    # removed. If there is none, return s.
    if ch not in s:
        return s
    
    newString = ""
    removed = False
    for i in s:
        if i == ch and not removed:
            newString += ""
            removed = True
        else:
            newString += i
    return newString

def myRemoveAll(s, ch):
    # Return a new string with all occurrences of ch
    # removed. If there are none, return s.
    newString = ""
    if ch not in s:
        return s
    else:
        for i in s:
            if i == ch:
                newString += ""
            else:
                newString += i
        return newString

def myReverse(s):
    # Return a new string like s but with the characters
    # in the reverse order.
    newString = ""
    for i in range(len(s) - 1, -1, -1):
        chr = s[i]
        newString += chr
    return newString

