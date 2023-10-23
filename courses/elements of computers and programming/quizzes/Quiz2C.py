# CS 303E Quiz 2
# do NOT rename this file, otherwise Gradescope will not accept your submission
# Problem 1: Clothing Purchases
def clothingPurchases():
    # write your solution to problem 1 here
    shirt = 19.98
    jeans = 33.95
    cologne = 74.95
    belt = 48.72
    perfume = 81.81

    missing1 = str(input())
    missing2 = str(input())

    if missing1 == "T-Shirt" and missing2 == "Jeans":
        cost = cologne + belt + perfume
        print("$" + format(cost, "0.2f"))
    elif missing1 == "T-Shirt" and missing2 == "Cologne":
        cost = jeans + belt + perfume
        print("$" + format(cost, "0.2f"))
    elif missing1 == "T-Shirt" and missing2 == "Belt":
        cost = jeans + cologne + perfume
        print("$" + format(cost, "0.2f"))

    pass

# Problem 2: First Term Larger Than k
def firstTermLarger():
    # write your solution to problem 2 here
    k = float(input())
    n = 1

    while True:
        a = (0.65 * (n ** 2)) + (1.32 * n)

        if a < k:
            n += 1
            continue
        elif a > k:
            print(format(a, "0.2f"))
            return

    pass

if __name__=="__main__":
    """
    If you want to test your code on your computer, uncomment the respective
    function call(s) below.
    
    DO NOT CALL YOUR FUNCTIONS ANYWHERE OUTSIDE OF THIS AREA
    """
    # clothingPurchases()
    # firstTermLarger()
    # DO NOT DELETE THIS PASS
    pass
    # DON'T DO IT