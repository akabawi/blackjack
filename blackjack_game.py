import time
import random

class deck:

	def __init__(self):
		self.cards_deck = ["2S","2H","2D","2C","3S","3H","3D","3C","4S","4H","4D","4C","5S","5H","5D","5C","6S","6H","6D","6C","7S","7H","7D","7C","8S","8H","8D","8C","9S","9H","9D","9C","10S","10H","10D","10C","JS","JH","JD","JC","QS","QH","QD","QC","KS","KH","KD","KC","AS","AH","AD","AC"]

	def shuffle_deck(self):

		self.cards_deck = random.sample(self.cards_deck, k=len(self.cards_deck))
		return self.cards_deck

class player:

	def __init__(self):
		self.hand=[]
		self.hand_total=0

	def add_card(self,crd):
		self.hand.append(crd)
		
	def calc_hand_total(self):
		self.hand_total=0
		for i in self.hand:
			if i[0] != 'A' and i[0] != 'J' and i[0] != 'Q' and i[0] != 'K':
				if len(i) == 2: 
					self.hand_total = self.hand_total + int(i[0])
				else:
					self.hand_total = self.hand_total + 10		
			else:
				if str(i[0]) == "A":
					if (self.hand_total + 10) > 21:
						self.hand_total = self.hand_total + 1
					else:
						self.hand_total = self.hand_total + 10
				else:
					self.hand_total = self.hand_total + 10
		

def display_hands(dealer,player):


	print("\n------------------------------")
	print ("Dealer's Hand: ", end=" ")
	print (dealer.hand[0] + " | X |")
	print("------------------------------")

	print ("Your Hand: ", end=" ")
	for i in player.hand:
		print (i + " |", end=" ")
	print("\nYour Total: " + str(player.hand_total))
	print("------------------------------\n")

def display_hands_cpu(dealer,player):


	print("\n------------------------------")
	print ("Dealer's Hand: ", end=" ")
	for i in CPU.hand:
		print (i + " |", end=" ")
	print("\nDealer Total: " + str(CPU.hand_total))
	print("------------------------------")

	print ("Your Hand: ", end=" ")
	for i in player.hand:
		print (i + " |", end=" ")
	print("\nYour Total: " + str(player.hand_total))
	print("------------------------------\n")


###################################################
# MAIN PROGRAM
###################################################

playing = True


while playing == True:

	player_lose = False
	CPU_lose = False
	stand = False
	blackj = False
	cpu_blackj = False

	cd = deck()
	cd.shuffle_deck()
	

	CPU = player() 
	player1 = player()
	
	CPU.add_card(cd.cards_deck.pop())
	CPU.add_card(cd.cards_deck.pop())
	CPU.calc_hand_total()
	player1.add_card(cd.cards_deck.pop())
	player1.add_card(cd.cards_deck.pop())
	player1.calc_hand_total()

	display_hands(CPU,player1)

	while player_lose == False and stand == False :
		ans = input ("Stand (s) or Hit (h)? ")
		if ans == 'h':
			player1.add_card(cd.cards_deck.pop())
			player1.calc_hand_total()
			display_hands(CPU,player1)

			if player1.hand_total > 21 :
				player_lose = True
			if player1.hand_total == 21 :
				blackj = True
				stand = True

		else:
			stand = True

	if player_lose == False:
		
		print("Player stands, dealer hits")

		stand = False

		while cpu_blackj == False and stand == False:
			if CPU.hand_total >= player1.hand_total:
				player_lose = True
				stand = True
			else:
				CPU.add_card(cd.cards_deck.pop())
				CPU.calc_hand_total()
				display_hands_cpu(CPU,player1)

				if CPU.hand_total == 21:
					player_lose = True
					stand = True
				if CPU.hand_total > 21:
					CPU_lose = True
					stand = True



	print("\n==============================\n")
	display_hands_cpu(CPU,player1)

	if player_lose == True :
		print("You lose!")
	if CPU_lose == True:
		print("You win!")

	ans = input("\nPlay again? (y/n): ")
	if ans == 'y':
		playing = True
	else:
		playing = False




#d = player()
#d.add_card("3S")
#d.add_card("3C")
#d.add_card("3D")
#d.calc_hand_total()

#d1 = player()
#d1.add_card("4D")
#d1.calc_hand_total()

#d1.add_card("1S")
#d1.calc_hand_total()

#d1.add_card("AD")
#d1.calc_hand_total()

#display_hands(d,d1)
