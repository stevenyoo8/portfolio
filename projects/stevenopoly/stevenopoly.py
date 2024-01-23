def create_locations():
    locations = {
        "Properties": {
            "Brown": ["MEDITERRANEAN AVENUE", "BALTIC AVENUE"],
            "Light Blue": ["ORIENTAL AVENUE", "VERMONT AVENUE", "CONNECTICUT AVENUE"],
            "Pink": ["ST. CHARLES PLACE", "STATES AVENUE", "VIRGINIA AVENUE"],
            "Orange": ["ST. JAMES PLACE", "TENNESSEE AVENUE", "NEW YORK AVENUE"],
            "Red": ["KENTUCKY AVENUE", "INDIANA AVENUE", "ILLINOIS AVENUE"],
            "Yellow": ["ATLANTIC AVENUE", "VENTNOR AVENUE", "MARVIN GARDENS"],
            "Green": ["PACIFIC AVENUE", "NORTH CAROLINA AVENUE", "PENNSYLVANIA AVENUE"],
            "Blue": ["PARK PLACE", "BOARDWALK"],
            "Railroad": ["READING RAILROAD", "PENNSYLVANIA RAILROAD", "B. & O. RAILROAD", "SHORT LINE"],
            "Utility": ["ELECTRIC COMPANY", "WATER WORKS"],
        },
        "Chance": ["Advance to GO. Collect $200.", "Advance to Illinois Ave. If you pass Go, collect $200.", "Advance to St. Charles Place. If you pass Go, collect $200.", "Go To Jail.",
                   "Advance to Boardwalk.", "Advance to the next Railroad. If you pass Go, collect $200.", "Go back 3 spaces.", "You lost a bet, pay each player $50.", "Pay school tax of $150"],
        "Community Chest": ["Advance to GO. Collect $200.", "Doctor's fees. Pay $50.", "Bank error in your favor. Collect $200.", "From sale of stock you get $50.", "Go To Jail.",
                            "Grand Opera Night. Collect $50 from each player.", "Fund Matures. Receive $100", "Property taxes due. Pay $40 per house and $115 per hotel you own", "It's your lucky day, you found $150."],
        "Tax": ["INCOME TAX", "LUXURY TAX"]
    }
    
    return locations



