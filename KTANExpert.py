# Keep Talking and Nobody Explodes Manual "Expert"
# Created By Reese Ford 07/13/2021
# https://www.github.com/RicePerson/KTANExpert


#Imports
import time
import math

#Def Vars
isDoing = True
explode = False
module = "EMPTY"

serialNum = "EMPTY"
batteries = "EMPTY"
litIndicators = ["EMPTY"]
parallelPort = "EMPTY"


# Module Declarations

#Wires (inputx7(8) -> output)
def wires():
	#Def Vars
	global serialNum
	number = input("Number of Wires? (3/4/5/6): ")
	wirelist = []

	#Logic - 3 Wires
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
				    "Error. You didn't do the right thing. Please rerun module")
				return
			wirelist.append(wirelistadd)
		print("Your wires are " + str(wirelist))
		print(" ")

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

	#Logic - 4 Wires
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
		print(" ")

		if wirelist.count("r") > 1:
			if serialNum == "EMPTY":
				serialNum = int(input("Last Digit of Serial: "))
			if ((wirelist.count("r") > 1) and (serialNum % 2)):
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

	#Logic - 5 Wires
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
		print(" ")

		if wirelist[-1] == "bla":
			if serialNum == "EMPTY":
				serialNum = int(input("Last Digit of Serial: "))
			if ((wirelist[-1] == "bla") and (serialNum % 2)):
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

	#Logic - 6 Wires
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
		print(" ")

		if wirelist.count("y") == 0:
			if serialNum == "EMPTY":
				serialNum = int(input("Last Digit of Serial: "))
			if ((wirelist.count("y") == 0) and (serialNum % 2)):
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

	#If Not: 
	return

#Button (inputs various -> output)
def button():
    # Vars
    color = "EMPTY"
    text = "EMPTY"
    instruction = "EMPTY"
    strip = "EMPTY"

    global batteries
    global litIndicators

    # Logic
    #Starting Information

    color = input("What is the color of the button? (blu, w, y, r, other): ")

    #Manual Step 1
    if color == "b":
        if text == "EMPTY":
            text = input("What does the button say? (all lowercase): ")
        if text == "abort":
            instruction = "hold"

    #Manual Step 2
    if batteries == "EMPTY":
        batteries = int(input("How many batteries are on the bomb?: "))
    if batteries > 1:
        if text == "EMPTY":
            text = input("What does the button say? (all lowercase): ")
        if text == "detonate":
            instruction = "pressRelease"

    #Manual Step 3
    if color == "w":
        if litIndicators == ["EMPTY"]:
            litIndicators = input("Please list all the lit indicators (all uppcase with a single space between each one): ").split()
        if "CAR" in litIndicators:
            instruction = "hold"

    #Manual Step 4
    if batteries == "EMPTY":
        batteries = int(input("How many batteries are on the bomb?: "))
    if batteries > 2:
        if litIndicators == ["EMPTY"]:
            litIndicators = input("Please list all the lit indicators (all uppcase with a single space between each one): ").split()
        if "FRK" in litIndicators:
            instruction = "pressRelease"

    #Manual Step 5
    if color == "y":
        instruction = "hold"

    #Manual Step 6
    if color == "r":
        if text == "EMPTY":
            text = input("What does the button say? (all lowercase): ")
        if text == "hold":
            instruction = "pressRelease"

    #Manual Step 7
    else:
        instruction = "hold"

    #Releasing a held button
    if instruction == "hold":
        print(" ")
        strip = input("Press and hold the button. While holding, input the color of the strip immediately to the right of the button (blu, w, y, other): ")
        if strip == "blu":
            print(" ")
            print("Release the button when the countdown timer has a 4 in any position")
            return
        elif strip == "w":
            print(" ")
            print("Release the button when the countdown timer has a 1 in any position")
            return
        elif strip == "y":
            print(" ")
            print("Release the button when the countdown timer has a 5 in any position")
            return
        else:
            print(" ")
            print("Release the button when the countdown timer has a 1 in any position")
    elif instruction == "pressRelease":
        print(" ")
        print("Press and immediately release the button")
        return
    else:
        return

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
	userKeys = []
	for i in keys:
		print(i)

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
	answerColumn = []
	if all(elem in c1 for elem in userKeys):
		answerColumn = c1
		#print("Column: " + str(answerKeys))
	elif all(elem in c2 for elem in userKeys):
		answerColumn = c2
		#print("Column: " + str(answerKeys))
	elif all(elem in c3 for elem in userKeys):
		answerColumn = c3
		#print("Column: " + str(answerKeys))
	elif all(elem in c4 for elem in userKeys):
		answerColumn = c4
		#print("Column: " + str(answerKeys))
	elif all(elem in c5 for elem in userKeys):
		answerColumn = c5
		#print("Column: " + str(answerKeys))
	elif all(elem in c6 for elem in userKeys):
		answerColumn = c6
		#print("Column: " + str(answerKeys))
	else:
		print("No collum has all of the inputed keys")

	#Final print()
	finalList = [x for x in answerColumn if x in userKeys]
	print(" ")
	print("Click these buttons in order: ")
	for i in range(4):
		print(str(i+1)+") " + str(finalList[i]))

