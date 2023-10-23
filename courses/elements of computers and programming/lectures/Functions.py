# sum to N
def sumToN(n):
    sum = (n * (n + 1)) // 2
    print(sum)

# find 100 primes
def print100Primes():
    primeCount = 0
    onLine = 0
    num = 0
    while primeCount < 100:
        if onLine >= 10:
            print()
            onLine = 0
        nextPrime = findNextPrime(num)
        num = nextPrime
        primeCount += 1
        print(format(nextPrime, "3d"), end = "  ")
        onLine += 1
    print()

def findNextPrime(num):
    if num < 2:
        return 2
    
    if num % 2 == 0:
        num -= 1
    guess = num + 2

    while not isPrime(guess):
        guess += 2
    return guess

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

isPrime(10)