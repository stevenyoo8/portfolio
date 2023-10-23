# CS 303E Quiz 5C
# do NOT rename this file, otherwise Gradescope will not accept your submission
# also, do NOT change any of the function names or parameters

# Problem 1: First Vowel Locations
def firstVowelLocations(strings):
    # replace pass with your solution to problem 1
    vowelSet = set("aeiouAEIOU")
    dictionary = {}
    # for word in strings:
    #     for letter in word:
    #         print(letter)
    #         if letter in vowels:
    #             index = letter
    
    for word in strings:
        for i in range(len(word)):
            if word[i] in vowelSet:
                index = i
                break
            else:
                index = -1
        dictionary[word] = index
    return dictionary

# Problem 2: List of Even Integers
def listOfEvenIntegers(lst):
    # replace pass with your solution to problem 2
    if not lst:
        return []
    elif lst[0] % 2 == 0:
        return [lst[0]] + listOfEvenIntegers(lst[1:])
    else:
        return listOfEvenIntegers(lst[1:])

if __name__ == '__main__':
    # uncomment the following lines to run the given test cases
    # note that the output will look slightly different
    # due to how the expected output is formatted
    # print(firstVowelLocations({'apple', 'pteradactyl', 'bcdfghjklmnpqrstvwxyz'}))
    # print(firstVowelLocations({'GDC', 'ABC', '1two3four'}))
    # print(firstVowelLocations(set()))
    # print(listOfEvenIntegers([18, -30, 10, -11, 38, -49, 18, 49, -11, 29, 0, -28]))
    # print(listOfEvenIntegers([24, 56, 64, 71, 46, 77, 68]))
    # print(listOfEvenIntegers([1, 3, 5, 7]))
    # DO NOT DELETE THIS PASS
    pass
    # DON'T DO IT
