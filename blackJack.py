#Where the game is played
import player
import cardDeck

#Start game
Play = input("You ready to play? (Y/N) ").upper()
while Play != 'Y' and Play !='N':
	Play = input("You ready to play? (Y/N) ").upper()

if Play == 'N':
	 print("Okay then leave my table!")


Name = str(input("What's your name friend? "))

Money = 100

#Create player instance
Player = player.player(Name,Money)

#Create dealer instance
Dealer = cardDeck.dealer()

winner = ''

#check the win
def checkWinner(player,dealer):
	playerTotal = 0
	dealerTotal = 0
	for i in player:
		for j in i:
			if i[j] == 'Jack' or i[j] == 'Queen' or i[j] == 'King':
				playerTotal = 10 + playerTotal
				continue
			if i[j] == 'Ace':
				Ace = input("Do you want your Ace to be 1 or 11: ")
				while Ace != '1' and Ace != '11':
					Ace = input("Do you want your Ace to be 1 or 11: ")
				playerTotal = int(Ace) + playerTotal
				continue
			playerTotal = i[j] + playerTotal

	for i in dealer:
			if dealer[i] == 'Jack' or dealer[i] == 'Queen' or dealer[i] == 'King':
				dealerTotal = 10 + dealerTotal
				continue
			if dealer[i] == 'Ace':
				Ace = input("Do you want your Ace to be 1 or 11: ")
				while Ace != '1' and Ace != '11':
					Ace = input("Do you want your Ace to be 1 or 11: ")
				dealerTotal = int(Ace) + dealerTotal
				continue
			dealerTotal = int(dealer[i]) + dealerTotal

	print("Your score {} \nDealer's Score {}".format(playerTotal, dealerTotal))
	if playerTotal > 21:
		return "Bust! House wins!"
	if playerTotal > dealerTotal:
		return "You win!"
	if playerTotal < dealerTotal or playerTotal == dealerTotal:
		return "House wins!"

def busted(player):
	playerTotal = 0
	for i in player:
		for j in i:
			if i[j] == 'Jack' or i[j] == 'Queen' or i[j] == 'King':
				playerTotal = 10 + playerTotal
				continue
			if i[j] == 'Ace':
				Ace = input("Do you want your Ace to be 1 or 11: ")
				while Ace != '1' and Ace != '11':
					Ace = input("Do you want your Ace to be 1 or 11: ")
				playerTotal = int(Ace) + playerTotal
				continue
			playerTotal = i[j] + playerTotal
	if playerTotal > 21:
		return True
	return False


while winner == '':

	if len(Player.hand) == 0:
		Wager = int(input("How much do you want to wager: "))
		Player.bet(Wager)
		print('Deal me in!')
		Player.yourHand(Dealer.hit())
	if len(Player.hand) < 2:
		Player.yourHand(Dealer.hit())

	doubleBet = input("Do you want double down (Y/N) ").upper()
	while doubleBet != 'Y' and doubleBet != 'N':
		doubleBet = input("Do you want double down  (Y/N) ").upper()

	if doubleBet == 'Y':
		Player.doubleDown()

	Hit = input("Do you want to hit or stand (hit/stand) ").lower()
	while Hit != 'hit' and Hit != 'stand':
		Hit = input("Do you want to hit or stand (hit/stand) ").lower()

	if Hit == 'hit':
		Player.yourHand(Dealer.hit())

	if Hit == 'stand':
		Dealer.stand()
		winner = checkWinner(Player.hand, Dealer.dealerHand)
		if winner == "Bust! House wins!" or winner == "House wins!":
			Player.lose()
			print(winner)
			print("You have this much money : ${}".format(Player.money))
		else:
			Player.win()
			print(winner)
			print("You have this much money : ${}".format(Player.money))

		#Start the game over
		Replay = input("Do you want to keep playing (Y/N) ").upper()
		while Replay != 'Y' and Replay != 'N':
			doubleBet = input("Do you want to keep playing (Y/N) ").upper()
		if Replay == 'Y':
			Player.clearHand()
			Dealer.reset()
			winner = ''

	if busted(Player.hand):
		winner = "Bust! House wins!"
		Player.lose()
		print(winner)
		print("You have this much money : ${}".format(Player.money))
		Replay = input("Do you want to keep playing (Y/N) ").upper()
		while Replay != 'Y' and Replay != 'N':
			doubleBet = input("Do you want to keep playing (Y/N) ").upper()
		if Replay == 'Y':
			Player.clearHand()
			Dealer.reset()
			winner = ''
	



print("You have this much money : ${}".format(Player.money))
