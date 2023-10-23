year = int(input("Enter Year: "))

# nested if else
def main():
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                isLeapYear = True
            else: 
                isLeapYear = False
        else: 
            isLeapYear = False
    else:
        isLeapYear = False
    
    # runs if isLeapYear is true. Runs else when isLeapYear is false (boolean)
    if isLeapYear:
        print(year, "is a leap year")
    else:
        print(year, "is not a leap year")

main()

# use elif to avoid nested if else statements
def main():
    # put 400 first bc if divisible by 400, then also divisible by 100 and 4
    if year % 400 == 0:
        isLeapYear = True
    elif year % 100 == 0:
        isLeapYear = False
    elif year % 4 == 0:
        isLeapYear = True
    else:
        isLeapYear = False
    
    if isLeapYear:
        print(year, "is a leap year")
    else:
        print(year, "is not a leap year")

main()

isLeapYear = (year % 4 == 0) and (not(year % 100 == 0) or (year % 400 == 0))

### "", 0 are considered false in boolean. True means anything not false.