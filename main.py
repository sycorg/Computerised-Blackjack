import Account as ac
import DealerHand as dh
import PlayerChoices
import AIPlayer1
import AIPlayer2
import AIPlayer3
import AIPlayer4
import AIPlayer5
import AIPlayer6
import Dealer
import random
import os
import time
import Betting as bt

def foldbet(bet, fold):
	if fold == True:
		bet /= 2
	else:
		bet = bet
	bet = int(bet)
	return bet

def foldbet2(bet, fold1, fold2):
	bet2 = bet
	if fold1 != True and fold2 == True:
		bet2 //= 2
	elif fold1 == True and fold2 != True:
		bet //= 2
	elif fold1 == True and fold2 == True:
		bet //= 2
		bet2 //= 2
	else:
		bet = bet
		bet2 = bet2
	bet = int(bet)
	bet2 = int(bet)
	return bet, bet2
def BJ(hand, handtotal):
	if len(hand) == 2 and handtotal == 21:
		Blackjack = True
	else:
		Blackjack = False
	return Blackjack
def CH(hand, handtotal):
	if len(hand) == 5 and handtotal <= 21:
		Charlie = True
	else:
		Charlie = False
	return Charlie
def checkBJ(bj, bet):
	if bj == True:
		win = bt.BJWin(bet)
	return win

def winBJ1(hand1, hand2, handtotal1, handtotal2, bet1, bet2):
	if len(hand1) == 2 and handtotal1 == 21:
		BJ = True
		winAmount = checkBJ(BJ, bet1)
	else:
		winAmount = 0
	if len(hand2) == 2 and handtotal2 == 21:
		BJ = True
		winAmount2 = checkBJ(BJ, bet2)
	else:
		winAmount2 = 0
	return winAmount, winAmount2

def winBJ2(hand, handtotal, bet):
	if len(hand) == 2 and handtotal == 21:
		BJ = True
		AI1WA = checkBJ(BJ, bet)
	else:
		AI1WA = 0
	return AI1WA

def winCH2(hand, handtotal, bet):
	if len(hand) == 2 and handtotal == 21:
		CH = True
		AI1WA = checkCH(CH, bet)
	else:
		AI1WA = 0
	return AI1WA

def checkCH(charlie, bet):
	if charlie == True:
		win = bt.win(bet)
	return win
while True:
	accountChoice = input("Do you want to load an account (if you don't have one already, you will have the opportunity after the first round)? (y/n) ")
	print()
	try:
		accountChoice == 'y' or accountChoice == 'n'
	except:
		print("Please type in 'y' for yes or 'n' for no.")
		continue
	break
if accountChoice == 'y':
	while True:
		username = input("What is your username? ")
		code = input("\nWhat is your passcode? ")
		try:
			account = ac.accountLoad(username, code)
			accBal, accWin, accLoss, accBJ, accCH, accMA = account
		except:
			print("\nThe username or passcode is incorrect, please try again!\n")
			continue
		while True:
			if accMA > accWin + accLoss:
				accLoss -= 1
			else:
				break
		break
else:
	accBal = 1000
	accLoss = 0
	accWin = 0
	accBJ = 0
	accCH = 0
	accMA = 0
while True:
	pn = input("How many Players do you wish to play against? (1-6) ")
	try:
		pn = int(pn)
	except:
		print('Please use a number from 1 to 6.')
		continue
	break
