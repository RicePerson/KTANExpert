# Keep Talking and Nobody Explodes Manual "Expert"
# Created By Reese Ford 07/13/2021
# https://www.github.com/RicePerson/KTANExpert


#Imports
import time
import math

#External Module Imports
from modules.wires import *
from modules.button import *
from modules.buttonNew import *
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
module = "EMPTY"
serialNum = "EMPTY"

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
