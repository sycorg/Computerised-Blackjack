import linecache
import msvcrt

def accountSave(balance, wins, losses, blackjacks, charlies, matches):
	balance = str(balance)
	wins = str(wins)
	losses = str(losses)
	blackjacks = str(blackjacks)
	charlies = str(charlies)
	matches = str(matches)
	while True:
		accountExists = input("Do you have an account? (y/n) ")
		try:
			accountExists == 'y' or accountExists == 'n'
		except:
			print("type in 'y' for yes or 'n' for no")
			continue
		break
	if accountExists == 'y':
		while True:
			username = input("What is your username? ")
			code = input("What is your passcode? ")
			try:
				open(f"{username}{code}.txt", "r")
			except:
				print('The username or passcode is incorrect, please try again!')
				continue
			break
		account = open(f"{username}{code}.txt", "w")
		#row 1
		account.write(f"{balance}\n")
		account.close()
		account = open(f"{username}{code}.txt", "a")
		#row 2
		account.write(f"{wins}\n")
		#row 3
		account.write(f"{losses}\n")
		#row 4
		account.write(f"{blackjacks}\n")
		#row 5
		account.write(f"{charlies}\n")
		#row 6
		account.write(f"{matches}\n")
		account.close()
	else:
		while True:
			username = input("What is your desired username? ")
			code = input("What is your desired passcode? (4 numbers) ")
			try:
				code = int(code)
			except:
				print("Please use numbers for your passcode (i.e. 1234)")
				continue
			if len(str(code)) == 4:
				code = int(code)
				break
			else:
				print("Please use 4 numbers for your passcode (i.e. 1234)")
				continue
		account = open(f"{username}{code}.txt", "w")
		#row 1
		account.write(f"{balance}\n")
		account.close()
		account = open(f"{username}{code}.txt", "a")
		#row 2
		account.write(f"{wins}\n")
		#row 3
		account.write(f"{losses}\n")
		#row 4
		account.write(f"{blackjacks}\n")
		#row 5
		account.write(f"{charlies}\n")
		#row 6
		account.write(f"{matches}\n")
		account.close()

def accountBal(username, code):
	try:
		open(f"{username}{code}.txt", "r")
	except:
		print('The username or passcode is incorrect, please try again!')
		return 0
	Balance = linecache.getline(rf"{username}{code}.txt", 1)
	return Balance

def accountWins(username, code):
	try:
		open(f"{username}{code}.txt", "r")
	except:
		print('The username or passcode is incorrect, please try again!')
		return 0
	accountWins = linecache.getline(rf"{username}{code}.txt", 2)
	return accountWins

def accountLosses(username, code):
	try:
		open(f"{username}{code}.txt", "r")
	except:
		print('The username or passcode is incorrect, please try again!')
		return 0
	accountLosses = linecache.getline(rf"{username}{code}.txt", 3)
	return accountLosses

def accountBJ(username, code):
	try:
		open(f"{username}{code}.txt", "r")
	except:
		print('The username or passcode is incorrect, please try again!')
		return 0
	accountBJ = linecache.getline(rf"{username}{code}.txt", 4)
	return accountBJ

def accountCharlies(username, code):
	try:
		open(f"{username}{code}.txt", "r")
	except:
		print('The username or passcode is incorrect, please try again!')
		return 0
	accountCharlies = linecache.getline(rf"{username}{code}.txt", 5)
	return accountCharlies

def accountLoad(username, code):
	open(f"{username}{code}.txt", "r")
	bal = int(linecache.getline(rf"{username}{code}.txt", 1))
	wins = int(linecache.getline(rf"{username}{code}.txt", 2))
	losses = int(linecache.getline(rf"{username}{code}.txt", 3))
	blackjacks = int(linecache.getline(rf"{username}{code}.txt", 4))
	charlies = int(linecache.getline(rf"{username}{code}.txt", 5))
	matches = int(linecache.getline(rf"{username}{code}.txt", 6))
	return bal, wins, losses, blackjacks, charlies, matches