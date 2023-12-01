# /$$   /$$ /$$$$$$$$ /$$$$$$  /$$   /$$ /$$$$$$$$                                           /$$    
#| $$  /$$/|__  $$__//$$__  $$| $$$ | $$| $$_____/                                          | $$    
#| $$ /$$/    | $$  | $$  \ $$| $$$$| $$| $$       /$$   /$$  /$$$$$$   /$$$$$$   /$$$$$$  /$$$$$$  
#| $$$$$/     | $$  | $$$$$$$$| $$ $$ $$| $$$$$   |  $$ /$$/ /$$__  $$ /$$__  $$ /$$__  $$|_  $$_/  
#| $$  $$     | $$  | $$__  $$| $$  $$$$| $$__/    \  $$$$/ | $$  \ $$| $$$$$$$$| $$  \__/  | $$    
#| $$\  $$    | $$  | $$  | $$| $$\  $$$| $$        >$$  $$ | $$  | $$| $$_____/| $$        | $$ /$$
#| $$ \  $$   | $$  | $$  | $$| $$ \  $$| $$$$$$$$ /$$/\  $$| $$$$$$$/|  $$$$$$$| $$        |  $$$$/
#|__/  \__/   |__/  |__/  |__/|__/  \__/|________/|__/  \__/| $$____/  \_______/|__/         \___/  
#                                                           | $$                                    
#                                                           | $$                                    
#                                                           |__/                                    

# Keep Talking and Nobody Explodes Manual Expert
# Created By Reese Ford 07/13/2021
# https://www.github.com/RicePerson/KTANExpert


#Imports
from os import system
import os

#Def Vars
isDoing = True
explode = False
module = "EMPTY"

serialNum = "EMPTY"
batteries = "EMPTY"
litIndicators = []
parallelPort = "EMPTY"
vowel = "EMPTY"

#Application Window
system("title "+ "KTANExpert by Reese Ford")

# Module Declarations

#Wires (inputx7(8) -> output)
def wires():
    #Def Vars
    global serialNum
    wireList = []
    instruction = "EMPTY"

    number = str(input("How many wires do you have? (3/4/5/6): "))
    if number == "...":
        print("Exit Command Detected. Exitting")
        return
    if number not in ["3","4","5","6"]:
        print("Error. Invalid number, '" + str(number) + "'. Resetting")
        return
    else:
        number = int(number)

    #Assigning Wires
    wireList = str(input("What are the " + str(number) + " wire colors from top to bottom? (w/y/r/blu/bla): "))
    if wireList == "...":
        print("Exit Command Detected. Exitting")
        return
    wireList = wireList.split(";")
    if len(wireList) != number:
        print("Error. Invalid number of wires, '" + str(len(wireList)) + "'. Resetting")
        return

    for c in wireList:
        if c not in ["w","y","r","blu","bla"]:
            print("Error. Invalid color, '" + str(c) + "'. Resetting")
            return

    #Logic - 3 Wires
    if number == 3:
        if "r" not in wireList:
            instruction = "cutwire2"
        elif wireList[number-1] == "w":
            instruction = "cutwirelast"
        elif wireList.count("blu") > 1:
            instruction = "cutwirelastblue"
        else:
            instruction = "cutwirelast"

    #Logic - 4 Wires
    elif number == 4:
        if (wireList.count("r") > 1) and (serialNum == "EMPTY" or serialNum%2 == 1):
            if serialNum == "EMPTY":
                serialNum = str(input("What is the last digit of the serial number?: "))
                if serialNum not in ["1","2","3","4","5","6","7","8","9","0"]:
                    print("Error. Invalid serial num, '" + str(serialNum) + "'. Resetting")
                    serialNum = "EMPTY"
                    return
                else:
                    serialNum = int(serialNum)
            if serialNum%2 == 1:
                instruction = "cutwirelastred"
        if (instruction == "EMPTY") and (wireList[number-1] == "y") and ("r" not in wireList):
            instruction = "cutwirefirst"
        if (instruction == "EMPTY") and (wireList.count("blu") == 1):
            instruction = "cutwirefirst"
        if (instruction == "EMPTY") and (wireList.count("y") > 1):
            instruction = "cutwirelast"
        if instruction == "EMPTY":
            instruction = "cutwiresecond"

    #Logic - 5 Wires
    elif number == 5:
        if (wireList[number-1] == "bla") and (serialNum == "EMPTY" or serialNum%2 == 1):
            if serialNum == "EMPTY":
                serialNum = str(input("What is the last digit of the serial number?: "))
                if serialNum not in ["1","2","3","4","5","6","7","8","9","0"]:
                    print("Error. Invalid serial num, '" + str(serialNum) + "'. Resetting")
                    serialNum = "EMPTY"
                    return
                else:
                    serialNum = int(serialNum)
            if serialNum%2 == 1:
                instruction = "cutwirefourth"
        if (instruction == "EMPTY") and (wireList.count("r") == 1) and (wireList.count("y") > 1):
            instruction = "cutwirefirst"
        if (instruction == "EMPTY") and ("bla" not in wireList):
            instruction = "cutwiresecond"
        if instruction == "EMPTY":
            instruction = "cutwirefirst"

    #Logic - 6 Wires
    elif number == 6:
        if (wireList.count("y") == 0) and (serialNum == "EMPTY" or serialNum%2 == 1):
            if serialNum == "EMPTY":
                serialNum = str(input("What is the last digit of the serial number?: "))
                if serialNum not in ["1","2","3","4","5","6","7","8","9","0"]:
                    print("Error. Invalid serial num, '" + str(serialNum) + "'. Resetting")
                    serialNum = "EMPTY"
                    return
                else:
                    serialNum = int(serialNum)
            if serialNum%2 == 1:
                instruction = "cutwirethird"
        if (instruction == "EMPTY") and (wireList.count("y") == 1) and (wireList.count("w") > 1):
            instruction = "cutwirefourth"
        if (instruction == "EMPTY") and ("r" not in wireList):
            instruction = "cutwirelast"
        if instruction == "EMPTY":
            instruction = "cutwirefourth"

    else:
        print("Something went wrong with the wire logic. Please try again")
        return

    #Instruction Output
    print(" ")
    match instruction:
        case("cutwirefirst"):
            print("Cut the first wire")
            return
        case("cutwiresecond"):
            print("Cut the second wire")
            return
        case("cutwirethird"):
            print("Cut the third wire")
            return
        case("cutwirefourth"):
            print("Cut the fourth wire")
            return
        case("cutwirelastblue"):
            print("Cut the last BLUE wire")
            return
        case("cutwirelastred"):
            print("Cut the last RED wire")
            return
        case("cutwirelast"):
            print("Cut the last wire")
            return
        case other:
            print("Something went wrong with the instruction logic. Please try again")
            return

