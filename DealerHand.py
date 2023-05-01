import random
import Deck
import CardValues
def saveHand():
	handComplete = 0
	deck = Deck.getDeck()
	deck = random.choice(deck)
	hand1 = []
	cardno = 0
	while handComplete != 2:
		cardpick = random.choice(deck)
		index = deck.index(cardpick)
		hand1 = hand1[:index] + [cardpick] + hand1[index:]
		deck.remove(cardpick)
		handComplete += 1
	hand = hand1
	file = open("DealerHand.txt", "w")
	for x in hand:
		file.write("\n"+hand1[cardno])
		cardno += 1
	file.close()
	return hand
def hand():
	file = open("DealerHand.txt", "r")
	fileList = []
	for line in file:
		line = file.read()
		line_pair = line.split("\n")
		line = line_pair
		fileList.append(line)
	fileList = random.choice(fileList)
	fileList = list(fileList)
	return fileList
	file.close()
#A function used to determine the value of the dealer's revealed card.
def dealerValue():
	hand1 = hand()
	handnum = [num.split('|', 3)[2] for num in hand1]
	#the program checks to see if the card value is a number. If it is, it sets 'value' as the card value as an integer
	try: value = int(handnum[1])
	#if the card value isn't a number, but a letter, it goes into an if statement
	except:
		#if the value is not an ace, 'value' is set to a value of ten
		if handnum[1] != 'A':
			value = CardValues.faceCard(handnum[1])
		#otherwise, 'value' is set to 'A'
		else:
			value = 11
	return value