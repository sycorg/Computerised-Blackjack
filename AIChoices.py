import DealerHand
import HandType
#This function is the algorithm used to determine the decisions the AI should make
def Choice(handtotal, value, value1, value2):
	if len(value) >= 2 or HandType.hardHand(value1, value2) == True and HandType.pairs(value1, value2) == False and HandType.softHand(value1, value2) == False:
		if 5 <= handtotal <= 11:
			decision = 1
		elif 7 <= DealerHand.dealerValue() <= 10 and 12 <= handtotal <= 14:
			decision = 1
		elif 7 <= DealerHand.dealerValue() <= 9 and handtotal == 15:
			decision = 1
		elif 7 <= DealerHand.dealerValue() <= 8 and handtotal == 16:
			decision = 1
		elif 2 <= DealerHand.dealerValue() <= 3 and handtotal == 12:
			decision = 1
		elif DealerHand.dealerValue() == 11 and 5 <= handtotal <= 14:
			decision = 1
		elif 2 <= DealerHand.dealerValue() <= 6 and 13 <= handtotal <= 16:
			decision = 2
		elif 4 <= DealerHand.dealerValue() <= 6 and handtotal == 12:
			decision = 2
		elif 2 <= DealerHand.dealerValue() <= 10 and 18 <= handtotal <= 21:
			decision = 2
		elif 2 <= DealerHand.dealerValue() <= 10 and handtotal == 17:
			decision = 2
		elif DealerHand.dealerValue() == 11 and 18 <= handtotal <= 21:
			decision = 2
		elif DealerHand.dealerValue() == 11 and handtotal == 17:
			decision = 3
		elif 9 <= DealerHand.dealerValue() <= 10 and handtotal == 16:
			decision = 3
		elif DealerHand.dealerValue() == 10 and handtotal == 15:
			decision = 3
	if HandType.softHand(value1, value2) == True and HandType.pairs(value1, value2) == False and HandType.hardHand(value1, value2) == False and len(value) == 2:
		if 2 <= DealerHand.dealerValue() <= 10 and value == ['A', '9'] or value == ['9', 'A']:
			decision = 2
		elif 2 <= DealerHand.dealerValue() <= 10 and value == ['A', '8'] or value == ['8', 'A']:
			decision = 2
		elif 2 <= DealerHand.dealerValue() <= 8 and value == ['A', '7'] or value == ['7', 'A']:
			decision = 2
		elif DealerHand.dealerValue() == 11 and value == ['A', '9'] or value == ['9', 'A']:
			decision = 2
		elif DealerHand.dealerValue() == 11 and value == ['A', '8'] or value == ['8', 'A']:
			decision = 2
		elif 2 <= DealerHand.dealerValue() <= 10 and value == ['A', '2'] or value == ['2', 'A']:
			decision = 1
		elif 2 <= DealerHand.dealerValue() <= 10 and value == ['A', '3'] or value == ['3', 'A']:
			decision = 1
		elif 2 <= DealerHand.dealerValue() <= 10 and value == ['A', '4'] or value == ['4', 'A']:
			decision = 1
		elif 2 <= DealerHand.dealerValue() <= 10 and value == ['A', '5'] or value == ['5', 'A']:
			decision = 1
		elif 2 <= DealerHand.dealerValue() <= 10 and value == ['A', '6'] or value == ['6', 'A']:
			decision = 1
		elif 9 <= DealerHand.dealerValue() <= 10 and value == ['A', '7'] or value == ['7', 'A']:
			decision = 1
		elif DealerHand.dealerValue() == 11 and value == ['A', '2'] or value == ['2', 'A']:
			decision = 1
		elif DealerHand.dealerValue() == 11 and value == ['A', '3'] or value == ['3', 'A']:
			decision = 1
		elif DealerHand.dealerValue() == 11 and value == ['A', '4'] or value == ['4', 'A']:
			decision = 1
		elif DealerHand.dealerValue() == 11 and value == ['A', '5'] or value == ['5', 'A']:
			decision = 1
		elif DealerHand.dealerValue() == 11 and value == ['A', '6'] or value == ['6', 'A']:
			decision = 1
		elif DealerHand.dealerValue() == 11 and value == ['A', '7'] or value == ['7', 'A']:
			decision = 1
	if HandType.pairs(value1, value2) == True and HandType.softHand(value1, value2) == False and HandType.hardHand(value1, value2) == False and len(value) == 2:
		if value == ['A', 'A']:
			decision = 4
		elif 2 <= DealerHand.dealerValue() <= 6 and value == ['9', '9']:
			decision = 4
		elif 8 <= DealerHand.dealerValue() <= 9 and value == ['9', '9']:
			decision = 4
		elif 2 <= DealerHand.dealerValue() <= 10 and value == ['8', '8']:
			decision = 4
		elif 2 <= DealerHand.dealerValue() <= 7 and value == ['7', '7']:
			decision = 4
		elif 2 <= DealerHand.dealerValue() <= 6 and value == ['6', '6'] or value == ['3', '3'] or value == ['2', '2']:
			decision = 4
		elif 5 <= DealerHand.dealerValue() <= 6 and value == ['4', '4']:
			decision = 4
		elif value == ['10', '10'] or value == ['J', 'J'] or value == ['Q', 'Q'] or value == ['K', 'K']:
			decision = 2
		elif DealerHand.dealerValue() == 7 and value == ['9', '9']:
			decision = 2
		elif DealerHand.dealerValue() == 10 and value == ['9', '9']:
			decision = 2
		elif DealerHand.dealerValue() == 11 and value == ['9', '9']:
			decision = 2
		elif 8 <= DealerHand.dealerValue() <= 10 and value == ['7', '7'] or value == ['2', '2'] or value == ['3', '3']:
			decision = 1
		elif 7 <= DealerHand.dealerValue() <= 10 and value == ['6', '6'] or value == ['4', '4']:
			decision = 1
		elif value == ['5', '5']:
			decision = 1
		elif 2 <= DealerHand.dealerValue() <= 4 and value == ['4', '4']:
			decision = 1
		elif DealerHand.dealerValue() == 11 and value == ['7', '7'] or value == ['6', '6'] or value == ['4', '4'] or value == ['3', '3'] or value == ['2', '2']:
			decision = 1
		elif DealerHand.dealerValue() == 11 and value == ['8', '8']:
			decision = 4
	return decision