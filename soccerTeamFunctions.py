# Matthew Pulsipher
# Professor Anderson
# Section 2
# Definition: simulate a womens soccer team season by taking user input, randomizing scores for season games,
# and outputing the team's record with an accompanying evaluation of the record. 

import random
from functions import *

# intialize necessary variables to store user input
dGameRecord = {}
start()

sTeamName = str(input("Enter the home team's name: "))
iGameCount = int(input("Enter how many games the team will play for the season: "))
print("\n")

# based on the input for how many games in the season, iterate through the following 
# to create a game score and opposing team for each game.
for iGameNum in range(iGameCount) :
    # get the name of opposing team for each game, then generate a random number for each team score
    sOppName = input(f"Enter the name of the away team for game {str(iGameNum + 1)}: ")
    iHomeScore = random.randint(0,5)
    iOppScore = random.randint(0,5)

    # if the scores are the same regenerate scores until they don't equal
    while iHomeScore == iOppScore :
        iHomeScore = random.randint(0,5)
        iOppScore = random.randint(0,5)

    # with the random scores determine whether the home team won or lost
    sWinLose = ""
    if iHomeScore > iOppScore :
        sWinLose = "win"
    else :
        sWinLose = "lose"
    # store the game into the game record dictionary
    dGameRecord[sOppName] = [iHomeScore, iOppScore, sWinLose]

# print out all of the games with their corresponding opposing team and scores
# also, count the amount of wins and losses to create the final win-loss record
iWins = 0
iLosses = 0
print("\n")
for sCurrTeamName in dGameRecord :
    print(f"{sTeamName}'s score: {str(dGameRecord[sCurrTeamName][0])} {sCurrTeamName}'s score: {str(dGameRecord[sCurrTeamName][1])}")
    if dGameRecord[sCurrTeamName][2] == "win" :
        iWins += 1
    else :
        iLosses += 1

# with the info gathered from the above loop, print out the final win-loss record
print(f"\nFinal season record: {sTeamName} {str(iWins)}-{str(iLosses)}")

# finally, calculate the win percentage and print out the appropiate message for the teams record
fWinLossPercentage = iWins / iGameCount
if fWinLossPercentage >= 0.75 :
    print("Qualified for the NCAA Women's Soccer Tournament")
elif fWinLossPercentage >= 0.5 :
    print("You had a good season")
else :
    print("Your team needs to practice!")