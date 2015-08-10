#!/usr/bin/env python
# HW04_ex00

# Create a program that does the following:
#     - creates a random integer from 1 - 25
#     - asks the user to guess what the number is
#     - validates input is a number
#     - tells the user if they guess correctly
#         - if not: tells them too high/low
#     - only lets the user guess five times
#         - then ends the program
################################################################################
# Imports

from random import randint


# Body

def fiveGuesses():
	randomNumber = randint(1,25)
	guesses = 1
	while guesses <= 5:
		guess = raw_input("Guess a number between 1 and 25, please: \n")
		guess = int(guess)
		if type(guess) != int:
			guess = raw_input("Hey, that's not a number. Please enter a number. \n")
		elif guess > randomNumber:
			print("Too high! Try again.")
			guesses = guesses + 1
		elif guess < randomNumber: 
			print("Too low! Try again.")
			guesses = guesses + 1
		else: 
			print("Good work; you guessed it right!")
	if guesses > 5:
		print("Ope! You've run out of guesses. Better luck next time!")


################################################################################
def main():


    print("Hello World!") # Remove this and replace with your function calls

    fiveGuesses()
    

if __name__ == '__main__':
    main()