

def button():
    # Vars
    color = "EMPTY"
    text = "EMPTY"
    instruction = "EMPTY"
    strip = "EMPTY"

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

    #Manual Step 5
    if color == "y":
        instruction = "hold"

    #Manual Step 6
    if color == "r":
        if text == "EMPTY":
            text = input("What does the button say? (all lowercase): ")
        if text == "hold":
            instruction = "pressRelease"

    #Manual Step 7
    else:
        instruction = "hold"

    #Releasing a held button
    if instruction == "hold"
        print(" ")
        strip = input("Press and hold the button. While holding, input the color of the strip immediately to the right of the button (blu, w, y, other): ")
        if strip == "blu"
            print(" ")
            print("Release the button when the countdown timer has a 4 in any position")
            return
        elif strip == "w":
            print(" ")
            print("Release the button when the countdown timer has a 1 in any position")
            return
        elif strip == "y":
            print(" ")
            print("Release the button when the countdown timer has a 5 in any position")
            return
        else:
            print(" ")
            print("Release the button when the countdown timer has a 1 in any position")
    elif instruction == "pressRelease":
        print(" ")
        print("Press and immediately release the button")
        return
    else:
        return





    
