"""
========================
Rock Scissors Paper v0.12
======================== 

@author Jason Kim
@created 12-10-2016

"""

import random

def computer_hand():
    """
    ramdomly generate compyter hand
    """
    return random.randrange(0, 3)

def win_lose(computer, player):
    """
    determines who wins or lose
    """
    if(computer == player):
        return "tied"
    elif(computer == 0):
        if(player == 1):
            return "lost"
        else:
            return "won"
    elif(computer == 1):
        if(player == 0):
            return "won"
        else:
            return "lost"
    elif(computer == 2):
        if(player == 0):
            return "lost"
        else:
            return "won"

def get_input():
    """
    get player input
    """
    i = 0
    player = input("// rock : 0, scissors : 1, paper : 2 //\n--> ")
    while not(player.isdigit() and (0 <= int(player) <= 2)):
        if(i == 0):
            player = input("input from above\n--> ")
        elif(i == 7):
            player = input("are you blind?\n--> ")
        else:
            player = input("--> ")
        i += 1
    return player

def main():
    """
    main function
    """
    rsp = ["rock", "scissors", "paper"]
    computer = computer_hand()
    player = get_input()

    print("computers hand was " + rsp[computer] + "\nyou " + win_lose(computer, int(player)))

main()
