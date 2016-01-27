
#-------------------Setup (This is where all of my definitions are)'

def travelTo(place):
    print("You have Travled to " + str(place))

def printCondition(condition, gameState):
    print("\n ... And you have " + str(condition) + "\n\n\n\n\n")
    if(condition == "dysentery"):
        gameState = False
    return gameState


def getNewLocation():
    newLocation = int(raw_input("Where should we go now? \n 1) Oregon \n 2) California \n 3) Utah \n"))
    if(newLocation == 1): return "Oregon"
    elif(newLocation == 2): return "California"
    elif(newLocation == 3): return "Utah"
    return "Never heardof that place before"

def getNewCondition():
    return "dysentery"

def game():
    print "\n\n\n\n\nHowdy Partner! Welcome to Nick's Oregon Trail"
    gameState = True
    location = "St. Louis"
    condition = "good health"

    while(gameState == True):
        location = getNewLocation()
        condition = getNewCondition()

        travelTo(location)
        gameState = printCondition(condition, gameState)

    print("\nThanks for playing! \n\n\n\n")




#----------------Main (this is where my program runs)

game()