#Button (inputs various -> output)
def button():
    # Vars
    color = "EMPTY"
    text = "EMPTY"
    instruction = "EMPTY"
    givenInstruction = False
    strip = "EMPTY"

    global batteries
    global litIndicators

    # Logic
    #Starting Information

    color = str(input("What is the color of the button? (blu, w, y, r): "))
    if color not in ["blu","w","y","r"]: #Testing color
        print("Error. Invalid color, '" + str(color) + "'. Resetting")
        return
    if color == "...": # Exit Command
        print("Exit Command Detected. Exiting...")
        return

    #Manual Step 1
    if color == "blu":
        if text == "EMPTY":
            text = str(input("What does the button say? (all lowercase): "))
            if text == "...": # Exit Command
                print("Exit Command Detected. Exiting...")
                return
        if text == "abort":
            instruction = "hold"
            givenInstruction = True

    #Manual Step 2
    if (givenInstruction == False) and (batteries == "EMPTY"):
        batteries = str(input("How many batteries are on the bomb?: "))
        if batteries == "...": # Exit Command
            print("Exit Command Detected. Exiting...")
            batteries = "EMPTY"
            return
        if batteries in ["0","1","2","3","4","5","6","7","8","9","10"]:
            batteries = int(batteries)
        else:
            print("Error. Incorrect number of batteries. Resetting")
            batteries = "EMPTY"
            return
    if (givenInstruction == False) and (batteries > 1):
        if text == "EMPTY":
            text = str(input("What does the button say? (all lowercase): "))
            if text == "...": # Exit Command
                print("Exit Command Detected. Exiting...")
                text = "EMPTY"
                return
        if text == "detonate":
            instruction = "pressRelease"
            givenInstruction = True

    #Manual Step 3
    if (givenInstruction == False) and (color == "w"):
        if litIndicators == []:
            litIndicators = str(input("Please list all the lit indicators (all uppercase with a semicolon between each one): ")).split(";")
            if litIndicators == "...": # Exit Command
                print("Exit Command Detected. Exiting...")
                litIndicators = "EMPTY"
                return
        if "CAR" in litIndicators:
            instruction = "hold"
            givenInstruction = True

    #Manual Step 4
    if (givenInstruction == False) and (batteries == "EMPTY"):
        batteries = str(input("How many batteries are on the bomb?: "))
        if batteries == "...": # Exit Command
            print("Exit Command Detected. Exiting...")
            batteries = "EMPTY"
            return
        if batteries in ["0","1","2","3","4","5","6","7","8","9","10"]:
            batteries = int(batteries)
        else:
            print("Error. Invalid number of batteries, '" + str(batteries) + "'. Resetting")
            batteries = "EMPTY"
            return
    if (givenInstruction == False) and (batteries > 2):
        if litIndicators == []:
            litIndicators = str(input("Please list all the lit indicators (all uppercase with a semicolon between each one): ")).split(";")
            if litIndicators == "...": # Exit Command
                print("Exit Command Detected. Exiting...")
                litIndicators = "EMPTY"
                return
        if "FRK" in litIndicators:
            instruction = "pressRelease"
            givenInstruction = True

    #Manual Step 5
    if (givenInstruction == False) and (color == "y"):
        instruction = "hold"
        givenInstruction = True

    #Manual Step 6
    if (givenInstruction == False) and (color == "r"):
        if text == "EMPTY":
            text = str(input("What does the button say? (all lowercase): "))
            if text == "...": # Exit Command
                print("Exit Command Detected. Exiting...")
                text = "EMPTY"
                return
        if text == "hold":
            instruction = "pressRelease"
            givenInstruction = True

    #Manual Step 7
    if (givenInstruction == False):
        instruction = "hold"
        givenInstruction = False

    #Releasing a held button
    match instruction:
        case "hold":
            print(" ")
            strip = str(input("Press and hold the button. While holding, input the color of the strip immediately to the right of the button (blu, w, y, other): "))
            match strip:
                case "...":
                    print("Exit Command Detected. Exiting...")
                    strip = "EMPTY"
                    return
                case "blu":
                    print(" ")
                    print("Release the button when the countdown timer has a 4 in any position")
                    return
                case "w":
                    print(" ")
                    print("Release the button when the countdown timer has a 1 in any position")
                    return
                case "y":
                    print(" ")
                    print("Release the button when the countdown timer has a 5 in any position")
                    return
                case other:
                    print(" ")
                    print("Release the button when the countdown timer has a 1 in any position")
        case "pressRelease":
            print(" ")
            print("Press and immediately release the button")
            return
        case other:
            print("Error. Something went wrong. Resetting.")
            return

#Keypad (specific inputx4 -> output)
def keypad():
    #Def Vars - keyLists
    keys = [
        "lolli", "at", "lambda", "light", "staff", "h", "backC", "mouth",
        "slap", "starW", "?", "copy", "butt", "kk", "stroke", "6", "para",
        "bT", "smile", "trident", "forwardC", "shrek3", "starB", "stitch",
        "ae", "headN", "omega"
    ]
    c1 = ["lolli", "at", "lambda", "light", "staff", "h", "backC"]
    c2 = ["mouth", "lolli", "backC", "slap", "starW", "h", "?"]
    c3 = ["copy", "butt", "slap", "kk", "stroke", "lambda", "starW"]
    c4 = ["6", "para", "bT", "staff", "kk", "?", "smile"]
    c5 = ["trident", "smile", "bT", "forwardC", "para", "shrek3", "starB"]
    c6 = ["6", "mouth", "stitch", "ae", "trident", "headN", "omega"]

    #Def Vars - userLists
    userKeys = []
    for i in keys:
        print(i)

    userKeys = str(input("What are the symbols on the keypad seperated by semicolons? (See list above): "))
    if userKeys == "...": # Exit Command
        print("Exit Command Detected. Exiting...")
        userKeys = "EMPTY"
        return
    userKeys = userKeys.split(";")
    for k in userKeys:
        if k in keys:
            pass
        else:
            print("Error. Invlaid Key, '" + str(k) + "'. Resetting")
            userKeys = "EMPTY"
            return
    if len(userKeys) != 4:
        print("Error. Invalid Number of Keys, '" + str(len(userKeys)) + "'. Resetting")
        userKeys = "EMPTY"
        return

    #Logic
    answerColumn = []
    if all(elem in c1 for elem in userKeys):
        answerColumn = c1
        #print("Column: " + str(answerKeys))
    elif all(elem in c2 for elem in userKeys):
        answerColumn = c2
        #print("Column: " + str(answerKeys))
    elif all(elem in c3 for elem in userKeys):
        answerColumn = c3
        #print("Column: " + str(answerKeys))
    elif all(elem in c4 for elem in userKeys):
        answerColumn = c4
        #print("Column: " + str(answerKeys))
    elif all(elem in c5 for elem in userKeys):
        answerColumn = c5
        #print("Column: " + str(answerKeys))
    elif all(elem in c6 for elem in userKeys):
        answerColumn = c6
        #print("Column: " + str(answerKeys))
    else:
        print("Error. No column has all of the inputed keys. Resetting")
        return

    #Final print()
    finalList = [x for x in answerColumn if x in userKeys]
    print(" ")
    print("Click these buttons in order: ")
    for i in range(4):
        print(str(i+1)+") " + str(finalList[i]))

#New Simon Says (inputxIndefinite -> output x#)
def newnewSimon():
    flash = 1
    flashSeq = []
    global vowel
    strikes = "EMPTY"

    if vowel == "EMPTY":
        vowel = str(input("Is there a vowel in the serial number? (y/n): "))
        match vowel:
            case("y"): vowel = True
            case("n"): vowel = False
            case("..."):
                print("Exit Command Detected. Exiting")
                return
            case other:
                print("Error. Invalid response, '" + str(vowel) + "'. Resetting")
                vowel = "EMPTY"
                return
    
    strikes = str(input("How many strikes are currently on the bomb? (0/1/2): "))
    match strikes:
        case("0"):strikes = 0
        case("1"):strikes = 1
        case("2"):strikes = 2
        case("..."):
            print("Exit Command Detected. Exiting")
            return
        case other:
            print("Error. Invalid number of strikes, '" + str(strikes) + "'. Resetting")
            strikes = "EMPTY"
            return


    while True:
        finalSimon = []
        inputSuccess = False
        user = str(input("What color is flash " + str(flash) +"? (r/blu/y/g/done): "))
        match user:
            case("r"): 
                flashSeq.append("r")
                inputSuccess = True
            case("blu"): 
                flashSeq.append("blu")
                inputSuccess = True
            case("y"): 
                flashSeq.append("y")
                inputSuccess = True
            case("g"): 
                flashSeq.append("g")
                inputSuccess = True
            case("..."):
                print("Exit Command Detected. Exitting")
                return
            case("done"):
                return
            case other: 
                print("Error. Invalid color, '" + str(user) + "'. Please try again")
                inputSuccess = False
                pass

        if inputSuccess == True:
            for f in flashSeq:
                if vowel == True:
                    match strikes:
                        case 0: 
                            match f: #Vowel, No Strikes
                                case("r"):finalSimon.append("blu")
                                case("blu"):finalSimon.append("r")
                                case("g"):finalSimon.append("y")
                                case("y"):finalSimon.append("g")
                                case other:
                                    print("Something went wrong. Resetting")
                                    return
                        case 1:
                            match f: #Vowel, One Strike
                                case("r"):finalSimon.append("y")
                                case("blu"):finalSimon.append("g")
                                case("g"):finalSimon.append("blu")
                                case("y"):finalSimon.append("r")
                                case other:
                                    print("Something went wrong. Resetting")
                                    return
                        case 2:
                            match f: #Vowel, Two Strikes
                                case("r"):finalSimon.append("g")
                                case("blu"):finalSimon.append("r")
                                case("g"):finalSimon.append("y")
                                case("y"):finalSimon.append("blu")
                                case other:
                                    print("Something went wrong. Resetting")
                                    return
                elif vowel == False:
                    match strikes:
                        case 0: 
                            match f: #No Vowel, No Strikes
                                case("r"):finalSimon.append("blu")
                                case("blu"):finalSimon.append("y")
                                case("g"):finalSimon.append("g")
                                case("y"):finalSimon.append("r")
                                case other:
                                    print("Something went wrong. Resetting")
                                    return
                        case 1:
                            match f: #No Vowel, One Strike
                                case("r"):finalSimon.append("r")
                                case("blu"):finalSimon.append("blu")
                                case("g"):finalSimon.append("y")
                                case("y"):finalSimon.append("g")
                                case other:
                                    print("Something went wrong. Resetting")
                                    return
                        case 2:
                            match f: #No Vowel, Two Strikes
                                case("r"):finalSimon.append("y")
                                case("blu"):finalSimon.append("g")
                                case("g"):finalSimon.append("blu")
                                case("y"):finalSimon.append("r")
                                case other:
                                    print("Something went wrong. Resetting")
                                    return

        print(" ")
        print("Click these buttons in order: ")
        for s in finalSimon:
            match s:
                case("r"):print("Red")
                case("blu"):print("Blue")
                case("y"):print("Yellow")
                case("g"):print("Green")
                case other:
                    print("Something went wrong. Resetting")
                    return
        print(" ")
        flash = flash + 1

