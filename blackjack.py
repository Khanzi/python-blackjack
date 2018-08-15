import random

# INITIALIZING VARIABLES
#rank = 1-10 and Jack(11), Queen(12), King(13), Ace(14)
#value =  1-11
#suit = Diamonds, Clubs, Hearts, or Spades
suits = ["Diamonds","Clubs","Hearts","Spades"]
ranks = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
orientation = ["Face Down","Face Up"]
selection = 0
playing = True
starting_balance = 1500
bet = 0

# FUNCTIONS
def winChecker():
	if dealer.hand.total() >=  21 and player.hand.total() >= 21: # Tie
		print("Both of you bust, this shouldn't theoretically happen...")
	elif player.hand.total() == 21 or dealer.hand.total() > 21: # Player Win
		print("Player wins this round!")
		player.bankroll.deposit(bet)
	elif dealer.hand.total() == 21 or player.hand.total() > 21:	# Dealer win
		print("Dealer wins this round!")
		dealer.bankroll.deposit(bet)

	
def initialDraw():
	player.hand.draw()
	player.hand.draw()

	dealer.hand.draw()
	dealer.hand.draw()
	dealer.hand.cards[0].orientation = orientation[0]

	print("Players Hand")
	player.hand.showHand()
	print("Dealers Hand")
	dealer.hand.showHand()

def makeBet():
	bet = 2 * int(input("Please make your bet"))
	print("Player")
	player.bankroll.withdraw(bet/2)
	print("Dealer")
	dealer.bankroll.withdraw(bet/2)
	print(f"Withdrawn funds are in the pot: {bet}")
def newRound():
	deck_of_cards = Deck()
	deck_of_cards.shuffle()
	makeBet()
	player.hand.cards = []
	dealer.hand.cards = []
	initialDraw()
def newGame():
	print("Player Account Balance")
	player.bankroll.balance=0
	player.bankroll.deposit(starting_balance)
	print("Dealer Account Balance")
	dealer.bankroll.balance=0
	dealer.bankroll.deposit(starting_balance)

	

def errorMessage(number):
	if number == 1:
		return("Error 1: Card not of type 'Ace'")
def playerMenu():
	player_selection = 0
	print("--------------------------")
	print("[1] Hit")
	print("[2] Stay")


# DEFINING CLASSES
class Card:

	def __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank
		self.ace = False
		self.orientation = orientation[1]
		if self.rank < 11:
			self.value = rank
		elif self.rank > 10 and self.rank != 14:
			self.value = 10
		elif self.rank == 14:
			self.value = 11
			self.ace = True

	def aceChange(self):
		if self.rank != 14:
			print(errorMessage(1))
			return None
		elif self.value == 11:
			self.value = 1
		else:
			self.value = 11
		return None

	def __str__(self):
		if self.orientation == orientation[0]:
			return "Card is face down"
		else:
			if self.rank < 11:
				return f"{self.rank} of {self.suit}"
			elif self.rank ==11:
				return f"Jack of {self.suit}"
			elif self.rank == 12:
				return f"Queen of {self.suit}"
			elif self.rank ==13:
				return f"King of {self.suit}"
			elif self.rank ==14:
				return f"Ace of {self.suit}"





class Deck:
	

	def __init__(self):
		self.deck = []
		for suit in suits:
			for rank in ranks:
				self.deck.append(Card(suit, rank))


	def shuffle(self):
		random.shuffle(self.deck)
		print("--------------------------")
		print("The deck has been shuffled")
		print("--------------------------")

	def __len__(self):
		return len(self.deck)

class Person:

	def __init__(self):
		self.bankroll = Bank()
		self.hand = Hand()




class Bank:

	def __init__(self):
		self.balance = 0

	def deposit(self, amount):
		self.balance += amount
		print("--------------------------")
		print(f" ${amount} has been added\n The new total is {self.balance}")
		print("--------------------------")
	def withdraw(self, amount):
		self.balance -= amount
		print("--------------------------")
		print(f" ${amount} has been withdrawn\n The new total is {self.balance}")
		print("--------------------------")


class Hand:

	def __init__(self):
		self.cards = []

	def draw(self):
		selection = random.randint(0,len(deck_of_cards)-1) 
		self.cards.append(deck_of_cards.deck[selection])
		del(deck_of_cards.deck[selection])
	def total(self):
		total = 0
		has_ace = False
		for card in self.cards:
			total += card.value
			if card.ace:
				has_ace = True
		if has_ace and total > 21:
			for card in self.cards:
				if card.ace:
					card.aceChange
					total = 0		
		for card in self.cards:
			total += card.value
		return total
	def showHand(self):
		print("--------------------------")
		for card in self.cards:
			print(card)
		print("--------------------------")
	

# INITIALIZING OBJECTS
deck_of_cards = Deck()
player = Person()
dealer = Person()


newGame()
newRound()
winChecker()
playerMenu()	