#New Simon Says (inputxIndefinite -> output x#)
def simon():
	#simon() is the streamlined but DEFINITELY more complicated version...hence the name
	#Logic (It's a loop)
	vowel = input("Vowel in Serial? (y/n): ")
	isDoing = True

	while isDoing == True:
		if vowel == "y":
			strikes = input("Number Of Strikes? (0/1/2): ")
			while strikes == "0":
				user = []
				finalSimon = []
				flash = 1
				print(" ")
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
				print(" ")
				print("Input: " + str(finalSimon))
				print(" ")

			while strikes == "1":
				user = []
				finalSimon = []
				flash = 1
				print(" ")
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
				print(" ")
				print("Input: " + str(finalSimon))
				print(" ")

			while strikes == "2":
				user = []
				finalSimon = []
				flash = 1
				print(" ")
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
				print(" ")
				print("Input: " + str(finalSimon))
				print(" ")

		elif vowel == "n":
			strikes = input("Number Of Strikes? (0/1/2): ")
			while strikes == "0":
				user = []
				finalSimon = []
				flash = 1
				print(" ")
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
				print(" ")
				print("Input: " + str(finalSimon))
				print(" ")

			while strikes == "1":
				user = []
				finalSimon = []
				flash = 1
				print(" ")
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
				print(" ")
				print("Input: " + str(finalSimon))
				print(" ")

			while strikes == "2":
				user = []
				finalSimon = []
				flash = 1
				print(" ")
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
				print(" ")
				print("Input: " + str(finalSimon))
				print(" ")

		else:
			print("Error. You input incorrectly. Please try again")
			return