def create_board():
    board = {
        "Board Locations": {0: "GO", 1: "MEDITERRANEAN AVENUE", 2: "COMMUNITY CHEST", 3: "BALTIC AVENUE", 4: "INCOME TAX", 5: "READING RAILROAD", 6: "ORIENTAL AVENUE", 7: "CHANCE", 8: "VERMONT AVENUE", 9: "CONNECTICUT AVENUE", 
                            10: "JUST VISITING JAIL", 11: "ST. CHARLES PLACE", 12: "ELECTRIC COMPANY", 13: "STATES AVENUE", 14: "VIRGINIA AVENUE", 15: "PENNSYLVANIA RAILROAD", 16: "ST. JAMES PLACE", 17: "COMMUNITY CHEST", 18: "TENNESSEE AVENUE", 19: "NEW YORK AVENUE", 
                            20: "FREE PARKING", 21: "KENTUCKY AVENUE", 22: "CHANCE", 23: "INDIANA AVENUE", 24: "ILLINOIS AVENUE", 25: "B. & O. RAILROAD", 26: "ATLANTIC AVENUE", 27: "VENTNOR AVENUE", 28: "WATER WORKS", 29: "MARVIN GARDENS", 
                            30: "GO TO JAIL", 31: "PACIFIC AVENUE", 32: "NORTH CAROLINA AVENUE", 33: "COMMUNITY CHEST", 34: "PENNSYLVANIA AVENUE", 35: "SHORT LINE", 36: "CHANCE", 37: "PARK PLACE", 38: "LUXURY TAX", 39: "BOARDWALK", 
                            999: "IN JAIL"
        },
        "Landmark Prices": {"MEDITERRANEAN AVENUE": 60, "BALTIC AVENUE": 60,
                            "ORIENTAL AVENUE": 100, "VERMONT AVENUE": 100, "CONNECTICUT AVENUE": 120,
                            "ST. CHARLES PLACE": 140, "STATES AVENUE": 140, "VIRGINIA AVENUE": 160, 
                            "ST. JAMES PLACE": 180, "TENNESSEE AVENUE": 180, "NEW YORK AVENUE": 200,
                            "KENTUCKY AVENUE": 220, "INDIANA AVENUE": 220, "ILLINOIS AVENUE": 240, 
                            "ATLANTIC AVENUE": 260, "VENTNOR AVENUE": 260, "MARVIN GARDENS": 280,
                            "PACIFIC AVENUE": 300, "NORTH CAROLINA AVENUE": 300, "PENNSYLVANIA AVENUE": 320, 
                            "PARK PLACE": 350, "BOARDWALK": 400,
                            "READING RAILROAD": 200, "PENNSYLVANIA RAILROAD": 200, "B. & O. RAILROAD": 200, "SHORT LINE": 200,
                            "ELECTRIC COMPANY": 150, "WATER WORKS": 150
        },
        "Rent Prices": {"MEDITERRANEAN AVENUE": [2, 10, 30, 90, 160, 250], "BALTIC AVENUE": [4, 20, 60, 180, 320, 450],
                            "ORIENTAL AVENUE": [6, 30, 90, 270, 400, 550], "VERMONT AVENUE": [6, 30, 90, 270, 400, 550], "CONNECTICUT AVENUE": [8, 40, 100, 300, 450, 6000],
                            "ST. CHARLES PLACE": [10, 50, 150, 450, 625, 750], "STATES AVENUE": [10, 50, 150, 450, 625, 750], "VIRGINIA AVENUE": [12, 60, 180, 500, 700, 900], 
                            "ST. JAMES PLACE": [14, 70, 200, 550, 750, 950], "TENNESSEE AVENUE": [14, 70, 200, 550, 750, 950], "NEW YORK AVENUE": [16, 80, 220, 600, 800, 1000],
                            "KENTUCKY AVENUE": [18, 90, 250, 700, 875, 1050], "INDIANA AVENUE": [18, 90, 250, 700, 875, 1050], "ILLINOIS AVENUE": [20, 100, 300, 750, 925, 1100], 
                            "ATLANTIC AVENUE": [22, 110, 330, 800, 975, 1150], "VENTNOR AVENUE": [22, 110, 330, 800, 975, 1150], "MARVIN GARDENS": [24, 120, 360, 850, 1025, 1200],
                            "PACIFIC AVENUE": [26, 130, 390, 900, 1100, 1275], "NORTH CAROLINA AVENUE": [26, 130, 390, 900, 1100, 1275], "PENNSYLVANIA AVENUE": [28, 150, 450, 1000, 1200, 1400], 
                            "PARK PLACE": [35, 175, 500, 1100, 1300, 1500], "BOARDWALK": [50, 200, 600, 1400, 1700, 2000],
                            "READING RAILROAD": [0, 25, 50, 100, 200], "PENNSYLVANIA RAILROAD": [0, 25, 50, 100, 200], "B. & O. RAILROAD": [0, 25, 50, 100, 200], "SHORT LINE": [0, 25, 50, 100, 200],
                            "ELECTRIC COMPANY": [0, 4, 10], "WATER WORKS": [0, 4, 10]
        },
        "Building Prices": {"MEDITERRANEAN AVENUE": 50, "BALTIC AVENUE": 50,
                            "ORIENTAL AVENUE": 50, "VERMONT AVENUE": 50, "CONNECTICUT AVENUE": 50,
                            "ST. CHARLES PLACE": 100, "STATES AVENUE": 100, "VIRGINIA AVENUE": 100, 
                            "ST. JAMES PLACE": 100, "TENNESSEE AVENUE": 100, "NEW YORK AVENUE": 100,
                            "KENTUCKY AVENUE": 150, "INDIANA AVENUE": 150, "ILLINOIS AVENUE": 150, 
                            "ATLANTIC AVENUE": 150, "VENTNOR AVENUE": 150, "MARVIN GARDENS": 150,
                            "PACIFIC AVENUE": 200, "NORTH CAROLINA AVENUE": 200, "PENNSYLVANIA AVENUE": 200, 
                            "PARK PLACE": 200, "BOARDWALK": 200
        }
    }

    return board



