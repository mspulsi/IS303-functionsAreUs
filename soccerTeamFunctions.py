# Matthew Pulsipher, Logan Hodges, Saxon Cullimore, Markus Walker, Scott Peterson
# Professor Anderson
# Section 2
# Definition: simulate a womens soccer team season by taking user input, randomizing scores for season games,
# and outputing the team's record with an accompanying evaluation of the record. this time utilizing functions
# defined in another python file.


from functions import *

dTeamRecord = {}
sUserName = start()
sHomeTeam = selectTeams()

iMenuChoice = displayMenu()
while iMenuChoice != 3:
    if iMenuChoice == 1:
        sOppTeam = selectTeams(sHomeTeam)
        dTeamRecord[sOppTeam] = getGameScore()
        if dTeamRecord[sOppTeam][2] == "win":
            print(f"Congrats {sUserName}, your team won. {sHomeTeam}: {dTeamRecord[sOppTeam][0]} {sOppTeam}: {dTeamRecord[sOppTeam][1]}")
        else:
            print(f"Sorry {sUserName}, your team lost. {sHomeTeam}: {dTeamRecord[sOppTeam][0]} {sOppTeam}: {dTeamRecord[sOppTeam][1]}")
    else:
        printRecord(sHomeTeam, dTeamRecord)
    iMenuChoice = displayMenu()
    
print(f"\nThanks for playing, goodbye {sUserName}")
