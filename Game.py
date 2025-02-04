import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


choice = input("Enter... \n 1: for Rock \n 2:for Paper \n 3:for Scissors\n\n ")
player = int(choice) 

Pc_choice = random.choice("123")
computer = int(Pc_choice)

if player < 1 or player > 3:
    sys.exit("Chose between 1,2 and 3 only ")

print("")
print("You chose : " + str(RPS(player)).replace('RPS.',''))
print("You chose : " + str(RPS(computer)).replace('RPS.',''))
print("")



if player == 1 and computer == 3:
    print("You won ")
elif player == 3 and computer == 2:
    print("You won ")
elif player == 2 and computer == 3:
    print("You won ")
elif player == computer:
    print("Match Tie ")
else:
    print("Python Win")


