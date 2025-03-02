# Matthew Pulsipher, Logan Hodges, Saxon Cullimore, Markus Walker, Scott Peterson
# Professor Anderson
# Section 2
# Definition: simulate a womens soccer team season by taking user input, randomizing scores for season games,
# and outputing the team's record with an accompanying evaluation of the record. this time utilizing functions
# defined in another python file.


from functions import *

#initialize variables to hold essential user input and track the season record
dTeamRecord = {}
sUserName = start()
sHomeTeam = selectTeams()

#begin to take user imput to simulate a soccer season
iMenuChoice = displayMenu()
while iMenuChoice != 3:
    if iMenuChoice == 1:
        #call functions to retrieve an opposing team, a game score, and then output the results of that game.
        sOppTeam = selectTeams(sHomeTeam)
        dTeamRecord[sOppTeam] = getGameScore()
        if dTeamRecord[sOppTeam][2] == "win":
            print(f"Congrats {sUserName}, your team won. {sHomeTeam}: {dTeamRecord[sOppTeam][0]} {sOppTeam}: {dTeamRecord[sOppTeam][1]}")
        else:
            print(f"Sorry {sUserName}, your team lost. {sHomeTeam}: {dTeamRecord[sOppTeam][0]} {sOppTeam}: {dTeamRecord[sOppTeam][1]}")
    else:
        #print the season record by passing the record and home team to the print function
        printRecord(sHomeTeam, dTeamRecord)
    iMenuChoice = displayMenu()
    
# end of game message
print(f"\nThanks for playing, goodbye {sUserName}")
