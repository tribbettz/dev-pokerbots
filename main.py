import poker
import players as p
import helper_functions as hf
from names import names

PLAYERS			= 3
STRATEGY		= None
START_MONEY 	= 300
HANDS_TO_PLAY	= 5000
table 			= poker.table()

for i in range(0, PLAYERS):
	name 		= hf._choose_name(names)
	strategy	= hf._choose_strategy()
	money		= START_MONEY
	table.add_player(p.player(name, strategy, money))
	
hand_number = 1

while hand_number < HANDS_TO_PLAY:
	table.new_hand()
	table.deck.shuffle()
	table.move_blinds()
	table.take_blinds()
	
	if len(table.players) < 2:
		break
	else:
		for p in table.players:
			p.cards.append(table.deck.pop())
		for p in table.players:
			p.cards.append(table.deck.pop())
		
		table.bet()
		table.flop()
		
		table.bet()
		table.turn()
		
		table.bet()
		table.finish_hand()
		hand_number += 1

print(table.players[0].name + ' is the winner!')
