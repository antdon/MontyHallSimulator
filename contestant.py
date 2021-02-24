import os
import sys
import pdb
from random import *


def remaining_door(line, choice):
    notchange = int(line[86])
    doors = [1,2,3]
    doors.remove(choice)
    doors.remove(notchange)
    return(str(doors[0]))

def contestant(change):
    (read_fd, write_fd) = os.pipe() #Create pipe1
    (read_fd2, write_fd2) = os.pipe() #Create pipe2
    n = os.fork()
    if n == 0:
        #child process
        os.dup2(read_fd, 0) #replace stdin with the read end of pipe1
        os.close(write_fd)
       #os.dup2(write_fd2, 1) #replace stdout with the write end of pipe2
        os.execlp("python3", "python3", "montyhall.py") 
    else:
        #parent process
        os.dup2(write_fd, 1) #replace stdout with the write end of pipe1
       #os.close(read_fd) 
       #os.dup2(read_fd2, 0) #replace stdin with the read end of pipe 2
       #os.close(read_fd2) 
        choice = randint(1,3)
        input("")
        print(choice)
        input("")
        if change == False:
            print("n")
            didYouWin = input("")
            if didYouWin[0] == "C":
                return True
            else:
                return False
        else:
            print("y")
            line = input("")
            remainingDoor = remaining_door(line, choice)
            print(remainingDoor)
            didYouWin = input("")
            if didYouWin[0] == "C":
                return True
            else:
                return False
            
boy = contestant(True)
if boy:
    print("yeah", sys.stderr)
else:
    print("nah", sys.stderr)










