

#Wires (inputx7(8) -> output)
def wires():
	#Def Vars
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

	#If Not: 
	return