#Whos on First (input -> output, input -> outputx?)
def whofirst():
	#Lists of STEP 2 Words
	#Copy this to make it easier: ", ". So basically WORD CtrlV WORD CtrlV WORD and so on and so forth

	ready = ["yes", "okay", "what", "middle", "left", "press", "right", "blank", "ready"]
	first = ["left", "okay", "yes", "middle", "no", "right", "nothing", "uhhh", "wait", "ready", "blank", "what", "press", "first"]
	no = ["blank", "uhhh", "wait", "first", "what", "ready", "right", "yes", "nothing", "left", "press", "okay", "no"]
	blank = ["wait", "right", "okay", "middle", "blank"]
	nothing = ["uhhh", "right", "okay", "middle", "yes", "blank", "no", "press", "left", "what", "wait", "first", "nothing"]
	yes = ["okay", "right", "uhhh", "middle", "first", "what", "press", "ready", "nothing", "yes"]
	what = ["uhhh", "what"]
	uhhh = ["ready", "nothing", "left", "what", "okay", "yes", "right", "no", "press", "blank", "uhhh"]
	left = ["right", "left"]
	right = ["yes", "nothing", "ready", "press", "no", "wait", "what", "right"]
	middle = ["blank", "ready", "okay", "what", "nothing", "press", "no", "wait", "left", "middle"]
	okay = ["middle", "no", "first", "yes", "uhhh", "nothing", "wait", "okay"]
	wait = ["uhhh", "no", "blank", "okay", "yes", "left", "first", "press", "what", "wait"]
	press = ["right", "middle", "yes", "ready", "press"]
	you = ["sure", "you are", "your", "you're", "next", "uh huh", "ur", "hold", "what?", "you"]
	youare = ["your", "next", "like", "uh huh", "what?", "done", "uh uh", "hold", "you", "u", "you're", "sure", "ur", "you are"]
	your = ["uh uh", "you are", "uh huh", "your"]
	youre = ["you", "you're"]
	ur = ["done", "u", "ur"]
	u = ["uh huh", "sure", "next", "what?", "you're", "ur", "uh uh", "done", "u"]
	uhhuh = "uh huh"
	uhuh = ["ur", "u", "you are", "you're", "next", "uh uh"]
	whatq = ["you", "hold", "you're", "your", "u", "done", "uh uh", "like", "you are", "uh huh", "ur", "next", "what?"]
	done = ["sure", "uh huh", "next", "what?", "your", "ur", "you're", "hold", "like", "you", "u", "you are", "uh uh", "done"]
	next = ["what?", "uh huh", "uh uh", "your", "hold", "sure", "next"]
	hold = ["you are", "u", "done", "uh uh", "you", "ur", "sure", "what?", "you're", "next", "hold"]
	sure = ["you are", "done", "like", "you're", "you", "hold", "uh huh", "ur", "sure"]
	like = ["you're", "next", "u", "ur", "hold", "done", "uh uh", "what?", "uh huh", "you", "like"]

	whoWorking = True
	while whoWorking:
		#Def Vars: Step 1
		step1 = "EMPTY"
		spot = "EMPTY"
		step1Work = True
	
		#Logic: Step 1
		while step1Work:
			while spot == "EMPTY":
				step1 = input("STEP 1 - What does the display read? (lowercase) (If the display has nothing, input *blank*): ")
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

		#Def Vars: Step 2
		step2 = "EMPTY"
		readList = "EMPTY"
		answer = "EMPTY"
	
		#Logic: Step 2
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
				print(" ")
				print("Click the word " + str(i))
				print(" ")
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
	#Def Vars
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

	#Def Vars: Stage 1 - Settings Lists
	stage1un = input("Stage1 - What are the numbers given? (1,2,3,4,r): ")
	if stage2un == "r":
		print("Reset detected. Resetting expert...")
		return
	stage1 = stage1un.split()
	for i in range(len(stage1)):
		stage1[i] = int(stage1[i])
		if stage1[i] in (1, 2, 3, 4):
			pass
		else:
			print("Error. You inputed wrong numbers, please press a button to restart the module in KTANE")
			return
	print("Inputed Display: " + str(stage1[0]))
	print("Inputed Numbers: " + str(stage1[1:5]))

	#Logic: Stage 1
	print(" ")
	if stage1[0] == 1:
		print("Press the button labeled " + str(stage1[2]))
		positions.append(2)
		numbers.append(stage1[2])
	elif stage1[0] == 2:
		print("Press the button labeled " + str(stage1[2]))
		positions.append(2)
		numbers.append(stage1[2])
	elif stage1[0] == 3:
		print("Press the button labeled " + str(stage1[3]))
		positions.append(3)
		numbers.append(stage1[3])
	elif stage1[0] == 4:
		print("Press the button labeled " + str(stage1[4]))
		positions.append(4)
		numbers.append(stage1[4])
	print(" ")


	#Def Vars: Stage2 - Settings Lists
	stage2un = input("Stage2 - What are the numbers given? (1,2,3,4,r): ")
	if stage2un == "r":
		print("Reset detected. Resetting expert...")
		return
	stage2 = stage2un.split()
	for i in range(len(stage2)):
		stage2[i] = int(stage2[i])
		if stage2[i] in (1, 2, 3, 4):
			pass
		else:
			print("Error. You inputed wrong numbers, please press a button to restart the module in KTANE")
			return
	print("Inputed Display: " + str(stage2[0]))
	print("Inputed Numbers: " + str(stage2[1:5]))


	#Logic Stage2
	print(" ")
	if stage2[0] == 1:
		print("Press the button labeled 4")
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
	print(" ")


	#Def Vars: Stage 3 - Settings Lists
	stage3un = input("Stage3 - What are the numbers given? (1,2,3,4,r): ")
	if stage2un == "r":
		print("Reset detected. Resetting expert...")
		return
	stage3 = stage3un.split()
	for i in range(len(stage3)):
		stage3[i] = int(stage3[i])
		if stage3[i] in (1, 2, 3, 4):
			pass
		else:
			print("Error. You inputed wrong numbers, please press a button to restart the module in KTANE")
			return
	print("Inputed Display: " + str(stage3[0]))
	print("Inputed Numbers: " + str(stage3[1:5]))


	#Logic: Stage 3
	print(" ")
	if stage3[0] == 1:
		print("Press the button labeled " + str(numbers[1]))
		index = stage3.index(numbers[1])
		positions.append(index)
		numbers.append(numbers[1])
	elif stage3[0] == 2:
		print("Press the button labeled " + str(numbers[0]))
		index = stage3.index(numbers[0])
		positions.append(index)
		numbers.append(numbers[0])
	elif stage3[0] == 3:
		print("Press the button labeled " + str(stage3[3]))
		positions.append(3)
		numbers.append(stage3[3])
	elif stage3[0] == 4:
		print("Press the button labeled 4")
		index = stage3.index(4, 1, 5)
		positions.append(index)
		numbers.append(4)
	print(" ")


	#Def Vars: Stage 4 - Settings Lists
	stage4un = input("Stage4 - What are the numbers given? (1,2,3,4,r): ")
	if stage2un == "r":
		print("Reset detected. Resetting expert...")
		return
	stage4 = stage4un.split()
	for i in range(len(stage4)):
		stage4[i] = int(stage4[i])
		if stage4[i] in (1, 2, 3, 4):
			pass
		else:
			print("Error. You inputed wrong numbers, please press a button to restart the module in KTANE")
			return
	print("Inputed Display: " + str(stage4[0]))
	print("Inputed Numbers: " + str(stage4[1:5]))


	#Logic: Stage 4
	print(" ")
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
	print(" ")


	#Def Vars: Stage 5 - Settings Lists
	stage5un = input("Stage5 - What are the numbers given? (1,2,3,4,r): ")
	if stage2un == "r":
		print("Reset detected. Resetting expert...")
		return
	stage5 = stage5un.split()
	for i in range(len(stage5)):
		stage5[i] = int(stage5[i])
		if stage5[i] in (1, 2, 3, 4):
			pass
		else:
			print("Error. You inputed wrong numbers, please press a button to restart the module in KTANE")
			return
	print("Inputed Display: " + str(stage5[0]))
	print("Inputed Numbers: " + str(stage5[1:5]))


	#Logic: Stage 5
	print(" ")
	if stage5[0] == 1:
		print("Press the button labeled " + str(numbers[0]))
		index = stage5.index(numbers[0])
		positions.append(index)
		numbers.append(numbers[0])
	elif stage5[0] == 2:
		print("Press the button labeled " + str(numbers[1]))
		index = stage5.index(numbers[1])
		positions.append(index)
		numbers.append(numbers[1])
	elif stage5[0] == 3:
		print("Press the button labeled " + str(numbers[3]))
		index = stage5.index(numbers[3])
		positions.append(index)
		numbers.append(numbers[3])
	elif stage5[0] == 4:
		print("Press the button labeled " + str(numbers[2]))
		index = stage5.index(numbers[2])
		positions.append(index)
		numbers.append(numbers[2])
	print(" ")

