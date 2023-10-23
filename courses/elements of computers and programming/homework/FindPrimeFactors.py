# File: FindPrimeFactors.py
# Student: Jongho Yoo
# UT EID: jy23294
# Course Name: CS303E
# 
# Date: March 18, 2023
# Description of Program: Program that outputs the prime factorization of a given number in a list form

print("Find Prime Factors:")

# find next prime number
def findNextPrime(num):
    if num < 2:
        return 2
    
    if num % 2 == 0:
        num -= 1
    guess = num + 2

    while not isPrime(guess):
        guess += 2
    return guess

# determine if number is prime
def isPrime(num):
    # Deal with evens and numbers < 2.
    if (num < 2 or num % 2 == 0):
        return num == 2
    # See if there are any odd divisors
    # up to the square root of num.
    import math
    divisor = 3
    while (divisor <= math.sqrt(num)):
        if (num % divisor == 0):
            return False
        else:
            divisor += 2
    return True

while True:
    num = int(input("Enter a positive integer (or 0 to stop): "))
    if num == 0:
        print("Goodbye!")
        break
    elif num == 1:
        print("1 has no prime factorization.")
        continue
    elif num < 0:
        print("Negative integer entered. Try again.")
        continue
    elif isPrime(num):
        primeNum = [num]
        print(primeNum)
        continue
    else:
        primeList = []
        d = 2
        while num > 1:
            if num % d == 0:
                primeList.append(d)
                num = num / d
                continue
            d = findNextPrime(d)
        print(primeList)
        continue