#Whos on First (input -> output, input -> outputx?)
def whofirst():
    #Lists of STEP 2 Words
    #Copy this to make it easier: ", ". So basically WORD CtrlV WORD CtrlV WORD and so on and so forth

    displayWords = ["yes", "first", "display", "okay", "says", "nothing", "*blank*","blank", "no", "led", "lead", "read", 
                "red", "reed", "leed", "hold on", "you", "you are", "your", "you're", "ur", "there", "they're", "their", "they are", "see", "c", "cee"]

    ready = ["yes", "okay", "what", "middle", "left", "press", "right", "blank", "ready"]
    first = ["left", "okay", "yes", "middle", "no", "right", "nothing", "uhhh", "wait", "ready", "blank", "what", "press", "first"]
    no = ["blank", "uhhh", "wait", "first", "what", "ready", "right", "yes", "nothing", "left", "press", "okay", "no"]
    blank = ["wait", "right", "okay", "middle", "blank"]
    nothing = ["uhhh", "right", "okay", "middle", "yes", "blank", "no", "press", "left", "what", "wait", "first", "nothing"]
    yes = ["okay", "right", "uhhh", "middle", "first", "what", "press", "ready", "nothing", "yes"]
    what = ["uhhh", "what"]
    uhhh = ["ready", "nothing", "left", "what", "okay", "yes", "right", "no", "press", "blank", "uhhh"]
    left = ["right", "left"]
    right = ["yes", "nothing", "ready", "press", "no", "wait", "what", "right"]
    middle = ["blank", "ready", "okay", "what", "nothing", "press", "no", "wait", "left", "middle"]
    okay = ["middle", "no", "first", "yes", "uhhh", "nothing", "wait", "okay"]
    wait = ["uhhh", "no", "blank", "okay", "yes", "left", "first", "press", "what", "wait"]
    press = ["right", "middle", "yes", "ready", "press"]
    you = ["sure", "you are", "your", "you're", "next", "uh huh", "ur", "hold", "what?", "you"]
    youare = ["your", "next", "like", "uh huh", "what?", "done", "uh uh", "hold", "you", "u", "you're", "sure", "ur", "you are"]
    your = ["uh uh", "you are", "uh huh", "your"]
    youre = ["you", "you're"]
    ur = ["done", "u", "ur"]
    u = ["uh huh", "sure", "next", "what?", "you're", "ur", "uh uh", "done", "u"]
    uhhuh = ["uh huh"]
    uhuh = ["ur", "u", "you are", "you're", "next", "uh uh"]
    whatq = ["you", "hold", "you're", "your", "u", "done", "uh uh", "like", "you are", "uh huh", "ur", "next", "what?"]
    done = ["sure", "uh huh", "next", "what?", "your", "ur", "you're", "hold", "like", "you", "u", "you are", "uh uh", "done"]
    nextt = ["what?", "uh huh", "uh uh", "your", "hold", "sure", "next"]
    hold = ["you are", "u", "done", "uh uh", "you", "ur", "sure", "what?", "you're", "next", "hold"]
    sure = ["you are", "done", "like", "you're", "you", "hold", "uh huh", "ur", "sure"]
    like = ["you're", "next", "u", "ur", "hold", "done", "uh uh", "what?", "uh huh", "you", "like"]

    totalList = displayWords+ready+first+no+blank+nothing+yes+what+uhhh+left+right+middle+\
        okay+wait+press+you+youare+your+youre+ur+u+uhhuh+uhuh+whatq+done+nextt+hold+sure+like

    while True:
        # STEP 1 - Player Input (0:Display 1,2,3:TopLeft-to-BottomLeft 4,5,6:TopRight-to-BottomRight)
        userWords = "EMPTY"
        userWords = str(input("What are the words on the module, starting with display, then topleft to bottomleft, then topright to bottomright?: "))
        if userWords == "...": # Exit Command
            print("Exit Command Detected. Exiting...")
            userWords = "EMPTY"
            return
        userWords = userWords.split(";")
        #Checks
        if len(userWords) != 7:
            print("Error. Invalid number of words, '" + str(len(userWords)) + "'. Resetting")
            return
        else:
            for i in range(0,6):
                if i == 0:
                    if userWords[0] not in displayWords:
                        print("Error. Invalid display word ,'" + str(userWords[0]) + "'. Resetting")
                        return
                if userWords[i] not in totalList:
                    print("Error. Invalid word .'" + str(userWords[i])+ "'. Resetting")
                    return
    
        # DisplayWord's Sacred Button, ButtonWord, Logic
        buttonWord = "EMPTY"
        displayWordsButtonIndex = [2, 4, 6, 4, 6, 2, 3, 5, 6, 2, 6, 5, 5, 3, 3, 6, 5, 6, 5, 5, 1, 6, 3, 5, 2, 6, 4, 6]
        #buttonIndex = displayWordsButtonIndex[displayWords.index(userWords[0])]
        buttonWord = userWords[displayWordsButtonIndex[displayWords.index(userWords[0])]] #This line turns the display word in userWords[0] into a corresponding button from userWords

        # STEP 2 - Assigning the buttonWord's appropriate list
        buttonWordsList=[]
        match (buttonWord):
            case"ready":buttonWordsList=ready
            case"first":buttonWordsList=first
            case"no":buttonWordsList=no
            case"blank":buttonWordsList=blank
            case"nothing":buttonWordsList=nothing
            case"yes":buttonWordsList=yes
            case"what":buttonWordsList=what
            case"uhhh":buttonWordsList=uhhh
            case"left":buttonWordsList=left
            case"right":buttonWordsList=right
            case"middle":buttonWordsList=middle
            case"okay":buttonWordsList=okay
            case"wait":buttonWordsList=wait
            case"press":buttonWordsList=press
            case"you":buttonWordsList=you
            case"you are":buttonWordsList=youare
            case"your":buttonWordsList=your
            case"you're":buttonWordsList=youre
            case"ur":buttonWordsList=ur
            case"u":buttonWordsList=u
            case"uh huh":buttonWordsList=uhhuh
            case"uh uh":buttonWordsList=uhuh
            case"what?":buttonWordsList=whatq
            case"done":buttonWordsList=done
            case"next":buttonWordsList=nextt
            case"hold":buttonWordsList=hold
            case"sure":buttonWordsList=sure
            case"like":buttonWordsList=like
            case other:
                print("Error. Invalid button word, '" + str(buttonWord) + "'. Resetting")
                return

        print(" ")
        success = False
        for w in buttonWordsList:
            if w in userWords[1:]:
                success = True
                print("Press the button labeled " + str(w))
                print(" ")
                if str(input("Is the module complete? (y/n): ")) == "y":
                    return
                else:
                    print(" ")
                    break

        # If none of them match...
        if success == False:
            print("Error. No buttons match buttonWordsList. Resetting.")
            return

