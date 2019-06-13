#Class for building out a player

class player:

	def __init__(self,name,money):
		self.name = name
		self.money = money
		self.betAmount = 0
		self.hand = []
		print("Welcome {}! \nYou have ${}".format(self.name, self.money))

	#Print the amount of money you have
	def getMoney(self):
		return self.money

	#Player places in their bet
	def bet(self, amount):
		if amount > self.money:
			print("You don't have the money")
		else:
			self.betAmount = self.betAmount + amount
			print("Your bet is {}".format(self.betAmount))
			#print("Your money left is {}".format(self.money))

	#If the player wins the bet gets added to the count	
	def win(self):
		self.money = self.money + self.betAmount
		self.betAmount = 0

	#If the player loses bet gets zeroed out
	def lose(self):
		self.money = self.money - self.betAmount
		self.betAmount = 0

	#Adds the card to player's hand
	def yourHand(self,card):
		self.hand.append(card)
		print(self.hand)

	#Cleared out the player's hand
	def clearHand(self):
		self.hand = []


	#Double down
	def doubleDown(self):
		if self.money - self.betAmount < 0:
			return "Sorry {} don't have the money".format(self.name)
		self.betAmount = self.betAmount * 2
		#self.money = self.money - self.betAmount
		print("Your bet is {}".format(self.betAmount))
		print("Your money left is {}".format(self.money))



