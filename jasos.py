# JASSOS GAME 
# importing the librarys that i need
import os
import random

# Words on Game ( you can add more )
words = ["Casino", "oropa", "afghanestan", "pride", "motor 125", "karkhone", "kotlet", "asia", "lavashak", "sibil", "arsalan", "sib", "khorshid" ]
random_words = random.choice(words)

# Funtions :
# a function that get a number of players 
def setPlayerNumber(number:int):
    d = {}
    global p

    for i in range(1,number+1):    
        d["player{0}".format(i)] = "shahrvand"
        p = d
    return p


def startGame():
    totalPlayers = len(p)

    global Maximum_jasos
    Maximum_jasos = len(range(1,totalPlayers, 4))

    for x in range(1, Maximum_jasos+1):
        y = random.randint(1, totalPlayers)
        p.update({f"player{y}":"jasos"})
    return p


random_words = random.choice(words)
def ShowPlayer(np):
    player_role = p.get(f"player{np}")
    if player_role == "shahrvand":
        print(f"your role is : << shahrvand >> \n The Word is : {random_words}" )
    else:
        print("your role is : !! jassos !!")


# Game On Terminal
try:
    numberOfplayers = int(input("How many players are in the game : ")) 
except:
    print("Somthing went wrong plz try again !! \nBug Reason :")

if numberOfplayers <= 30:
    setPlayerNumber(numberOfplayers)
    Game_ready = True
elif numberOfplayers >= 30 : 
    Game_ready = False
    print("plz try a lower number to run a game")

# Starting Game
if Game_ready == True:
    Roles = startGame()

# Roles Picking up
MaxPlayer = 1
while MaxPlayer <= numberOfplayers:
    for i in range(1,numberOfplayers+1):
        player = ""
        print(f"<< Player {i} Role >>")
        player = input("[ Press Enter To Continue ]\ndo you want to know your Role ?? :")
        ShowPlayer(i)
        see_role = input("did you get your role ??")
        if see_role == "y" or "1":
            os.system("cls")

        MaxPlayer += 1
print("Now have fun :)")