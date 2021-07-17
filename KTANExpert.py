#imports
import time
import math
from who2lists import *
from morse import *


#variables
isDoing = True
explode = False
skip = input("Skip intro? y/n: ")
module = "EMPTY"


#MODULE FUNCTIONS

#Wires (inputx7(8) -> output)
def wires():
	#variables
	number = input("Number of Wires? (3/4/5/6): ")
	wirelist = []
	#if number of wires is 3
	if number == "3":
		for i in range(3):
			wirelistadd = input("Wire " + str(i + 1) + "? (w/y/blu/bla/r): ")
			if wirelistadd == "w":
				pass
			elif wirelistadd == "y":
				pass
			elif wirelistadd == "blu":
				pass
			elif wirelistadd == "bla":
				pass
			elif wirelistadd == "r":
				pass
			else:
				print(
				    "Error. You didn't do the right thing. Please rerun module"
				)
				return
			wirelist.append(wirelistadd)
		print("Your wires are " + str(wirelist))

		if "r" not in wirelist:
			print("Cut the Second Wire")
			return
		elif wirelist[-1] == "w":
			print("Cut the Last Wire")
			return
		elif wirelist.count("blu") > 2:
			print("Cut last BLUE wire")
			return
		else:
			print("Cut last wire")
			return

	#if number of wires is 4
	if number == "4":
		for i in range(4):
			wirelistadd = input("Wire " + str(i + 1) + "? (w/y/blu/bla/r): ")
			if wirelistadd == "w":
				pass
			elif wirelistadd == "y":
				pass
			elif wirelistadd == "blu":
				pass
			elif wirelistadd == "bla":
				pass
			elif wirelistadd == "r":
				pass
			else:
				print(
				    "Error. You didn't do the right thing. Please rerun module"
				)
				return
			wirelist.append(wirelistadd)
		print("Your wires are " + str(wirelist))

		if wirelist.count("r") > 1:
			serial = int(input("Last Digit of Serial: "))
		if ((wirelist.count("r") > 1) and (serial % 2)):
			print("Cut the last RED wire")
			return
		elif ((wirelist[-1] == "y") and (wirelist.count("r") == 0)):
			print("Cut the First Wire")
			return
		elif wirelist.count("blu") == 1:
			print("Cut the First Wire")
			return
		else:
			print("Cut the Second Wire")
			return

	#if number of wires is 5
	if number == "5":
		for i in range(5):
			wirelistadd = input("Wire " + str(i + 1) + "? (w/y/blu/bla/r): ")
			if wirelistadd == "w":
				pass
			elif wirelistadd == "y":
				pass
			elif wirelistadd == "blu":
				pass
			elif wirelistadd == "bla":
				pass
			elif wirelistadd == "r":
				pass
			else:
				print(
				    "Error. You didn't do the right thing. Please rerun module"
				)
				return
			wirelist.append(wirelistadd)
		print("Your wires are " + str(wirelist))

		if wirelist[-1] == "bla":
			serial = int(input("Last Digit of Serial: "))
		if ((wirelist[-1] == "bla") and (serial % 2)):
			print("Cut the Fourth Wire")
			return
		elif ((wirelist.count("r") == 1) and (wirelist.count("y") > 1)):
			print("Cut the First Wire")
			return
		elif wirelist.count("bla") == 0:
			print("Cut the Second Wire")
			return
		else:
			print("Cut the First Wire")
			return

	#if number of wires is 6
	if number == "6":
		for i in range(6):
			wirelistadd = input("Wire " + str(i + 1) + "? (w/y/blu/bla/r): ")
			if wirelistadd == "w":
				pass
			elif wirelistadd == "y":
				pass
			elif wirelistadd == "blu":
				pass
			elif wirelistadd == "bla":
				pass
			elif wirelistadd == "r":
				pass
			else:
				print(
				    "Error. You didn't do the right thing. Please rerun module"
				)
				return
			wirelist.append(wirelistadd)
		print("Your wires are " + str(wirelist))

		if wirelist.count("y") == 0:
			serial = int(input("Last Digit of Serial: "))
		if ((wirelist.count("y") == 0) and (serial % 2)):
			print("Cut the Third Wire")
			return
		elif ((wirelist.count("y") == 1) and (wirelist.count("w") > 1)):
			print("Cut the Fourth Wire")
			return
		elif wirelist.count("r") == 0:
			print("Cut the Last Wire")
			return
		else:
			print("Cut the Fourth Wire")
			return

	#else
	return

