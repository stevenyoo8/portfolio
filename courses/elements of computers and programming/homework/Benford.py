# File: Benford.py
# Student: Jongho Yoo
# UT EID: jy23294
# Course Name: CS303E
# 
# Date: 3/30/2023
# Description of Program: Program to verify Benford's Law by opening the file, adding the counts of the leading digits of each number, then writing the results into a new file

import os.path
def benford():
    # initialize empty set
    fileName = input("Enter the name of a file: ").strip()
    if not os.path.isfile(fileName):
        print("File does not exist")
        return
    set1 = set()
    keyNums = {"1": 0, 
                "2": 0, 
                "3": 0, 
                "4": 0, 
                "5": 0, 
                "6": 0, 
                "7": 0, 
                "8": 0, 
                "9": 0}
    f = open(fileName, "r")
    outfile = open("benford.txt", "w")
    line = f.readline()
    line = f.readline()
    while line:
        words = line.split()
        for word in words:
            if word[0] in keyNums:
                keyNums[str(word[0])] += 1
                set1.add(word)
        line = f.readline()
    totalCount = keyNums["1"] + keyNums["2"] + keyNums["3"] + keyNums["4"] + keyNums["5"] + keyNums["6"] + keyNums["7"] + keyNums["8"] + keyNums["9"]
    outfile.write("Total number of cities: " + str(totalCount) + "\n")
    outfile.write("Unique population counts: " + str(len(set1)) + "\n")
    outfile.write("First digit frequency distributions:" + "\n")
    outfile.write("Digit    " + "Count    " + "Percentage" + "\n")
    for key in keyNums:
        percentage = format((keyNums[key] / totalCount * 100), "0.1f")
        outfile.write(format(key, "9s") + format(str(keyNums[key]), "9s") + str(percentage) + "\n")
        line = f.readline()

    f.close()
    outfile.close()
    print("Output written to benford.txt")

benford()