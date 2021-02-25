from random import *


class montyhall:
    def __init__(self, swap, guess):
        self.doors = [1,2,3]
        self.car = self.doors[randint(0,2)]
        self.swap = swap
        self.guess = guess

    def runGame(self):
        self.doors.remove(self.guess)
        if self.swap == True:
            opendoor = self.doors[randint(0,1)]
            self.doors.remove(opendoor)
            self.guess = self.doors[0]
        if self.guess == self.car:
            return True
        else:
            return False

#Testing stuff
#   p = montyhall(False,1)
#   if p.runGame() == True:
#       print("win")
#   else:
#       print("lose")



        