#Button (lots of input -> output)
def button():
	def hold():
		print("Hold down the button")
		time.sleep(1)
		strip = input("Color of strip? (blu/w/y/other): ")
		if strip == "blu":
			print("Hold until countdown has 4")
		elif strip == "w":
			print("Hold until countdown has 1")
		elif strip == "y":
			print("Hold until countdown has 5")
		elif strip == "other":
			print("Hold until countdown has 1")
		else:
			print("You did something wrong at somepoint")

	#variables
	color = input("Color? (blu/w/y/r/NOtA): ")
	text = input("Text? (abort/detonate/hold/NOtA): ")
	batteries = int(input("Batteries? (1/2/3/4/more): "))
	indicator = input("Indicator? (CAR/FRK/other): ")

	if ((color == "blu") and (text == "abort")):
		hold()
		return
	elif ((batteries > 1) and (text == "detonate")):
		print("Press and release")
		return
	elif ((color == "w") and (indicator == "CAR")):
		hold()
		return
	elif ((batteries > 2) and (indicator == "FRK")):
		print("Press and release")
		return
	elif color == "y":
		hold()
		return
	elif ((color == "r") and (text == "hold")):
		print("Press and release")
		return
	else:
		hold()
		return

#Keypad (specific inputx4 -> output)
def keypad():
	#list defines
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

	#settings the userKeys list
	global userKeys
	userKeys = []
	print(keys)

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

	#checking collums
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

	#printing the final answer
	finalList = [x for x in answerKeys if x in userKeys]
	print(" ")
	print("Final: " + str(finalList))

#Old Simon Says (I dont rememeber)
def simonOld():
	#original simon module, robust, but bulky
	vowel = input("Vowel in Serial/ (y/n): ")
	isDoing = True
	while isDoing == True:
		if vowel == "y":
			strikes = input("Number Of Strikes? (0/1/2): ")
			while strikes == "0":
				#run table 1 row 1
				print(" ")
				user = input("What ya' got? (r/blu/g/y/strike/done)")
				if user == "r":
					print("Press Blue")
				elif user == "blu":
					print("Press Red")
				elif user == "g":
					print("Press Yellow")
				elif user == "y":
					print("Press Green")
				elif user == "strike":
					print("You now have one strike")
					strikes = "1"
				elif user == "done":
					print("Awesome!")
					return
				else:
					print("Error. You did something wrong")
					return

			while strikes == "1":
				user = input("What ya' got? (r/blu/g/y/strike/done)")
				if user == "r":
					print("Press Yellow")
				elif user == "blu":
					print("Press Green")
				elif user == "g":
					print("Press Blue")
				elif user == "y":
					print("Press Red")
				elif user == "strike":
					print("You now have two strikes")
					strikes = "2"
				elif user == "done":
					print("Awesome!")
					return
				else:
					print("Error. You did something wrong")
					return

			while strikes == "2":
				user = input("What ya' got? (r/blu/g/y/strike/done)")
				if user == "r":
					print("Press Green")
				elif user == "blu":
					print("Press Red")
				elif user == "g":
					print("Press Yellow")
				elif user == "y":
					print("Press Blue")
				elif user == "strike":
					print("Game Over")
					return
				elif user == "done":
					print("Awesome!")
					return
				else:
					print("Error. You did something wrong")
					return
		elif vowel == "n":
			strikes = input("Number Of Strikes? (0/1/2): ")
			while strikes == "0":
				print(" ")
				user = input("What ya' got? (r/blu/g/y/strike/done)")
				if user == "r":
					print("Press Blue")
				elif user == "blu":
					print("Press Yellow")
				elif user == "g":
					print("Press Green")
				elif user == "y":
					print("Press Red")
				elif user == "strike":
					print("You now have one strike")
					strikes = "1"
				elif user == "done":
					print("Awesome!")
					return
				else:
					print("Error. You did something wrong")
					return

			while strikes == "1":
				user = input("What ya' got? (r/blu/g/y/strike/done)")
				if user == "r":
					print("Press Red")
				elif user == "blu":
					print("Press Blue")
				elif user == "g":
					print("Press Yellow")
				elif user == "y":
					print("Press Green")
				elif user == "strike":
					print("You now have two strikes")
					strikes = "2"
				elif user == "done":
					print("Awesome!")
					return
				else:
					print("Error. You did something wrong")
					return

			while strikes == "2":
				user = input("What ya' got? (r/blu/g/y/strike/done)")
				if user == "r":
					print("Press Yellow")
				elif user == "blu":
					print("Press Green")
				elif user == "g":
					print("Press Blue")
				elif user == "y":
					print("Press Red")
				elif user == "strike":
					print("Game Over")
					return
				elif user == "done":
					print("Awesome!")
					return
				else:
					print("Error. You did something wrong")
					return
		else:
			print("Error. You did something wrong")
			return

