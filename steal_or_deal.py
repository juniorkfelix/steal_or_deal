#
# File: fileName.py
# Author: your name
# SAIBT Id: your email id
# Description: Assignment 1 - place assignment description here...
# This is my own work as defined by the University’s
# Academic Misconduct policy.
#
import random


player_choice = input("Would you like to play Steal or Deal [y|n]?")


if(player_choice == "y"):
	print("Jackpot: 200")
	choice2 = input("Steal, Deal or Quit [S|D|Q]?")
	

	if (choice2 == "s"):

		computer_choice = random.randint(1,2)
		
		if (computer_choice==1):
			computer_choice = "Steal"

		elif(computer_choice==2):
			computer_choice="Deal"

		print("C:  Steal  |  ",computer_choice)


	elif (choice2 == "d"):
		computer_choice = random.randint(1,2)

		if (computer_choice==1):
			computer_choice = "Steal"

		elif(computer_choice==2):
			computer_choice="Deal"
		print("C:  Deal  |  ",computer_choice)


	elif (choice2 == "q"):
		print("No worries... another time perhaps... :) ")

	else:
		print("invalid choice")


elif(player_choice == "n"):
	print("No worries... another time perhaps... :)")


else:
	print("invalid choice")