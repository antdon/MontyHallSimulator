from random import *
import pdb


class Montyhall:
    def __init__(self, swap, guess):
        self.doors = [1,2,3]
        self.car = self.doors[randint(0,2)]
        self.swap = swap
        self.guess = guess

    def runGame(self):
        self.doors.remove(self.guess)
        if self.swap == True:
            if self.guess == self.car:
                opendoor = self.doors[randint(0,1)]
            else:
                self.doors.remove(self.car)
                opendoor = self.doors[0]
                self.doors.append(self.car)
            self.doors.remove(opendoor)
            self.guess = self.doors[0]
        if self.guess == self.car:
            return True
        else:
            return False

#example
#   p = Montyhall(True,1)
#   if p.runGame() == True:
#       print("win")
#   else:
#       print("lose")



        
