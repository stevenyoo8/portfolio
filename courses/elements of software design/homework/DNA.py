#  File: DNA.py
#  Student Name: Jongho Yoo
#  Student UT EID: jy23294

#  Description: Given pairs of DNA sequences, find the longest common subsequence(s) between each pair

import sys

# Input: s1 and s2 are two strings that represent strands of DNA
# Output: returns a sorted list of substrings that are the longest
#         common subsequence. The list is empty if there are no
#         common subsequences.
def longest_subsequence(s1, s2):
    # intialize list to store all substrings present between the two strings
    substrings_present = []
    # initialize list to store the longest substring(s) present between the two strings
    longest_substrings = []

    # create step size constant (start at 2 because substring of length 1 is not considered a sequence)
    step = 2
    # iterate through all possible substrings present in s1
    while step <= len(s1):
        start = 0 # begin reading frame at index 0
        end = start + step # stop reading frame at index of defined end
        # while the end reading frame index does not pass last element in s1
        while end <= len(s1):
            if s1[start:start + step] in s2: # only store substrings present in s1 and s2
                substrings_present.append(s1[start:start + step])
            # next reading frame keeping step size the same
            start += 1
            end += 1
        step += 1 # increase reading frame step size

    # add longest substring(s) to second list
    for item in substrings_present: # iterate through substrings present in first list
        # because step size increases, last element has longest length
        if len(item) == len(substrings_present[-1]) and item not in longest_substrings: # no duplicates
            longest_substrings.append(item) # append to second list
    
    # sort list (order alphabetically)
    longest_substrings.sort()
    # result
    return longest_substrings
        

# Input: list of strings, one string per file input line
# Output: process each pair of DNA strings in the list
def process_lines(lines):
    pass
    num_pairs = lines[0] # number of pairs
    num_pairs = num_pairs.strip() # remove whitespace
    num_pairs = int(num_pairs)
    line_count = 1
    for i in range(num_pairs):
        s1 = lines[line_count] # set s1 as first element in pair
        s1 = s1.strip()
        s1 = s1.upper() # convert to upper
        line_count += 1 
        s2 = lines[line_count] # set s2 as second element in pair
        s2 = s2.strip()
        s2 = s2.upper()
        line_count += 1
        result_list = longest_subsequence(s1, s2) # use the string pair to find longest subsequence

        # print the result
        if len(result_list) == 0:
            print("No Common Sequence Found")
        else:
            for item in result_list:
                print(item)
        # inset blank line
        print()
        

''' ##### DRIVER CODE ##### '''

def main():
    # Debug flag
    debug = True
    if debug:
        in_data = open('dna.in')
    else:
        in_data = sys.stdin

    # input will be list of strings, one string per line
    lines = in_data.readlines()
    # process the lines
    process_lines(lines)
    in_data.close()


if __name__ == "__main__":
    main()