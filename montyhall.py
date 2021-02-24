from random import *
car_door = randint(1,3)
doors = [1,2,3]
doors.remove(car_door)
answer_invalid = True

if __name__ == "__main__":
    while answer_invalid:
        choice = input("You have a choice of door 1 2 and 3 which door do you think the car is behind: ")
        if choice == '1' or choice == '2' or choice == '3':
            answer_invalid = False
            choice = int(choice)

    if choice != car_door:
        doors.remove(choice)
    if len(doors) == 2:
        opendoor = doors[randint(0,1)]
    else:
        opendoor = doors[0]
    change = input(f"oooo interesting choice. I can assure you that one of the doors you did not pick, door {opendoor} is not correct door \nknowing this do you want to change your answer(y/n) ")
    if (change == 'y'):
        choice = int(input("what would you like to change your answer to? "))
    if choice == car_door:
        print("Congratulations your were correct you won the car")
    else:
        print("Unlucky you were incorrect")

    
    


