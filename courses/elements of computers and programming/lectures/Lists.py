### lists are mutable; u don't have to create a new list to change list (you have to in strings)

# averages scores
grades = [58, 89, 39, 49, 90, 96, 93, 69, 38, 58, 100, 95]

total = 0
for score in grades:
    total += score
average = total / len(grades)
print("Class average:", format(average, "0.2f"))

average = sum(grades) / len(grades)
print("Class average:", format(average, "0.2f"))

# create list
print(range(0, 4))
print(list(range(4)))
print(list("abcd"))

### lists are a class. So functions like sum, max, min, etc. are functions defined in the lists class. Len is a method of the class.

# List Comprehension
print(range(4))
print([x for x in range(4)]) # create list of range
print([x ** 2 for x in range(4)])
lst = [2, 3, 5, 7, 11, 13]
print([x ** 3 for x in lst])
print([s[0] for s in ["red", "green", "blue"]])
print([s[0] for s in ["red", "green", "blue"] if s <= "green"])

# list functions
l1 = [1, 2, 3]
l1.append(4)
print(l1)

l2 = [5, 6, 7]
l1.extend(l2) # use extend to add a list onto another list
print(l1)

print(l1.index(5)) # where does 5 occur in l1 (position/element 4)

str1 = "abc, def, ghi"
str1.split(",")
print(str1)

studentData = ["Charlie, 90, 75",
               "Frank, 8, 77",
               "Johnnie, 40",
               "Susie, 60, 80"]
print(studentData)

def ProcessStudentData(studentData):
    print("Name         MT  FN   Avg")
    print("--------------------------")

    for line in studentData:
        fields = line.split(",")
        if len(fields) < 3:
            print(fields[0], "Bad student record")
            continue
        else:
            name, midterm, final = fields[0].strip(), int(fields[1].strip()), int(fields[2].strip())
            avg = (midterm + final) / 2
            print(format(name, "10s"), format(midterm, "4d"), format(final, "3d"), format(avg, "6.2f"))

ProcessStudentData(studentData)

# creating new copies of a list
list1 = [1, 2, 3, 4]
list2 = list1 # this simply means there are two pointers to the same list
list1.append(5)
print(list2) # appending 5 to list 1 also appended it to list 2 because they are pointers to the same list

list1 = [1, 2, 3, 4]
list3 = [x for x in list1] # this method creates a new copy
print(list3)

# pointers
def alterList(lst):
    lst.pop()

def main():
    lst = [1, 2, 3, 4]
    print("Before call:", lst)
    alterList(lst)
    print("After call:", lst)
main()

# Cards example
Ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
Suits = ["Spades", "Diamonds", "Hearts", "Clubs"]

class Card:
    def __init__(self, rank, suit):
        # Create a Card object with the given rank and suit
        self.__rank = rank
        self.__suit = suit
        
    def getRank (self):
        print(self.__rank)
        
    def getSuit (self):
        print(self.__suit)
    
    def __str__ (self):
    # Return a string that is the print representation of this Card’s value. 
        return self.__rank + " of " + self.__suit

class Deck:
    # initializer - create deck
    def __init__(self):
        self.__cards = []
        for suit in Suits:
            for rank in Ranks:
                c = Card(rank, suit) # call back to Card class to return card in correct format
                self.__cards.append(c)

    # shuffle deck
    def shuffle(self):
        import random
        random.shuffle(self.__cards)
    
    # deal card - reomve top card from Deck
    def deal(self):
        if len(self) == 0: # need to define __len__ method in class
            print("Deck is empty.")
            return
        else:
            return self.__cards.pop(0) # remove top element which was dealt
    
    def __len__(self):
        return len(self.__cards) 
    
    def __str__(self):
        result = ""
        for c in self.__cards:
            result = result + str(c) + "\n" # str only works bc __str__ method was defined here
        return result

# Define hands class (poker hand) - Can't create hands without defining the deck first
class Hand:    
    def __init__(self, deck):
        if len(deck) < 5:
            print("Not enough cards left!")
            return
        self.__cards = []
        for i in range(5): # 5 cards in a hand
            card = deck.deal()
            self.__cards.append(card)

    def getCard(self, i):
        if 0 <= i <= 4:
            return self.cards[i]
        else:
            return 
    
    def __str__(self):
        result = ""
        for card in self.__cards:
            result = result + str(card) + "\n"
        return result
     