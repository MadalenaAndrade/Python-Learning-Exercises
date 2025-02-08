# Write your solution here
from random import choice

def roll(die: str):
    die_a = "333336"
    die_b = "222555"
    die_c = "144444"

    if die == "A":
        return int(choice(die_a))
    elif die == "B":
        return int(choice(die_b))
    else:
        return int(choice(die_c))
    
def play(die1: str, die2: str, times: int):
    die1_wins = 0
    die2_wins = 0
    ties = 0

    while times != 0:
        roll_first = roll(die1)
        roll_second = roll(die2)
        if roll_first > roll_second:
            die1_wins += 1
        elif roll_first < roll_second:
            die2_wins += 1
        else:
            ties += 1
        times -= 1
    
    return die1_wins, die2_wins, ties

