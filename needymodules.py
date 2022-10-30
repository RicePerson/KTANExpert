# Needy Modules Sub-Expert
# Created by Reese Ford 10/17/2022
# https://www.github.com/RicePerson/KTANExpert

from os import system

system("title " + "NeedyModule Sub-Expert")

# Knobs
def knobs():
    leds = "EMPTY"
    leds = str(input("What is the led pattern?: "))
    if leds == "...": #Exit Command
        print("Exit Command Detected. Exitting")
        leds = "EMPTY"
        return
    ledsList = [x for x in leds]
    for l in ledsList: #Checking for non-binaries
        if l == "1" or l == "0":
            pass
        else:
            print("Error. Non-binary character detected. Resetting")
            return
    if len(ledsList) != 12: #Checking Length
        print("Error. Incorrect number of leds detected. Resetting")
        return

    side = "EMPTY"
    side = str(input("What side is 'up' on? (north,east,south,west): "))
    if side == "...": #Exit Command
        print("Exit Command Detected. Exitting")
        side = "EMPTY"
        return
    match side:
        case("north"): side = 0
        case("east"): side = 1
        case("south"): side = 2
        case("west"): side = 3
        case other:
            print("Error. Incorrect Direction Detected. Resetting")
            return

    match leds:
        case("001011111101"):
            position = 0
        case("101010011011"):
            position = 0

        case("011001111101"):
            position = 2
        case("101010010001"):
            position = 2

        case("000010100111"):
            position = 3
        case("000010000110"):
            position = 3

        case("101111111010"):
            position = 1
        case("101100111010"):
            position = 1

        case other:
            print("Error. Incorrect leds detected. Resetting")
            return

    position = (position + side)%4
    print(" ")
    match position:
        case 0:
            print("Turn the knob to the north position")
            return
        case 1:
            print("Turn the knob to the east position")
            return
        case 2:
            print("Turn the knob to the south position")
            return
        case 3:
            print("Turn the knob to the west position")
            return
        case other:
            print("Something went wrong. Resetting")
            return

#Starting Text
print("Needy Modules Sub-Expert")
print("Created by Reese Ford")
print(" ")

print("Needy Modules are pretty simple. There are only 3 possible ones.")
print("There is Venting Gas, Capacitor Discharge, and Knobs")
print("For Venting Gas, just follow the prompts on the screen with the goal to vent gas")
print("For Cap Discharge, pull down the lever to discharge the capacitor before it explodes")
print("For Knobs, follow the instructions below:")
while True:
    print(" ")
    knobs()




