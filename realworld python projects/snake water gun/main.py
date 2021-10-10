import random


def winner(comp, player):

    if comp == "snake":
        if player == "gun":
            return True
        elif player == "water":
            return False
        if player == "snake":
            return "another"
    elif comp == "water":
        if player == "snake":
            return True
        elif player == "gun":
            return False
        if player == "water":
            return "another"
    elif comp == "gun":
        if player == "snake":
            return False
        elif player == "water":
            return True
        if player == "gun":
            return "another"
    else:
        print("please choose only from s , w and g")


randomnum = random.randint(1, 3)

if randomnum == 1:
    comp = "water"
elif randomnum == 2:
    comp = "snake"
elif randomnum == 3:
    comp = "gun"


player = input("Your Turn Say : snake(s) , water(w) or gun(g)")

if player == "w":
    player = "water"
elif player == "s":
    player = "snake"
elif player == "g":
    player = "gun"

a = winner(comp, player)


if a == True:
    print(f"You won😊🥳.\nYou choose {player} and computer choose {comp}")
    game_over=True

elif a == False:
    print(f"You lost😢.\nYou choose {player} and Computer choose {comp}")

elif a == "another":
    print(f"Game Tied🤦‍♂️🤷‍♂️.\nYou choose {player} and Computer also choose {comp}")

else:
    print("please only choose from s,w and g")
