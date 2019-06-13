#Class for Deck
import random


class dealer:

	def __init__(self):
		self.played = {
			'Clubs': [],
			'Spades': [],
			'Diamonds':[],
			'Hearts': []
		}
		self.dealerHand = {}
		self.deck = {
		'Clubs' : [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace'],
		'Spades' : [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace'],
		'Diamonds':[2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace'],
		'Hearts' : [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']
		}

	#Player asks for hit
	def hit(self):
		card = {}
		house = random.choice(list(self.deck.keys()))
		card[house] = random.choice(self.deck[house])
		while card[house] in self.played[house]:
			card[house] = random.choice(self.deck[house])
		self.played[house].append(card[house])
		return card

	#Dealer deals to self
	def stand(self):
		print("Player Stands, Dealer's Turn")
		self.dealerHand = {}
		while len(self.dealerHand) < 2:
			house = random.choice(list(self.deck.keys()))
			self.dealerHand[house] = random.choice(self.deck[house])
			while self.dealerHand[house] in self.played[house]:
				self.dealerHand[house] = random.choice(self.deck[house])
			self.played[house].append(self.dealerHand[house])
		print(self.dealerHand)

	#If player decides to play again
	def reset(self):
		self.played = {
			'Clubs': [],
			'Spades': [],
			'Diamonds':[],
			'Hearts': []
		}
		self.dealerHand = {}




