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
		past_actions = []
		for player in self.players:
			if not player.fold:
				action = player.action()
				past_actions.append(action)
				if (action[0] == 'bet' and past_actions[-1] != 'bet'):
					self.pot		+= int(action[1])
					player.money	-= int(action[1])
					self.last_bet 	= [len(self.open_cards), player, \
											int(action[1])]
				elif action[0] == 'call' and self.last_bet:
					self.pot		+= int(self.last_bet[2])
					player.money	-= int(self.last_bet[2])
				else:
					player.fold = True
					player.bank += (player.money - player.start_money)
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
	intermediate_winners	= []
	intermediate_hand		= (-1, None)
	for p in players:
		current_hand	= calculate_hand(p.cards, river)
		if current_hand > intermediate_hand:
			intermediate_winners = [p]
			intermediate_hand = current_hand
		elif current_hand == intermediate_hand:
			intermediate_winners.append(p)
	return intermediate_winners
	
def calculate_hand(hand, river):
	cards		= hand + river
	combination	= 8
	high_card = check_royal_flush(cards)
	if not high_card:
		combination -= 1 								# 7
		high_card = check_4_of_a_kind(cards)
		if not high_card:
			combination -= 1							# 6
			high_card = check_full_house(cards)
			if not high_card:
				combination -= 1						# 5
				high_card = check_flush(cards)
				if not high_card:
					combination -= 1					# 4
					high_card = check_straight(cards)
					if not high_card:
						combination -= 1				# 3
						high_card = check_3_of_a_kind(cards)
						if not high_card:
							combination -= 1			# 2
							high_card = check_2_pairs(cards)
							if not high_card:
								combination -= 1		# 1
								high_card = check_pair(cards)
								if not high_card:
									combination -= 1	# 0
	return (combination, high_card)
	
def check_royal_flush(card_set):
	pass

def check_4_of_a_kind(card_set):
	pass

def check_full_house(card_set):
	'''three of a kind + pair'''
	pass

def check_flush(card_set):
	'''5 or more cards of the same suit'''
	suits = [card.suit for card in card_set]

	for suit in cards.suits:
		n = len(list(filter(lambda s: s == suit, suits)))
		if n >= 5:
			return True

	return False
	pass

def check_straight(card_set):
	pass

def check_3_of_a_kind(card_set):
	pass

def check_2_pairs(card_set):
	pass

def check_pair(card_set):
	pass	