#The Morse -> Letter
def morseToAlpha(input):
    if input == ".-":
        return "A"
    elif input == "-...":
        return "B"
    elif input == "-.-.":
        return "C"
    elif input == "-..":
        return "D"
    elif input == ".":
        return "E"
    elif input == "..-.":
        return "F"
    elif input == "--.":
        return "G"
    elif input == "....":
        return "H"
    elif input == "..":
        return "I"
    elif input == ".---":
        return "J"
    elif input == "-.-":
        return "K"
    elif input == ".-..":
        return "L"
    elif input == "--":
        return "M"
    elif input == "-.":
        return "N"
    elif input == "---":
        return "O"
    elif input == ".--.":
        return "P"
    elif input == "--.-":
        return "Q"
    elif input == ".-.":
        return "R"
    elif input == "...":
        return "S"
    elif input == "-":
        return "T"
    elif input == "..-":
        return "U"
    elif input == "...-":
        return "V"
    elif input == ".--":
        return "W"
    elif input == "-..-":
        return "X"
    elif input == "-.--":
        return "Y"
    elif input == "--..":
        return "Z"
    else:
        return

shell = ["S", "H", "E", "L", "L"]
halls = ["H", "A", "L", "L", "S"]
slick = ["S", "L", "I", "C", "K"]
trick = ["T", "R", "I", "C", "K"]
boxes = ["B", "O", "X", "E", "S"]
leaks = ["L", "E", "A", "K", "S"]
strobe = ["S", "T", "R", "O", "B", "E"]
bistro = ["B", "I", "S", "T", "R", "O"]
flick = ["F", "L", "I", "C", "K"]
bombs = ["B", "O", "M", "B", "S"]
bbreak = ["B", "R", "E", "A", "K"]
brick = ["B", "R", "I", "C", "K"]
steak = ["S", "T", "E", "A", "K"]
sting = ["S", "T", "I", "N", "G"]
vector = ["V", "E", "C", "T", "O", "R"]
beats = ["B", "E", "A", "T", "S"] 

