#
# File: fileName.py
# Author: your name
# SAIBT Id: your email id
# Description: Assignment 1 - place assignment description here...
# This is my own work as defined by the University’s
# Academic Misconduct policy.
#

import random
import sys



def start_game():
	player_choice = input("Would you like to play Steal or Deal [y|n]?")

	if(player_choice == "y"):
		n = 1
		while n<=2:
			play()
			n+=1
		print ("game limit reached")
		

	elif(player_choice == "n"):
		quit()

	else: 
		start_game()

def play():

	print("Jackpot: 200")
	choice2 = input("Steal, Deal or Quit [S|D|Q]?")
	if (choice2 == "s" or choice2 == "S"):
		steal()

	elif (choice2 == "d" or choice2 == "D"):
		deal()

	elif (choice2 == "q" or choice2 == "Q"):
		quit()

	else:
		play()
	
def steal():	

		computer_choice = random.randint(1,2)
		
		if (computer_choice==1):
			computer_choice = "Steal"
			computer_winnings = 0
			player_winnings = 0
			a = str(computer_winnings)
			b = str(player_winnings)
			message1 = "Too greedy !"
			message2 = "You get nothing !"

		elif(computer_choice==2):
			computer_choice="Deal"
			computer_winnings = 0
			player_winnings = 200
			a = str(computer_winnings)
			b = str(player_winnings)
			message1 = "You win !"
			message2 = "Jackpot !"

		print("C:  Steal  |  ",computer_choice)
		print("\nS:  ",b+"  |  ",a)
		print(message1 , message2, sep='\n')


def deal():	

		computer_choice = random.randint(1,2)

		if (computer_choice==1):
			computer_choice = "Steal"
			computer_winnings = 200
			player_winnings = 0
			a = str(computer_winnings)
			b = str(player_winnings)
			message1 = "You loose !"
			message2 = "You get nothing !"

		elif(computer_choice==2):
			computer_choice="Deal"
			computer_winnings = 100
			player_winnings = 100
			a = str(computer_winnings)
			b = str(player_winnings)
			message1 = "Draw !"
			message2 = "Split pot !"

		print("C:  Deal  |  ",computer_choice)
		print("\nS:  ",b+"  |  ",a)
		print(message1 , message2, sep='\n')

def quit():
	sys.exit("No worries... another time perhaps... :)")





start_game()