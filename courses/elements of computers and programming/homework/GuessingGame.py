# File: GuessingGame.py
# Student: Jongho Yoo
# UT EID: jy23294
# Course Name: CS303E
# 
# Date: Jan 31, 2023
# Description of Program: Create a program for the user to guess a random number within 10 tries

# define function main
def main(answer = None):
    imported = True
    if not answer: # if answer is not None
        import random
        answer = random.randint(1, 999)
        imported = False

   # print welcome message
    print()
    print("Welcome to the guessing game! Good luck!")
    print()

    # ask user if they are ready to play
    while True:
        status = input("Are you ready to play (Y/N): ")
        if status == "Y":
            print()
            print("See if you can guess the 'secret number'!")
            print()
            break
        elif status == "N":
            print()
            print("Well, come again later. Goodbye!")
            print()
            return
        else:
            print("Sorry, I didn't recognize your answer. Try again!")
            print()
            continue
        
    # set attempt to 1
    attempt = 1

    #start while loop
    while True:
        guess = int(input("Enter an integer from 1 to 999: "))
        if guess < 1 or guess > 999:
            print("That's an illegal guess. Try again! You have", 11 - attempt, "guesses left.")
            print()
            continue
        elif guess < answer and attempt < 10:
            print("Your guess is too low. Try again! You have", 10 - attempt, "guesses left.")
            print()
            attempt += 1
            continue       
        elif guess > answer and attempt < 10:
            print("Your guess is too high. Try again! You have", 10 - attempt, "guesses left.")
            print()
            attempt += 1
            continue
        elif guess == answer and attempt <= 10:
            print("Congratulations, you got it! You took", attempt, "guesses!")
            print()
            attempt = 1
            if not imported:
                answer = random.randint(1, 999)
            while True:
                status = input("Are you ready to play (Y/N): ")
                if status == "Y":
                    print()
                    print("See if you can guess the 'secret number'!")
                    print()
                    break
                elif status == "N":
                    print()                    
                    print("Well, come again later. Goodbye!")
                    print()
                    return
                else:
                    print("Sorry, I didn't recognize your answer. Try again!")
                    print()
                    continue                               
        elif attempt == 10:
            if guess < answer:
                print("Your guess is too low. Try again! You have", 10 - attempt, "guesses left.")
            elif guess > answer:
                print("Your guess is too high. Try again! You have", 10 - attempt, "guesses left.")
            print("Sorry! You took too many guesses. The answer was " + str(answer) + ". Better luck next time!")
            print()
            attempt = 1
            if not imported:
                answer = random.randint(1, 999)
            while True:
                status = input("Are you ready to play (Y/N): ")
                if status == "Y":
                    print()
                    print("See if you can guess the 'secret number'!")
                    print()
                    break
                elif status == "N":
                    print()                    
                    print("Well, come again later. Goodbye!")
                    print()
                    return
                else:
                    print("Sorry, I didn't recognize your answer. Try again!")
                    print()
                    continue

main()
