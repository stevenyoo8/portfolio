# pwd = print working directory

# '\n' escape character as new line
print("abc\ndef")
# 'r' in front of string denotes raw string and will print exactly whatever is there
print(r"abc\ndef")

# find current directory
import os
print("Current Directory: " + os.getcwd())
# get list of files in the current directory
myfiles = os.listdir()
for file in myfiles:
    print(file)

### file methods
# open: establish connection to file. Opens a local file handle
# close: terminate connection to file. Throw handle file away
# read: input data from file into your program (this is a mode)
# write: output data from your program to a file (this is a mode)
## need to establish new connection for different modes. Have to establish connection to read. Then close and re-establish to write.

### Opening a File
## general form for opening file
# fileHandle = open(filename, mode)

# 'outfile' is the file handle we will use to refer to the file
outfile = open("myNewFile", "w") # first checks if file exists, if it does, it overwrites. If not, then creates a new file and writes it.
outfile.write("My dog has fleas!\n")

# close handle
outfile.close()

# exit python interactive to use this to just see contents of file
# cat myNewFile 

### file modes
# r = open for reading
# w = open for writing. If file exists, old contents overwritten
# a = open for appending data to end of file
# rb = open for reading binary text
# wb = open for writing binary text

### Closing a file
## general form
# fileHandle.close()

### Reading/Writing a file
## these functions advance an internal file points
# fileHandle.read() = return entire remaining contents of file as string
# fileHandle.read(k) = return next k characters from file as string
# fileHandle.readline() = return next line as a string
# fileHandle.readlines() = return all remaining lines in the file as a list of strings
# fileHandle.write(str) = write the string to the file

### check if file exists
import os.path
print(os.path.isfile("Files.py")) # returns True or False

# -------------------------------------- slideset 2 --------------------------------------
### reading files
def main():
    if not os.path.isfile("gettsburg-address"):
        print("File does not exist")
        return
    gaFile = open("gettsburg-address", "r")
    lineCount = 0
    line = gaFile.readline()
    while line: # if file is not empty
        lineCount += 1
        print(format(lineCount, "3d"), ":", line.strip(), sep = "") # strip removed extraneous white space in the front
        line = gaFile.readline()
    print("\nFound", lineCount, "lines.")
    gaFile.close()

# on os, 'wc' counts words, lines, characters in a file
# wc gettysburg-address

### writing files
# multiplication table example from before
# write does not include new line like print, so you have to define it ("\n")
limit = 13
def multiplicationTable():
    outfile = open("MTable", "w")
    outfile.write("Multiplication Table".center (6 + 4 * (limit - 1)) + "\n") # center just centers the text (method on strings)
    # display number title
    outfile.write("     |")
    for i in range(1, limit):
        outfile.write(format(i, "4d"))
    outfile.write("\n") # new line
    outfile.write("------" + "----" * (limit -1) + "\n")

    for i in range(1, limit):
        outfile.write(format(i, "3d") + " |")
        for j in range(1, limit):
            outfile.write(format(i*j, "4d"))
        outfile.write("\n")
    outfile.close()

multiplicationTable()

### reading one file, writing another
import os.path

# copy contents from file1 to file2
def copyFile():
    f1 = input("Source filename: ").strip()
    f2 = input("Target filename: ").strip()

    if os.path.isfile(f1) == False: # make sure file exists
        print(f1 + " does not exist")
        return
    if os.path.isfile(f2): # so that we don't overwrite an existing file
        print(f2 + " already exists")
        return
    infile = open(f1, "r")
    outfile = open(f2, "w")

    for line in infile:
        outfile.write(line)
    infile.close()
    outfile.close()

copyFile()
