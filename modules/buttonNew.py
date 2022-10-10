

def button():
    # Vars
    color = "EMPTY"
    text = "EMPTY"
    instruction = "EMPTY"

    global batteries
    global litIndicators

    # Logic
    #Starting Information

    color = input("What is the color of the button? (blu, w, y, r, other): ")

    #Manual Step 1
    if color == "b":
        if text == "EMPTY":
            text = input("What does the button say? (all lowercase): ")
        if text == "abort":
            instruction = "hold"

    #Manual Step 2
    if batteries == "EMPTY":
        batteries = input("How many batteries are on the bomb?: ")
    if batteries > 1:
        if text == "EMPTY":
            text = input("What does the button say? (all lowercase): ")
        if text == "detonate":
            instruction = "pressRelease"

    #Manual Step 3
    if color == "w":
        if litIndicators == ["EMPTY"]:
            litIndicators = input("Please list all the lit indicators (all uppcase with a single space between each one): ").split()
        if "CAR" in litIndicators:
            instruction = "hold"

    #Manual Step 4
    if batteries == "EMPTY":
        batteries = input("How many batteries are on the bomb?: ")
    if batteries > 2:
        if litIndicators == ["EMPTY"]:
            litIndicators = input("Please list all the lit indicators (all uppcase with a single space between each one): ").split()
        if "FRK" in litIndicators:
            instruction = "pressRelease"




    
