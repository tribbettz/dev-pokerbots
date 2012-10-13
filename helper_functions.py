from random import randrange

def _choose_name(names):
	pos			= randrange(len(names))
	name		= names[pos]
	names[pos]	= names[-1]
	del names[-1]
	return name
	
def _choose_strategy():
	return None