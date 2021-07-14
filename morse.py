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