#Memory (input -> output x5) (This is as simple as I want in terms of input and output)
def memory():
    #Def Vars
    positions = []
    numbers = []
    print("Input the numbers starting with Display, and then left to right")

    #Def Vars: Stage 1 - Settings Lists
    stage1un = "EMPTY"
    stage1 = "EMPTY"
    stage1un = str(input("Stage1 - What are the numbers given? (1,2,3,4,r): "))
    if stage1un == "...": # Exit Command
        print("Exit Command Detected. Exiting...")
        stage1un = "EMPTY"
        return
    if stage1un == "r":
        print("Reset detected. Resetting expert...")
        return
    stage1 = [x for x in stage1un]

    if len(stage1) != 5:
        print("Error. Incorrect length, '" + str(len(stage1)) + "'. Please Try Again")
        return
    for i in range(len(stage1)):
        if stage1[i] in ["1","2","3","4"]:
            stage1[i]=int(stage1[i])
            pass
        else:
            print("Error. Incorrect number, '" + str(stage1[i]) + "'. Please Try Again")
            return
    existing = []
    for i in stage1[1:]:
        if i in existing:
            print("Error. Duplicate button number ,'" + str(i) + "'. Please Try Again")
            return
        else:
            existing.append(i)

    #Logic: Stage 1
    print(" ")
    match stage1[0]:
        case 1:
            print("Press the button labeled " + str(stage1[2]))
            positions.append(2)
            numbers.append(stage1[2])
        case 2:
            print("Press the button labeled " + str(stage1[2]))
            positions.append(2)
            numbers.append(stage1[2])
        case 3:
            print("Press the button labeled " + str(stage1[3]))
            positions.append(3)
            numbers.append(stage1[3])
        case 4:
            print("Press the button labeled " + str(stage1[4]))
            positions.append(4)
            numbers.append(stage1[4])
    print(" ")


    #Def Vars: Stage3 - Settings Lists
    stage2complete = False
    while stage2complete == False:
        stage2un = "EMPTY"
        stage2 = "EMPTY"
        stage2error = False
        stage2un = str(input("Stage2 - What are the numbers given? (1,2,3,4,r): "))
        if stage2un == "...": # Exit Command
            print("Exit Command Detected. Exiting...")
            stage2un = "EMPTY"
            return
        if stage2un == "r": # Reset Command
            print("Reset detected. Resetting expert...")
            return
        stage2 = [x for x in stage2un]

        if len(stage2) != 5: # Is the number of inputs correct? No...
            print("Error. Incorrect length, '" + str(len(stage2)) + "'. Please Try Again")
            stage2error = True
        for i in range(len(stage2)):
            if stage2[i] in ["1","2","3","4"]: # Are the inputs numbers?
                stage2[i]=int(stage2[i])
            else: # No...
                print("Error. Incorrect number, '" + str(stage2[i]) + "'. Please Try Again")
                stage2error = True
                break
        existing = []
        for i in stage2[1:]:
            if i in existing:
                print("Error. Duplicate button number ,'" + str(i) + "'. Please Try Again")
                stage2error = True
                break
            else:
                existing.append(i)

        if stage2error:
            continue
        else:
            #Logic Stage2
            print(" ")
            match stage2[0]:
                case 1:
                    print("Press the button labeled 4")
                    index = stage2.index(4, 1, 5)
                    positions.append(index)
                    numbers.append(4)
                    stage2complete = True
                case 2:
                    print("Press the button labeled " + str(stage2[positions[0]]))
                    positions.append(positions[0])
                    numbers.append(stage2[positions[0]])
                    stage2complete = True
                case 3:
                    print("Press the button labeled " + str(stage2[1]))
                    positions.append(1)
                    numbers.append(stage2[1])
                    stage2complete = True
                case 4:
                    print("Press the button labeled " + str(stage2[positions[0]]))
                    positions.append(positions[0])
                    numbers.append(stage2[positions[0]])
                    stage2complete = True
                case other:
                    print("Error. Something went wrong. Please Try Again")
            print(" ")


    #Def Vars: Stage 3 - Settings Lists
    stage3complete = False
    while stage3complete == False:
        stage3un = "EMPTY"
        stage3 = "EMPTY"
        stage3error = False
        stage3un = str(input("Stage3 - What are the numbers given? (1,2,3,4,r): "))
        if stage3un == "...": # Exit Command
            print("Exit Command Detected. Exiting...")
            stage3un = "EMPTY"
            return
        if stage3un == "r": # Reset Command
            print("Reset detected. Resetting expert...")
            return #RF
        stage3 = [x for x in stage3un]

        if len(stage3) != 5: # Is the number of inputs correct? No...
            print("Error. Incorrect length, '" + str(len(stage3)) + "'. Please Try Again")
            stage3error = True
        for i in range(len(stage3)):
            if stage3[i] in ["1","2","3","4"]: # Are the inputs numbers?
                stage3[i]=int(stage3[i])
            else: # No...
                print("Error. Incorrect number, '" + str(stage3[i]) + "'. Please Try Again")
                stage3error = True
                break
        existing = []
        for i in stage3[1:]:
            if i in existing:
                print("Error. Duplicate button number ,'" + str(i) + "'. Please Try Again")
                stage3error = True
                break
            else:
                existing.append(i)

        if stage3error:
            continue
        else:
            #Logic: Stage 3
            print(" ")
            match stage3[0]:
                case 1:
                    print("Press the button labeled " + str(numbers[1]))
                    index = stage3.index(numbers[1])
                    positions.append(index)
                    numbers.append(numbers[1])
                    stage3complete = True
                case 2:
                    print("Press the button labeled " + str(numbers[0]))
                    index = stage3.index(numbers[0])
                    positions.append(index)
                    numbers.append(numbers[0])
                    stage3complete = True
                case 3:
                    print("Press the button labeled " + str(stage3[3]))
                    positions.append(3)
                    numbers.append(stage3[3])
                    stage3complete = True
                case 4:
                    print("Press the button labeled 4")
                    index = stage3.index(4, 1, 5)
                    positions.append(index)
                    numbers.append(4)
                    stage3complete = True
            print(" ")


    #Def Vars: Stage 4 - Settings Lists
    stage4complete = False
    while stage4complete == False:
        stage4un = "EMPTY"
        stage4 = "EMPTY"
        stage4error = False
        stage4un = str(input("Stage4 - What are the numbers given? (1,2,3,4,r): "))
        if stage4un == "...": # Exit Command
            print("Exit Command Detected. Exiting...")
            stage4un = "EMPTY"
            return
        if stage4un == "r": # Reset Command
            print("Reset detected. Resetting expert...")
            return
        stage4 = [x for x in stage4un]

        if len(stage4) != 5: # Is the number of inputs correct? No...
            print("Error. Incorrect length, '" + str(len(stage4)) + "'. Please Try Again")
            stage4error = True
        for i in range(len(stage4)):
            if stage4[i] in ["1","2","3","4"]: # Are the inputs numbers?
                stage4[i]=int(stage4[i])
            else: # No...
                print("Error. Incorrect number, '" + str(stage4[i]) + "'. Please Try Again")
                stage4error = True
                break
        existing = []
        for i in stage4[1:]:
            if i in existing:
                print("Error. Duplicate button number ,'" + str(i) + "'. Please Try Again")
                stage4error = True
                break
            else:
                existing.append(i)

        if stage4error:
            continue
        else:
            #Logic: Stage 4
            print(" ")
            match stage4[0]:
                case 1:
                    print("Press the button labeled " + str(stage4[positions[0]]))
                    positions.append(positions[0])
                    numbers.append(stage4[positions[0]])
                    stage4complete = True
                case 2:
                    print("Press the button labeled " + str(stage4[1]))
                    positions.append(1)
                    numbers.append(stage4[1])
                    stage4complete = True
                case 3:
                    print("Press the button labeled " + str(stage4[positions[1]]))
                    positions.append(positions[1])
                    numbers.append(stage4[positions[1]])
                    stage4complete = True
                case 4:
                    print("Press the button labeled " + str(stage4[positions[1]]))
                    positions.append(positions[1])
                    numbers.append(stage4[positions[1]])
                    stage4complete = True
            print(" ")


    #Def Vars: Stage 5 - Settings Lists
    stage5complete = False
    while stage5complete == False:
        stage5un = "EMPTY"
        stage5 = "EMPTY"
        stage5error = False
        stage5un = str(input("Stage5 - What are the numbers given? (1,2,3,4,r): "))
        if stage5un == "...": # Exit Command
            print("Exit Command Detected. Exiting...")
            stage5un = "EMPTY"
            return
        if stage5un == "r": # Reset Command
            print("Reset detected. Resetting expert...")
            return
        stage5 = [x for x in stage5un]

        if len(stage5) != 5: # Is the number of inputs correct? No...
            print("Error. Incorrect length, '" + str(len(stage5)) + "'. Please Try Again")
            stage5error = True
        for i in range(len(stage5)):
            if stage5[i] in ["1","2","3","4"]: # Are the inputs numbers?
                stage5[i]=int(stage5[i])
            else: # No...
                print("Error. Incorrect number, '" + str(stage5[i]) + "'. Please Try Again")
                stage5error = True
                break
        existing = []
        for i in stage5[1:]:
            if i in existing:
                print("Error. Duplicate button number ,'" + str(i) + "'. Please Try Again")
                stage5error = True
                break
            else:
                existing.append(i)

        if stage5error:
            continue
        else:
            #Logic: Stage 5
            print(" ")
            match stage5[0]:
                case 1:
                    print("Press the button labeled " + str(numbers[0]))
                    index = stage5.index(numbers[0])
                    positions.append(index)
                    numbers.append(numbers[0])
                    stage5complete = True
                case 2:
                    print("Press the button labeled " + str(numbers[1]))
                    index = stage5.index(numbers[1])
                    positions.append(index)
                    numbers.append(numbers[1])
                    stage5complete = True
                case 3:
                    print("Press the button labeled " + str(numbers[3]))
                    index = stage5.index(numbers[3])
                    positions.append(index)
                    numbers.append(numbers[3])
                    stage5complete = True
                case 4:
                    print("Press the button labeled " + str(numbers[2]))
                    index = stage5.index(numbers[2])
                    positions.append(index)
                    numbers.append(numbers[2])
                    stage5complete = True
            print(" ")