def create_portfolio(players):
    portfolio = {
        "Finances": {},
        "Owned Properties": {}, # format in {player name: {property name: number of houses}} # for railroads/utility, indicates total number of railroad/utility properties owned. 
        "Property List": {},
        "Jail Counter": {}
    }

    for player in players:
        portfolio["Finances"][player] = 1500 # everyone start with $1500
        portfolio['Owned Properties'][player] = {} # initialize properties
        portfolio['Property List'][player] = []
        portfolio["Jail Counter"][player] = 0

    return portfolio


def rollDice():
    import random
    dice1, dice2 = random.randint(1, 6), random.randint(1, 6)
    isDouble = False
    if dice1 == dice2:
        print("DOUBLES!")
        isDouble = True
    roll = dice1 + dice2
    return isDouble, roll



##### PLAY JAIL TURNS #####
def jail(portfolio, player):
    # still in jail
    if portfolio['Jail Counter'][player] < 3:
        while True:
            print(f"Turns in jail: {portfolio['Jail Counter'][player]}")
            jailOption = str(input((f"Pay $50 fine or try to roll for a double? (P or R): ")))
            jailOption = jailOption.strip().lower()
            if jailOption == "r":
                isDouble, roll = rollDice()
                print(f"You rolled a {roll}.")
                if isDouble:
                    print(f"Escape from jail!")
                    portfolio['Jail Counter'][player] = 0
                    outcome = "ESCAPE"
                    break
                else:
                    print(f"No doubles...")
                    portfolio['Jail Counter'][player] += 1
                    outcome = "STAY"
                    break
            elif jailOption == "p":
                portfolio['Jail Counter'][player] = 0
                portfolio['Finances'][player] -= 50
                print(f"{player}'s new bank balance: ${portfolio['Finances'][player]}")
                outcome = "RELEASED"
                break
            elif jailOption != "roll" or jailOption != "pay":
                print("Please input a valid option (P or R)")
                continue
    else: # waited 3 turns
        print(f"You are now released from jail.")
        portfolio['Jail Counter'][player] = 0
        outcome = "RELEASED"
    
    if outcome == "ESCAPE":
        position = 10 + roll
    elif outcome == "STAY":
        position = 999
    else: # released
        position = 10

    return position
    


##### PLAY CHANCE CARDS #####
def chanceCards(chance_index, player, players, portfolio, position):
    if chance_index == 0: # advance to go, collect $200
        portfolio['Finances'][player] += 200
        print(f"{player}'s new bank balance: ${portfolio['Finances'][player]}")
        new_position = 0
        movedPosition = True
    elif chance_index == 1: # advance to illinois ave.
        if position > 24:
            print("Passed GO, collect $200")
            portfolio['Finances'][player] += 200
            print(f"{player}'s new bank balance: ${portfolio['Finances'][player]}")
            new_position = 24
        else:
            new_position = 24
        movedPosition = True
    elif chance_index == 2: # advance to st. charles place
        if position > 11:
            print("Passed GO, collect $200")
            portfolio['Finances'][player] += 200
            print(f"{player}'s new bank balance: ${portfolio['Finances'][player]}")
            new_position = 11
        else:
            new_position = 11
        movedPosition = True
    elif chance_index == 3: # go to jail
        new_position = 999
        movedPosition = True
    elif chance_index == 4: # advance to boardwalk
        new_position = 39
        movedPosition = True
    elif chance_index == 5: # advance to the next railroad
        if position == 7:
            new_position = 15
        elif position == 22:
            new_position = 25
        else:
            print("Passed GO, collect $200")
            portfolio["Finances"][player] += 200
            print(f"{player}'s new bank balance: ${portfolio['Finances'][player]}")
            new_position = 5
        movedPosition = True 
    elif chance_index == 6: # move back 3 spaces
        new_position = position - 3
        movedPosition = True
    elif chance_index == 7: # pay each player $50
        for other_player in players:
            if other_player != player:
                portfolio["Finances"][other_player] += 50
                print(f"{other_player}'s new bank balance: ${portfolio['Finances'][other_player]}")
        portfolio["Finances"][player] -= 50 * (len(players) - 1)
        print(f"{player}'s new bank balance: ${portfolio['Finances'][player]}")
        new_position = position
        movedPosition = False
    elif chance_index == 8: # pay $150
        portfolio["Finances"][player] -= 150
        print(f"{player}'s new bank balance: ${portfolio['Finances'][player]}")
        new_position = position
        movedPosition = False


    return new_position, movedPosition