#Morse Code Logic (input -> output)
def morse():
	#Def Vars
	userMorseUnsplit = input("What is your Morse Code (see README.md for instructions)?: ")
	userMorse = userMorseUnsplit.split()
	print("Inputed Morse: " + str(userMorse))
	alphaList = []
	for i in userMorse:
		alphaElement = morseToAlpha(i)
		alphaList.append(alphaElement)
	print("Alpha List: " + str(alphaList))

	#Logic
	print(" ")
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

#Complicated Wires (input x4 -> output, loop until complete)
def compWires():
	while True:
		#Def Vars
		colBlu = input("Does the wire have Blue coloring? (y/n): ")
		colRed = input("Does the wire have Red coloring? (y/n): ")
		wireLED = input("Is the LED on? (y/n): ")
		hasStar = input("Does the wire have a star symbol? (y/n): ")

		global serialNum
		global batteries
		global parallelPort

		if colBlu== "y":
			colBlu = True
		elif colBlu == "n":
			colBlu = False
		else:
			print("You did something wrong")
			return
			
		if colRed == "y":
			colRed = True
		elif colRed == "n":
			colRed = False
		else:
			print("You did something wrong")
			return

		if wireLED == "y":
			wireLED = True
		elif wireLED == "n":
			wireLED = False
		else:
			print("You did something wrong")
			return

		if hasStar == "y":
			hasStar = True
		elif hasStar == "n":
			hasStar = False
		else:
			print("You did something wrong")
			return

		print("Blue: " + str(colBlu))
		print("Red: " + str(colRed))
		print("Star: " + str(hasStar))
		print("LED: " + str(wireLED))

		#Input Logic
		instruction = "EMPTY"

		if colBlu:
			if colRed:
				if wireLED:
					if hasStar:
						instruction = "D"
					else:
						instruction = "S"
				else:
					if hasStar:
						instruction = "P"
					else:
						instruction = "S"
			else:
				if wireLED:
					instruction = "P"
				else:
					if hasStar:
						instruction = "D"
					else:
						instruction = "S"
		elif colRed:
			if wireLED:
				instruction = "B"
			else:
				if hasStar:
					instruction = "C"
				else:
					instruction = "S"
		elif wireLED:
			if hasStar:
				instruction = "B"
			else:
				instruction = "D"
		elif hasStar:
			instruction = "C"
		else:
			instruction = "C"
		print(" ")

		#Output Logic
		match (instruction):
			case ("D"): 
				print("Do not Cut this wire")
			case ("C"): 
				print("Cut this wire")
			case ("S"): 
				if serialNum == "EMPTY":
					serialNum = int(input("What is the last number of the bomb serial number?: "))
				if serialNum%2 == 0:
					print("Cut this wire")
				else:
					print("Do not cut this wire")
			case ("P"):
				if parallelPort == "EMPTY":
					if input("Does the bomb have a parallel port (y/n)?: ") == "y":
						parallelPort = True
					else:
						parallelPort = False
				if parallelPort == True:
					print("Cut this wire")
				else:
					print("Do not cut this wire")
			case ("B"):
				if batteries == "EMPTY":
					batteries = int(input("How many batteries are on the bomb?: "))
				if batteries >= 2:
					print("Cut this wire")
				else:
					print("Do not cut this wire")
			case other:
				print("Something messed up at somepoint. Please try that wire again")

		#Breaking Loop
		print(" ")
		done = input("Are there more wires to process? (y/n): ")
		if done == "n":
			return
		else:
			print(" ")
			pass

