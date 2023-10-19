# File: FunctionExamples.py
# Student: Jongho Yoo
# UT EID: jy23294
# Course Name: CS303E
# 
# Date Created: Feb 04, 2023
# Description of Program: Create a program using functions to satisfy each condition

# 1. Write a function to return the sum of three numbers.
def sum3Numbers (x, y, z):
    print(x + y + z)
    
# 2. Write a function to return the product of three numbers.
def multiply3Numbers(x, y, z):
    print(x * y * z)

# 3. Write a function to return the sum of up to 3 numbers.  It should
#    accept 1, 2, or 3 parameters.  Hint: any parameter not given
#    should default to 0.
def sumUpTo3Numbers (x, y = 0, z = 0):
    if y != 0:
        y = y
    if z != 0:
        z = z
    print(x + y + z)

# 4. Write a function to return the product of up to 3 numbers.  It
#    should accept 1, 2, or 3 parameters.  Hint: what should the
#    default be in this case?
def multiplyUpTo3Numbers (x, y = 1, z = 1):
    if y != 1:
        y = y
    if z != z:
        z = z
    print(x * y * z)

# 5. Write a function that takes 2 numbers as input and prints them
#    out in ascending order.  Make sure it works if they are equal.
def printInOrder(x, y):
    if x < y:
        print(x, y)
    elif x > y:
        print(y, x)
    else: 
        print(x, y)

# 6. Write a function that returns the area of a square, given the length of a side.
#    Print an error message if side is negative. 
def areaOfSquare(side):
    if side < 0:
        print("Negative value entered")
    else:
        area = side ** 2
        print(area)

# 7. Write a function that returns the perimeter of a square, given
#    the length of a side.  Print an error message if side is negative.
def perimeterOfSquare(side):
    if side < 0:
        print("Negative value entered")
    else:
        perimeter = side * 4
        print(perimeter)

# 8. Write a function that returns the area of a circle, given the
#    radius.  Use math.pi. Print an error message if radius is negative.
def areaOfCircle(radius):
    if radius < 0:
        print("Negative value entered")
    else:
        import math
        area = math.pi * (radius ** 2)
        print(area)

# 9. Write a function that returns the circumference of a circle given
#    the radius.  Use math.pi. Print an error if radius is negative.
def circumferenceOfCircle(radius):
    if radius < 0:
        print("Negative value entered")
    else:
        import math
        circumference = 2 * math.pi * radius
        print(circumference)

# 10. Write a function: given parameters d1, d2, x, returns whether
#    both d1 and d2 are both factors (evenly divide) x.  You can
#    assume all values are integers.
def bothFactors(d1, d2, x):
    if (x % d1 == 0 and x % d2 == 0):
        print(True)
    else:
        print(False)

# 11. Given a value x, compute and print out the area and circumference of a circle with
#    radius x and the area and perimeter of a square with side x.  Use your previous 
#    functions for these computations.  Leave a blank line above and below the printing.
def squareAndCircle(x):
    import math
    area_circle = math.pi * (x ** 2)
    circumference_circle = 2 * math.pi * x
    area_square = x ** 2
    perimeter_square = x * 4
    print()
    print("Circle with radius", x, "has:")
    print("   Area:", area_circle)
    print("   Circumference:", circumference_circle)
    print("Square with side", x, "has:")
    print("   Area:", area_square)
    print("   Perimeter:", perimeter_square)
    print()

# 12. Write a function that returns the factorial of a positive
#     integer n.  Use a for loop to compute the factorial.  You can
#     assume the input is an integer, but print an error message if
#     it's not positive and return None.
def factorial(n):
    if n < 0:
        print("Input must be positive.")
    elif n == 0:
        factorial = 1
        print(factorial)
    else:
        factorial = 1
        for i in range(1, n + 1): # end value of range is not included, so do n + 1
            factorial = factorial * i
        print(factorial)
