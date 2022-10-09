

#Complicated Wires (input x4 -> output, loop until complete)
def compWires():
	while True:
		#Def Vars
		colBlu = input("Does the wire have Blue coloring? (y/n): ")
		colRed = input("Does the wire have Red coloring? (y/n): ")
		wireLED = input("Is the LED on? (y/n): ")
		hasStar = input("Does the wire have a star symbol? (y/n): ")

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
		print(" ")

		#Logic
		if colBlu:
			if colRed:
				if wireLED:
					if hasStar:
						print("Do not cut")
					else:
						print("If Serial even, cut")
				else:
					if hasStar:
						print("If Parallel Port, cut")
					else:
						print("If Serial even, cut")
			else:
				if wireLED:
					print("If Parallel Port, cut")
				else:
					if hasStar:
						print("Do not Cut")
					else:
						print("If Serial even, cut")
		elif colRed:
			if wireLED:
				print("If 2 Battery, cut")
			else:
				if hasStar:
					print("Cut")
				else:
					print("If Serial even, cut")
		elif wireLED:
			if hasStar:
				print("If 2 Battery, cut")
			else:
				print("Do not cut")
		elif hasStar:
			print("Cut")
		else:
			print("Cut")
		print(" ")

		#Breaking Loop
		done = input("Are there more wires to process? (y/n): ")
		if done == "n":
			return
		else:
			pass