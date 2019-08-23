import random
import sys



def start_game():
	player_choice = input("Would you like to play Steal or Deal [y|n]?")

	if(player_choice == "y"):
		play()

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

		elif(computer_choice==2):
			computer_choice="Deal"

		print("C:  Steal  |  ",computer_choice)

def deal():	

		computer_choice = random.randint(1,2)

		if (computer_choice==1):
			computer_choice = "Steal"

		elif(computer_choice==2):
			computer_choice="Deal"
		print("C:  Deal  |  ",computer_choice)

	




def quit():
	sys.exit("No worries... another time perhaps... :)")



start_game()
