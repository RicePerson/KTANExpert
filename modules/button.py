

#Button (lots of input -> output)
def button():
	def hold():
		print("Hold down the button")
		time.sleep(1)
		strip = input("Color of strip? (blu/w/y/other): ")
		print(" ")
		if strip == "blu":
			print("Hold until countdown has 4")
		elif strip == "w":
			print("Hold until countdown has 1")
		elif strip == "y":
			print("Hold until countdown has 5")
		elif strip == "other":
			print("Hold until countdown has 1")
		else:
			print("You did something wrong at somepoint")

	#Def Vars
	color = input("Color? (blu/w/y/r/NOtA): ")
	text = input("Text? (abort/detonate/hold/NOtA): ")
	batteries = int(input("Batteries? (1/2/3/4/more): "))
	indicator = input("Indicator? (CAR/FRK/other): ")

	#Logic
	print(" ")
	if ((color == "blu") and (text == "abort")):
		hold()
		return
	elif ((batteries > 1) and (text == "detonate")):
		print("Press and release")
		return
	elif ((color == "w") and (indicator == "CAR")):
		hold()
		return
	elif ((batteries > 2) and (indicator == "FRK")):
		print("Press and release")
		return
	elif color == "y":
		hold()
		return
	elif ((color == "r") and (text == "hold")):
		print("Press and release")
		return
	else:
		hold()
		return