#New Simon Says (inputx? -> output x#)
def simon():
	#simonSimple is the streamlined but DEFINITELY more complicated version...hence the name
	global userInputing
	global finalSimon
	vowel = input("Vowel in Serial? (y/n): ")
	isDoing = True
	while isDoing == True:
		if vowel == "y":
			strikes = input("Number Of Strikes? (0/1/2): ")
			while strikes == "0":
				user = []
				finalSimon = []
				flash = 1
				while True:
					userInput = input("What is flash " + str(flash) +
					                  "? (r/blu/g/y/end/done):")
					if userInput == "r":
						user.append("r")
						flash += 1
					elif userInput == "blu":
						user.append("blu")
						flash += 1
					elif userInput == "g":
						user.append("g")
						flash += 1
					elif userInput == "y":
						user.append("y")
						flash += 1
					elif userInput == "done":
						isDoing = False
						return

					if userInput == "end":
						print("Currently flashing: " + str(user))
						break
				
				for i in user:
					if i == "r":
						finalSimon.append("blu")
					elif i == "blu":
						finalSimon.append("r")
					elif i == "g":
						finalSimon.append("y")
					elif i == "y":
						finalSimon.append("g")
					elif i == "end":
						pass
					else:
						print("How?")
						return
				print("Input: " + str(finalSimon))
				print(" ")

			while strikes == "1":
				user = []
				finalSimon = []
				flash = 1
				while True:
					userInput = input("What is flash " + str(flash) +
					                  "? (r/blu/g/y/end/done):")
					if userInput == "r":
						user.append("r")
						flash += 1
					elif userInput == "blu":
						user.append("blu")
						flash += 1
					elif userInput == "g":
						user.append("g")
						flash += 1
					elif userInput == "y":
						user.append("y")
						flash += 1
					elif userInput == "done":
						isDoing = False
						return

					if userInput == "end":
						print("Currently flashing: " + str(user))
						break
				
				for i in user:
					if i == "r":
						finalSimon.append("y")
					elif i == "blu":
						finalSimon.append("g")
					elif i == "g":
						finalSimon.append("blu")
					elif i == "y":
						finalSimon.append("r")
					elif i == "end":
						pass
					else:
						print("How?")
						return
				print("Input: " + str(finalSimon))
				print(" ")

			while strikes == "2":
				user = []
				finalSimon = []
				flash = 1
				while True:
					userInput = input("What is flash " + str(flash) +
					                  "? (r/blu/g/y/end/done):")
					if userInput == "r":
						user.append("r")
						flash += 1
					elif userInput == "blu":
						user.append("blu")
						flash += 1
					elif userInput == "g":
						user.append("g")
						flash += 1
					elif userInput == "y":
						user.append("y")
						flash += 1
					elif userInput == "done":
						isDoing = False
						return

					if userInput == "end":
						print("Currently flashing: " + str(user))
						break
				
				for i in user:
					if i == "r":
						finalSimon.append("g")
					elif i == "blu":
						finalSimon.append("r")
					elif i == "g":
						finalSimon.append("y")
					elif i == "y":
						finalSimon.append("blu")
					elif i == "end":
						pass
					else:
						print("How?")
						return
				print("Input: " + str(finalSimon))
				print(" ")

		elif vowel == "n":
			strikes = input("Number Of Strikes? (0/1/2): ")
			while strikes == "0":
				user = []
				finalSimon = []
				flash = 1
				while True:
					userInput = input("What is flash " + str(flash) +
					                  "? (r/blu/g/y/end/done):")
					if userInput == "r":
						user.append("r")
						flash += 1
					elif userInput == "blu":
						user.append("blu")
						flash += 1
					elif userInput == "g":
						user.append("g")
						flash += 1
					elif userInput == "y":
						user.append("y")
						flash += 1
					elif userInput == "done":
						isDoing = False
						return

					if userInput == "end":
						print("Currently flashing: " + str(user))
						break
				
				for i in user:
					if i == "r":
						finalSimon.append("blu")
					elif i == "blu":
						finalSimon.append("y")
					elif i == "g":
						finalSimon.append("g")
					elif i == "y":
						finalSimon.append("r")
					elif i == "end":
						pass
					else:
						print("How?")
						return
				print("Input: " + str(finalSimon))
				print(" ")

			while strikes == "1":
				user = []
				finalSimon = []
				flash = 1
				while True:
					userInput = input("What is flash " + str(flash) +
					                  "? (r/blu/g/y/end/done):")
					if userInput == "r":
						user.append("r")
						flash += 1
					elif userInput == "blu":
						user.append("blu")
						flash += 1
					elif userInput == "g":
						user.append("g")
						flash += 1
					elif userInput == "y":
						user.append("y")
						flash += 1
					elif userInput == "done":
						isDoing = False
						return

					if userInput == "end":
						print("Currently flashing: " + str(user))
						break
				
				for i in user:
					if i == "r":
						finalSimon.append("r")
					elif i == "blu":
						finalSimon.append("blu")
					elif i == "g":
						finalSimon.append("y")
					elif i == "y":
						finalSimon.append("g")
					elif i == "end":
						pass
					else:
						print("How?")
						return
				print("Input: " + str(finalSimon))
				print(" ")

			while strikes == "2":
				user = []
				finalSimon = []
				flash = 1
				while True:
					userInput = input("What is flash " + str(flash) +
					                  "? (r/blu/g/y/end/done):")
					if userInput == "r":
						user.append("r")
						flash += 1
					elif userInput == "blu":
						user.append("blu")
						flash += 1
					elif userInput == "g":
						user.append("g")
						flash += 1
					elif userInput == "y":
						user.append("y")
						flash += 1
					elif userInput == "done":
						isDoing = False
						return

					if userInput == "end":
						print("Currently flashing: " + str(user))
						break
				
				for i in user:
					if i == "r":
						finalSimon.append("y")
					elif i == "blu":
						finalSimon.append("g")
					elif i == "g":
						finalSimon.append("blu")
					elif i == "y":
						finalSimon.append("r")
					elif i == "end":
						pass
					else:
						print("How?")
						return
				print("Input: " + str(finalSimon))
				print(" ")

		else:
			print("Error. You input incorrectly. Please try again")
			return

