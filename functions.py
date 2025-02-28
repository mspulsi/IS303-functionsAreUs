# a repository of all the functions
def start(): 
    userName = input("What is your name?: ")
    print(f"Welcome {userName}!")
    print("How this game works:"
          "\n1) It asks you for the name of your team and the total number of games your team will play this season\n"
          "2) it asks for the name of the opponents for each game.\n"
          "3) The game will then randomly generate the scores for each of those games\n"
          "4) It will display the scores generated for those games along with the home and opposing team names\n"
          "5) It displays a win-loss record and tells you how your team did! (needs improvement, qualified for NCAA tournament, etc.)")
    