#Wire Sequences (inputx1 -> outputx1, loop 4 repeats)
def wireSeq():
	rOcc = 0
	bluOcc = 0
	blaOcc = 0
	for i in range(0,4):
		#Def Vars
		wiresList = []
		wires = []
		wireUn = input("What is the wire color and letter of each wire on panel " + str(i+1) + " from top to bottom? (r,blu,bla>A,B,C;)(if there is no wire in a slot, use blank) : ")

		if wireUn == "stop":
			return
		else:
			wiresList = wireUn.split(";")
		uCount = 0
		for u in wiresList: #Reformatting Blanks so that the Logic doesn't explode
			if u == "blank":
				wiresList[uCount] = "_>_"
			uCount += 1

		# Splits the wiresList into individual details. 0,2,4 are colors and 1,3,5 are endpoints
		for w in wiresList:
			wires.append(w.split(">")[0])
			wires.append(w.split(">")[1])


		#Occurance Logic
		print(" ")
		dCount = 0
		wCount = 0
		for d in wires:
			if (dCount%2 == 0): #Evens Colors
				wCount += 1
				match (d): #Testing Color of current wire
					case ("r"): #Wire is RED
						rOcc += 1
						match (wires[dCount + 1]): #Testing endpoint of RED wire
							case ("A"):
								if rOcc in [3,4,6,7,8]:
									print("Wire "+str(wCount) + ": "+str(wiresList[wCount-1]) + ") Cut")
								else:
									print("Wire "+str(wCount) + ": "+str(wiresList[wCount-1]) + ") Do NOT Cut")
							case ("B"):
								if rOcc in [2,5,7,8,9]:
									print("Wire "+str(wCount) + ": "+str(wiresList[wCount-1]) + ") Cut")
								else:
									print("Wire "+str(wCount) + ": "+str(wiresList[wCount-1]) + ") Do NOT Cut")
							case ("C"):
								if rOcc in [1,4,6,7]:
									print("Wire "+str(wCount) + ": "+str(wiresList[wCount-1]) + ") Cut")
								else:
									print("Wire "+str(wCount) + ": "+str(wiresList[wCount-1]) + ") Do NOT Cut")

					case ("blu"): #Wire is BLUE
						bluOcc += 1
						match (wires[dCount + 1]): #Testing endpoint of BLUE wire
							case ("A"):
								if bluOcc in [2,4,8,9]:
									print("Wire "+str(wCount) + ": "+str(wiresList[wCount-1]) + ") Cut")
								else:
									print("Wire "+str(wCount) + ": "+str(wiresList[wCount-1]) + ") Do NOT Cut")
							case ("B"):
								if bluOcc in [1,3,5,6]:
									print("Wire "+str(wCount) + ": "+str(wiresList[wCount-1]) + ") Cut")
								else:
									print("Wire "+str(wCount) + ": "+str(wiresList[wCount-1]) + ") Do NOT Cut")
							case ("C"):
								if bluOcc in [2,6,7,8]:
									print("Wire "+str(wCount) + ": "+str(wiresList[wCount-1]) + ") Cut")
								else:
									print("Wire "+str(wCount) + ": "+str(wiresList[wCount-1]) + ") Do NOT Cut")

					case ("bla"): #Wire is BLACK
						blaOcc += 1
						match (wires[dCount + 1]): #Testing endpoint of BLACK wire
							case ("A"):
								if blaOcc in [2,4,8,9]:
									print("Wire "+str(wCount) + ": "+str(wiresList[wCount-1]) + ") Cut")
								else:
									print("Wire "+str(wCount) + ": "+str(wiresList[wCount-1]) + ") Do NOT Cut")
							case ("B"):
								if blaOcc in [1,3,5,6]:
									print("Wire "+str(wCount) + ": "+str(wiresList[wCount-1]) + ") Cut")
								else:
									print("Wire "+str(wCount) + ": "+str(wiresList[wCount-1]) + ") Do NOT Cut")
							case ("C"):
								if blaOcc in [2,6,7,8]:
									print("Wire "+str(wCount) + ": "+str(wiresList[wCount-1]) + ") Cut")
								else:
									print("Wire "+str(wCount) + ": "+str(wiresList[wCount-1]) + ") Do NOT Cut")
					case("_"): #Blank Slot
						print("Wire " + str(wCount)+") No wire, ignore")
			dCount += 1
		print(" ")
					
		
			

print("Incase you haven't launched the game before, the verification code as of 10/9/2022 is 241")

#Module Loop
while isDoing == True:
	#checking which module you are currently working on
	print(" ")
	module = input("Module? (w/b/k/s/who/m/mO/cW/wS/done): ")
	if module == "w":
		print(" ")
		wires()
	elif module == "b":
		print(" ")
		button()
	elif module == "k":
		print(" ")
		keypad()
	elif module == "s":
		print(" ")
		simon()
	elif module == "who":
		print(" ")
		whofirst()
	elif module == "m":
		print(" ")
		memory()
	elif module == "mO":
		print(" ")
		morse()
	elif module == "cW":
		print(" ")
		compWires()
	elif module == "wS":
		print(" ")
		wireSeq()
	elif module == "done":
		print(" ")
		print("Bomb Complete. Congrats Defuser")
		isDoing = False
	else:
		print("Please enter a valid module")
		isDoing = True
