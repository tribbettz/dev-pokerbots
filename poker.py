import random
import cards
import players

class table:
	def __init__(self, small=2, big=4):
		self.deck 			= cards.deck()
		self.open_cards		= []
		self.players 		= []
		self.pot			= 0
		self.small_blind	= int(small)
		self.big_blind		= int(big)
		self.blinds			= {'small': None, 'big': None}
		self.last_bet		= []
		
	def new_hand(self):
		self.deck 		= cards.deck()
		self.open_cards = []
		self.last_bet 	= []
		self.pot		= 0
		for player in self.players:
			player.reset_state()
			
	def add_player(self, player):
		self.players.append(player)
		
	def next_player_for(self, player):
		index = 0
		if player in self.players:
			index = (self.players.index(player) + 1) % len(self.players)
		return self.players[index]
		
	def move_blinds(self):
		self.blinds['small'] 	= self.next_player_for(self.blinds['small'])
		self.blinds['big']		= self.next_player_for(self.blinds['small'])
	
	def take_blinds(self):
		self.blinds['small'].money 	-= self.small_blind
		self.blinds['big'].money	-= self.big_blind
		self.pot += (self.big_blind + self.small_blind)
		
	def bet(self):
		for player in self.players:
			if not player.fold:
				action = player.action()
				if action[0] == 'bet':
					last_bet = [player, int(action[1].get('bet'))]
				print(player.name +'\'s action: ' + str(action))
	
	def flop(self):
		for i in range(1, 4):
			self.open_cards.append(self.deck.pop())
	
	def turn(self):
		self.open_cards.append(self.deck.pop())
	
	def river(self):
		self.open_cards.append(self.deck.pop())
		
	def finish_hand(self):
		winners = showdown(self.players, self.open_cards)
		winning = self.pot // len(winners)
		for winner in winners:
			winner.money	+= winning
			winner.bank		+= winner.money - winner.start_money
			
def showdown(players, river):
	return []
	
def calculate_hand(hand, river):
	return (-1, None)
		