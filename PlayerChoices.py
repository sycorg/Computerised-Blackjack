import random
import Deck
import CardValues
import time
import DealerHand as dh
from tkinter import *
def choice(totalvalue, value, value2, hand):					#player decisions
	if totalvalue < 21:
		print()
		print("What move do you want to make?")
		print()
		print("1. Hit")
		print("2. Stay")
		print("3. Fold")
		if value == value2 and len(hand) == 2:					#if 'value' and 'value2' are the same and there are only two cards in the hand, you can split.
			print("4. Split")
		print()
		while True:
			choice = input()
			try:
				choice = int(choice)
			except:
				print("Please use the numbers before the move (i.e. for '1. Hit', type '1' )")
				continue
			break
		print()
		return choice
def split_list(a_list):					#splits hand1 into two lists
    half = len(a_list)//2
    return a_list[:half], a_list[half:]
def Player():
	dh.hand()
	DLRhand1 = dh.hand()
	print(f"The Dealer's hand is: [UNKONWN, {DLRhand1[1]}]")
	hand1 = []
	hand2 = "N/A"
	handtotal2 = 0
	handComplete = 0
	deck = Deck.getDeck()
	deck = random.choice(deck)
	cardno = 1
	nexthand = False
	Blackjack = False
	Blackjack2 = False
	Fold = False
	Fold2 = False
	charlie = False
	charlie2 = False
	print()
	print('===============================================\n')
	
	while handComplete != 2:					#keeps picking up cards until there is two cards in the hand
		cardpick = random.choice(deck)					#randomly picks an element in the 'deck' array
		index = deck.index(cardpick)
		hand1 = hand1[:index] + [cardpick] + hand1[index:]					#inserts the chosen card into the array
		deck.remove(cardpick)
		handComplete += 1
	handnum = [num.split('|', 3)[2] for num in hand1]					#splits an element in the array into colour, shape, and number
	print(hand1)
	print()
	handtotal = CardValues.faceCard(handnum[0]) + CardValues.faceCard(handnum[1])					#adds the two card's values together
	if handtotal == 21:					#checks for a blackjack
		print("Congratulations!!! You got a Blackjack!")
		Blackjack = True
	else:
		print(f"Your hand total is: {handtotal}")
	while True:					#infinite loop until broken
		time.sleep(random.randint(2, 5))
		if Blackjack == True:					#if there is a blackjack, the loop is broken
			break
		elif hand2 != "N/A":
			if len(hand2) == 2 and handtotal2 == 21:
				print("Congratulations!!!! You got a Blackjack in your second hand!")
				Blackjack2 = True
		elif len(hand1) == 5 and handtotal <= 21:					#if your first hand has 5 cards and your card total is less than 21, you win.
			print("Congratulations!!! You win because you have 5 cards in your hand without busting!")
			if nexthand == True:					#if you have split your hand (if you have two hands)
				charlie2 = True
				cardno = 0					#resets 'cardno'
				nexthand = True
			else:
				charlie = True
				break					#if you only have one hand, your turn ends and the loop breaks
		if nexthand != True:
			decision = choice(handtotal, handnum[0], handnum[1], hand1) 				#runs the "choice()" function
		elif len(hand2) == 1:
			decision = choice(handtotal2, handnum2[0], 0, hand2)
		else:
			decision = choice(handtotal2, handnum2[0], handnum[1], hand2)
		if decision == 1:					#if the player chose it hit
			cardpick = random.choice(deck)					#picks up a card
			index = deck.index(cardpick)
			if nexthand != True:					#if there is only one hand
				hand1 = hand1[:index] + [cardpick] + hand1[index:] 					#inserts the picked up card into the hand
				deck.remove(cardpick)					#removes the picked up card from the list 
				if hand2 != "N/A":
					print(f"First Hand: {hand1}")
				else:
					print(hand1)
				cardno += 1					#adds 1 to 'cardno', which has a default number of 2. This variable determines the number of cards in the hand
				handnum = [num.split('|', 3)[2] for num in hand1]					#splits an element in the array into colour, shape, and number
				handtotal += CardValues.faceCard(handnum[cardno])					#adds the cards number to the previous total
			elif nexthand == True:					#if the first hand has been 'completed,' the second hand is put into play
				hand2 = hand2[:index] + [cardpick] + hand2[index:]					#inserts the picked up card into the hand
				deck.remove(cardpick)					#removes the picked up card from the list
				cardno += 1					#adds 1 to 'cardno', which has a default number of 2. This variable determines the number of cards in the hand
				handnum2 = [num.split('|', 3)[2] for num in hand2]					#splits an element in the array into colour, shape, and number
				handtotal2 += CardValues.faceCard(handnum2[cardno])					#adds the cards value to the previous total
			print()
			if handtotal < 21:
				print(f"Your First Hand's total is: {handtotal}")
			elif handtotal == 21:					#if you get 21, your turn ends.
				print(f"Your First Hand's total is {handtotal}, your turn ends.")
				if hand2 != "N/A":
					cardno = 0
					nexthand = True
				else:
					break
			else:					#if you're card total is higher than 21, you bust and your turn ends.
				print(f"You have busted! Your First Hand's total is: {handtotal}. Your turn ends.")						
				if hand2 != "N/A":
					cardno = 0
					nexthand = True
				else:
					break
			print()
			if hand2 != "N/A" and handtotal2 != 0:
				print(f"Second Hand: {hand2}")
			print()
			if handtotal2 != 0:
				if handtotal2 < 21:
					print(f"Your Second Hand's total is: {handtotal2}")
				elif len(hand2) == 5 and handtotal2 <= 21:
					print("Congratulations!!! You win because you have 5 cards in your hand without busting!")
					break
				elif handtotal2 == 21:
					print(f"Your Second Hand's total is {handtotal2}, your turn ends.")
					break
				else:
					print(f"You have busted! Your Second Hand's total is: {handtotal2}")
					break
		elif decision == 2:
			if hand2 != "N/A":
				if nexthand == False:
					cardno = 0
					nexthand = True
					print("You have stayed on your first hand.")
					continue
				else:
					print("You have stayed on your second hand. your Turn has now ended")
					break
			else:
				print("You have decided to stay, your turn has now ended")
			break
		elif decision == 3:
			print("You have folded. Half of your bet has been forfeighted and has been given to the dealer")
			if nexthand == False:
				Fold = True
				if hand2 != "N/A":
					continue
				else:
					break
			else:
				Fold2 = True
		elif decision == 4:
			hand1, hand2 = split_list(hand1)					#splits 'hand1' into 'hand1' and 'hand2'
			cardno = 0					#'cardno' is reset.
			handnum1 = [num.split('|', 3)[2] for num in hand1]
			handtotal = CardValues.faceCard(handnum1[cardno])
			handnum2 = [num.split('|', 3)[2] for num in hand2]
			handtotal2 = CardValues.faceCard(handnum2[cardno])
			print()
			print("Your bet has been doubled and split between the two hands.")
			print()
			print(f"First Hand: {hand1}")
			print()
			print(f"Your First Hand's total is: {handtotal}")
			print()
			print(f"Second Hand: {hand2}")
			print()
			print(f"Your Second Hand's total is: {handtotal2}")
	if hand2 == "N/A":
		print(f"You have {len(hand1)} cards in your hand")
	else:
		print(f"You have {len(hand1)} cards in your first hand")
		print(f"You have {len(hand2)} cards in your second hand")
	P1 = hand1
	if hand2 != "N/A":
		P2 = hand2
	Pt1 = handtotal
	if hand2 != "N/A":
		Pt2 = handtotal2
	if nexthand == True:
		return P1, P2, Pt1, Pt2, Fold, Fold2, nexthand, Blackjack, Blackjack2, charlie, charlie2
	else:
		return P1, Pt1, Fold, nexthand, Blackjack, charlie