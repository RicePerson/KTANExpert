

#Wire Sequences (input x2 -> output, loop until complete)
def wireSeq():
	redOcc = 0
	bluOcc = 0
	blkOcc = 0
	while True:
		#Def Vars
		print(" ")
		wire = []
		wireUn = input("What is the wire color and letter?: ")
		wire = wireUn.split()
		print("Wire: " + str(wire))

		#Logic - Occurences
		if wire[0] == "red":
			redOcc += 1
			print("Occur: " + str(redOcc))
		elif wire[0] == "blu":
			bluOcc += 1
			print("Occur: " + str(bluOcc))
		elif wire[0] == "bla":
			blkOcc += 1
			print("Occur: " + str(blkOcc))
		else:
			if wire[0] == "exit":
				pass
			else:
				print("Try Again")
		print(" ")

		#Logic - Processing
		#Red Wire
		if wire[0] == "red":
			if redOcc == 1:
				if wire[1] == "C":
					print("Cut that wire")
				else:
					print("Don't cut that wire")
			elif redOcc == 2:
				if wire[1] == "B":
					print("Cut that wire")
				else:
					print("Don't cut that wire")
			elif redOcc == 3:
				if wire[1] == "A":
					print("Cut that wire")
				else:
					print("Don't cut that wire")
			elif redOcc == 4:
				if wire[1] in ["A", "C"]:
					print("Cut that wire")
				else:
					print("Don't cut that wire")
			elif redOcc == 5:
				if wire[1] == "B":
					print("Cut that wire")
				else:
					print("Don't cut that wire")
			elif redOcc == 6:
				if wire[1] in ["A", "C"]:
					print("Cut that wire")
				else:
					print("Don't cut that wire")
			elif redOcc == 7:
				if wire[1] in ["A", "B", "C"]:
					print("Cut that wire")
				else:
					print("Don't cut that wire")
			elif redOcc == 8:
				if wire[1] in ["A", "B"]:
					print("Cut that wire")
				else:
					print("Don't cut that wire")
			elif redOcc == 9:
				if wire[1] == "B":
					print("Cut that wire")
				else:
					print("Don't cut that wire")

		#Blue Wire
		elif wire[0] == "blu":
			if bluOcc == 1:
				if wire[1] == "B":
					print("Cut that wire")
				else:
					print("Don't cut that wire")
			elif bluOcc == 2:
				if wire[1] in ["A", "C"]:
					print("Cut that wire")
				else:
					print("Don't cut that wire")
			elif bluOcc == 3:
				if wire[1] == "B":
					print("Cut that wire")
				else:
					print("Don't cut that wire")
			elif bluOcc == 4:
				if wire[1] == "A":
					print("Cut that wire")
				else:
					print("Don't cut that wire")
			elif bluOcc == 5:
				if wire[1] == "B":
					print("Cut that wire")
				else:
					print("Don't cut that wire")
			elif bluOcc == 6:
				if wire[1] in ["B", "C"]:
					print("Cut that wire")
				else:
					print("Don't cut that wire")
			elif bluOcc == 7:
				if wire[1] == "C":
					print("Cut that wire")
				else:
					print("Don't cut that wire")
			elif bluOcc == 8:
				if wire[1] in ["A", "C"]:
					print("Cut that wire")
				else:
					print("Don't cut that wire")
			elif bluOcc == 9:
				if wire[1] == "A":
					print("Cut that wire")
				else:
					print("Don't cut that wire")

		#Black Wire			
		elif wire[0] == "bla":
			if blkOcc == 1:
				if wire[1] in ["A", "B", "C"]:
					print("Cut that wire")
				else:
					print("Don't cut that wire")
			elif blkOcc == 2:
				if wire[1] in ["A", "C"]:
					print("Cut that wire")
				else:
					print("Don't cut that wire")
			elif blkOcc == 3:
				if wire[1] == "B":
					print("Cut that wire")
				else:
					print("Don't cut that wire")
			elif blkOcc == 4:
				if wire[1] in ["A", "C"]:
					print("Cut that wire")
				else:
					print("Don't cut that wire")
			elif blkOcc == 5:
				if wire[1] == "B":
					print("Cut that wire")
				else:
					print("Don't cut that wire")
			elif blkOcc == 6:
				if wire[1] in ["B", "C"]:
					print("Cut that wire")
				else:
					print("Don't cut that wire")
			elif blkOcc == 7:
				if wire[1] in ["A", "B"]:
					print("Cut that wire")
				else:
					print("Don't cut that wire")
			elif blkOcc == 8:
				if wire[1] == "C":
					print("Cut that wire")
				else:
					print("Don't cut that wire")
			elif blkOcc == 9:
				if wire[1] == "C":
					print("Cut that wire")
				else:
					print("Don't cut that wire")

		#Exit
		elif wire[0] == "exit":
			return

		#If nothing else
		else:
			print("Something Happened, try again")