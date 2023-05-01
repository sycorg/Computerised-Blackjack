#converts face cards (A, J, Q, K) into numerical values, and has a fail-safe incase a number is inputted into 'character'
def faceCard(character):
	if character == "J":
		value = 10
	elif character == "Q":
		value = 10
	elif character == "K":
		value = 10
	elif character == "A":
		acevalue = int(input("What value do you want your Ace to be? (1 or 11) "))
		value = acevalue
	else:
		value = int(character)
	return value



def AIfaceCard(character):
	if character == "J":
		value = 10
	elif character == "Q":
		value = 10
	elif character == "K":
		value = 10
	elif character == "A":
		value = 11
	else:
		value = int(character)
	return value