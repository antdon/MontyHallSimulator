import pdb
from random import *
from montyhall import Montyhall

class contestant:
    def __init__(self, runs):
        self.runs = runs
    def play(self):
        swapCount = 0
        stayCount = 0
        for i in range(self.runs):
            monty = Montyhall(True, randint(1,3))
            if monty.runGame() == True:
                 swapCount += 1
        for i in range(self.runs):
            monty2 = Montyhall(False, randint(1,3))
            if monty2.runGame() == True:
                 stayCount += 1

        return([["swap", swapCount/self.runs],["stay", stayCount/self.runs]])

#example
#anton = contestant(10000)
#print(anton.play())











