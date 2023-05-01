import random
def userbet(balance):
	print(f"Current Balance = {balance}")
	while True:
		while True:
			amount = input("How much do you want to bet? ")
			try:
				amount = int(amount)
			except:
				print('Please use numbers. (i.e. 10)')
				continue
			break
		newBal = balance - amount
		if newBal >= 0:
			break
		else:
			print("You don't have enough money for this!")
			print("Try again!")
	return amount, newBal

def aibetStrat(balance, previousAmount):
	while True:
		if previousAmount == 0:
			amount = 5
		else:
			amount = previousAmount * 2
		newBal = balance - amount
		if newBal >= 0:
			break
		else:
			previousAmount /= 2
	return amount, newBal

def aibetRand(balance):
	while True:
		amount = min(random.randint(1, balance), random.randint(1, balance))
		newBal = balance - amount
		if newBal >= 0:
			break
		else:
			continue
	return amount, newBal

def BJWin(amount):
	payout = amount + (amount * (3//2))
	return payout

def win(amount):
	payout = 2 * amount
	return payout