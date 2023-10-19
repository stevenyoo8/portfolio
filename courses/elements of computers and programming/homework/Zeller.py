# File: Zeller.py
# Student: Jongho Yoo
# UT EID: jy23294
# Course Name: CS303E
# 
# Date: Jan 23, 2023
# Description of Program: Program to give the day of the week given year, month, and date

def main():
    # Function defined as "main" to be called later for execution 

    # Accept the year from the user and convert it to an int
    Y = int(input("\nEnter year (e.g., 2008): "))
    # If the year is not greater than 1752, print an error
    # message and exit the program. 
    if (Y < 1753):
        print("Year must be > 1752.  Illegal year entered:", Y, "\n")
        return

    # Accept the month from the user and convert it to an int
    m = int(input("\nEnter month (1-12): "))
    # If the month is not between 1-12, print an error 
    # message and exit the program
    if (m < 1 or m > 12):
        print("Month must be in [1...12]. Illegal month enetered:", m, "\n")
        return

    # Accept the day from the user and convert it to an int
    d = int(input("\nEnter day of the month (1-31): "))
    # If the day is not between 1-31, print an error 
    # message and exit the program
    if (d < 1 or d > 31):
        print("Day must be in [1...31]. Illegal day entered:", d, "\n")
        return

    # Compute the other variables, including h
    # If month is 1 or 2, add 12 to m and subract 1 from Y
    if m == 1 or m == 2:
        m += 12
        Y -= 1

    # Compute K by taking the remainder of Y divided by 100
    K = Y % 100
    # Compute J by doing integer division of Y by 100
    J = Y // 100

    # Compute h using the Zeller's Congruence formula
    h = (d + (13 * (m + 1))//5 + K + K//4 + J//4 + 5 * J) % 7

    # Compute the name of the day from h
    if (h == 0):
        day = "Saturday"
    elif (h == 1):
        day = "Sunday"
    elif (h == 2):
        day = "Monday"
    elif (h == 3):
        day = "Tuesday"
    elif (h == 4):
        day = "Wednesday"
    elif (h == 5):
        day = "Thursday"
    else:
        day = "Friday"

    # print the day of week message
    print("Day of the week is", str(day))

# call function to execute program

print(13 % 7)
