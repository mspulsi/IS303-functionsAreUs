# a file of all the functions
import random

def start(): 
    # get the username and then output a simple explanatory message for how the game works.
    userName = input("What is your name?: ")
    print(f"Welcome {userName} to our soccer game simulation!\n")
    print("How the game works:\n")
    print("You'll choose a home team and opponents to play from a list of teams we provide that are in the Big 12.\nOur code will simulate a soccer season and will report your game record.\nFollow the prompts to play!\n")
    return userName

def displayMenu():
    # set a while loop to ensure all inputs are valid
    exitloop = False
    while exitloop == False:
        # implement try to make sure an integer is entered
        try:
            # ask for user input and check to make sure it is 1, 2, or 3
            iMenuChoice = int(input("\nMenu\n     1. Simulate a game\n     2. See your team's record\n     3. Quit\n\nEnter 1, 2, or 3: "))
            if iMenuChoice != 1 and iMenuChoice != 2 and iMenuChoice != 3:
                print("\nInvalid choice.  Please enter a number from the menu.")
            else:
                exitloop = True
        except:
            print("\nInvalid input.  Please enter a number from the menu.")        
    return iMenuChoice

def getGameScore():
    # generate two random scores
    iOppScore = random.randint(0,5)
    iHomeScore = random.randint(0,5)
    
    #check to make sure the scores do not equal to prevent a tie
    while iHomeScore == iOppScore :
        iHomeScore = random.randint(0,5)
        iOppScore = random.randint(0,5)

    # with the random scores determine whether the home team won or lost
    sWinLose = ""
    if iHomeScore > iOppScore :
        sWinLose = "win"
    else :
        sWinLose = "loss"
    # return the scores and whether it is a win or loss
    lGameResult = [iHomeScore, iOppScore, sWinLose]
    return lGameResult

def selectTeams(homeTeam = None):
    listTeams = ["Arizona State", "Arizona", "BYU", "Baylor", "Cincinnati", "Colorado", "Houston", "Iowa State", "Kansas", "Kansas State", "Oklahoma State", "TCU", "Texas Tech", "UCF", "Utah", "West Virginia"]
    if homeTeam == None :
        # display menu with all team names
        for iCount in range(0, len(listTeams)): 
            print(f"{str(iCount+1)}. {listTeams[iCount]}")

        # receive home team selection
        bContinue = False
        while bContinue == False:
            try:
                iHomeTeamSelection = int(input("\nEnter the number of the home team: "))
                sTeamSelection = listTeams[(iHomeTeamSelection - 1)]
                print(f"\n{sTeamSelection} is the home team\n")
                bContinue = True
                return sTeamSelection
            except (IndexError, ValueError):
                print("\nInvalid choice. Please enter a number from the menu.")

    else:
        listTeams.remove(homeTeam)
        # display menu with all other team names except the home team
        for iCount in range(0, len(listTeams)): 
            print(f"{str(iCount+1)}. {listTeams[iCount]}")

        # get opposing team selection
        bContinue = False
        while bContinue == False:
            try:
                iOppTeamSelection = int(input("\nEnter the number of the opposing team: "))
                sTeamSelection = listTeams[(iOppTeamSelection - 1)]
                print(f"\n{sTeamSelection} is the away team\n")
                bContinue = True
                return sTeamSelection
            except (IndexError, ValueError):
                print("\nInvalid choice. Please enter a number from the menu.")
    
def printRecord(sTeamName, dTeamRecord):
    # print out all of the games with their corresponding opposing team and scores
    # also, count the amount of wins and losses to create the final win-loss record
    iWins = 0
    iLosses = 0
    print("\n")
    for sCurrTeamName in dTeamRecord :
        print(f"{sTeamName}'s score: {str(dTeamRecord[sCurrTeamName][0])} {sCurrTeamName}'s score: {str(dTeamRecord[sCurrTeamName][1])}")
        if dTeamRecord[sCurrTeamName][2] == "win" :
            iWins += 1
        else :
            iLosses += 1

    # with the info gathered from the above loop, print out the final win-loss record
    print(f"\nFinal season record: {sTeamName} {str(iWins)}-{str(iLosses)}")

    # finally, calculate the win percentage and print out the appropiate message for the teams record
    fWinLossPercentage = iWins / len(dTeamRecord)
    if fWinLossPercentage >= 0.75 :
        print("Qualified for the NCAA Women's Soccer Tournament")
    elif fWinLossPercentage >= 0.5 :
        print("You had a good season")
    else :
        print("Your team needs to practice!")