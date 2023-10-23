# CS 303E Quiz 3
# do NOT rename this file, otherwise Gradescope will not accept your submission
# also, do NOT change any of the function names or parameters
# Problem 1: Slithering String
def slitheringString(s):
    # replace pass with your solution to problem 1
    newString = "" 
    for i in range(len(s)):
        chr = s[i]
        if chr == " ":
            newString += "_"
        elif chr == "!":
            newString += "."
        elif chr == "?":
            newString += "."
        else:
            newString += chr
    return newString

# Problem 2: Locked Phone Class
class LockedPhone:
    # REMEMBER TO MAKE YOUR DATA MEMBERS PRIVATE
    def __init__(self, brand, password, unlocked = False):
        self.__brand = brand
        self.__password = password
        self.__unlocked = unlocked

    def unlock(self, password):
        if self.__password == password:
            self.__unlocked = True
            return  self.__unlocked
        else:
            return self.__unlocked

    def changePassword(self, newPassword):
        if self.__unlocked == True:
            self.__password = newPassword

    def lock(self):
        self.__unlocked = False

    def __str__(self):
        if self.__unlocked == False:
            return "This " + self.__brand + " phone is currently locked."
        elif self.__unlocked == True:
            return "This " + self.__brand + " phone is currently not locked."

if __name__ == '__main__':
    # uncomment the following lines to run the given test cases
    # note that the output will look slightly different
    # due to how the expected output is formatted
    # print(slitheringString("I am SO excited for the TWICE concert in May!!"))
    # print(slitheringString("Me too! Who's your bias?"))
    # print(slitheringString("My bias is Tzuyu! What about you?"))
    # lp = LockedPhone('Samsung', 'v3rys3cr3tpa55w0rd')
    # print(lp.unlock('v3rys3cr3tpa55w0rd'))
    # lp = LockedPhone('Apple', 'notsosecretpassword')
    # lp.lock()
    # print(str(lp))
    # lp = LockedPhone('Nokia', 'psswrd')
    # lp.changePassword('nwpsswrd')
    # lp.lock()
    # print(lp.unlock('nwpsswrd'))
    # print(lp.unlock('psswrd'))
    # print(str(lp))
    # DO NOT DELETE THIS PASS
    pass
    # DON'T DO IT