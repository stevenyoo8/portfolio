# File: Project1.py
# Student: Jongho Yoo
# UT EID: jy23294
# Course Name: CS303E
# 
# Date: Feb 13, 2023
# Description of Program: Program a rock-paper-scissors game 

def startGame():
    print("Welcome to a game or Rock, Paper, Scissors!")
    print()
    userPlay()

def userPlay():
    games = 0
    wins = 0
    losses = 0
    draws = 0 
    
    while True:
        # computer choice
        import random
        computer_choice = random.choice(["1", "2", "3"])
        if computer_choice == "1":
            computer_choice = "rock"
        elif computer_choice == "2":
            computer_choice = "paper"
        else:
            computer_choice = "scissors"

        # promot user choice
        print("Choose your play:")
        print("  Enter 1 for rock;")
        print("  Enter 2 for paper;")
        print("  Enter 3 for scissors;")
        user_choice = input("  Enter 4 to exit: ")

        if user_choice == "1":
            user_choice = "rock"
        elif user_choice == "2":
            user_choice = "paper"
        elif user_choice == "3":
            user_choice = "scissors"
        elif user_choice == "4" and games > 0:
            printStats(games, wins, losses, draws)
            return
        elif user_choice == "4" and games == 0:
            print("No games were completed.")
            print("Thanks for playing. Goodbye!")
            print()
            return
        else:
            print("Illegal play entered. Try again!")
            print()
            continue

        # compare plays
        if computer_choice == user_choice:
            print("You played", user_choice + "; your opponent played", computer_choice)
            print("There is no winner. Try again!")
            print()
            games += 1
            draws += 1
            continue
        elif computer_choice == "rock" and user_choice == "paper":
            print("You played", user_choice + "; your opponenet played", computer_choice)
            print("Sorry, you lost!")
            print()
            losses += 1
            games += 1
            continue
        elif computer_choice == "rock" and user_choice == "scissors":
            print("You played", user_choice + "; your opponenet played", computer_choice)
            print("Congratulations, you won!")
            print()
            wins += 1
            games += 1
            continue
        elif computer_choice == "paper" and user_choice == "rock":
            print("You played", user_choice + "; your opponenet played", computer_choice)
            print("Sorry, you lost!")
            print()
            losses += 1
            games += 1
            continue
        elif computer_choice == "paper" and user_choice == "scissors":
            print("You played", user_choice + "; your opponenet played", computer_choice)
            print("Congratulations, you won!")
            print()
            wins += 1
            games += 1
            continue
        elif computer_choice == "scissors" and user_choice == "rock":
            print("You played", user_choice + "; your opponenet played", computer_choice)
            print("Congratulations, you won!")
            print()
            wins += 1
            games += 1
            continue
        else: # last option is computer_choice == "scissors" and user_choice == "paper"
            print("You played", user_choice + "; your opponenet played", computer_choice)
            print("Sorry, you lost!")
            print()
            losses += 1
            games += 1
            continue

def printStats(games, wins, losses, draws):
    print("Game statistics:")
    print("  Games played:", games)
    print("  You won:     ", wins, "(" + format((wins / games), "0.1%") + ")")
    print("  You lost:    ", losses, "(" + format((losses / games), "0.1%") + ")")
    print("  No winner:   ", draws, "(" + format((draws / games), "0.1%") + ")")
    print("Thanks for playing. Goodbye!")
    print()

startGame()
