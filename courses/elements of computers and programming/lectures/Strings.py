# concatentation
s1 = "Hello"
s2 = ", World!"

print(s1 + s2) # combine/concatenate strings
print(s1 * 3) # repeat string n times

# change lower to upper and upper to lower
diff = ord("a") - ord("A")
print(diff)

def swapCase(s):
    result = ""
    for ch in s:
        if "A" <= ch <= "Z":
            result += chr(ord(ch) + diff)
        elif "a" <= ch <= "z":
            result += chr(ord(ch) - diff)
        else:
            result += ch
    print(result)
swapCase("abCDefGH")

def swapCase2(s):
    result = ""
    for i in range(len(s)):
        ch = s[i]
        if "A" <= ch <= "Z":
            result += chr(ord(ch) + diff)
        elif "a" <= ch <= "z":
            result += chr(ord(ch) - diff)
        else:
            result += ch
    print(result)
swapCase2("abCDefGH")

# this does not work bc strings are immutable and u can't change a character in place in existing place (gives runtime error)
# the previous two work because we are creating a new string, not changing the original string
def swapCaseWrong(s):
    for i in range(len(s)):
        if "A" <= s[i] <= "Z":
            s[i] = chr(ord(s[i]) + diff)
        elif "a" <= s[i] <= "z":
            s[i] = chr(ord(s[i]) - diff)
        else:
            s[i] = i
    print(s)

# this does not work again bc the string is immutable, and you can't change the first character of the string from P to R
s = "Pat"
# s[0] = "R"
# this works because you are creating a new string. You always have to create a new string to change something in an existing string
s2 = "R" + s[1:]
s2

# -----------------------
# METHODS

# test whether string input represents a decimal integer
def isInt(s):
    print(s.isdigit() or ((s[0] == "-" or s[0] == "+" and s[1:].isdigit())))
isInt("-1234.1234")
isInt("123455")
isInt(input("Enter a number: "))

print("hello world! 5".upper())
print("hello world! 5".title())

# remove whitespace
ans = input("Please enter \"YES\" or \"NO\": ").strip()
print(ans)

# return everything before and after comma (use split function going forward)
# good for things like a csv file
def SplitOnComma(str):
    if "," in str:
        index = str.find(",")
        print(str[:index], str[index + 1])
    else:
        print(str, "")

s = "hello"
print(s.find("t"))