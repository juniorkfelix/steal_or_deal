#
# File: fileName.py
# Author: your name
# SAIBT Id: your email id
# Description: Assignment 1 - place assignment description here...
# This is my own work as defined by the University’s
# Academic Misconduct policy.
#


choice = input("Would you like to play Steal or Deal [y|n]?")

if(choice == "y"):
	print("Jackpot: 200")
	choice2 = input("Steal, Deal or Quit [S|D|Q]? S")

	if (choice2 == "s"):
		print("Steal")

	elif (choice2 == "d"):
		print("Deal")

	elif (choice2 == "q"):
		print("Quit")

	else:
		print("invalid choice")


elif(choice == "n"):
	print("No worries... another time perhaps... :)")

else:
	print("invalid choice")