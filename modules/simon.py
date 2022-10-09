

#New Simon Says (inputx? -> output x#)
def simon():
	#simon() is the streamlined but DEFINITELY more complicated version...hence the name
	#Def Vars / Logic (It's a loop)
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