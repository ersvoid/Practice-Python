import random

suits = ['Clubs','Diamonds','Hearts','Spades']
ranks = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
values = {'Ace':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'Jack':10,'Queen':10,'King':10}

class Card(object):
	
	def __init__(self,suit,rank):
		self.suit = suit
		self.rank = rank
	
	def __str__(self):
		return "%s of %s" % (self.rank, self.suit)
		
class Deck(object):
	
	def __init__(self):
		self.cards = []
		self.build()
		
	def build(self):
		for suit in suits:
			for rank in ranks:
				self.cards.append(Card(suit,rank))
				
	def shuffle(self):
		random.shuffle(self.cards)
		print("The deck is shuffled.")
		
	def drawCard(self):
		single_card = self.cards.pop()
		return single_card
		
class Player(object):
	
	def __init__(self,bankroll = 100):
		self.bankroll = bankroll
		self.bet = 0
		
	def sub_bankroll(self,amount):
		self.bankroll -= amount
		self.bet += amount  
		
	def add_bankroll(self):
		self.bankroll += self.bet*2
		
class Hand (object):
	
	def __init__(self):
		self.hand = []
		self.value = 0
		
	def draw(self,card):
		self.hand.append(card)
		if (card.rank == "Ace" and self.value < 12):
			self.value += (values[card.rank] + 10)
		else:
			self.value += values[card.rank]
		
	def showHand(self):
		for h in self.hand:
			print(h)
		
	def __del__(self):
		pass

###NEW FUNCTIONS

def winning_hand():
	if player_hand.value == 21:
		print("You have won!!!")
		player.add_bankroll()
		player_hand.__del__()
		dealer_hand.__del__()
	elif player_hand.value > 21:
		print("You have busted, buster!!!")
		player_hand.__del__()
		dealer_hand.__del__()
	elif dealer_hand.value == 21:
		print("The dealer has won!!!")
		dealer_hand.showHand()
		player_hand.__del__()
		dealer_hand.__del__()
	elif dealer_hand.value > 21:
		print("The dealer busted, so you won!!!")
		player.add_bankroll()
		dealer_hand.showHand()
		player_hand.__del__()
		dealer_hand.__del__()
	elif dealer_hand.value == player_hand.value:
		print("You have tied.")
		dealer_hand.showHand()
		player_hand.__del__()
		dealer_hand.__del__()
	elif player_hand.value > dealer_hand.value:
		print("Your hand is higher! You won!")
		player.add_bankroll()
		player_hand.__del__()
		dealer_hand.__del__()
	else:
		print("The dealer's hand is higher. The dealer has won!!!")
		dealer_hand.showHand()
		player_hand.__del__()
		dealer_hand.__del__()
	
def replay_function():
	global replay,game_on
	player_replay = str(input("Would you like to continue playing? (Y?N) "))
	player_replay.lower()
	if player_replay == "y":
		print("Dealing next round.")
	else:
		print("Thank you for playing!")
		replay = False
		game_on = False

def game_switch():
	global replay,game_on
	if player.bankroll <= 0:
		print("You are out of money deadbeat!!!")
		replay = False
		game_on = False
	else:
		pass

game_on = True
replay = True

while game_on == True:

	print("Welcome to Eric's Blackjack Game Scripted in Python!!!")
	
	player = Player()
	dealer = Player()
	
	while replay == True:
	
		game_deck = Deck()
		game_deck.shuffle()
		player_hand = Hand()
		dealer_hand = Hand()
		player_hand.draw(game_deck.drawCard())
		dealer_hand.draw(game_deck.drawCard())
		player_hand.draw(game_deck.drawCard())
		dealer_hand.draw(game_deck.drawCard())
		print("The dealer is showing: " + dealer_hand.hand[0].__str__())
		print("Your hand: ")
		player_hand.showHand()
		print("Count: " + str(player_hand.value))
		print("You have " + str(player.bankroll) + " dollars left.")
		amount = int(input("How much do you want to bet? "))
		player.sub_bankroll(amount)
		print("Count: " + str(player_hand.value))
		player_input = str(input("Would you like to hit or stay? "))
		player_input.lower()
		while player_input == "h" and player_hand.value < 21:
			player_hand.draw(game_deck.drawCard())
			print("Your hand: ")
			player_hand.showHand()
			print("Count: " + str(player_hand.value))
			player_input = str(input("Would you like to hit or stay? "))
			player_input.lower()
		while dealer_hand.value < 17:
			dealer_hand.draw(game_deck.drawCard())
		winning_hand()
		player.bet = 0
		replay_function()
		game_switch()