#The Morse -> Letter
def morseToAlpha(morseIn):
    match morseIn:
        case ".-": return "A"
        case "-...": return "B"
        case "-.-.": return "C"
        case "-..": return "D"
        case ".": return "E"
        case "..-.": return "F"
        case "--.": return "G"
        case "....": return "H"
        case "..": return "I"
        case ".---": return "J"
        case "-.-": return "K"
        case ".-..": return "L"
        case "--": return "M"
        case "-.": return "N"
        case "---": return "O"
        case ".--.": return "P"
        case "--.-": return "Q"
        case ".-.": return "R"
        case "...": return "S"
        case "-": return "T"
        case "..-": return "U"
        case "...-": return "V"
        case ".--": return "W"
        case "-..-": return "X"
        case "-.--": return "Y"
        case "--..": return "Z"
        case other:
            print("Error. Invaild morse, '" + str(morseIn) + "'. Resetting")
            return "ERROR"

#Morse Code Logic (input -> output)
def morse():
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

    #Def Vars
    userMorseUnsplit = str(input("What is your Morse Code (see README.md for instructions)?: "))
    if userMorseUnsplit == "...": # Exit Command
        print("Exit Command Detected. Exiting...")
        userMorseUnsplit = "EMPTY"
        return
    userMorse = userMorseUnsplit.split()
    print("Inputed Morse: " + str(userMorse))
    alphaList = []
    for i in userMorse:
        alphaElement = morseToAlpha(i)
        alphaList.append(alphaElement)
    print("Alpha List: " + str(alphaList))

    #Logic
    print(" ")
    if all(elem in shell for elem in alphaList):
        print("Word was: Shell")
        print("Input 3.505 MHz")
        return
    elif all(elem in halls for elem in alphaList):
        print("Word was: Halls")
        print("Input 3.515 MHz")
        return
    elif all(elem in slick for elem in alphaList):
        print("Word was: Slick")
        print("Input 3.522 MHz")
        return	
    elif all(elem in trick for elem in alphaList):
        print("Word was: Trick")
        print("Input 3.532 MHz")
        return
    elif all(elem in boxes for elem in alphaList):
        print("Word was: Boxes")
        print("Input 3.535 MHz")
        return
    elif all(elem in leaks for elem in alphaList):
        print("Word was: Leaks")
        print("Input 3.542 MHz")
        return
    elif all(elem in strobe for elem in alphaList):
        print("Word was: Strobe")
        print("Input 3.545 MHz")
        return
    elif all(elem in bistro for elem in alphaList):
        print("Word was: Bistro")
        print("Input 3.552 MHz")
        return
    elif all(elem in flick for elem in alphaList):
        print("Word was: Flick")
        print("Input 3.555 MHz")
        return
    elif all(elem in bombs for elem in alphaList):
        print("Word was: Bombs")
        print("Input 3.565 MHz")
        return
    elif all(elem in bbreak for elem in alphaList):
        print("Word was: Break")
        print("Input 3.572 MHz")
        return
    elif all(elem in brick for elem in alphaList):
        print("Word was: Brick")
        print("Input 3.575 MHz")
        return
    elif all(elem in steak for elem in alphaList):
        print("Word was: Steak")
        print("Input 3.582 MHz")
        return
    elif all(elem in sting for elem in alphaList):
        print("Word was: Sting")
        print("Input 3.592 MHz")
        return
    elif all(elem in vector for elem in alphaList):
        print("Word was: Vector")
        print("Input 3.595 MHz")
        return
    elif all(elem in beats for elem in alphaList):
        print("Word was: Beats")
        print("Input 3.600 MHz")
        return
    else:
        print("Error. Invalid/Incomplete morse input. Resetting")
        return