##### PLAY COMMUNITY CHANCE CARDS #####
def communityChestCards(commChest_index, player, players, portfolio, position, locations):
    if commChest_index == 0: # advance to go, collect $200
        portfolio['Finances'][player] += 200
        print(f"{player}'s new bank balance: ${portfolio['Finances'][player]}")
        new_position = 0
        movedPosition = True
    elif commChest_index == 1: # pay $50
        portfolio['Finances'][player] -= 50
        print(f"{player}'s new bank balance: ${portfolio['Finances'][player]}")
        new_position = position
        movedPosition = False
    elif commChest_index == 2: # collect $200
        portfolio['Finances'][player] += 200
        print(f"{player}'s new bank balance: ${portfolio['Finances'][player]}")
        new_position = position
        movedPosition = False
    elif commChest_index == 3: # collect $50
        portfolio['Finances'][player] += 50
        print(f"{player}'s new bank balance: ${portfolio['Finances'][player]}")
        new_position = position
        movedPosition = False
    elif commChest_index == 4: # go to jail
        new_position = 999
        movedPosition = True
    elif commChest_index == 5: # collect $50 from each player
        for other_player in players:
            if player != other_player:
                portfolio["Finances"][other_player] -= 50
                print(f"{other_player}'s new bank balance: ${portfolio['Finances'][other_player]}")
        portfolio["Finances"][player] += 50 * (len(players) - 1)
        print(f"{player}'s new bank balance: ${portfolio['Finances'][player]}")
        new_position = position
        movedPosition = False
    elif commChest_index == 6: # collect $100
        portfolio['Finances'][player] += 100
        print(f"{player}'s new bank balance: ${portfolio['Finances'][player]}")
        new_position = position
        movedPosition = False
    elif commChest_index == 7: # pay $40 per house and $115 per hotel
        paymentAmount = 0
        for landmark_name in portfolio["Property List"][player]:
            property_type = checkPropertyType(landmark_name, locations)
            if property_type == "Landmark":
                numHouses = portfolio["Owned Properties"][player][landmark_name]
                if numHouses == 0:
                    continue
                elif numHouses < 5: # has b/w 1 and 4 houses
                    paymentAmount += numHouses * 40
                else: # has a hotel (5 houses)
                    paymentAmount += 115
        if paymentAmount == 0:
            print("You own no houses or hotels, no payment required!")
        else:
            print(f"You must pay ${paymentAmount}...")
            portfolio["Finances"][player] -= paymentAmount
            print(f"{player}'s new bank balance: ${portfolio['Finances'][player]}")
        new_position = position
        movedPosition = False
    elif commChest_index == 8: # collect $150
        portfolio["Finances"][player] += 150
        print(f"{player}'s new bank balance: ${portfolio['Finances'][player]}")
        new_position = position
        movedPosition = False

                
    return new_position, movedPosition



##### PLAY PROPERTY CARDS #####
def checkProperty(location, locations):
    # is location a property
    if location in [property for properties_list in locations['Properties'].values() for property in properties_list]: # is location a property
        isProperty = True
    else:
        isProperty = False

    return isProperty

def checkPropertyType(location, locations):
    if location in locations["Properties"]["Railroad"]:
        propertyType = "Railroad"
    elif location in locations["Properties"]["Utility"]:
        propertyType = "Utility"
    else:
        propertyType = "Landmark"
    
    return propertyType