#Whos on First (input -> output, input -> outputx?)
def whofirst():
	whoWorking = True
	while whoWorking:
		#variables
		step1 = "EMPTY"
		spot = "EMPTY"
		step1Work = True
	
		#Step 1
		while step1Work:
			while spot == "EMPTY":
				step1 = input("STEP 1 - What does the display read? (lowercase): ")
				if step1 == "ur":
					spot = "TopLeft"
				elif step1 in ("yes", "nothing", "led", "they are"):
					spot = "MidLeft"
				elif step1 in ("they're", "reed", "leed", "*blank*"):
					spot = "BottLeft"
				elif step1 in ("first", "okay", "c"):
					spot = "TopRight"
				elif step1 in ("blank", "read", "red", "you", "your", "you're", "their"):
					spot = "MidRight"
				elif step1 in ("display", "says", "no", "lead", "hold on", "you are", "there", "see", "cee"):
					spot = "BottRight"
				step1Work = False
				if spot == "EMPTY":
					print("Please input a valid Display Word")
					step1Work = True

		#Step 2
		step2 = "EMPTY"
		readList = "EMPTY"
		answer = "EMPTY"
	
		while readList == "EMPTY":
			step2 = input("STEP 2 - What word is in the " + str(spot) + " position? (DO NOT CLICK IT YET, Lowercase): ")
			if step2 == "ready":
				readList = ready
			elif step2 == "first":
				readList = first
			elif step2 == "no":
				readList = no
			elif step2 == "blank":
				readList = blank
			elif step2 == "nothing":
				readList = nothing
			elif step2 == "yes":
				readList = yes
			elif step2 == "what":
				readList = what
			elif step2 == "uhhh":
				readList = uhhh
			elif step2 == "left":
				readList = left
			elif step2 == "right":
				readList = right
			elif step2 == "middle":
				readList = middle
			elif step2 == "okay":
				readList = okay
			elif step2 == "wait":
				readList = wait
			elif step2 == "press":
				readList = press
			elif step2 == "you":
				readList = you
			elif step2 == "you are":
				readList = youare
			elif step2 == "your":
				readList = your
			elif step2 == "you're":
				readList = youre
			elif step2 == "ur":
				readList = ur
			elif step2 == "u":
				readList = u
			elif step2 == "uh huh":
				readList = uhhuh
			elif step2 == "uh uh":
				readList = uhuh
			elif step2 == "what?":
				readList = whatq
			elif step2 == "done":
				readList = done
			elif step2 == "next":
				readList = next
			elif step2 == "hold":
				readList = hold
			elif step2 == "sure":
				readList = sure
			elif step2 == "like":
				readList = like
			else:
				print("That is not a valid word.")


		for i in readList:
			advance = "EMPTY"
			done2 = False
			advance = input("Is the word " + str(i) + " there? (y/n): ")
			if advance == "n":
				pass
			elif advance == "y":
				print("Click the word " + str(i))
				done2 = True
				break
		if done2 == False:
			print("How did you mess this up")
			print("Just press the word " + str(readList[-1]) + " dummy.")
			time.sleep(1)

		if input("Are there more steps? (y/n): ") == "n":
			whoWorking = False
		else:
			pass
		
