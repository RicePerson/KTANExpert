import time
import math

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