#Complicated Wires (input x4 -> output, loop until complete)
def compWires():

    #Def Vars
    global serialNum
    global batteries
    global parallelPort

    blueList = "EMPTY"
    redList = "EMPTY"
    ledList = "EMPTY"
    starList = "EMPTY"

    # Input Logic
    ledList = str(input("What wires have an LED above them? (as a binary list): "))
    if ledList == "...": # Exit Command
        print("Exit Command Detected. Exiting...")
        ledList = "EMPTY"
        return
    blueList = str(input("What wires have blue coloring? (as a binary list): "))
    if blueList == "...": # Exit Command
        print("Exit Command Detected. Exiting...")
        blueList = "EMPTY"
        return
    redList = str(input("What wires have red coloring? (as a binary list): "))
    if redList == "...": # Exit Command
        print("Exit Command Detected. Exiting...")
        redlist = "EMPTY"
        return
    starList = str(input("What wires have a star beneath them? (as a binary list): "))
    if starList == "...": # Exit Command
        print("Exit Command Detected. Exiting...")
        starList = "EMPTY"
        return

    blueList = [x for x in blueList]
    redList = [x for x in redList]
    ledList = [x for x in ledList]
    starList = [x for x in starList]

    # Length Error Check
    if len(blueList) != len(redList):
        print("Error. Number of wires inconsistant across inputs. Resetting.")
        return
    if len(blueList) != len(ledList):
        print("Error. Number of wires inconsistant across inputs. Resetting.")
        return
    if len(blueList) != len(starList):
        print("Error. Number of wires inconsistant across inputs. Resetting.")
        return

    # Contents Error Check
    for i in (blueList+redList+ledList+starList):
        if i == "1":
            pass
        elif i == "0":
            pass
        else:
            print("Error. Invalid binary input ,'" + str(i) + "'. Resetting.")
            return


    # Determine-Instruction Logic
    for n in range(0,2): #It runs twice to compensate for mid-loop questions about bomb details
        if n == 1:
            print(" ")
        instruction = "EMPTY"
        for i in range(0,len(blueList)):
            colBlu = False
            colRed = False
            wireLED = False
            hasStar = False

            if blueList[i] == "1":
                colBlu = True
            if redList[i] == "1":
                colRed = True
            if ledList[i] == "1":
                wireLED = True
            if starList[i] == "1":
                hasStar = True


            if colBlu:
                if colRed:
                    if wireLED:
                        if hasStar:
                             instruction = "D"
                        else:
                             instruction = "S"
                    else:
                        if hasStar:
                             instruction = "P"
                        else:
                             instruction = "S"
                else:
                    if wireLED:
                        instruction = "P"
                    else:
                        if hasStar:
                             instruction = "D"
                        else:
                             instruction = "S"
            elif colRed:
                if wireLED:
                    instruction = "B"
                else:
                    if hasStar:
                        instruction = "C"
                    else:
                        instruction = "S"
            elif wireLED:
                if hasStar:
                    instruction = "B"
                else:
                    instruction = "D"
            elif hasStar:
                instruction = "C"
            else:
                instruction = "C"

            #Output Logic
            match (instruction):
                case ("C"): 
                    if n == 1:
                        print("Wire " + str(i+1) + ") Cut")
                case ("D"):
                    if n == 1:
                        print("Wire " + str(i+1) + ") Do Not Cut")
                case ("S"): 
                    if serialNum == "EMPTY":
                        print(" ")
                        serialNum = str(input("Last Digit of Serial: "))
                        if serialNum == "...": # Exit Command
                            print("Exit Command Detected. Exiting...")
                            serialNum = "EMPTY"
                            return
                        if serialNum in ["0","1","2","3","4","5","6","7","8","9"]:
                            serialNum = int(serialNum)
                        else:
                            print("Error. Invalid serial digit, '" + str(serialNum) + "'. Resetting.")
                            serialNum = "EMPTY"
                            return
                    if serialNum%2 == 0:
                        if n == 1:
                            print("Wire " + str(i+1) + ") Cut")
                    else:
                        if n == 1:
                            print("Wire " + str(i+1) + ") Do Not Cut")
                case ("P"):
                    if parallelPort == "EMPTY":
                        print(" ")
                        if str(input("Does the bomb have a parallel port (y/n)?: ")) == "y":
                            parallelPort = True
                        else:
                            parallelPort = False
                    if parallelPort == True:
                        if n == 1:
                            print("Wire " + str(i+1) + ") Cut")
                    else:
                        if n == 1:
                            print("Wire " + str(i+1) + ") Do Not Cut")
                case ("B"):
                    if batteries == "EMPTY":
                        print(" ")
                        batteries = str(input("How many batteries are on the bomb?: "))
                        if batteries == "...": # Exit Command
                            print("Exit Command Detected. Exiting...")
                            batteries = "EMPTY"
                            return
                        if batteries in ["0","1","2","3","4","5","6","7","8","9","10"]:
                            batteries = int(batteries)
                        else:
                            print("Error. Invalid number of batteries, '" + str(batteries) + "'. Resetting")
                            batteries = "EMPTY"
                            return
                    if batteries >= 2:
                        if n == 1:
                            print("Wire " + str(i+1) + ") Cut")
                    else:
                        if n == 1:
                            print("Wire " + str(i+1) + ") Do Not Cut")
                case other:
                    print("Error. Something went so wrong, I don't know what happened. Resetting.")
                    return

#Wire Sequences (inputx1 -> outputx1, loop 4 repeats)
def wireSeq():
    rOcc = 0
    bluOcc = 0
    blaOcc = 0
    for i in range(0,4):
        #Def Vars
        inputSuccess = [False, False, False]
        while (False in inputSuccess):
            inputSuccess = [False, False, False]
            wiresList = []
            wires = []
            wireUn = str(input("What is the wire color and letter of each wire on panel " + str(i+1) + " from top to bottom? (r,blu,bla>A,B,C;)(if there is no wire in a slot, use blank) : "))
            if wireUn == "...": # Exit Command
                print("Exit Command Detected. Exiting...")
                wireUn = "EMPTY"
                return
            wiresList = wireUn.split(";")

            if len(wiresList) != 3: #Testing length
                print("Error. Invalid number of inputs, '" + str(len(wiresList)) + "'. Try Again")
                print(" ")
                continue

            uCount = -1
            for u in wiresList: #Testing each "color>endpoint"S
                uCount = uCount + 1

                testList = []
                if u == "blank":
                    inputSuccess[uCount] = True
                    continue
                testList = u.split(">")

                colorSuccess = False
                endpointSuccess = False
                match testList[0]: #Testing color
                    case("r"): colorSuccess = True
                    case("blu"): colorSuccess = True
                    case("bla"): colorSuccess = True
                    case other:
                        print("Error. Invalid color, '" + str(testList[0]) + "'. Try again")
                        print(" ")
                match testList[1]: #Testing Endpoint
                    case("A"): endpointSuccess = True
                    case("B"): endpointSuccess = True
                    case("C"): endpointSuccess = True
                    case other:
                        print("Error. Invalid Endpoint, '" + str(testList[1]) + "'. Try again")
                        print(" ")

                if colorSuccess and endpointSuccess: #Are both Color and Endpoint good?
                    inputSuccess[uCount] = True

            # wiresList[wiresList.index("blank")] = "_>_"
        # Splits the wiresList into individual details. 0,2,4 are colors and 1,3,5 are endpoints
        for w in wiresList:
            workingList = []
            if w == "blank":
                workingList = ["_","_"]
            else:
                workingList = w.split(">")
            wires = wires + workingList
            


        #Occurance Logic
        print(" ")
        dCount = 0
        wCount = 0
        for d in wires:
            if (dCount%2 == 0): #Evens Colors
                wCount += 1
                match (d): #Testing Color of current wire
                    case ("r"): #Wire is RED
                        rOcc += 1
                        match (wires[dCount + 1]): #Testing endpoint of RED wire
                            case ("A"):
                                if rOcc in [3,4,6,7,8]:
                                    print("Wire "+str(wCount) + ": "+str(wiresList[wCount-1]) + ") Cut")
                                else:
                                    print("Wire "+str(wCount) + ": "+str(wiresList[wCount-1]) + ") Do NOT Cut")
                            case ("B"):
                                if rOcc in [2,5,7,8,9]:
                                    print("Wire "+str(wCount) + ": "+str(wiresList[wCount-1]) + ") Cut")
                                else:
                                    print("Wire "+str(wCount) + ": "+str(wiresList[wCount-1]) + ") Do NOT Cut")
                            case ("C"):
                                if rOcc in [1,4,6,7]:
                                    print("Wire "+str(wCount) + ": "+str(wiresList[wCount-1]) + ") Cut")
                                else:
                                    print("Wire "+str(wCount) + ": "+str(wiresList[wCount-1]) + ") Do NOT Cut")

                    case ("blu"): #Wire is BLUE
                        bluOcc += 1
                        match (wires[dCount + 1]): #Testing endpoint of BLUE wire
                            case ("A"):
                                if bluOcc in [2,4,8,9]:
                                    print("Wire "+str(wCount) + ": "+str(wiresList[wCount-1]) + ") Cut")
                                else:
                                    print("Wire "+str(wCount) + ": "+str(wiresList[wCount-1]) + ") Do NOT Cut")
                            case ("B"):
                                if bluOcc in [1,3,5,6]:
                                    print("Wire "+str(wCount) + ": "+str(wiresList[wCount-1]) + ") Cut")
                                else:
                                    print("Wire "+str(wCount) + ": "+str(wiresList[wCount-1]) + ") Do NOT Cut")
                            case ("C"):
                                if bluOcc in [2,6,7,8]:
                                    print("Wire "+str(wCount) + ": "+str(wiresList[wCount-1]) + ") Cut")
                                else:
                                    print("Wire "+str(wCount) + ": "+str(wiresList[wCount-1]) + ") Do NOT Cut")

                    case ("bla"): #Wire is BLACK
                        blaOcc += 1
                        match (wires[dCount + 1]): #Testing endpoint of BLACK wire
                            case ("A"):
                                if blaOcc in [1,2,4,7]:
                                    print("Wire "+str(wCount) + ": "+str(wiresList[wCount-1]) + ") Cut")
                                else:
                                    print("Wire "+str(wCount) + ": "+str(wiresList[wCount-1]) + ") Do NOT Cut")
                            case ("B"):
                                if blaOcc in [1,3,5,6,7]:
                                    print("Wire "+str(wCount) + ": "+str(wiresList[wCount-1]) + ") Cut")
                                else:
                                    print("Wire "+str(wCount) + ": "+str(wiresList[wCount-1]) + ") Do NOT Cut")
                            case ("C"):
                                if blaOcc in [1,2,4,6,8,9]:
                                    print("Wire "+str(wCount) + ": "+str(wiresList[wCount-1]) + ") Cut")
                                else:
                                    print("Wire "+str(wCount) + ": "+str(wiresList[wCount-1]) + ") Do NOT Cut")
                    case("_"): #Blank Slot
                        print("Wire " + str(wCount)+": No wire, ignore")
            dCount += 1
        print(" ")