#Memory (input -> output x5) (This is as simple as I want in terms of input and output)
def memory():
	#variables
	stage1un = "EMPTY"
	stage1 = "EMPTY"
	stage2un = "EMPTY"
	stage2 = "EMPTY"
	stage3un = "EMPTY"
	stage3 = "EMPTY"
	stage4un = "EMPTY"
	stage4 = "EMPTY"
	stage5un = "EMPTY"
	stage5 = "EMPTY"
	positions = []
	numbers = []
	print("Input the numbers starting with Display, and then left to right, seperated by spaces")
	#Stage 1 - Settings Lists
	stage1un = input("Stage1 - What are the numbers given?: ")
	stage1 = stage1un.split()
	for i in range(len(stage1)):
		stage1[i] = int(stage1[i])
		if stage1[i] in (1, 2, 3, 4):
			pass
		else:
			print("Error. You inputed wrong numbers, please press a button to restart the module in KTANE")
			return
	print("Inputed numbers: " + str(stage1))

	#Stage 1 - Programming
	if stage1[0] == 1:
		print("Press the button labeled  " + str(stage1[2]))
		positions.append(2)
		numbers.append(stage1[2])
	elif stage1[0] == 2:
		print("Press the button labeled  " + str(stage1[2]))
		positions.append(2)
		numbers.append(stage1[2])
	elif stage1[0] == 3:
		print("Press the button labeled  " + str(stage1[3]))
		positions.append(3)
		numbers.append(stage1[3])
	elif stage1[0] == 4:
		print("Press the button labeled  " + str(stage1[4]))
		positions.append(4)
		numbers.append(stage1[4])
	print("Num: " + str(numbers))
	print("Pos: " + str(positions))
	print(" ")
		

	#Stage2 - Settings Lists
	stage2un = input("Stage2 - What are the numbers given?: ")
	stage2 = stage2un.split()
	for i in range(len(stage2)):
		stage2[i] = int(stage2[i])
		if stage2[i] in (1, 2, 3, 4):
			pass
		else:
			print("Error. You inputed wrong numbers, please press a button to restart the module in KTANE")
			return
	print("Inputed numbers: " + str(stage2))

	#Stage2 - Programming
	if stage2[0] == 1:
		print("Press the button labeled  4")
		index = stage2.index(4, 1, 5)
		positions.append(index)
		numbers.append(4)
	elif stage2[0] == 2:
		print("Press the button labeled " + str(stage2[positions[0]]))
		positions.append(positions[0])
		numbers.append(stage2[positions[0]])
	elif stage2[0] == 3:
		print("Press the button labeled " + str(stage2[1]))
		positions.append(1)
		numbers.append(stage2[1])
	elif stage2[0] == 4:
		print("Press the button labeled " + str(stage2[positions[0]]))
		positions.append(positions[0])
		numbers.append(stage2[positions[0]])
	print("Num: " + str(numbers))
	print("Pos: " + str(positions))
	print(" ")


	#Stage 3 - Settings Lists
	stage3un = input("Stage3 - What are the numbers given?: ")
	stage3 = stage3un.split()
	for i in range(len(stage3)):
		stage3[i] = int(stage3[i])
		if stage3[i] in (1, 2, 3, 4):
			pass
		else:
			print("Error. You inputed wrong numbers, please press a button to restart the module in KTANE")
			return
	print("Inputed numbers: " + str(stage3))

	#Stage 3 - Programming
	if stage3[0] == 1:
		print("Press the button labeled  " + str(numbers[1]))
		index = stage3.index(numbers[1])
		positions.append(index)
		numbers.append(numbers[1])
	elif stage3[0] == 2:
		print("Press the button labeled  " + str(numbers[0]))
		index = stage3.index(numbers[0])
		positions.append(index)
		numbers.append(numbers[0])
	elif stage3[0] == 3:
		print("Press the button labeled  " + str(stage3[3]))
		positions.append(3)
		numbers.append(stage3[3])
	elif stage3[0] == 4:
		print("Press the button labeled  4")
		index = stage3.index(4, 1, 5)
		positions.append(index)
		numbers.append(4)
	print("Num: " + str(numbers))
	print("Pos: " + str(positions))
	print(" ")


	#Stage 4 - Settings Lists
	stage4un = input("Stage4 - What are the numbers given?: ")
	stage4 = stage4un.split()
	for i in range(len(stage4)):
		stage4[i] = int(stage4[i])
		if stage4[i] in (1, 2, 3, 4):
			pass
		else:
			print("Error. You inputed wrong numbers, please press a button to restart the module in KTANE")
			return
	print("Inputed numbers: " + str(stage4))

	#Stage 4 - Programming
	if stage4[0] == 1:
		print("Press the button labeled " + str(stage4[positions[0]]))
		positions.append(positions[0])
		numbers.append(stage4[positions[0]])
	elif stage4[0] == 2:
		print("Press the button labeled " + str(stage4[1]))
		positions.append(1)
		numbers.append(stage4[1])
	elif stage4[0] == 3:
		print("Press the button labeled " + str(stage4[positions[1]]))
		positions.append(positions[1])
		numbers.append(stage4[positions[1]])
	elif stage4[0] == 4:
		print("Press the button labeled " + str(stage4[positions[1]]))
		positions.append(positions[1])
		numbers.append(stage4[positions[1]])
	print("Num: " + str(numbers))
	print("Pos: " + str(positions))
	print(" ")


	#Stage 5 - Settings Lists
	stage5un = input("Stage5 - What are the numbers given?: ")
	stage5 = stage5un.split()
	for i in range(len(stage5)):
		stage5[i] = int(stage5[i])
		if stage5[i] in (1, 2, 3, 4):
			pass
		else:
			print("Error. You inputed wrong numbers, please press a button to restart the module in KTANE")
			return
	print("Inputed numbers: " + str(stage5))

	#Stage 5 - Programming
	if stage5[0] == 1:
		print("Press the button labeled  " + str(numbers[0]))
		index = stage5.index(numbers[0])
		positions.append(index)
		numbers.append(numbers[0])
	elif stage5[0] == 2:
		print("Press the button labeled  " + str(numbers[1]))
		index = stage5.index(numbers[1])
		positions.append(index)
		numbers.append(numbers[1])
	elif stage5[0] == 3:
		print("Press the button labeled  " + str(numbers[3]))
		index = stage5.index(numbers[3])
		positions.append(index)
		numbers.append(numbers[3])
	elif stage5[0] == 4:
		print("Press the button labeled  " + str(numbers[2]))
		index = stage5.index(numbers[2])
		positions.append(index)
		numbers.append(numbers[2])
	print("Num: " + str(numbers))
	print("Pos: " + str(positions))
	print(" ")

