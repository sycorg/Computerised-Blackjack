def getDeck(): #getting all cards in deck.txt and putting it inside a list
	deck = open("deck.txt", "r")
	deckList = []
	for line in deck:
		line = deck.read()
		line_pair = line.split("\n")
		line = line_pair
		deckList.append(line)
	return deckList
	deck.close()