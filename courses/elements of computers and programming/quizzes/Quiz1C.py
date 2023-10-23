# CS 303E Quiz 1
# do NOT rename this file, otherwise Gradescope will not accept your submission
# Problem 1: Fan Fiction Financials

def fanFictionFinancials():
    # write your solution to problem 1 here
    import math
    w = float(input())
    c = float(input())
    f = float(input())
    profit= ((w / (50 * c)) ** 3) + (math.sqrt((c ** 3) + (f / 5)))
    print("Your friend will gain $" + str(format(profit, "0.2f")))
    pass

# Problem 2: Cake Baking
def cakeBaking():
    # write your solution to problem 2 here
    eggs = int(input())
    butter = float(input())
    powder = float(input())
    cake_eggs = eggs // 3
    cake_butter = butter / 1.4
    cake_powder = powder / 2.3
    cake_count = int(min(cake_eggs, cake_butter, cake_powder))
    print(cake_count)
    pass
if __name__=="__main__":
    """
    If you want to test your code on your computer, uncomment the respective
    function call(s) below.
    
    DO NOT CALL YOUR FUNCTIONS ANYWHERE OUTSIDE OF THIS AREA
    """

    # fanFictionFinancials()
    # cakeBaking()
    # DO NOT DELETE THIS PASS
    pass
    # DON'T DO IT