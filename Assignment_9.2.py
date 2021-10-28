# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: <author>
# Creation Date: <date>
# Below is a simple program with 10 issues (some are syntax errors and some are logic errors.  You need to identify the issues and correct them.

import random
import time

def displayIntro():
	print('''You are in a land full of dragons. In front of you,
	you see two caves. In one cave, the dragon is friendly
	and will share his treasure with you. The other dragon
	is greedy and hungry, and will eat you on sight.''')
	print()

def chooseCave():
#    cave = ''
	cave = ''
# Threw error due to mixing spaces and tabs
	while cave != '1' and cave != '2':
		print('Which cave will you go into? (1 or 2)')
		cave = input()

#	return caves
	return cave
# Caves not defined. Should be cave.

def checkCave(chosenCave):
	print('You approach the cave...')
	#sleep for 2 seconds
	time.sleep(2)
	print('It is dark and spooky...')
	#sleep for 2 seconds
	time.sleep(3)
	print('A large dragon jumps out in front of you! He opens his jaws and...')
#	print()
# Blank Line or No Line
# Unnecessary
	#sleep for 2 seconds
	time.sleep(2)
	friendlyCave = random.randint(1, 2)

	if chosenCave == str(friendlyCave):
		print('Gives you his treasure!')
	else:
#		print 'Gobbles you down in one bite!'
		print('Gobbles you down in one bite!')
# Used spaces instead of paranthesis

playAgain = 'yes'
#while playAgain = 'yes' or playAgain = 'y':
while playAgain == 'yes' or playAgain == 'y':
# Requires double equal for exact input
	displayIntro()
#	caveNumber = choosecave()
	caveNumber = chooseCave()
# Wrong case to call function
	checkCave(caveNumber)
    
	print('Do you want to play again? (yes or no)')
	playAgain = input()
	if playAgain == "no":
#		print("Thanks for planing")
		print("Thanks for playing")
# Typo in print. Probably not one of the corrections the instructor is looking for since it is not syntax or logic.