#Passwords
def password():
    #Defining List Vars
    allWords = ["about","after","again","below","could",
                "every","first","found","great","house",
                "large","learn","never","other","place",
                "plant","point","right","small","sound",
                "spell","still","study","their","there",
                "these","thing","think","three","water",
                "where","which","world","would","write"] #Every word that the module is aware of
    removedWords = [] #Any words that are impossible to input (reset after each display)
    possibleWords = allWords #Any words that are currently possible to try (reduced after each display)

    #Testing letters in each display
    for d in [0,1,2,3,4]:
        if len(possibleWords) == 1: #If there is one possible words left, print it
                print(" ")
                print("Input the word " + str(possibleWords) + " into the module")
                return

        #Getting the possible letters for display d
        testLetters = "EMPTY"
        testLetters = str(input("Please list all 6 possible letters in display " + str(d+1) + ": "))
        if testLetters == "...":
            print("Exit Command Detected. Exiting")
            testLetters = "EMPTY"
            return

        testLetters = [x for x in testLetters]
        if len(testLetters) != 6:
            print("Error. Invalid number of letters ,'" + str(len(testLetters)) + "'. Resetting")
            return
        for t in testLetters:
            if t not in ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]:
                print("Error. Invalid letter, '" + str(t) + "'. Resetting")
                return

        #Testing the letters possible against the possible words remaining
        testingWord = "EMPTY"
        for testingWord in possibleWords:
            testingWordLetters = [x for x in testingWord]

            if testingWordLetters[d] in testLetters:
                pass
            else:
                removedWords.append(testingWord)

        #Removing any impossible words from the list of test words
        for r in removedWords:
            possibleWords.remove(r)
        removedWords = []
        print("Number of possible words remaining: " + str(len(possibleWords)))
    
    #No words matched the list
    print("Error. No words possible from inputs. Resetting")
    return

#Intro
print(" ")
print(" /$$   /$$ /$$$$$$$$ /$$$$$$  /$$   /$$ /$$$$$$$$                                           /$$    ")
print("| $$  /$$/|__  $$__//$$__  $$| $$$ | $$| $$_____/                                          | $$    ")
print("| $$ /$$/    | $$  | $$  \ $$| $$$$| $$| $$       /$$   /$$  /$$$$$$   /$$$$$$   /$$$$$$  /$$$$$$  ")
print("| $$$$$/     | $$  | $$$$$$$$| $$ $$ $$| $$$$$   |  $$ /$$/ /$$__  $$ /$$__  $$ /$$__  $$|_  $$_/  ")
print("| $$  $$     | $$  | $$__  $$| $$  $$$$| $$__/    \  $$$$/ | $$  \ $$| $$$$$$$$| $$  \__/  | $$    ")
print("| $$\  $$    | $$  | $$  | $$| $$\  $$$| $$        >$$  $$ | $$  | $$| $$_____/| $$        | $$ /$$")
print("| $$ \  $$   | $$  | $$  | $$| $$ \  $$| $$$$$$$$ /$$/\  $$| $$$$$$$/|  $$$$$$$| $$        |  $$$$/")
print("|__/  \__/   |__/  |__/  |__/|__/  \__/|________/|__/  \__/| $$____/  \_______/|__/         \___/  ")
print("                                                           | $$                                    ")
print("                                                           | $$                                    ")
print("                                                           |__/                                    ")
print(" ")

print("KTANExpert by Reese Ford")
print("For specific instructions, visit https://github.com/RicePerson/KTANExpert#readme")
print("In case you haven't launched the game before, the verification code as of 10/9/2022 is 241")

#Module Loop
os.startfile("needymodules.exe")
while isDoing:
    #checking which module you are currently working on
    print(" ")
    module = input("Module? (w/b/k/s/who/m/mO/cW/wS/p/resetbomb/done): ")
    match module:
        case "w":
            print(" ")
            wires()
        case "b":
            print(" ")
            button()
        case "k":
            print(" ")
            keypad()
        case "s":
            print(" ")
            newnewSimon()
        case "who":
            print(" ")
            whofirst()
        case "m":
            print(" ")
            memory()
        case "mO":
            print(" ")
            morse()
        case "cW":
            print(" ")
            compWires()
        case "wS":
            print(" ")
            wireSeq()
        case "p":
            print(" ")
            password()
        case "resetbomb":
            serialNum = "EMPTY"
            batteries = "EMPTY"
            litIndicators = []
            parallelPort = "EMPTY"
            vowel = "EMPTY"
            print("Bomb Reset. All bomb-wide varaible are now empty")
        case "done":
            print(" ")
            print("Bomb Complete. Congrats Defuser")
            isDoing = False
        case other:
            print("Please enter a valid module")
            isDoing = True



# The wasteland (A place for commented out code that could be usefull later...)

#def simon():
#    #Logic (It's a loop)
#    vowel = str(input("Vowel in Serial? (y/n): "))
#    isDoing = True

#    while isDoing == True:
#        if vowel == "y":
#            strikes = str(input("Number Of Strikes? (0/1/2): "))
#            if strikes == "...": # Exit Command
#                print("Exit Command Detected. Exiting...")
#                strikes = "EMPTY"
#                return
#            while strikes == "0":
#                user = "EMPTY"
#                flashSeq = []
#                finalSimon = []
#                flash = 1
#                print(" ")
                
#                inputSuccess = False
#                user = str(input("What color is flash " + str(flash) +"? (r/blu/y/g): "))
#                match user:
#                    case("r"): 
#                        flashSeq.append("r")
#                        inputSuccess = True
#                    case("blu"): 
#                        flashSeq.append("blu")
#                        inputSuccess = True
#                    case("y"): 
#                        flashSeq.append("y")
#                        inputSuccess = True
#                    case("g"): 
#                        flashSeq.append("g")
#                        inputSuccess = True
#                    case other: 
#                        print("Error. Invalid color. Please try again")
#                        inputSuccess = False
#                        pass
                    
#                for i in flashSeq:
#                    case("r")
#                print(" ")
#                #print("Input: " + str(finalSimon))
#                print("Click these buttons in order:")
#                for f in finalSimon:
#                    match f:
#                        case "r":print("Red")
#                        case "y":print("Yellow")
#                        case "g":print("Green")
#                        case "blu":print("Blue")
#                        case other: return
#                print(" ")

