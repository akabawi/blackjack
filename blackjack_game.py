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
		print(self.hand)

	def calc_hand_total(self):
		t=0
		for i in self.hand:
			t = t + int(i[0])
		self.hand_total = self.hand_total + t

#def display_hands():

d = player()
d.add_card("3S")
d.add_card("3C")
d.add_card("3D")
d.calc_hand_total()

print(d.hand_total)