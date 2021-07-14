import time
import math

#The Morse -> Letter
def morseToAlpha(input):
    if input == ".-":
        return "A"
    elif input == "-...":
        return "B"
    elif input == "-.-.":
        return "C"
    elif input == "-..":
        return "D"
    elif input == ".":
        return "E"
    elif input == "..-.":
        return "F"
    elif input == "--.":
        return "G"
    elif input == "....":
        return "H"
    elif input == "..":
        return "I"
    elif input == ".---":
        return "J"
    elif input == "-.-":
        return "K"
    elif input == ".-..":
        return "L"
    elif input == "--":
        return "M"
    elif input == "-.":
        return "N"
    elif input == "---":
        return "O"
    elif input == ".--.":
        return "P"
    elif input == "--.-":
        return "Q"
    elif input == ".-.":
        return "R"
    elif input == "...":
        return "S"
    elif input == "-":
        return "T"
    elif input == "..-":
        return "U"
    elif input == "...-":
        return "V"
    elif input == ".--":
        return "W"
    elif input == "-..-":
        return "X"
    elif input == "-.--":
        return "Y"
    elif input == "--..":
        return "Z"
    else:
        return

shell = ["S", "H", "E", "L", "L"]
halls = ["H", "A", "L", "L", "S"]
slick = ["S", "L", "I", "C", "K"]
trick = ["T", "R", "I", "C", "K"]
boxes = ["B", "O", "X", "E", "S"]
leaks = ["L", "E", "A", "K", "S"]
strobe = ["S", "T", "R", "O", "B", "E"]
bistro = ["B", "I", "S", "T", "R", "O"]
flick = ["F", "L", "I", "C", "K"]
bombs = ["B", "O", "M", "B", "S"]
bbreak = ["B", "R", "E", "A", "K"]
brick = ["B", "R", "I", "C", "K"]
steak = ["S", "T", "E", "A", "K"]
sting = ["S", "T", "I", "N", "G"]
vector = ["V", "E", "C", "T", "O", "R"]
beats = ["B", "E", "A", "T", "S"] 