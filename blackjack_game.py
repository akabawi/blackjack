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
	print (dealer.hand[0])
	print("------------------------------")

	print ("Your Hand: ", end=" ")
	for i in player.hand:
		print (i + " |", end=" ")
	print("\nYour Total: " + str(player.hand_total))
	print("------------------------------\n")

def overflow(p):
	if p.hand_total > 21:
		return True
	else:
		return False



###################################################
# MAIN PROGRAM
###################################################

playing = True

while playing == True:
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