#Morse Code
def morse():
	userMorseUnsplit = input("What is your Morse Code (see README.md for instructions)?: ")
	userMorse = userMorseUnsplit.split()
	print("Inputed Morse: " + str(userMorse))
	alphaList = []
	for i in userMorse:
		alphaElement = morseToAlpha(i)
		alphaList.append(alphaElement)
	print("Alpha List: " + str(alphaList))

	if all(elem in shell for elem in alphaList):
		print("Word was: Shell")
		print("Input 3.505 MHz")
		return
	elif all(elem in halls for elem in alphaList):
		print("Word was: Halls")
		print("Input 3.515 MHz")
		return
	elif all(elem in slick for elem in alphaList):
		print("Word was: Slick")
		print("Input 3.522 MHz")
		return	
	elif all(elem in trick for elem in alphaList):
		print("Word was: Trick")
		print("Input 3.532 MHz")
		return
	elif all(elem in boxes for elem in alphaList):
		print("Word was: Boxes")
		print("Input 3.535 MHz")
		return
	elif all(elem in leaks for elem in alphaList):
		print("Word was: Leaks")
		print("Input 3.542 MHz")
		return
	elif all(elem in strobe for elem in alphaList):
		print("Word was: Strobe")
		print("Input 3.545 MHz")
		return
	elif all(elem in bistro for elem in alphaList):
		print("Word was: Bistro")
		print("Input 3.552 MHz")
		return
	elif all(elem in flick for elem in alphaList):
		print("Word was: Flick")
		print("Input 3.555 MHz")
		return
	elif all(elem in bombs for elem in alphaList):
		print("Word was: Bombs")
		print("Input 3.565 MHz")
		return
	elif all(elem in bbreak for elem in alphaList):
		print("Word was: Break")
		print("Input 3.572 MHz")
		return
	elif all(elem in brick for elem in alphaList):
		print("Word was: Brick")
		print("Input 3.575 MHz")
		return
	elif all(elem in steak for elem in alphaList):
		print("Word was: Steak")
		print("Input 3.582 MHz")
		return
	elif all(elem in sting for elem in alphaList):
		print("Word was: Sting")
		print("Input 3.592 MHz")
		return
	elif all(elem in vector for elem in alphaList):
		print("Word was: Vector")
		print("Input 3.595 MHz")
		return
	elif all(elem in beats for elem in alphaList):
		print("Word was: Beats")
		print("Input 3.600 MHz")
		return
	else:
		print("You did something wrong. Try again.")
		return



#PROGRAM
#Intro
if skip == "y":
	print("Gotch ya")
else:
	print("Welcome to Keep Talking and Nobody Explodes")
	time.sleep(1)
	print(
	    "Currently, the only modules supported are Wires, Button, Keypad, Simon Says, Who's on First, and Memory")
	time.sleep(2)
	print("NOtA = None of the Above")
	time.sleep(1)
	print(
	    "blu is Blue, and bla is Black. Every other color is just the first letter"
	)
	time.sleep(3)

#Module Loop
while isDoing == True:
	#checking which module you are currently working on
	print(" ")
	module = input("Module? (w/b/k/s/who/m/mO): ")
	if module == "w":
		wires()
	elif module == "b":
		button()
	elif module == "k":
		keypad()
	elif module == "s":
		simon()
	elif module == "who":
		whofirst()
	elif module == "m":
		memory()
	elif module == "mO":
		morse()
	elif module == "stop":
		print("Bomb Complete. Congrats Defuser")
		isDoing = False
	else:
		print("Please enter a valid module")
		isDoing = True
