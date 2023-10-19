# File: Handicap.py
# Student: Jongho Yoo
# UT EID: jy23294
# Course Name: CS303E
# 
# Date: Jan 21, 2023
# Description of Program: Program to calculate a bowler's average score and handicap after three games

# prompt user to enter bowler's name
name = input("Enter bowler's name: ")
# prompt user to enter score's for 3 games
score1 = int(input("Enter Game 1: "))
score2 = int(input("Enter Game 2: "))
score3 = int(input("Enter Game 3: "))

# calculate average score and handicap
averageScore = (score1 + score2 + score3) // 3
handicap = int((200 - averageScore) * 0.80)
# if handicap is negative, handicap is set to 0
handicap = max(0, handicap)

# print results
print("Handicap report for " + name + ":")
print("  " + name + "\'s" + " average is: " + str(averageScore))
print("  " + name + "\'s" + " handicap is: " + str(handicap))
print("")
print("It's time to Bowl!")
