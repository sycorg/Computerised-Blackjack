import random
import time
import Deck
import CardValues
import AIChoices
from tkinter import *
#used to split the hand
def split_list(a_list):
    half = len(a_list)//2
    return a_list[:half], a_list[half:]

#The Bot's Algorithm
def Player():
	print('Player 5')
	hand1 = []
	hand2 = "N/A"
	handnum2 = []
	handtotal2 = 0
	handComplete = 0
	deck = Deck.getDeck()
	deck = random.choice(deck)
	cardno = 1
	nexthand = False
	dealt = 0
	decision = 0
	Blackjack = False
	Fold = False
	Fold2 = False
	AVC = 0					#Ace Value Change
	#keeps picking up cards until there is two cards in the hand
	while handComplete != 2:
		cardpick = random.choice(deck)
		index = deck.index(cardpick)
		hand1 = hand1[:index] + [cardpick] + hand1[index:]
		deck.remove(cardpick)
		handComplete += 1
	handnum = [num.split('|', 3)[2] for num in hand1]
	handtotal = CardValues.AIfaceCard(handnum[0]) + CardValues.AIfaceCard(handnum[1])
	if AVC != 1:
		for i in handnum:
			if i == 'A' and handtotal > 21:
				handtotal -= 10
				AVC = 1
				break
	if handtotal == 21:
		Blackjack = True
	while True:
		time.sleep(random.randint(2, 5))
		if Blackjack == True:
			break
		if len(hand1) == 2:
			decision = AIChoices.Choice(handtotal, handnum, handnum[0], handnum[1])
		if len(hand2) == 2:
			decision = AIChoices.Choice(handtotal2, handnum2, handnum2[0], handnum2[1])
		if len(hand1) == 1:
			decision = 1
		if len(hand2) == 1:
			decision = 1
		if len(hand1) == 5 and handtotal <= 21:
			decision = 2
		if len(hand2) == 2 and handtotal2 <= 21:
			decision = 2
		if decision == 1:
			cardpick = random.choice(deck)
			index = deck.index(cardpick)
			if nexthand != True:
				hand1 = hand1[:index] + [cardpick] + hand1[index:]
				deck.remove(cardpick)
				cardno += 1
				handnum = [num.split('|', 3)[2] for num in hand1]
				handtotal += CardValues.AIfaceCard(handnum[cardno])
			elif nexthand == True:
				hand2 = hand2[:index] + [cardpick] + hand2[index:]
				deck.remove(cardpick)
				cardno += 1
				handnum2 = [num.split('|', 3)[2] for num in hand2]
				handtotal2 += CardValues.AIfaceCard(handnum2[cardno])
				dealt += 1
			if handnum[cardno] == 'A' and handtotal > 21:
				handtotal -= 10
			elif handtotal > 21:
				print("Player 5 stayed, their turn has now ended")
			if hand2 != "N/A":
				if handnum2[cardno] == 'A' and handtotal2 > 21:
					handtotal -= 10
				elif handtotal > 21:
					print("Player 5 stayed, their turn has now ended")
			if handtotal < 21:
				continue
			elif len(hand1) == 5 and handtotal <= 21:
				Charlie = True
				if hand2 != "N/A":
					cardno = 0
					nexthand = True
				else:
					break
			elif handtotal == 21:
				
				if hand2 != "N/A":
					cardno = 0
					nexthand = True
				else:
					break
			else:
				if hand2 != "N/A":
					cardno = 0
					nexthand = True
				else:
					break
			if handtotal2 != 0:
				if handtotal2 < 21:
					continue
				elif len(hand2) == 5 and handtotal2 <= 21:
					break
				elif handtotal2 == 21:
					break
				else:
					break
		elif decision == 2:
			if hand2 != "N/A":
				if nexthand == False:
					nexthand = True
					print("Player 5 has stayed on their first hand.")
				else:
					print("Player 5 has stayed on their second hand. Their Turn has now ended")
					break
			else:
				print("Player 5 has decided to stay, their turn has now ended")
			break
		elif decision == 3:
			print("Player 5 has folded. Their bet has been forfeighted and has been given to the dealer")
			if nexthand == False:
				Fold = True
				if hand2 != "N/A":
					continue
				else:
					break
			else:
				Fold2 = True
		elif decision == 4:
			print("Player 5 has decided to split their hand. Their bet has been doubled then split between their hands")
			hand1, hand2 = split_list(hand1)
			cardno = 0
			handnum1 = [num.split('|', 3)[2] for num in hand1]
			handtotal = CardValues.faceCard(handnum1[cardno])
			handnum2 = [num.split('|', 3)[2] for num in hand2]
			handtotal2 = CardValues.faceCard(handnum2[cardno])
	print()
	if hand2 == "N/A":
		print(f"Player 5 has {len(hand1)} cards in their hand")
	else:
		print(f"Player 5 has {len(hand1)} cards in their first hand")
		print(f"Player 5 has {len(hand2)} cards in their second hand")
	AI1 = hand1
	if hand2 != "N/A":
		AI2 = hand2
	AIt1 = handtotal
	if hand2 != "N/A":
		AIt2 = handtotal2
	if nexthand == True:
		return AI1,	AI2, AIt1, AIt2, Fold, Fold2, nexthand
	else:
		return AI1, AIt1, Fold, nexthand