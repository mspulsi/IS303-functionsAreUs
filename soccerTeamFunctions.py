# Matthew Pulsipher
# Professor Anderson
# Section 2
# Definition: simulate a womens soccer team season by taking user input, randomizing scores for season games,
# and outputing the team's record with an accompanying evaluation of the record. 

import random

# intialize necessary variables to store user input
dGameRecord = {}
sTeamName = input("Enter the Home Team's name: ")
iGameCount = int(input("Enter how many games for the season: "))
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





from functions import selectTeams

# print welcome message (we should include something about the Big 12 because that's where I got the teams from)
# first function goes here

# set list of teams
listTeams = ["Arizona State", "Arizona", "BYU", "Baylor", "Cincinnati", "Colorado", "Houston", "Iowa State", "Kansas", "Kansas State", "Oklahoma State", "TCU", "Texas Tech", "UCF", "Utah", "West Virginia"]

# print menu options and receive choice (simulate a game or display a team's record)
# iMenuChoice = second function (make the user try again if they enter an invalid option (not 1, 2, or 3))

#if the user selects this option, simulate a game, print results, and save in dictionary
selectTeams(listTeams)
# we would probably put my function in the simulate game function, so the final syntax will look something like this:
# fourthFunction(selectTeams(listTeams))

# if the user selects this option, print the list of teams and show the record of the team that the user selects (return an error message if the team has not played any games)
# fifth function goes here

# if the user selects this option, exit the program\