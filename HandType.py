#checks if a hand is a soft hand (a hand with an ace and a value), a hard hand (a hand without an ace), or a pair (a hand with cards with two of the same values.)
def softHand(value1, value2):
	if value1 == 'A' or value2 == 'A':
		boolean = True
	elif value1 == 'A' and value2 == 'A':
		boolean = False
	else:
		boolean = False
	return boolean


#checks if a hand is a soft hand, a hard hand, or a pair.
def hardHand(value1, value2):
	if value1 == 'A' or value2 == 'A':
		boolean = False
	elif value1 == 'A' and value2 == 'A':
		boolean = False
	else:
		boolean = True
	return boolean


	
#checks if a hand is a pair.
def pairs(value1, value2):
	if value1 == value2:
		boolean = True
	else:
		boolean = False
	return boolean