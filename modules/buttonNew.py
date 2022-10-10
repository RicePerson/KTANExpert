

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

    
