Below are the original instructions for the project:

Project 1
Text Adventure

Introduction

You will create a simple text adventure game! The player should be provided with a game "world" that has the following features:

Requirements

Write at least 3 functions corresponding to areas or rooms to explore. Each area should provide the player with a brief description and things for the player to interact with. When the user enters a room, any global variables for things they have, like HP or treasure, will go with them. When they exit the room, the states of those variables are returned and updated as needed.
There should be at least one value that tracks progress (wealth, health, number of treasures found, etc.) These statistics must have some affect on the user's progress. For example, a puzzle may require a certain number of items or the game might end if the user reaches 0 health points.
The player carries a backpack that has holds items. The player can look in their backpack at any point and see what items they currently hold. Of course, that means there should be a way for the player to collect items and way for them to be used to make progress in your adventure. You must handle this by making a function that is called whenever the user checks their backpack. Then, you can reuse this function in every room the user might visit. You must utilize the backpack to solve a puzzle or advance the user's progress in some non-trivial way in order to receive full points.
Valid commands should be written out to the user. The player needs to be able to enter commands (a direction, identify an object to pick up, etc.). Tell the user what options they have before they input. If the user types an invalid command it should simply loop back to the start of the “room” and ask them to input a valid option.
Code must be well documented, including having the author's name at the top of the program source code. Variables should follow good naming conventions and not be generically named.
You may NOT use the “global” keyword in your functions (see rubric below; most categories have high point penalties for using it). You must send variables as arguments and return them when the player has finished the area.
Total: 80 points (see rubric at bottom of page)

Bonus: 10 points: Implement a way for a user to save their progress to a file, and a way to load their progress to resume their game. You will have to use file close/open operations.

