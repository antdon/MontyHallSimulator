import pdb
from random import *
from montyhall import Montyhall

class Contestant:
    def __init__(self, runs):
        self.runs = runs
    def play(self) -> []:
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

        return([("swap wins", swapCount), ("swap runs", self.runs), ("stay wins", stayCount), ("stay runs", self.runs)])

#example
anton = Contestant(100000)
print(anton.play())











