

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
		print("Press the button labeled  4")
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
