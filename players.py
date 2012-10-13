
import random

class player:
	def __init__(self, name, strategy=None, money=None):
		self.name 			= name
		self.strategy		= strategy
		self.start_money	= money
		self.money			= self.start_money
		self.bank			= 0
		self.cards 			= []
		self.bets			= {}
		self.fold 			= False
		
	def action(self):
		actions		= ['bet', 'call', 'fold']
		action		= [None, 0]
		action[0]	= random.choice(actions)
		if action[0] == 'bet':
			action[1]	= random.randrange(1,31)
		return action
		
	def reset_state(self):
		self.cards = []
		self.money = self.start_money
		self.fold = False
		
	def __str__(self):
		return self.name
		
	def __repr__(self):
		return self.name