#            while strikes == "1":
#                user = []
#                finalSimon = []
#                flash = 1
#                print(" ")
#                while True:
#                    userInput = str(input("What is flash " + str(flash) +
#                                      "? (r/blu/g/y/end/done):"))
#                    if userInput == "...": # Exit Command
#                        print("Exit Command Detected. Exiting...")
#                        userInput = "EMPTY"
#                        return
#                    if userInput == "r":
#                        user.append("r")
#                        flash += 1
#                    elif userInput == "blu":
#                        user.append("blu")
#                        flash += 1
#                    elif userInput == "g":
#                        user.append("g")
#                        flash += 1
#                    elif userInput == "y":
#                        user.append("y")
#                        flash += 1
#                    elif userInput == "done":
#                        isDoing = False
#                        return

#                    if userInput == "end":
#                        print("Currently flashing: " + str(user))
#                        break
                
#                for i in user:
#                    if i == "r":
#                        finalSimon.append("y")
#                    elif i == "blu":
#                        finalSimon.append("g")
#                    elif i == "g":
#                        finalSimon.append("blu")
#                    elif i == "y":
#                        finalSimon.append("r")
#                    elif i == "end":
#                        pass
#                    else:
#                        print("How?")
#                        return
#                print(" ")
#                #print("Input: " + str(finalSimon))
#                print("Click these buttons in order:")
#                for f in finalSimon:
#                    match f:
#                        case "r":print("Red")
#                        case "y":print("Yellow")
#                        case "g":print("Green")
#                        case "blu":print("Blue")
#                        case other: return
#                print(" ")

#            while strikes == "2":
#                user = []
#                finalSimon = []
#                flash = 1
#                print(" ")
#                while True:
#                    userInput = str(input("What is flash " + str(flash) +
#                                      "? (r/blu/g/y/end/done):"))
#                    if userInput == "...": # Exit Command
#                        print("Exit Command Detected. Exiting...")
#                        userInput = "EMPTY"
#                        return
#                    if userInput == "r":
#                        user.append("r")
#                        flash += 1
#                    elif userInput == "blu":
#                        user.append("blu")
#                        flash += 1
#                    elif userInput == "g":
#                        user.append("g")
#                        flash += 1
#                    elif userInput == "y":
#                        user.append("y")
#                        flash += 1
#                    elif userInput == "done":
#                        isDoing = False
#                        return

#                    if userInput == "end":
#                        print("Currently flashing: " + str(user))
#                        break
                
#                for i in user:
#                    if i == "r":
#                        finalSimon.append("g")
#                    elif i == "blu":
#                        finalSimon.append("r")
#                    elif i == "g":
#                        finalSimon.append("y")
#                    elif i == "y":
#                        finalSimon.append("blu")
#                    elif i == "end":
#                        pass
#                    else:
#                        print("How?")
#                        return
#                print(" ")
#                #print("Input: " + str(finalSimon))
#                print("Click these buttons in order:")
#                for f in finalSimon:
#                    match f:
#                        case "r":print("Red")
#                        case "y":print("Yellow")
#                        case "g":print("Green")
#                        case "blu":print("Blue")
#                        case other: return
#                print(" ")

#        elif vowel == "n":
#            strikes = str(input("Number Of Strikes? (0/1/2): "))
#            if strikes == "...": # Exit Command
#                print("Exit Command Detected. Exiting...")
#                strikes = "EMPTY"
#                return
#            while strikes == "0":
#                user = []
#                finalSimon = []
#                flash = 1
#                print(" ")
#                while True:
#                    userInput = str(input("What is flash " + str(flash) +
#                                      "? (r/blu/g/y/end/done):"))
#                    if userInput == "...": # Exit Command
#                        print("Exit Command Detected. Exiting...")
#                        userInput = "EMPTY"
#                        return
#                    if userInput == "r":
#                        user.append("r")
#                        flash += 1
#                    elif userInput == "blu":
#                        user.append("blu")
#                        flash += 1
#                    elif userInput == "g":
#                        user.append("g")
#                        flash += 1
#                    elif userInput == "y":
#                        user.append("y")
#                        flash += 1
#                    elif userInput == "done":
#                        isDoing = False
#                        return

#                    if userInput == "end":
#                        print("Currently flashing: " + str(user))
#                        break
                
#                for i in user:
#                    if i == "r":
#                        finalSimon.append("blu")
#                    elif i == "blu":
#                        finalSimon.append("y")
#                    elif i == "g":
#                        finalSimon.append("g")
#                    elif i == "y":
#                        finalSimon.append("r")
#                    elif i == "end":
#                        pass
#                    else:
#                        print("How?")
#                        return
#                print(" ")
#                #print("Input: " + str(finalSimon))
#                print("Click these buttons in order:")
#                for f in finalSimon:
#                    match f:
#                        case "r":print("Red")
#                        case "y":print("Yellow")
#                        case "g":print("Green")
#                        case "blu":print("Blue")
#                        case other: return
#                print(" ")

#            while strikes == "1":
#                user = []
#                finalSimon = []
#                flash = 1
#                print(" ")
#                while True:
#                    userInput = str(input("What is flash " + str(flash) +
#                                      "? (r/blu/g/y/end/done):"))
#                    if userInput == "...": # Exit Command
#                        print("Exit Command Detected. Exiting...")
#                        userInput = "EMPTY"
#                        return
#                    if userInput == "r":
#                        user.append("r")
#                        flash += 1
#                    elif userInput == "blu":
#                        user.append("blu")
#                        flash += 1
#                    elif userInput == "g":
#                        user.append("g")
#                        flash += 1
#                    elif userInput == "y":
#                        user.append("y")
#                        flash += 1
#                    elif userInput == "done":
#                        isDoing = False
#                        return

#                    if userInput == "end":
#                        print("Currently flashing: " + str(user))
#                        break
                
#                for i in user:
#                    if i == "r":
#                        finalSimon.append("r")
#                    elif i == "blu":
#                        finalSimon.append("blu")
#                    elif i == "g":
#                        finalSimon.append("y")
#                    elif i == "y":
#                        finalSimon.append("g")
#                    elif i == "end":
#                        pass
#                    else:
#                        print("How?")
#                        return
#                print(" ")
#                #print("Input: " + str(finalSimon))
#                print("Click these buttons in order:")
#                for f in finalSimon:
#                    match f:
#                        case "r":print("Red")
#                        case "y":print("Yellow")
#                        case "g":print("Green")
#                        case "blu":print("Blue")
#                        case other: return
#                print(" ")

#            while strikes == "2":
#                user = []
#                finalSimon = []
#                flash = 1
#                print(" ")
#                while True:
#                    userInput = str(input("What is flash " + str(flash) +
#                                      "? (r/blu/g/y/end/done):"))
#                    if userInput == "...": # Exit Command
#                        print("Exit Command Detected. Exiting...")
#                        userInput = "EMPTY"
#                        return
#                    if userInput == "r":
#                        user.append("r")
#                        flash += 1
#                    elif userInput == "blu":
#                        user.append("blu")
#                        flash += 1
#                    elif userInput == "g":
#                        user.append("g")
#                        flash += 1
#                    elif userInput == "y":
#                        user.append("y")
#                        flash += 1
#                    elif userInput == "done":
#                        isDoing = False
#                        return

#                    if userInput == "end":
#                        print("Currently flashing: " + str(user))
#                        break
                
#                for i in user:
#                    if i == "r":
#                        finalSimon.append("y")
#                    elif i == "blu":
#                        finalSimon.append("g")
#                    elif i == "g":
#                        finalSimon.append("blu")
#                    elif i == "y":
#                        finalSimon.append("r")
#                    elif i == "end":
#                        pass
#                    else:
#                        print("How?")
#                        return
#                print(" ")
#                #print("Input: " + str(finalSimon))
#                print("Click these buttons in order:")
#                for f in finalSimon:
#                    match f:
#                        case "r":print("Red")
#                        case "y":print("Yellow")
#                        case "g":print("Green")
#                        case "blu":print("Blue")
#                        case other: return
#                print(" ")

#    print("Error. You input incorrectly. Please try again")
#    return #Pre Issue 80 / Not used anymore
# Reese Ford
