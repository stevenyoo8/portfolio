# File: Project3.py
# Student: Jongho Yoo
# UT EID: jy23294
# Course Name: CS303E
# 
# Date Created: Apr 02, 2023
# Date Last Modified: 
# Description of Program: Program to give the population of cities in Texas

import os.path

def commandOptions():
    print("Enter any of the following commands:")
    print("\033[1m" + "Help - " + "\033[0m" + "list available commands;")
    print("\033[1m" + "Quit - " + "\033[0m" + "exit this dashboard;")
    print("\033[1m" + "Cities - " + "\033[0m" + "list all Texas cities;")
    print("\033[1m" + "Census <cityName>/Texas - " + "\033[0m" + "population in 2020 census by specified city or statewide;")
    print("\033[1m" + "Estimated <cityName>/Texas - " + "\033[0m" + "estimated population in 2023 by specified city or statewide.")
    print("\033[1m" + "Growth <cityName>/Texas - " + "\033[0m" + "percent change from 2020 to 2023, by city or statewide.")

def dictionary(fileName, command, city_name):
    # create connection to read
    f = open(fileName, "r")
    line = f.readline()
    # skip first line
    line = f.readline()
    # initialize total population count
    total2023 = 0
    total2020 = 0
    # initialize list of city names, 2023 populations, and 2020 populations
    cityList = []
    pop2023List = []
    pop2020List = []
    # initialize dictionary
    cityDictionary = {}

    while line: # while line exists
        if "#" in line: # skip line with "#"
            line = f.readline()
            continue
        else:
            # separate each line into separate values on comma
            words = line.split(sep = ",")

            # extract first column as int
            estimated2023 = int(words[0])
            # extract second column as int
            census2020 = int(words[1])
            # remove any quotes from city names
            cityName = words[3].replace("'", "")

            # population totals
            total2023 += estimated2023
            total2020 += census2020
            # append population total lists
            pop2023List.append(estimated2023)
            pop2020List.append(census2020)
            # append city names list
            cityList.append(cityName)

            line = f.readline() # move onto next line
            continue

    # add key and values to dictionary
    for i in range(len(cityList)):
        cityDictionary[cityList[i]] = (pop2020List[i], pop2023List[i])
    cityDictionary['Texas'] = (total2020, total2023)

    # create a copy of city names list without texas
    cityNamesList = [city for city in cityList]
    cityNamesList.sort() # sort alphabetically

    # add Texas values to city names list and population lists
    cityList.append("Texas")
    pop2020List.append(total2020)
    pop2023List.append(total2023)

    # sort dictionary
    myKeys = list(cityDictionary.keys())
    myKeys.sort()
    cityDictionarySorted = {i: cityDictionary[i] for i in myKeys}

    if command == "citiesCommand":
        cityNamesList.sort()
        lineCount = 1
        for i in range(len(cityNamesList)):
            if lineCount == 10:
                print(cityNamesList[i])
                lineCount = 1
            else:
                print(cityNamesList[i] + ", ", end = "")
                lineCount += 1
        return
    elif command == "censusCommand":
        if city_name not in cityList:
            print("City " + city_name + " is not recognized.")
            return 
        elif city_name[-1] == "s":
            print(city_name + "\' total population in the 2020 Census: " + str(pop2020List[cityList.index(city_name)]))
            return
        else:
            print(city_name + "\'s total population in the 2020 Census: " + str(pop2020List[cityList.index(city_name)]))
            return
    elif command == "estimatedCommand":
        if city_name not in cityList:
            print("City " + city_name + " is not recognized.")
            return
        elif city_name[-1] == "s": 
            print(city_name + "\' estimated population in 2023: " + str(pop2023List[cityList.index(city_name)]))
            return
        else:
            print(city_name + "\'s estimated population in 2023: " + str(pop2023List[cityList.index(city_name)]))
            return
    elif command == "growthCommand":
        if city_name not in cityList:
            print("City " + city_name + " is not recognized.")
            return
        else:
            percent_change = ((pop2023List[cityList.index(city_name)] - pop2020List[cityList.index(city_name)]) / pop2020List[cityList.index(city_name)]) * 100
            print(city_name + " had a percent population change 2020 to 2023: " + str(format(percent_change, "0.2f")) + "%")
            return

    f.close()

def main():
    fileName = "citiesData.csv"

    if not os.path.isfile(fileName):
        print("File does not exist")
        return
    
    # welcome message
    print()
    print("\033[1m" + "Welcome to the Texas Cities Population Dashboard" + "\033[0m")
    print("This provides census data from the 2020 census and \nestimated poulation data in Texas as of 2023.")
    print()
    print("Creating dictionary from file: " + fileName)
    print()

    # print command options
    commandOptions()
    print()

    while True:
        # input command and transform to evaluate
        command = str(input("\033[1m" + "Please enter a command: " + "\033[0m"))
        command = command.split()
        if len(command) > 2: # occurs when city name is 2 or more words
            command[0] = command[0].lower()
            for i in range(len(command) - 2):
                command[1] = command[1] + " " + command[i + 2]
        else:
            command[0] = command[0].lower()       
        
        # evaluate input command
        if command[0] == "help":
            commandOptions()
            print()
            continue
        elif command[0] == "quit":
            print("\033[1m" + "Thank you for using the Texas Cities Population Database Dashboard. Goodbye!" + "\033[0m")
            print()
            exit()
        elif command[0] == "cities":
            dictionary(fileName, "citiesCommand", None)
            print()
            continue
        elif command[0] == "census":
            dictionary(fileName, "censusCommand", command[1])
            print()
            continue
        elif command[0] == "estimated":
            dictionary(fileName, "estimatedCommand", command[1])
            print()
            continue
        elif command[0] == "growth":
            dictionary(fileName, "growthCommand", command[1])
            print()
            continue
        else:
            print("Command is not recognized. Try again!")
            print()
            continue

main()