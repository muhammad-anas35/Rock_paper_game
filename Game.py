import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


choice = input("Enter... \n1: for Rock \n 2:for Paper \n 3:for Scissors\n\n ")
player = int(choice) 
if player < 1 or player > 3:
    sys.exit("Chose between 1,2 and 3 only ")
# print("You chose : " + str(RPS(player)).replace('RPS.',''))