def propertyCards(player, players, board, portfolio, location, locations, roll):
    # get property type
    propertyType = checkPropertyType(location, locations)

    # does someone else own the property
    for other_player in players:
        if other_player == player:
            continue

        if location in portfolio['Property List'][other_player]:
            isOtherPlayerProperty = True
            break
        else:
            isOtherPlayerProperty = False
    
    # land on property owned by another player
    if isOtherPlayerProperty:
        # land on utility property
        if propertyType == "Utility":
            num_of_utility_prop = portfolio['Owned Properties'][other_player][location] # see how many utility properties other player has
            utility_multipler = board["Rent Prices"][location][num_of_utility_prop]
            rent_amount = roll * utility_multipler # get rent amount

        # land on landmark or railroad property
        else:
            number_of_houses = portfolio['Owned Properties'][other_player][location] # see how many number of houses/railroad properties other player has
            rent_amount = board["Rent Prices"][location][number_of_houses] # get rent amount

        # pay rent
        print(f"{other_player} owns this proprty, you owe them ${rent_amount}")
        portfolio["Finances"][player] -= rent_amount
        portfolio["Finances"][other_player] += rent_amount
        print(f"{player}'s new bank balance: ${portfolio['Finances'][player]}")
        print(f"{other_player}'s new balance: ${portfolio['Finances'][other_player]}")


    # land on unowned property
    if (not isOtherPlayerProperty) and (location not in portfolio["Property List"][player]):
        property_price = board["Landmark Prices"][location]
        action = str(input(f"Would you like to to purchase {location} for ${property_price}? (yes or no): "))
        # if player wants to buy property
        if action == "yes":
            # begin counter at 1 for utility and railroad properties
            if propertyType == "Utility":
                if ("ELECTRIC COMPANY" not in portfolio["Property List"][player]) and ("WATER WORKS" not in portfolio["Property List"][player]): # has neither utility properties
                    portfolio["Owned Properties"][player][location] = 1
                else: # has 1 of the utility properties
                    portfolio["Owned Properties"][player]["WATER WORKS"] = 2
                    portfolio["Owned Properties"][player]["ELECTRIC COMPANY"] = 2
            elif propertyType == "Railroad":
                railroadPropertiesList = []
                for railroadProperty in portfolio["Property List"][player]:
                    if ("RAILROAD" in railroadProperty) or ("SHORT" in railroadProperty):
                        railroadPropertiesList.append(railroadProperty)
                if len(railroadPropertiesList) == 0: # has no railroad properties: start count at 1
                    portfolio["Owned Properties"][player][location] = 1
                elif len(railroadPropertiesList) == 1: # has 1 rr property: set count of both to 2
                    portfolio["Owned Properties"][player][location] = 2
                    portfolio["Owned Properties"][player][railroadPropertiesList[0]] = 2
                elif len(railroadPropertiesList) == 2: # has 2 rr properties: set count of all 3 to 3
                    portfolio["Owned Properties"][player][location] = 3
                    portfolio["Owned Properties"][player][railroadPropertiesList[0]] = 3
                    portfolio["Owned Properties"][player][railroadPropertiesList[1]] = 3
                elif len(railroadPropertiesList) == 3: # has 3 rr properties: set count of all 4 to 4
                    portfolio["Owned Properties"][player][location] = 4
                    portfolio["Owned Properties"][player][railroadPropertiesList[0]] = 4
                    portfolio["Owned Properties"][player][railroadPropertiesList[1]] = 4
                    portfolio["Owned Properties"][player][railroadPropertiesList[2]] = 4

            # begin house counter at 0 for landmark properties
            elif propertyType == "Landmark":
                portfolio["Owned Properties"][player][location] = 0
            portfolio['Finances'][player] -= property_price
            print(f"{player}'s new bank balance: ${portfolio['Finances'][player]}")
            print(f"{player}'s properties: {portfolio['Owned Properties'][player]}")
            portfolio["Property List"][player].append(location)
    # land on player's own property
    elif location in portfolio["Property List"][player]:
        print(f"You already own {location}!")

    return portfolio



