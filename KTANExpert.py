#Imports
import time
import math

#External Module Imports
from modules.wires import *
from modules.button import *
from modules.keypad import *
from modules.simon import *
from modules.whofirst import *
from modules.memory import *
from modules.morseModule import *
from modules.compWires import *
from modules.wireSeq import *


#Def Vars
isDoing = True
explode = False
skip = input("Skip intro? y/n: ")
module = "EMPTY"


#Logic
#Intro
if skip == "y":
	print("Gotch ya")
else:
	print("Welcome to Keep Talking and Nobody Explodes")
	time.sleep(1)
	print(
	    "Currently, the only modules supported are Wires, Button, Keypad, Simon Says, Who's on First, Memory, Complicated Wires, and Wire Sequences")
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
	module = input("Module? (w/b/k/s/who/m/mO/cW/wS): ")
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
