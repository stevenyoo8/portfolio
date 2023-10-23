# File: EasterSunday.py
# Student: Jongho Yoo
# UT EID: jy23294
# Course Name: C S 303E
# 
# Date: January 17, 2023
# Description of Program: Program to find the month and day of Easter Sunday given a year


# prompt user to enter year
y = int(input("Enter year: "))

# assign variables using algorithm invented by Gauss
a = y % 19
b = y // 100
c = y % 100
d = b // 4
e = b % 4
g = (8 * b + 13) // 25
h = (19 * a + b - d - g + 15) % 30
j = c // 4
k = c % 4
m = (a + 11 * h) // 319
r = (2 * e + 2 * j - k - h + m + 32) % 7
n = (h - m + r + 90) // 25
p = (h - m + r + n + 19) % 32

# print results
print("In", y, "Easter Sunday is on month", n, "and day", p)