##### BUILD HOUSES #####
def buildHouses(portfolio, player, board, locations):
    while True:
        show_properties_dict = {}
        for propertySet in locations["Properties"].keys():
            show_properties_dict[propertySet] = {}
            for propertyName in locations["Properties"][propertySet]:
                if propertyName in portfolio["Property List"][player]:
                    show_properties_dict[propertySet][propertyName] = portfolio["Owned Properties"][player][propertyName]
        result_dict = {key: value for key, value in show_properties_dict.items() if value}
        print(result_dict)

        landmarkChoice = str(input("Which landmark would you like to build on?: "))
        landmarkChoice = landmarkChoice.upper()
        if landmarkChoice not in portfolio["Property List"][player]: # player does not own the property
            print(f"You do not own {landmarkChoice}!")
        elif landmarkChoice in portfolio["Property List"][player]:  # player owns property
            missing_in_set = []
            for landmarkSet in locations['Properties'].keys():
                if landmarkChoice in locations['Properties'][landmarkSet]:
                    correctLandmarkSet = landmarkSet
                    break
                else:
                    continue

            for landmarkName in locations['Properties'][correctLandmarkSet]:
                if landmarkName in portfolio["Property List"][player]:
                    continue
                else:
                    missing_in_set.append(landmarkName)

            if missing_in_set: # missing a property in the property set
                hasPropertySet = False 
                print(f"You do not own the {correctLandmarkSet} property set!")
                print(f"You are missing {missing_in_set} to complete the set! ")
            else: # owns complete set (all properties in set)
                hasPropertySet = True

            if hasPropertySet == True: # player owns property and property set
                currentNumHouses = portfolio['Owned Properties'][player][landmarkChoice]
                print(f"You currently have {currentNumHouses}/5 houses on {landmarkChoice}")

                while True:
                    houseCost = board['Building Prices'][landmarkChoice]
                    numHousesBuild = int(input(f"Each house costs {houseCost} to build for this property. How many would you like to build?: "))

                    if (numHousesBuild < 1) or (numHousesBuild > 5):
                        print("You can build a minimum of 1 and a maximum of 5 houses, input a valid number")
                        continue
                    elif currentNumHouses + numHousesBuild > 5:
                        print("You can have a maximum of 5 houses on a single property. Please input a new number")
                        continue
                    else:
                        portfolio["Owned Properties"][player][landmarkChoice] = currentNumHouses + numHousesBuild
                        print(f"{player} built {numHousesBuild} on {landmarkChoice}")
                        print(f"{player} now has {portfolio['Owned Properties'][player][landmarkChoice]} houses on {landmarkChoice}")
                        print(f"Current Balance: ${portfolio['Finances'][player]}\n")
                        break
        else:
            print(f"{landmarkChoice} is not an existing landmark! Please input a valid landmark name (space sensitive). Please try again.")
            continue
        
        buildMoreHouses = str(input("Would you like to continue building? (yes or no): "))
        buildMoreHouses = buildMoreHouses.lower().strip()


        if buildMoreHouses == "yes":
            continue
        elif buildMoreHouses == "no":
            break



