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
				    "Error. You didn't do the right thing. Please rerun module"
				)
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

#Button
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
        batteries = input("How many batteries are on the bomb?: ")
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
        batteries = input("How many batteries are on the bomb?: ")
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



print("Incase you haven't launched the game before, the verification code as of 10/9/2022 is 241")

#Module Loop
while isDoing == True:
	#checking which module you are currently working on
	print(" ")
	module = input("Module? (w/b/k/s/who/m/mO/cW/wS/stop): ")
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
	elif module == "cW":
		compWires()
	elif module == "wS":
		wireSeq()
	elif module == "stop":
		print("Bomb Complete. Congrats Defuser")
		isDoing = False
	else:
		print("Please enter a valid module")
		isDoing = True