print('\n===============================================\n')
AI1bet = 0
AI4bet = 0
AI6bet = 0
while True:
	print(f"Balance: {accBal}")
	print(f"Career Wins: {accWin}")
	print(f"Career Losses: {accLoss}")
	print(f"Career Blackjacks: {accBJ}")
	print(f"Career Charlies: {accCH}")
	print(f"Total Matches: {accMA}")
	dh.saveHand()
	hand1 = dh.hand()
	print('\n===============================================\n')
	print(f"The Dealer's hand is: [UNKONWN, {hand1[1]}]\n")
	print('===============================================\n')
	print()
	Loss = 0
	aiBal1 = random.randint(500, 3500)
	aiBal2 = random.randint(500, 3500)
	aiBal3 = random.randint(500, 3500)
	aiBal4 = random.randint(500, 3500)
	aiBal5 = random.randint(500, 3500)
	aiBal6 = random.randint(500, 3500)
	AI2bet = bt.aibetRand(aiBal2)
	AI3bet = bt.aibetRand(aiBal3)
	AI5bet = bt.aibetRand(aiBal5)
	AI2bet, aiBal2 = AI2bet
	AI3bet, aiBal3 = AI3bet
	AI5bet, aiBal5 = AI5bet
	bal = accBal
	bet = bt.userbet(bal)
	bet, bal = bet
	AI1bet = bt.aibetStrat(aiBal1, AI1bet)
	AI4bet = bt.aibetStrat(aiBal4, AI4bet)
	AI6bet = bt.aibetStrat(aiBal6, AI6bet)
	AI1bet, aiBal1 = AI1bet
	AI4bet, aiBal4 = AI4bet
	AI6bet, aiBal6 = AI6bet
	if pn >= 1:
		print(f"Player 1 bet: ${AI1bet}")
	if pn >= 2:
		print(f"Player 2 bet: ${AI2bet}")
	if pn >= 3:
		print(f"Player 3 bet: ${AI3bet}")
	if pn >= 4:
		print(f"Player 4 bet: ${AI4bet}")
	if pn >= 5:
		print(f"Player 5 bet: ${AI5bet}")
	if pn >= 6:
		print(f"Player 6 bet: ${AI6bet}")
	if pn == 1:
		AI1 = AIPlayer1.Player()
		time.sleep(5)
		os.system('cls')
		PC = PlayerChoices.Player()
		time.sleep(3)
		os.system('cls')
		DLR = Dealer.Player()
		time.sleep(10)
		os.system('cls')
	elif pn == 2:
		AI1 = AIPlayer1.Player()
		time.sleep(5)
		os.system('cls')
		PC = PlayerChoices.Player()
		time.sleep(3)
		os.system('cls')
		AI2 = AIPlayer2.Player()
		time.sleep(3)
		os.system('cls')
		DLR = Dealer.Player()
		time.sleep(10)
		os.system('cls')
	elif pn == 3:
		AI1 = AIPlayer1.Player()
		time.sleep(5)
		os.system('cls')
		PC = PlayerChoices.Player()
		time.sleep(3)
		os.system('cls')
		AI2 = AIPlayer2.Player()
		time.sleep(3)
		os.system('cls')
		AI3 = AIPlayer3.Player()
		time.sleep(3)
		os.system('cls')
		DLR = Dealer.Player()
		time.sleep(10)
		os.system('cls')
	elif pn == 4:
		AI1 = AIPlayer1.Player()
		time.sleep(5)
		os.system('cls')
		PC = PlayerChoices.Player()
		time.sleep(3)
		os.system('cls')
		AI2 = AIPlayer2.Player()
		time.sleep(3)
		os.system('cls')
		AI3 = AIPlayer3.Player()
		time.sleep(3)
		os.system('cls')
		AI4 = AIPlayer4.Player()
		time.sleep(3)
		os.system('cls')
		DLR = Dealer.Player()
		time.sleep(10)
		os.system('cls')
	elif pn == 5:
		AI1 = AIPlayer1.Player()
		time.sleep(5)
		os.system('cls')
		PC = PlayerChoices.Player()
		time.sleep(3)
		os.system('cls')
		AI2 = AIPlayer2.Player()
		time.sleep(3)
		os.system('cls')
		AI3 = AIPlayer3.Player()
		time.sleep(3)
		os.system('cls')
		AI4 = AIPlayer4.Player()
		time.sleep(3)
		os.system('cls')
		AI5 = AIPlayer5.Player()
		time.sleep(3)
		os.system('cls')
		DLR = Dealer.Player()
		time.sleep(10)
		os.system('cls')
	elif pn == 6:
		AI1 = AIPlayer1.Player()
		time.sleep(5)
		os.system('cls')
		PC = PlayerChoices.Player()
		time.sleep(3)
		os.system('cls')
		AI2 = AIPlayer2.Player()
		time.sleep(3)
		os.system('cls')
		AI3 = AIPlayer3.Player()
		time.sleep(3)
		os.system('cls')
		AI4 = AIPlayer4.Player()
		time.sleep(3)
		os.system('cls')
		AI5 = AIPlayer5.Player()
		time.sleep(3)
		os.system('cls')
		AI6 = AIPlayer6.Player()
		time.sleep(3)
		os.system('cls')
		DLR = Dealer.Player()
		time.sleep(10)
		os.system('cls')
	print("Everyone, Display your hands")
	print()
	if pn >= 1:
		try: #the following variables (i.e AI1H) is read as followed "AI1" = the player and "H" is what is stored, in this case, the AI's first hand is stored
			AI1H,AI1H2,AI1Ht,AI1Ht2,AI1F,AI1F2,AI1NH = AI1
		except:
			AI1H,AI1Ht,AI1F,AI1NH = AI1
			AI1H2 = ['a']
			AI1Ht2 = 0
	try:
		PH,PH2,PHt,PHt2,PF,PF2,PNH, PBJ, PBJ2, PCh, PCh2 = PC
	except:
		PH,PHt,PF,PNH, PBJ, PCh = PC
		PH2 = ['a']
		PHt2 = 0
		PBJ2 = False
		PCh2 = False
	if pn >= 2:
		try:
			AI2H,AI2H2,AI2Ht,AI2Ht2,AI2F,AI2F2,AI2NH = AI2
		except:
			AI2H,AI2Ht,AI2F,AI2NH = AI2
			AI2H2 = ['a']
			AI2Ht2 = 0
	if pn >= 3:
		try:
			AI3H,AI3H2,AI3Ht,AI3Ht2,AI3F,AI3F2,AI3NH = AI3
		except:
			AI3H,AI3Ht,AI3F,AI3NH = AI3
			AI3H2 = ['a']
			AI3Ht2 = 0
	if pn >= 4:
		try:
			AI4H,AI4H2,AI4Ht,AI4Ht2,AI4F,AI4F2,AI4NH = AI4
		except:
			AI4H,AI4Ht,AI4F,AI4NH = AI4
			AI4H2 = ['a']
			AI4Ht2 = 0
	if pn >= 5:
		try:
			AI5H,AI5H2,AI5Ht,AI5Ht2,AI5F,AI5F2,AI5NH = AI5
		except:
			AI5H,AI5Ht,AI5F,AI5NH = AI5
			AI5H2 = ['a']
			AI5Ht2 = 0
	if pn == 6:
		try:
			AI6H,AI6H2,AI6Ht,AI6Ht2,AI6F,AI6F2,AI6NH = AI6
		except:
			AI6H,AI6Ht,AI6F,AI6NH = AI6
			AI6H2 = ['a']
			AI6Ht2 = 0
	try:
		DLRH,DLRH2,DLRHt,DLRHt2,DLRBJ,DLRBJ2,DLRNH = DLR
	except:
		DLRH,DLRHt,DLRBJ,DLRNH = DLR
		DLRH2 = ['a']
		DLRHt2 = 0
		DLRBJ2 = False
	if pn >= 1:
		print()
		print('===============================================\n')
		if AI1NH != True:
			print(f"Player 1's hand: {AI1H}")
			print(f"Hand Total = {AI1Ht}")
		else:
			print(f"Player 1's first hand: {AI1H}")
			print(f"First Hand's Total = {AI1Ht}")
			print(f"Player 1's second hand: {AI1H2}")
			print(f"Second Hand's Total = {AI1Ht2}")
	print()
	print('===============================================\n')
	if PNH != True:
		print(f"Your hand: {PH}")
		print(f"Hand Total = {PHt}")
	else:
		print(f"Your first hand: {PH}")
		print(f"First Hand's Total = {PHt}")
		print(f"Your second hand: {PH2}")
		print(f"Second Hand's Total = {PHt2}")
	if pn >= 2:
		print()
		print('===============================================\n')
		if AI2NH != True:
			print(f"Player 2's hand: {AI2H}")
			print(f"Hand Total = {AI2Ht}")
		else:
			print(f"Player 2's first hand: {AI2H}")
			print(f"First Hand's Total = {AI2Ht}")
			print(f"Player 2's second hand: {AI2H2}")
			print(f"Second Hand's Total = {AI2Ht2}")
	if pn >= 3:
		print()
		print('===============================================\n')
		if AI3NH != True:
			print(f"Player 3's hand: {AI3H}")
			print(f"Hand Total = {AI3Ht}")
		else:
			print(f"Player 3's first hand: {AI3H}")
			print(f"First Hand's Total = {AI3Ht}")
			print(f"Player 3's second hand: {AI3H2}")
			print(f"Second Hand's Total = {AI3Ht2}")
	if pn >= 4:
		print()
		print('===============================================\n')
		if AI4NH != True:
			print(f"Player 4's hand: {AI4H}")
			print(f"Hand Total = {AI4Ht}")
		else:
			print(f"Player 4's first hand: {AI4H}")
			print(f"First Hand's Total = {AI4Ht}")
			print(f"Player 4's second hand: {AI4H2}")
			print(f"Second Hand's Total = {AI4Ht2}")
	if pn >= 5:
		print()
		print('===============================================\n')
		if AI5NH != True:
			print(f"Player 5's hand: {AI5H}")
			print(f"Hand Total = {AI5Ht}")
		else:
			print(f"Player 5's first hand: {AI5H}")
			print(f"First Hand's Total = {AI5Ht}")
			print(f"Player 5's second hand: {AI5H2}")
			print(f"Second Hand's Total = {AI5Ht2}")
	if pn >= 6:
		print()
		print('===============================================\n')
		if AI6NH != True:
			print(f"Player 6's hand: {AI6H}")
			print(f"Hand Total = {AI6Ht}")
		else:
			print(f"Player 6's first hand: {AI6H}")
			print(f"First Hand's Total = {AI6Ht}")
			print(f"Player 6's second hand: {AI6H2}")
			print(f"Second Hand's Total = {AI6Ht2}")
	print()
	print('===============================================\n')
	if DLRNH != True:
		print(f"Dealer's hand: {DLRH}")
		print(f"Hand Total = {DLRHt}")
	else:
		print(f"Dealer's first hand: {DLRH}")
		print(f"First Hand's Total = {DLRHt}")
		print(f"Dealer's second hand: {DLRH2}")
		print(f"Second Hand's Total = {DLRHt2}")
	AI1B = AI1bet
	AI1B2 = AI1bet
	PB = bet
	PB2 = bet
	AI2B = AI2bet
	AI2B2 = AI2bet
	AI3B = AI3bet
	AI3B2 = AI3bet
	AI4B = AI4bet
	AI4B2 = AI4bet
	AI5B = AI5bet
	AI5B2 = AI5bet
	AI6B = AI6bet
	AI6B2 = AI6bet

	if pn >= 1:
		if AI1NH == True:
			AI1B = foldbet2(AI1bet, AI1F, AI1F2)
			AI1B, AI1B2 = AI1B
			if AI1F == True:
				AI1bet += AI1B
				AI1H = ['a']
				AI1Ht = 0
			if AI1F2 == True:
				AI1bet += AI1B2
				AI1H2 = ['a']
				AI1Ht2 = 0
		else:
			AIB = foldbet(AI1bet, AI1F)
			if AI1F == True:
				AI1bet += AI1B
				AI1H = ['a']
				AI1Ht = 0
	if PNH == True:
		PB = foldbet2(bet, PF, PF2)
		PB, PB2 = PB
		if PF == True:
			bet += PB
			PH = ['a']
			PHt = 0
		if PF2 == True:
			bet += PB2
			PH2 = ['a']
			PHt2 = 0
		Loss = 1
	else:
		PB = foldbet(bet, PF)
		if PF == True:
			bet += PB
			PH = ['a']
			PHt = 0
		Loss = 1
	if pn >= 2:
		if AI2NH == True:
			AI2B = foldbet2(AI2bet, AI2F, AI2F2)
			AI2B, AI2B2 = AI2B
			if AI2F == True:
				AI2bet += AI2B
				AI2H = ['a']
				AI2Ht = 0
			if AI2F2 == True:
				AI2bet += AI2B2
				AI2H2 = ['a']
				AI2Ht2 = 0
		else:
			AI2B = foldbet(AI2bet, AI2F)
			if AI2F == True:
				AI2bet += AI2B
				AI2H = ['a']
				AI2Ht = 0
	if pn >= 3:
		if AI3NH == True:
			AI3B = foldbet2(AI3bet, AI3F, AI3F2)
			AI3B, AI3B2 = AI3B
			if AI3F == True:
				AI3bet += AI3B
				AI3H = ['a']
				AI3Ht = 0
			if AI3F2 == True:
				AI3bet += AI3B2
				AI3H2 = ['a']
				AI3Ht2 = 0
		else:
			AI3B = foldbet(AI3bet, AI3F)
			if AI3F == True:
				AI3bet += AI3B
				AI3H = ['a']
				AI3Ht = 0
	if pn >= 4:
		if AI4NH == True:
			AI4B = foldbet2(AI4bet, AI4F, AI4F2)
			AI4B, AI4B2 = AI4B
			if AI4F == True:
				AI4bet += AI4B
				AI4H = ['a']
				AI4Ht = 0
			if AI4F2 == True:
				AI4bet += AI4B2
				AI4H2 = ['a']
				AI4Ht2 = 0
		else:
			AI4B = foldbet(AI4bet, AI4F)
			if AI4F == True:
				AI4bet += AI4B
				AI4H = ['a']
				AI4Ht = 0
	if pn >= 5:
		if AI5NH == True:
			AI5B = foldbet2(AI5bet, AI5F, AI5F2)
			AI5B, AI5B2 = AI5B
			if AI5F == True:
				AI5bet += AI5B
				AI5H = ['a']
				AI5Ht = 0
			if AI5F2 == True:
				AI5bet += AI5B2
				AI5H2 = ['a']
				AI5Ht2 = 0
		else:
			AI5B = foldbet(AI5bet, AI5F)
			if AI5F == True:
				AI5bet += AI5B
				AI5H = ['a']
				AI5Ht = 0
	if pn >= 6:
		if AI6NH == True:
			AI6B = foldbet2(AI6bet, AI6F, AI6F2)
			AI6B, AI6B2 = AI6B
			if AI6F == True:
				AI6bet += AI6B
				AI6H = ['a']
				AI6Ht = 0
			if AI6F2 == True:
				AI6bet += AI6B2
				AI6H2 = ['a']
				AI6Ht2 = 0
		else:
			AI6B = foldbet(AI6bet, AI6F)
			if AI6F == True:
				AI6bet += AI6B
				AI6H = ['a']
				AI6Ht = 0
	if Loss == 1:
		accLoss += 1
		Loss = 0
	if pn == 1:
		AI2H = ['a']
		AI2H2 = ['a']
		AI2Ht = 0
		AI2Ht2 = 0
		AI3H = ['a']
		AI3H2 = ['a']
		AI3Ht = 0
		AI3Ht2 = 0
		AI4H = ['a']
		AI4H2 = ['a']
		AI4Ht = 0
		AI4Ht2 = 0
		AI5H = ['a']
		AI5H2 = ['a']
		AI5Ht = 0
		AI5Ht2 = 0
		AI6H = ['a']
		AI6H2 = ['a']
		AI6Ht = 0
		AI6Ht2 = 0
	if pn == 2:
		AI3H = ['a']
		AI3H2 = ['a']
		AI3Ht = 0
		AI3Ht2 = 0
		AI4H = ['a']
		AI4H2 = ['a']
		AI4Ht = 0
		AI4Ht2 = 0
		AI5H = ['a']
		AI5H2 = ['a']
		AI5Ht = 0
		AI5Ht2 = 0
		AI6H = ['a']
		AI6H2 = ['a']
		AI6Ht = 0
		AI6Ht2 = 0
	if pn == 3:
		AI4H = ['a']
		AI4H2 = ['a']
		AI4Ht = 0
		AI4Ht2 = 0
		AI5H = ['a']
		AI5H2 = ['a']
		AI5Ht = 0
		AI5Ht2 = 0
		AI6H = ['a']
		AI6H2 = ['a']
		AI6Ht = 0
		AI6Ht2 = 0
	if pn == 4:
		AI5H = ['a']
		AI5H2 = ['a']
		AI5Ht = 0
		AI5Ht2 = 0
		AI6H = ['a']
		AI6H2 = ['a']
		AI6Ht = 0
		AI6Ht2 = 0
	if pn == 5:
		AI6H = ['a']
		AI6H2 = ['a']
		AI6Ht = 0
		AI6Ht2 = 0
	
	if AI1Ht > 21:
		AI1Ht = 0
	if PHt > 21:
		PHt = 0
	if AI1Ht2 > 21:
		AI1Ht2 = 0
	if AI2Ht > 21:
		AI2Ht = 0
	if AI2Ht2 > 21:
		AI2Ht2 = 0
	if AI3Ht > 21:
		AI3Ht = 0
	if AI3Ht2 > 21:
		AI3Ht2 = 0
	if AI4Ht > 21:
		AI4Ht = 0
	if AI4Ht2 > 21:
		AI4Ht2 = 0
	if AI5Ht > 21:
		AI5Ht = 0
	if AI5Ht2 > 21:
		AI5Ht2 = 0
	if AI6Ht > 21:
		AI6Ht = 0
	if AI6Ht2 > 21:
		AI6Ht2 = 0
	if DLRHt > 21:
		DLRHt = 0
	if DLRHt2 > 21:
		DLRHt2 = 0
	
	AI1BJ1 = BJ(AI1H, AI1Ht)
	AI1BJ2 = BJ(AI1H2, AI1Ht2)
	AI2BJ1 = BJ(AI2H, AI2Ht)
	AI2BJ2 = BJ(AI2H2, AI2Ht2)
	AI3BJ1 = BJ(AI3H, AI3Ht)
	AI3BJ2 = BJ(AI3H2, AI3Ht2)
	AI4BJ1 = BJ(AI4H, AI4Ht)
	AI4BJ2 = BJ(AI4H2, AI4Ht2)
	AI5BJ1 = BJ(AI5H, AI5Ht)
	AI5BJ2 = BJ(AI5H2, AI5Ht2)
	AI6BJ1 = BJ(AI6H, AI6Ht)
	AI6BJ2 = BJ(AI6H2, AI6Ht2)

	AI1CH1 = CH(AI1H, AI1Ht)
	AI1CH2 = CH(AI1H2, AI1Ht2)
	AI2CH1 = CH(AI2H, AI2Ht)
	AI2CH2 = CH(AI2H2, AI2Ht2)
	AI3CH1 = CH(AI3H, AI3Ht)
	AI3CH2 = CH(AI3H2, AI3Ht2)
	AI4CH1 = CH(AI4H, AI4Ht)
	AI4CH2 = CH(AI4H2, AI4Ht2)
	AI5CH1 = CH(AI5H, AI5Ht)
	AI5CH2 = CH(AI5H2, AI5Ht2)
	AI6CH1 = CH(AI6H, AI6Ht)
	AI6CH2 = CH(AI6H2, AI6Ht2)

	if AI1CH1 == True or AI1CH2 == True or PCh == True or PCh2 == True or AI2CH1 == True or AI2CH2 == True or AI3CH1 == True or AI3CH2 == True or AI4CH1 == True or AI4CH2 == True or AI5CH1 == True or AI5CH2 == True or AI6CH1 == True or AI6CH2 == True:
		if pn >= 1:
			if AI1NH == True:
				AI1WA = checkCH(AI1CH1, AI1B)
				AI1WA2 = checkCH(AI1CH2, AI1B2)
				aiBal1 += AI1WA + AI1WA2
			else:
				AI1WA = checkCH(AI1CH1, AI1B)
				aiBal1 += AI1WA
		if PNH == True:
			if PCh == True:
				PWA = checkBJ(PCh, PB)
				bal += PWA
			if PCh2 == True:
				PWA = checkBJ(PCh2, PB2)
				bal += PWA
		else:
			if PCh == True:
				PWA = checkBJ(PCh, PB)
				bal += PWA
		if pn >= 2:
			if AI2NH == True:
				AI2WA = checkCH(AI2CH1, AI2B)
				AI2WA2 = checkCH(AI2CH2, AI2B2)
				aiBal2 += AI2WA + AI2WA2
			else:
				AI2WA = checkCH(AI2CH1, AI2B)
				aiBal2 += AI2WA
		if pn >= 3:
			if AI3NH == True:
				AI3WA = checkCH(AI3CH1, AI3B)
				AI3WA2 = checkCH(AI3CH2, AI3B2)
				aiBal3 += AI3WA + AI3WA2
			else:
				AI3WA = checkCH(AI3CH1, AI3B)
				aiBal3 += AI3WA
		if pn >= 4:
			if AI4NH == True:
				AI4WA = checkCH(AI4CH1, AI4B)
				AI4WA2 = checkCH(AI4CH2, AI4B2)
				aiBal4 += AI4WA + AI4WA2
			else:
				AI4WA = checkCH(AI4CH1, AI4B)
				aiBal4 += AI4WA
		if pn >= 5:
			if AI5NH == True:
				AI5WA = checkCH(AI5CH1, AI5B)
				AI5WA2 = checkCH(AI5CH2, AI5B2)
				aiBal5 += AI5WA + AI5WA2
			else:
				AI5WA = checkCH(AI5CH1, AI5B)
				aiBal5 += AI5WA
		if pn >= 6:
			if AI6NH == True:
				AI6WA = checkCH(AI6CH1, AI6B)
				AI6WA2 = checkCH(AI6CH2, AI6B2)
				aiBal6 += AI6WA + AI6WA2
			else:
				AI6WA = checkCH(AI6CH1, AI6B)
				aiBal6 += AI6WA
	while True:
		if AI1BJ1 == True or AI1BJ2 == True or PBJ == True or PBJ2 == True or AI2BJ1 == True or AI2BJ2 == True or AI3BJ1 == True or AI3BJ2 == True or AI4BJ1 == True or AI4BJ2 == True or AI5BJ1 == True or AI5BJ2 == True or AI6BJ1 == True or AI6BJ2 == True:
			if pn >= 1:
				if AI1NH == True:
					AI1WA = winBJ1(AI1H, AI1H2, AI1Ht, AI1Ht2, AI1B, AI1B2)
					AI1WA, AI1WA2 = AI1WA
					aiBal1 += AI1WA + AI1WA2
				else:
					AI1WA = winBJ2(AI1H, AI1Ht, AI1B)
					aiBal1 += AI1WA
			if PNH == True:
				if PBJ == True:
					PWA = checkBJ(PBJ, PB)
				if PBJ2 == True:
					PWA += checkBJ(PBJ2, PB2)
				bal += PWA
			else:
				if PBJ == True:
					PWA = checkBJ(PBJ, PB)
				bal += PWA
			if pn >= 2:
				if AI2NH == True:
					AI2WA = winBJ1(AI2H, AI2H2, AI2Ht, AI2Ht2, AI2B, AI2B2)
					AI2WA, AI2WA2 = AI2WA
					aiBal2 += AI2WA + AI2WA2
				else:
					AI2WA = winBJ2(AI2H, AI2Ht, AI2B)
					aiBal2 += AI2WA
			if pn >= 3:
				if AI3NH == True:
					AI3WA = winBJ1(AI3H, AI3H2, AI3Ht, AI3Ht2, AI3B, AI3B2)
					AI3WA, AI3WA2 = AI3WA
					aiBal3 += AI3WA + AI3WA2
				else:
					AI3WA = winBJ2(AI3H, AI3Ht, AI3B)
					aiBal3 += AI3WA
			if pn >= 4:
				if AI4NH == True:
					AI4WA = winBJ1(AI4H, AI4H2, AI4Ht, AI4Ht2, AI4B, AI4B2)
					AI4WA, AI4WA2 = AI4WA
					aiBal4 += AI4WA + AI4WA2
				else:
					AI4WA = winBJ2(AI4H, AI4Ht, AI4B)
					aiBal4 += AI4WA
			if pn >= 5:
				if AI5NH == True:
					AI5WA = winBJ1(AI5H, AI5H2, AI5Ht, AI5Ht2, AI5B, AI5B2)
					AI5WA, AI5WA2 = AI5WA
					aiBal5 += AI5WA + AI5WA2
				else:
					AI5WA = winBJ2(AI5H, AI5Ht, AI5B)
					aiBal5 += AI5WA
			if pn >= 6:
				if AI6NH == True:
					AI6WA = winBJ1(AI6H, AI6H2, AI6Ht, AI6Ht2, AI6B, AI6B2)
					AI6WA, AI6WA2 = AI6WA
					aiBal6 += AI6WA + AI6WA2
				else:
					AI6WA = winBJ2(AI6H, AI6Ht, AI6B)
					aiBal6 += AI6WA
			if PBJ == True:
				print("You Win!!\n")
				print(f"You won ${PWA}")
				accWin += 1
			if PBJ2 == True:
				print("You Win!!\n")
				print(f"You won ${PWA}")
				accWin += 1
			if AI1BJ1 == True:
				print("Player 1 Wins!!\n")
				Loss = 1
			if AI1BJ2 == True:
				print("Player 1 Wins!!\n")
				Loss = 1
			if AI2BJ1 == True:
				print("Player 2 Wins!!\n")
				Loss = 1
			if AI2BJ2 == True:
				print("Player 2 Wins!!\n")
				Loss = 1
			if AI3BJ1 == True:
				print("Player 3 Wins!!\n")
				Loss = 1
			if AI3BJ2 == True:
				print("Player 3 Wins!!\n")
				Loss = 1
			if AI4BJ1 == True:
				print("Player 4 Wins!!\n")
				Loss = 1
			if AI4BJ2 == True:
				print("Player 4 Wins!!\n")
				Loss = 1
			if AI5BJ1 == True:
				print("Player 5 Wins!!\n")
				Loss = 1
			if AI5BJ2 == True:
				print("Player 5 Wins!!\n")
				Loss = 1
			if AI6BJ1 == True:
				print("Player 6 Wins!!\n")
				Loss = 1
			if AI6BJ2 == True:
				print("Player 6 Wins!!\n")
				Loss = 1
			if Loss == 1:
				Loss = 0
				accLoss += 1
			break
		elif DLRBJ == True or DLRBJ2 == True:
			print("The Dealer Wins!!")
			Loss = 1
			if Loss == 1:
				accLoss += 1
			break
		else:
			Loss = 0
			AI1Ht = int(AI1Ht)
			AI1Ht2 = int(AI1Ht2)
			PHt = int(PHt)
			PHt2 = int(PHt2)
			AI2Ht = int(AI2Ht)
			AI2Ht2 = int(AI2Ht2)
			AI3Ht = int(AI3Ht)
			AI3Ht2 = int(AI3Ht2)
			AI4Ht = int(AI4Ht)
			AI4Ht2 = int(AI4Ht2)
			AI5Ht = int(AI5Ht)
			AI5Ht2 = int(AI5Ht2)
			AI6Ht = int(AI6Ht)
			AI6Ht2 = int(AI6Ht2)
			DLRHt = int(DLRHt)
			DLRHt2 = int(DLRHt2)
			compareTotals = {"The Dealer's First Hand": DLRHt, "The Dealer's Second Hand": DLRHt2, "Player 1's First Hand": AI1Ht, "Player 1's Second Hand": AI1Ht2, 'Your First Hand': PHt, 'Your Second Hand': PHt2, "Player 2's First Hand": AI2Ht, "Player 2's Second Hand": AI2Ht2, "Player 3's First Hand": AI3Ht, "Player 3's Second Hand": AI3Ht2, "Player 4's First Hand": AI4Ht, "Player 4's Second Hand": AI4Ht2, "Player 5's First Hand": AI5Ht, "Player 5's Second Hand": AI5Ht2, "Player 6's First Hand": AI6Ht, "Player 6's Second Hand": AI6Ht2}
			winner = max(compareTotals, key=compareTotals.get)
			if winner == 'Your First Hand':
				print("Your First Hand Wins!!\n")
				Pwin = bt.win(PB)
				print(f"You won ${Pwin}")
				bal += Pwin
				print(f"Your balance is now {bal}")
				accWin += 1
			elif winner == 'Your Second Hand':
				print("Your Second Hand Wins!!\n")
				Pwin = bt.win(PB)
				print(f"You won ${Pwin}")
				bal += Pwin
				print(f"Your balance is now {bal}")
				accWin += 1
			elif winner == "Player 1's First Hand":
				print("Player 1's First Hand Wins!!\n")
				AI1win = bt.win(AI1B)
				aiBal1 += AI1win
				Loss = 1
			elif winner == "Player 1's Second Hand":
				print("Player 1's Second Hand Wins!!\n")
				AI1win = bt.win(AI1B2)
				aiBal1 += AI1win
				Loss = 1
			elif winner == "Player 2's First Hand":
				print("Player 2's First Hand Wins!!\n")
				AI2win = bt.win(AI2B)
				aiBal2 += AI2win
				Loss = 1
			elif winner == "Player 2's Second Hand":
				print("Player 2's Second Hand Wins!!\n")
				AI2win = bt.win(AI2B2)
				aiBal2 += AI2win
				Loss = 1
			elif winner == "Player 3's First Hand":
				print("Player 3's First Hand Wins!!\n")
				AI3win = bt.win(AI3B)
				aiBal3 += AI3win
				Loss = 1
			elif winner == "Player 3's Second Hand":
				print("Player 3's Second Hand Wins!!\n")
				AI3win = bt.win(AI3B2)
				aiBal3 += AI3win
				Loss = 1
			elif winner == "Player 4's First Hand":
				print("Player 4's First Hand Wins!!\n")
				AI4win = bt.win(AI4B)
				aiBal4 += AI4win
				Loss = 1
			elif winner == "Player 4's Second Hand":
				print("Player 4's Second Hand Wins!!\n")
				AI4win = bt.win(AI4B2)
				aiBal4 += AI4win
				Loss = 1
			elif winner == "Player 5's First Hand":
				print("Player 5's First Hand Wins!!\n")
				AI5win = bt.win(AI5B)
				aiBal5 += AI5win
				Loss = 1
			elif winner == "Player 5's Second Hand":
				print("Player 5's Second Hand Wins!!\n")
				AI5win = bt.win(AI5B2)
				aiBal5 += AI5win
				Loss = 1
			elif winner == "Player 6's First Hand":
				print("Player 6's First Hand Wins!!\n")
				AI6win = bt.win(AI6B)
				aiBal6 += AI6win
				Loss = 1
			elif winner == "Player 6's Second Hand":
				print("Player 6's Second Hand Wins!!\n")
				AI6win = bt.win(AI6B2)
				aiBal6 += AI6win
				Loss = 1
			elif winner == "The Dealer's First Hand":
				print("The Dealer's First Hand Wins!!\n")
				Loss = 1
			elif winner == "The Dealer's Second Hand":
				print("The Dealer's Second Hand Wins!!!\n")
				Loss = 1
			elif winner == "Player 1's First Hand" and AI1Ht == 0:
				print("No one wins!!")
				Loss = 1
			else:
				print("something went wrong, go to line 841")
			if Loss == 1:
				accLoss += 1
			break
	accBal = bal
	if PBJ == True:
		accBJ += 1
	if PBJ2 == True:
		accBJ += 1
	if PCh == True:
		accCH += 1
	if PCh2 == True:
		accCH += 1
	accMA += 1
	ac.accountSave(accBal, accWin, accLoss, accBJ, accCH, accMA)
	print('\n===============================================\n')