# a file of all the functions

# receives username and displays welcome message and menu
def start(): 
    sUserName = input("What is your name?: ")
    print(f"Welcome {sUserName}!")
    print("Menu:\n 1. enter the game\n 2. ")
    

def selectTeams(listTeams = None):

    # display menu with all team names
    for iCount in range(0, len(listTeams)): 
        print(f"{str(iCount+1)}. {listTeams[iCount]}")

    # receive home team selection
    iHomeTeamSelection = int(input("\nEnter the number of the home team: "))
    sHomeTeam = listTeams[(iHomeTeamSelection - 1)]
    print(f"\n{sHomeTeam} is the home team\n")

    # disply menu options for opponent teams
    iHomeTeamSelection = iHomeTeamSelection - 1
    for iCount in range(0, iHomeTeamSelection):
        print(f"{str(iCount + 1)}. {listTeams[iCount]}")
    for iCount in range((iHomeTeamSelection + 1), len(listTeams)):
        print(f"{str(iCount)}. {listTeams[iCount]}")

    # receive opponent team selection
    iOpponentTeamSelection = int(input("\nNow enter the number of the opposing team: "))
    if iOpponentTeamSelection == 1:
        sOpponentTeam = listTeams[iOpponentTeamSelection]
        print(f"\n{listTeams[iOpponentTeamSelection]} is the away team\n")
    elif iOpponentTeamSelection <= iHomeTeamSelection: 
        sOpponentTeam = listTeams[(iOpponentTeamSelection - 1)]
        print(f"\n{listTeams[(iOpponentTeamSelection - 1)]} is the away team\n")
    elif iOpponentTeamSelection > iHomeTeamSelection:
        sOpponentTeam = listTeams[iOpponentTeamSelection]
        print(f"\n{listTeams[iOpponentTeamSelection]} is the away team\n")

    # return home and away teams
    return [sHomeTeam, sOpponentTeam]

