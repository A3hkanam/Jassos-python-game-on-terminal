# JASSOS GAME 
# importing the library that i need
import library
import os
import random


try:
    numberOfplayers = int(input("How many players are in the game : ")) 
except:
    print("Somthing went wrong plz try again !! \nBug Reason :")

if numberOfplayers <= 30:
    library.setPlayerNumber(numberOfplayers)
    Game_ready = True
elif numberOfplayers >= 30 : 
    Game_ready = False
    print("plz try a lower number to run a game")

# Starting Game
if Game_ready == True:
    Roles = library.startGame()

random_words = random.choice(library.words)

# Roles Picking up

MaxPlayer = 1
while MaxPlayer <= numberOfplayers:
    for i in range(1,numberOfplayers+1):
        player = ""
        print(f"<< Player {i} Role >>")
        player = input("[ Press Enter To Continue ]\ndo you want to know your Role ?? :")
        library.ShowPlayer(i)
        see_role = input("did you get your role ??")
        if see_role == "y" or "1":
            os.system("cls")

        MaxPlayer += 1
