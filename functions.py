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



def displayMenu():
    exitloop = False
    while exitloop == False:
        try:
            iMenuChoice = int(input("\nMenu\n     1. Simulate a game\n     2. See a specific team's record\n     3. Quit\n\nEnter 1, 2, or 3: "))
            if iMenuChoice != 1 and iMenuChoice != 2 and iMenuChoice != 3:
                print("\nInvalid choice.  Please enter a number from the menu.")
            else:
                exitloop = True
        except:
            print("\nInvalid input.  Please enter a number from the menu.")        
    return iMenuChoice