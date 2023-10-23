
def isLowerLetter(ch):
    return "a" <= ch <= "z"

def countOccurances(text):
    counts = [0 for i in range(26)]
    wordList = text.split()
    for word in wordList:
        word = word.lower()
        for ch in word:
            if isLowerLetter(ch):
                index = ord(ch) - ord("a")
                counts[index] += 1
    return counts

def printCounts(counts):
    onLine = 0
    for i in range(26):
        letterOrd = i + ord("a")
        print(chr(letterOrd) + ":", counts[i], end = " ")
        onLine += 1
        if onLine == 10:
            print()
            onLine = 0
    print()

def main():
    text = "Hello World, my name is Steven."
    counts = countOccurances(text)
    printCounts(counts)

main()

### searching and sorting lists
# index occurance in list

## LINEAR SEARCH - use when list is not sorted (or sorted)
def linearSearch(lst, key):
    for i in range(len(lst)):
        if key == lst[i]:
            return i
    return -1

def findAllOccurrences(lst, key):
    found = []
    for i in range(len(lst)):
        if key == lst[i]:
            found.append(i)
    return found

lst = [1, 3, 5, 7, 7, 9]
linearSearch(lst, 7)
findAllOccurrences(lst, 7)

# index is a list method (error if key does not exist)
lst.index(7) # call print to see

## BINARY SEARCH - when list is in order (ordinal)
def binarySearch(lst, key):
    low = 0
    high = len(lst) - 1
    while high >= low:
        mid = (low + high) // 2
        if key < lst[mid]:
            high = mid - 1
        elif key == lst[mid]:
            return mid
        else:
            low = mid + 1
    # runs if no match found. Gives position in order of where it would fit in the list
    return (-low - 1)