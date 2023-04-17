#!/usr/bin/python3
import os
import random

def bagels():
	os.system('clear')

	# Introduce the game
	print('''I am thinking of a 3-digit number. Try to guess what it is.
	Here are some clues:
	When I say:     That means:
	  Pico            One digit is correct but in the wrong position.
	  Fermi           One digit is correct and in the right position.
	  Bagels          No digit is correct.

	I have though up a number.
	  You have 10 guesses to get it.''')

	# Variables
	guess = 1
	LIMIT = 10

	# Create a 3-digit number
	number = ""
	for _ in range(3):
		number += str(random.randint(0,9))


	# Loop through guesses until the user guess the number or run out of guesses
	while guess <= LIMIT:
		print(f"Guess #{guess}:")

		# Take the user's guess and validate it
		G = input("> ")

		while True:
			if G.isdigit():
				if 0 <= int(G) < 1000:
					break
				else:
					print("It should be a 3-digit number!")
			else:
				print("It should be only digits!")

			print("Try again.")
			print()
			print(f"Guess #{guess}:")
			G = input("> ")

		# Increment the guess
		guess += 1

		# Process the guess
		if G == number:
			print("You got it!")
		elif (G[0] in number) or (G[1] in number) or (G[2] in number):
			if (G[0] == number[0]) or (G[1] == number[1]) or (G[2] == number[2]):
				print("Fermi")
			else:
				print("Pico")
		else:
			print("Bagels")

# Main loop
while True:
	bagels()
	print("Do you want to play again? (yes or no)")
	resp = input("> ")
	if resp.lower() == "yes":

		continue
	else:
		break