##### PLAY MONOPOLY #####
def play(players, portfolio, board, locations):
    import random
    freeParking = 0 # amount in free parking
    player_positions = {} # keep track of where players are on board
    for player in players: 
        player_positions[player] = 0 # intialize all positions at GO

    while True: # until someone loses
        doublesCount = 0
        for player in players:
            print(f"{player}'s turn!")
            print(f"Current Balance: ${portfolio['Finances'][player]}") # show current bank balance
            print("Owned Properties:")
            show_properties_dict = {}
            for propertySet in locations["Properties"].keys():
                show_properties_dict[propertySet] = {}
                for propertyName in locations["Properties"][propertySet]:
                    if propertyName in portfolio["Property List"][player]:
                        show_properties_dict[propertySet][propertyName] = portfolio["Owned Properties"][player][propertyName]
            result_dict = {key: value for key, value in show_properties_dict.items() if value}
            print(result_dict)
            # print(f"Owned Properties: {portfolio['Owned Properties'][player]}\n") # show owned properties
            print(f"\nBeginning turn at {board['Board Locations'][player_positions[player]]}")
            while True: # until player's turn is over
                canRoll = True
                if board['Board Locations'][player_positions[player]] == "IN JAIL":
                    position = jail(portfolio, player)
                    player_positions[player] = position
                    if position == 999: # remain in jail
                        print("---------------------------------------------------------------")
                        break
                    elif position > 10: # rolled a double
                        canRoll = False
                        pass
                    else: # paid or waited 3 turns (position == 10)
                        pass

                if canRoll is not False:
                    print("'B' for Build or 'R' for Roll")
                    choice = str(input(f"{player}, indicate your option (B or R): "))
                    choice = choice.strip().lower()
                    print()

                # Build
                if choice == "b":
                    buildHouses(portfolio, player, board, locations)
                    print()

                # Roll
                if canRoll is not False:
                    isDouble, roll = rollDice()
                    print(f"You rolled a {roll}!")

                position = player_positions[player] # get current player's position
                if canRoll is not False:
                    if (position + roll > 39) and (position + roll < 52):
                        position = position + roll - 40
                        print("Passed GO, collect $200")
                        portfolio['Finances'][player] += 200
                        print(f"{player}'s new bank balance: ${portfolio['Finances'][player]}")
                    elif position + roll > 52:
                        position = 999
                    else:
                        position += roll

                    
                location = board['Board Locations'][position]
                print(f"You landed on {location}!\n")

                ### ----------- CORNERS ------------- ###    
                if location == "FREE PARKING":
                    print(f"Current amount accumilated in free parking: {freeParking}")
                    if freeParking != 0:
                        print(f"Collect ${freeParking} collected in Free Parking!")
                        portfolio["Finances"][player] += freeParking
                        print(f"{player}'s new bank balance: ${portfolio['Finances'][player]}")
                        freeParking = 0
                
                if location == "GO TO JAIL":
                    print(f"{player} got put behind bars!")
                    position = 999 # jail location
                    location = board['Board Locations'][position]
                
                ### ------------- TAX -------------- ###
                if (location == "INCOME TAX") or (location == "LUXURY TAX"):
                    tax_amount = 200 if location == "INCOME TAX" else 100
                    print(f"Pay ${tax_amount} in {location}")
                    portfolio['Finances'][player] -= tax_amount
                    print(f"{player}'s new bank balance: ${portfolio['Finances'][player]}")
                    freeParking += tax_amount # add tax to free parking

                ### ----------- CHANCE ------------- ###
                if location == "CHANCE": # chance cards
                    chance = random.choice(locations['Chance'])
                    print(f"Chance card: {chance}")
                    chance_index = locations['Chance'].index(chance)
                    new_position, movedPosition = chanceCards(chance_index, player, players, portfolio, position)

                    if movedPosition:
                        position = new_position
                        location = board['Board Locations'][position]

                ### ------- COMMUNITY CHEST --------- ###
                if location == "COMMUNITY CHEST": # community chest cards
                    commChest = random.choice(locations['Community Chest'])
                    print(f"Community chest card: {commChest}")
                    commChest_index = locations['Community Chest'].index(commChest)
                    new_position, movedPosition = communityChestCards(commChest_index, player, players, portfolio, position, locations)

                    if movedPosition:
                        position = new_position
                        location = board['Board Locations'][position]

                ### ---------- PROPERTY ------------ ###
                isProperty = checkProperty(location, locations)

                if isProperty:
                    portfolio = propertyCards(player, players, board, portfolio, location, locations, roll)


                # update position
                player_positions[player] = position

                if location == "IN JAIL":
                    print("---------------------------------------------------------------")
                    break
                elif isDouble:
                    print()
                    print("Go again, you rolled a double!")
                    print(f"Currently at {board['Board Locations'][player_positions[player]]}\n")
                    doublesCount += 1
                    continue
                elif portfolio['Finances'][player] < 0:
                    print(f"{player} ran out of money!!! {player} loses!\n")
                    print("FINAL RANKINGS:")
                    final_rankings = []
                    for i in players:
                        final_rankings.append(portfolio["Finances"][i])
                    final_rankings.sort(reverse = True)

                    if len(players) == 2:
                        for player in players:
                            if final_rankings[0] == portfolio["Finances"][player]:
                                print(f"1st Place: {player}")
                            else:
                                print(f"2nd Place: {player}")
                    else: # 3 or more players
                        for player in players:
                            if final_rankings[0] == portfolio["Finances"][player]:
                                print(f"1st Place: {player}")
                            elif final_rankings[1] == portfolio["Finances"][player]:
                                print(f"2nd Place: {player}")
                            elif final_rankings[2] == portfolio["Finances"][player]:
                                print(f"3rd Place: {player}")
                            else:
                                continue

                    print("\nThanks for playing Stevenopoly!!!")
                    exit()
                elif doublesCount == 3:
                    print("You rolled 3 consecutive doubles, GO TO JAIL!!!\n")
                    print("---------------------------------------------------------------")
                    player_positions[player] = 999
                    break
                else:
                    print()
                    print(f"Ending turn at {board['Board Locations'][player_positions[player]]}\n")
                    print("---------------------------------------------------------------")
                    break


                        
def main():
    numPlayers = int(input("How many players (minimum of 2)?: "))
    players = []
    for i in range(numPlayers):
        player = str(input(f"Input player {i + 1} name: "))
        players.append(player)

    print(f"\nWelcome to Stevenopoly! Have Fun!\n")

    locations = create_locations()
    board = create_board()
    portfolio = create_portfolio(players)
    play(players, portfolio, board, locations)

if __name__ == "__main__":
    main()