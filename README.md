## The Monty Hall Problem
This application is simulator for the famous problem known as the monty hall problem. The problem refers to a game show hosted by Monty Hall. For part of his show he would show th audience and a contestant 3 doors and tell them one door has a prize behind it. If the contestant chose the right door he would win the prize. What made it an interesting problem, is that once the contestant picked a door Monty would show the contestant that a different door (not the one they picked) didn't have the car behind it. He would then ask the contestant if they would like to change their choice to the remaining door. 

## Application Description
The project so far is split into three scripts. 
Montyhall.py contains a class representing one instance of the game show. An instance of montyhall takes arguments of a boolean representing whether or not the player would like to swap and an integer representing the players guess. The function returns True or False depending on whether the door the player ends up on had the car behind it. 
Contestant is a class that allows the user to run the game a certain number of times. Contestant takes a parameter runs. Runs represents the number of times the user would like to run the game. The function call contestant.play() will play the game runs times with both swap as True and swap as False. It then returns the number of wins and the number of iterations for both swap and stay.
Graph runs contestant 10000 times and outputs the data it produces. Number of iterations can easily be changed by changing the value of the runs variable on line 5.

## Usage
The are commented out examples of inputs at the bottom of each file.

## Findings
Naturally, as would be expected, with a reasonable number of trials, swap has aprox 2/3 rate of success and stay has a aprox 1/3 chance of success.
Below is a example of output from graph with the default of 10000 runs:

![montyHallGraph](https://user-images.githubusercontent.com/56383304/110052821-f1837e80-7da3-11eb-8c28-e6ed21302724.png)
