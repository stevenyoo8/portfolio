# compute factorial of N
def factorial():
    num = int(input("Compute factorial of: "))
    ans = 1
    i = 1
    while i <= num:
        ans = ans * i
        i = i + 1
    print("Factorial of", num, "is", ans)
#factorial()

#
def sumToN():
    while True:
        n = int(input("Sum to what positive integer: "))
        if n < 1:
            print("That's not positive. Try again!")
        else:
            break # This will exit the loop and return to beginning of loop

    sum = 0 
    i = n
    while i > 0:
        sum += i
        i -= 1
    print("The numbers to", n, "sum to", sum)
#sumToN()

def primeNumber():
    num = int(input("Enter an integer: "))
    isPrime = True
    if num < 2:
        isPrime = False
    elif num == 2:
        isPrime = True
    else:
        divisor = 2
        
        while divisor < num:
            if num % divisor == 0:
                isPrime = False
                break
            else:
                divisor += 1
    print(num, "is prime" if isPrime else "is not prime")
primeNumber()