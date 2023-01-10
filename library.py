import random


words = ["Casino", "oropa", "afghanestan", "pride", "motor 125", "karkhone", "kotlet", "asia", "lavashak", "sibil", "arsalan", "sib", "khorshid" ]

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


