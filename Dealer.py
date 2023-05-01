import random
import Deck
import CardValues
import DealerHand as dh
from tkinter import *
import time
def choice(totalvalue, value, value2, hand, handtype):
	if totalvalue < 17 or handtype == True:
		if value == value2 and len(hand) == 2:
			choice = 3
		else:
			print()
			choice = 1
			print()
		return choice
	else:
		choice = 2
		return choice

def split_list(a_list):
    half = len(a_list)//2
    return a_list[:half], a_list[half:]
def Player():
	hand1 = dh.hand()
	hand2 = "N/A"
	handtotal2 = 0
	deck = Deck.getDeck()
	deck = random.choice(deck)
	cardno = 1
	nexthand = False
	Blackjack = False
	Blackjack2 = False
	soft17 = False
	hard17 = False
	doneS17 = 0
	handnum = [num.split('|', 3)[2] for num in hand1]					
	handtotal = CardValues.AIfaceCard(handnum[0]) + CardValues.AIfaceCard(handnum[1])	
	if handtotal == 21:					
		print("The Dealer got Blackjack, the Dealer wins!")
		Blackjack = True
	elif handtotal == 17 and handnum[0] == "A" or handnum[1] == "A":
		print(f"The Dealer's hand total is: {handtotal}")
		soft17 = True
	elif handtotal == 17:
		print(f"The Dealer's hand total is: {handtotal}")
		hard17 = True
	else:
		print(f"The Dealer's hand total is: {handtotal}")
	while True:
		time.sleep(random.randint(2, 5))
		if len(hand1) == 2 and handtotal == 21:
			Blackjack = True
		if Blackjack == True:					
			break
		if hard17 == True:
			break
		if doneS17 == 1:
			break
		print(hand1)
		if nexthand != True:
			try:
				decision = choice(handtotal, handnum[0], handnum[1], hand1, soft17)
			except:
				decision = 1
		else:
			try:
				decision = choice(handtotal2, handnum2[0], handnum2[1], hand2, soft17)
			except:
				decision = 1
		if decision == 1:					
			cardpick = random.choice(deck)					
			index = deck.index(cardpick)
			if soft17 == True:
				doneS17 = 1
			if nexthand != True:					
				hand1 = hand1[:index] + [cardpick] + hand1[index:] 					
				deck.remove(cardpick)					
				if hand2 != "N/A":
					print(f"The Dealer's first hand is: {hand1}")
				else:
					print(hand1)
				handnum = [num.split('|', 3)[2] for num in hand1]					
				handtotal += CardValues.AIfaceCard(handnum[cardno])
				cardno += 1				
			elif nexthand == True:					
				hand2 = hand2[:index] + [cardpick] + hand2[index:]					
				deck.remove(cardpick)					
				handnum2 = [num.split('|', 3)[2] for num in hand2]					
				handtotal2 += CardValues.AIfaceCard(handnum2[cardno])
				cardno += 1
			print()
			if handtotal < 21:
				print(f"The Dealer's First Hand's total is: {handtotal}")
			elif len(hand1) == 5 and handtotal <= 21:					
				print("The Dealer's First Hand win's because they have 5 cards in their hand without busting!")
				if hand2 != "N/A":					
					cardno = 0					
					nexthand = True
				else:
					break					
			elif handtotal == 21:					
				print(f"The Dealer's First Hand's total is {handtotal}, their turn ends.")
				if hand2 != "N/A":
					cardno = 0
					nexthand = True
				else:
					break
			else:					
				print(f"The Dealer has busted! Their First Hand's total is: {handtotal}. Their turn ends.")			
				if hand2 != "N/A":
					cardno = 0
					nexthand = True
				else:
					break
			print()
			if hand2 != "N/A" and handtotal2 != 0:
				print(f"The Dealer's Second Hand is: {hand2}")
			print()
			if handtotal2 != 0:
				if handtotal2 < 21:
					print(f"The Dealer's Second Hand's total is: {handtotal2}")
				elif len(hand2) == 5 and handtotal2 <= 21:
					print("The Dealer's Second Hand win's because they have 5 cards in their hand without busting!")
					break
				elif handtotal2 == 21:
					if len(hand2) == 2:
						Blackjack2 = True
					print(f"The Dealer's Second Hand's total is {handtotal2}, their turn ends.")
					break
				else:
					print(f"The Dealer has busted! Their Second Hand's total is: {handtotal2}")
					break
		elif decision == 2:
			if hand2 != "N/A":
				if nexthand == False:
					cardno = 0
					nexthand = True
					if soft17 == True:
						print("The Dealer has been forced to stay on their first hand")
					else:
						print("The Dealer has decided to stay on their first hand")
				else:
					if hard17 == True:
						print("The Dealer has been forced to stay on their second hand. Their turn has now ended.")
						break
					else:
						print("The Dealer has decided to stay on their second hand. Their turn has now ended.")
						break
			else:
				if hard17 == True:
					print("The Dealer has been forced to stay. Their turn has now ended.")
					break
				else:
					print("The Dealer has decided to stay. Their turn has now ended.")
					break
		elif decision == 3:
			print("The Dealer has decided to split their hand. Their bet has been doubled then split between their hands")
			hand1, hand2 = split_list(hand1)
			cardno = 0
			handnum1 = [num.split('|', 3)[2] for num in hand1]
			handtotal = CardValues.faceCard(handnum1[cardno])
			handnum2 = [num.split('|', 3)[2] for num in hand2]
			handtotal2 = CardValues.faceCard(handnum2[cardno])
			print(f"Their First Hand is : {hand1}")
			print()
			print(f"Their First Hand's total is: {handtotal}")
			print()
			print(f"Their Second Hand is: {hand2}")
			print()
			print(f"Their Second Hand's total is: {handtotal2}")
	print()
	if hand2 == "N/A":
		print(f"The Dealer has {len(hand1)} cards in their hand")
	else:
		print(f"The Dealer has {len(hand1)} cards in their first hand")
		print(f"The Dealer has {len(hand2)} cards in their second hand")
	DLR1 = hand1
	if hand2 != "N/A":
		DLR2 = list(hand2)
	DLRt1 = int(handtotal)
	if hand2 != "N/A":
		DLRt2 = handtotal2
	if nexthand == True:
		return DLR1,DLR2, DLRt1, DLRt2, Blackjack, Blackjack2, nexthand
	else:
		return DLR1, DLRt1, Blackjack, nexthand