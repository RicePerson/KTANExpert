

#Whos on First (input -> output, input -> outputx?)
def whofirst():
	whoWorking = True
	while whoWorking:
		#Def Vars: Step 1
		step1 = "EMPTY"
		spot = "EMPTY"
		step1Work = True
	
		#Logic: Step 1
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
