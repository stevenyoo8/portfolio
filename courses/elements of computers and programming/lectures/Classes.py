# calculator class
class Calculator:
    accumilator = 0
    # Consructor for new class objects. Will implicitly run first
    # Constructor to initialize variables
    # Called initializer
    def __init__(self):
        self.accumilator = 0

    # Need this to be able to have a print output for the class
    # when you call print on a class, it will go to the __str__ function
    def __str__(self):
        return "Displaying: " + str(self.accumilator)
    
    def getAccumilator(self):
        print(self.accumilator)
    
    def clear(self):
        self.accumilator = 0

    def add(self,num):
        self.accumilator += num
    
    def sub(self, num):
        self.accumilator -= num
    
    def mult(self, num):
        self.accumilator *= num
    
    def div(self, num):
        if num == 0:
            print("Undefined")
        else:
            self.accumilator = self.accumilator / num

# calc = Calculator()
# calc.getAccumilator()
# Calculator().getAccumilator()
# calc.add(10)
# calc.getAccumilator()
# print(calc)

class Circle:
    def __init__(self, rad = 1):
        self.radius = rad

    def getRadius(self):
        print(self.radius)
    
    def setRadius(self, rad):
        self.radius = rad
    
    def getPerimeter(self):
        import math
        perimeter = 2 * math.pi * self.radius
        print(perimeter)

    def getArea(self):
        import math
        area = math.pi * (self.radius ** 2)
        print(area)

# c = Circle()
# c.getRadius()
# c.setRadius(5)
# c.getRadius()
# c.getArea()

# types and id's
# print(type(c))
# print(id(c))
# print(id(7))


def isRank(r):
    # Recognizer for a legal rank:
    return r == "Ace" or r == "2" or r == "3" or r == "4" \
    or r == "5" or r == "6" or r == "7" or r == "8" \
    or r == "9" or r == "10" or r == "Jack" \
    or r == "Queen" or r == "King"

def isSuit(s):
    # Recognizer for a legal suit
    return s == "Spades" or s == "Diamonds" or s == "Hearts" or s == "Clubs"

class Card:
    def __init__(self, rank, suit):
        # Create a Card object with the given rank and suit
        if not isRank(rank) or not isSuit(suit):
            print("Not a legal card specification.")
            return
        self.__rank = rank
        self.__suit = suit
        
    def getRank (self):
        print(self.__rank)
        
    def getSuit (self):
        print(self.__suit)
    
    def __str__ (self):
    # Return a string that is the print representation of this Card’s value. 
        return self.__rank + " of " + self.__suit

# isRank("Jack")
# isRank("Knave")
# isSuit("Clubs")
# isSuit("Spades")
# isRank("2")

c1 = Card("2", "Spades")
print(c1)
c1.getRank()
c1.getSuit()