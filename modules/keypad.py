

#Keypad (specific inputx4 -> output)
def keypad():
	#Def Vars - keyLists
	keys = [
	    "lolli", "at", "lambda", "light", "staff", "h", "backC", "mouth",
	    "slap", "starW", "?", "copy", "butt", "kk", "stroke", "6", "para",
	    "bT", "smile", "trident", "forwardC", "shrek3", "starB", "stitch",
	    "ae", "headN", "omega"
	]
	c1 = ["lolli", "at", "lambda", "light", "staff", "h", "backC"]
	c2 = ["mouth", "lolli", "backC", "slap", "starW", "h", "?"]
	c3 = ["copy", "butt", "slap", "kk", "stroke", "lambda", "starW"]
	c4 = ["6", "para", "bT", "staff", "kk", "?", "smile"]
	c5 = ["trident", "smile", "bT", "forwardC", "para", "shrek3", "starB"]
	c6 = ["6", "mouth", "stitch", "ae", "trident", "headN", "omega"]

	#Def Vars - userLists
	global userKeys
	userKeys = []
	print(keys)
	print(" ")

	for i in range(4):
		cont = False
		while cont == False:
			keyi = input("KeyButton " + str(i + 1) + "? (see list above): ")
			if keys.count(keyi) == 1:
				userKeys.append(keyi)
				cont = True
			else:
				print(
				    "Error. You typed something wrong. Please enter a valid key."
				)
				cont = False
	print("Your keys are " + str(userKeys))
	print(" ")

	#Logic
	global answerKeys
	answerKeys = []
	if all(elem in c1 for elem in userKeys):
		answerKeys = c1
		print("Collum: " + str(answerKeys))
	elif all(elem in c2 for elem in userKeys):
		answerKeys = c2
		print("Collum: " + str(answerKeys))
	elif all(elem in c3 for elem in userKeys):
		answerKeys = c3
		print("Collum: " + str(answerKeys))
	elif all(elem in c4 for elem in userKeys):
		answerKeys = c4
		print("Collum: " + str(answerKeys))
	elif all(elem in c5 for elem in userKeys):
		answerKeys = c5
		print("Collum: " + str(answerKeys))
	elif all(elem in c6 for elem in userKeys):
		answerKeys = c6
		print("Collum: " + str(answerKeys))
	else:
		print("No collum has all of the inputed keys")

	#Final print()
	finalList = [x for x in answerKeys if x in userKeys]
	print(" ")
	print("Final: " + str(finalList))