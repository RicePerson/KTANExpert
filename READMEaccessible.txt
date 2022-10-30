
 /$$   /$$ /$$$$$$$$ /$$$$$$  /$$   /$$ /$$$$$$$$                                           /$$    
| $$  /$$/|__  $$__//$$__  $$| $$$ | $$| $$_____/                                          | $$    
| $$ /$$/    | $$  | $$  \ $$| $$$$| $$| $$       /$$   /$$  /$$$$$$   /$$$$$$   /$$$$$$  /$$$$$$  
| $$$$$/     | $$  | $$$$$$$$| $$ $$ $$| $$$$$   |  $$ /$$/ /$$__  $$ /$$__  $$ /$$__  $$|_  $$_/  
| $$  $$     | $$  | $$__  $$| $$  $$$$| $$__/    \  $$$$/ | $$  \ $$| $$$$$$$$| $$  \__/  | $$    
| $$\  $$    | $$  | $$  | $$| $$\  $$$| $$        >$$  $$ | $$  | $$| $$_____/| $$        | $$ /$$
| $$ \  $$   | $$  | $$  | $$| $$ \  $$| $$$$$$$$ /$$/\  $$| $$$$$$$/|  $$$$$$$| $$        |  $$$$/
|__/  \__/   |__/  |__/  |__/|__/  \__/|________/|__/  \__/| $$____/  \_______/|__/         \___/  
                                                           | $$                                    
                                                           | $$                                    
                                                           |__/                                    

# KTANExpert
A Python BombManual Expert for the game, Keep Talking and Nobody Explodes
It's not done yet. As of right now, it only does:
* Wires
* Button
* Keypad
* Simon Says
* Who's On First
* Memory
* Morse-Code
* Complicated Wires
* Wire Sequences
* Passwords

(For more information on modules, visit bombmanual.com)

# TO INSTALL:
Download the KTANExpertV1.0 archive, extract both executables in the archive, and run KTANExpert.exe
Two windows will open, one titled "KTANExpert by Reese Ford"
And one titled "NeedyModule Sub-Expert"
The KTANExpert handles regular modules, while the Sub-Expert handles needy modules
Needy Modules have little timers at the top of them, and are covered at the bottom of this ReadMe, or at https://github.com/RicePerson/KTANExpert/wiki/Needy-Modules

# Module Instructions

## How to read these instructions
For every completed module in this Expert, there are accompanying instructions on how to properly input details and comply with instructions.
Every module has a description with basic instructions, as well as an example with real-world modules with what the player enters and what the expert outputs
Anything that will be entered into the Expert or will be output by the expert will be surrounded in back-ticks, like `this`.
To enter a module, type the module code that follows the name in these instructions when the expert asks Module? (*possible things to enter*):

### Glossary
There are some words used in these instructions that may mean something other than what common sense would infer. Here is what those words mean.
- KTANE Module: A module on the bomb in Keep Talking and Nobody Explodes
- The Expert: The program this README accompanies
- Player: You!
- Repeat: Some modules require that you do the module a few times, each with differing details. Each time you do the module is a Repeat
- Command Window: The window that you enter inputs into
- Input(s): Things the Player will type into the command window, then press ENTER
- Output(s): Things the Expert will tell the Player in the command window
- ENTER: Represents pressing the Enter Key

### Codes
There are short-hand codes used throughout to make inputs generally faster. Here they are
| Shorthand | What it means|
|-----------|--------------|
|   KTANE   | Keep Talking and Nobody Explodes |
|     y     | Yes |
|     n     | No |
|     r     | Red |
|    blu    | Blue |
|    bla    | Black |
|     w     | White |
|     y     | Yellow |
|     g     | Green |

### Inputting Answers to Questions
The Expert will ask questions. That's how this game works. 
When inputting answers, you must follow some rules so that the expert can understand what you are saying.
1) Everything is lowercase unless otherwise instructed (as of right now, the only uppercase inputs are the endpoints for the Wire Sequences module and the lit indicators in the Buttons module)
2) Separate details with a semicolon (;). Some modules have multiple inputs (like multiple keys or wires). Seperate these using a semicolon, with the exception to Morse-Code, which uses spaces
3) Only use spaces in words with spaces in them. As of right now, the only modules to use spaces are Who's on First (some words have spaces in them) and Morse-Code (the letters are separated by spaces)

### Resetting
At any point, `...` can be entered into the expert to reset that module and return to the module selection screen. 
Doing this will reset all the variables in that module, and will require you to restart that module if you do it later.
This will not reset bomb-wide variables like the serial number, number of batteries, etc. To reset these, type `resetbomb` into the module selection screen.


## Wires `w`
Select the number of wires present in the module (including cut wires from previous attempts).
Enter each wire color from the top (which is considered the first wire in the expert) to the bottom.
Follow the given instructions.

### Example:
0) KTANE gives you a wire module that goes:
- Empty
- RED 
- RED  
- Empty 
- BLUE 
- WHITE 

1) The Player inputs `4` as the wire number, 
2) The Expert asks `Wire 1? (r/y/blu/bla/r): `
3) The Player then inputs `r` ENTER `r` ENTER `blu` ENTER `w`
4) The Expert then asks `Last Digit of Serial: `
5) The Player checks the bomb for a serial number sticker, then inputs what the last digit is, which in the case of this example, is `3`
6) The Expert asks you to `Cut the last RED wire`, which prompts the player to cut the 3rd wire. *Module Complete, move on to the next one.* 


## Button `b`
This module just consists of a large button that has some text on it. To start, don't listen to it's lies. 
Sometimes you have to just click "hold" or hold down "press". When you enter the module in the expert, it will first ask you for a color. 
It will always ask this question. Once you enter the color, there are a couple different questions the expert may ask. 
Things like "What is the last digit of the serial number?" or "What does the button say?". Just answer the question. 
These bomb-wide details are shared across modules in the expert, so if you do another button, it won't ask you a question you have already answered. 
If it does, that's because that detail may change between modules, so just answer it. 
Keep answering the questions until it gives you an instruction. It will either ask you to press and immediately release the button.
Or to start holding the button and enter the color of the strip directly to the right of the button. The strip will only light up when holding the button,
and will light up even if you aren't supposed to hold it, so don't skip ahead. If holding, hold down the button and enter the color into the expert WITHOUT
letting go of the button. It will then give you an instruction like `Release when the countdown timer has a 4 in any position`. This just means if there is
a four on the countdown display, release the button. If not, wait.

### Example:
0) KTANE gives you a blue button with the word detonate on it
1) The Player selects the Button module with `b`
2) The Expert asks `What is the color of the button?`
3) The Player enters `blu` and presses ENTER.
4) The Expert asks `What does the button say?`
5) The Player enters `detonate` and presses ENTER.
6) The Expert asks `How many batteries are on the bomb?`
7) The Player, after looking around the bomb's edge, enters '1'
8) The Expert instructs the player to `Press and hold the button`
9) The Player starts holding the button, and sees a red strip directly to the right of it
10) The Player enters `r` for the strip color
11) The Expert tells the player to `Release the button when the countdown timer has a 1 in any position`
12) The Player complys. *Module Complete, move on to the next one.* 

## Keypad `k`
Once you enter the keypad module in the expert, it will list all possible keypad symbols, and then ask for the first one.
It does not matter what order you input the key's, only that you enter all four, one after another.
Find the symbol name from the list provided that most-closly matches the symbol in KTANE, and enter it, pressing ENTER after each symbol
Repeat until provivded a Final List. Enter these in order to complete the module

### Example:
0) The module in KTANE has an omega, ae, trident, and squished 6
1) The Player selects the keypad module with `k`
2) The Expert asks for a list of keys
3) The Player inputs `omega;ae;trident;6`
4) The Expert will then output `Click these buttons in order: 1)6 2)ae 3)trident 4)omega`
5) The Player clicks these inorder in KTANE. *Module Complete, move on to the next one.*


## Simon Says `s`
This can be considered the worst game of simon says, because you don't repeat it back exactly as it is presented to you.
Once the simon says module is selected in the expert (selected by `s`), it will ask a couple of preliminary questions about the bomb, which will determine which lookup-table it will use.
After answering these questions, watch the KTANE module for its flash sequence. The module will flash relatively quickly, and then repeat the sequence after a long pause.
When the expert asks for the flash color, only enter the last flash. The expert will remember the previous flashes. 
At every stage, the expert will output the full sequence to click. Click the colored buttons in the given order.
Repeat until the module is complete. To exit the module on the expert, input `done` at any step.

### Example:
0) The bomb has a vowel, and is sitting at one strike. The red button is currently flashing red slowly.
1) The Player selects the simon says module with `s`
2) The Expert asks if there is a vowel in the serial number, and then if there are any strikes
3) The Player answers `y` ENTER `1`
4) The Expert asks for button flash
5) The Player enters `r`
6) Expert outputs `Click these buttons in order: Yellow`
7) Player clicks the yellow button in KTANE
8) Repeat until module is complete, then Player:red_circle: inputs `done` into the expert:large_blue_circle:. *Module Complete, move on to the next one.*

Note: If for some reason, after clicking a colored button, it markes it as wrong and gives you a strike, 
enter `done` into the expert and start the module over, as the current number of strikes affects the module.


## Who's on First `who`
This module consists of seven words, six of them being on buttons. It also has a indicator with 3 lights telling us there are 3 repeats for this module
Based on what the display words is, the expert determines the position of the what I'm calling "The display's sacred button word". This word determines what happens in the next step.
Because this module was designed to make the user click the wrong button if they don't follow both sections of the manual, I have reduced this module down to a single input per repeat.
You're Welcome. Inputing to this module works by typing each word on the module in a specific order, seperated by a semicolon.
The order goes like this: 

`DisplayWord;TopLeft;MiddleLeft;BottomLeft;TopRight;MiddleRight;BottomRight`

It is imperative that the words are entered in this order, or the module will give you a wrong instruction.
Also, the display word can sometimes be, well, nothing. The display will be blank. In this case, pretend the word is `*blank*`

### Example:
*0) The KTANE module looks like this:*
|First|<- Display|
|-----|----------|
| Okay|  Middle  |
|Ready|  Blank   |
| Next|   Uhhh   |

1) The Player selects the Who's on First module using `who`
2) The Expert asks for the words on the current repeat of the module, starting with the display.
3) The Player enters `first;okay;ready;next;middle;blank;uhhh`
4) The Expert tells the player to `Press the button labeled blank` and asks if the module is complete
5) The Player clicks the button "blank" and answers `n`
6) The Player repeats this until the module is complete, then answers `y` to the experts exit question
7) *Module Complete, move on to the next one.*


## Memory `m`
This module consists of a display with a single digit and four buttons with numbers 1-4 on them, in an order that changes after every repeat, of which there are five.
This is a back-and-forth with the expert, and is fairly straightforward. At every repeat, input the numbers in the order: Display first-button second-button third-button fourth-button
The expert will then output some debug information, alongside an instruction, in the form of `Press the button labeled  #`. Follow this instruction.
Repeat until the module is complete. If you ever mess up, the KTANE module will reset back to stage one. To reset the expert, input `r` at any step.

### Example:
0) The KTANE module starts with the display being 4 and the buttons being, from left to right, 1 3 2 4
1) The Player enters the memory module with `m`
1) The Expert asks for the stage 1 numbers 
2) The Player inputs `4;1;3;2;4`
3) The Expert gives the instruction `Press the button labeled 4`. The Player complys. The numbers on the KTANE module change
4) Repeat 1 and 2 until the module is complete. *Module Complete, move on to the next one.* 


## Morse-Code `mO`
Enter the morse code as it is flashed to you in the module. 
If you don't know about Morse-Code, here's a little summary. MorseCode is a standard way of communicating used by the military that can use light or sound.

|MorseCode|Meaning|
|---------|-------|
|.        |Dot    |
|-        |Dash   |
|Short Space|Space between Morse Characters|
|Longer Space|Space between Letters|
|Really Long Space|Space Between Words / Repeating Message|

This module requires that you type the morse code, and then based on what the flashing word is, input a specific frequency and click TX.
The Expert doesn't care at which point in the word you start entering characters, just that you don't repeat characters. If you think you repeated characters, don't worry.
When you input the morse, the Expert will tell you what you just entered in english letters, so you can see what you repeated so you can rerun the module and try again.

### Example:
0) KTANE module is flashing `..`  `-.-.`  `-.-` `LongSpace` `-`  `.-.`  `..`  `-.-.`  `-.-` `LongSpace` `-`  `.-.`  **`..`  `-.-.`  `-.-` `LongSpace` `-`  `.-.`**  `..`  `-.-.`  `-.-`  repeating indefinitely
1) The Player enters the MorseCode module with `mO`
3) The Expert asks for the morse code being flashed
2) The Player inputs `.. -.-. -.- - .-.` ENTER
2) The Expert outputs `Word was: Trick    Input 3.532 MHz`
3) Player sets the frequency to 3.532 MHz in KTANE, and clicks TX. *Module Complete, move on to the next one.* 


## Complicated Wires `cW`
Going one wire at a time, answer the given questions with `y` for Yes and `n` for No. 
If you make a mistake, the module will be ended, and you will have to re-enter it at the Module Selector.
Once you have input the details about a wire, the Expert may ask you for more details about the bomb. 
For this module, it may ask about the last digit of the serial number, if the bomb has a parallel port *(The long, purple port)*, 
or how many batteries there are on the bomb. If you have entered any of these details in a earlier module, the expert will use those. 
Likewise, once you enter the detail in this module, it will be used in all of the others if they require it.
If a slot is blank, as in there are less than 6 wires, treat the blank slot as a wire with no led, blue, red, or star.

Once you have recieved an instruction, the Expert will ask if the wires are done. If not, answer `n`, and continue the module. If you are done, answer `y`, and you will be put back to the Module Selector. 

### Example:
0) KTANE gives you a red and blue twisted wire with an LED and no Star.
1) The Player selects the Complicated Wires module with `cW`
2) The Expert asks the player `Does the wire have blue coloring? (y/n): `
3) The Player enters `y` because there is blue coloring
4) The Expert continues asking questions about the wire until it has the details it needs
5) The Expert then asks `What is the last number of the bomb serial number?: `
6) The Player checks around the bomb to find that it is 6, so they enter `6`
7) The Expert tells the player to `Cut this wire`, so the player complys
8) The Expert asks the player `Are there more wires to process? (y/n): `
9) Because there are a few more wires, the player answers `y`, and repeats this until the module is complete
10) *Module Complete, move on to the next one.* 


## Wire Sequences `wS`
This module consists of four panel repeats, each with up to 3 wires of various color and endpoints. 
The goal is to cut specific wires based on their occurances and endpoints. Don't worry, the expert has got you covered :)
After selecting this module, the expert will ask for a "wire code". 
This is a way to encode the panel so that the expert can process it and give you instructions. Below is a guide for these wire codes:

`(r,blu,bla)>(A,B,C);(r,blu,bla)>(A,B,C);(r,blu,bla)>(A,B,C)`

For each wire, there is a color>endpoint code, with each wire seperated by a `;`. 
Using the standard shorthand (which can be found at the top of this readme), 
input the color and endpoint for each wire in the order they appear on the panel (the order of the wires is important, 
and is determined by the number on the left start point of the wire). If there is no wire for a startpoint (i.e. the startpoint is just a hole), 
just enter `blank` inplace of the color>endpoint code.

### Example:
0) KTANE gives you 2 wires in the first section. A Blue in 1 and B, and a Black in 3 and B.
1) The Player selects the Wire Sequences module with `wS`
2) The Expert asks for the wire code (see above for explanation)
3) The Player enters `blu>B;blank;bla>B`
4) The Expert tells the player to cut Wire 1 and Wire 3, ignoring wire 2 (because there is no wire 2)
5) The Player repeats this until all four panels are complete
6) *Module Complete, move on to the next one.* 


## Passwords `p`
This module consists of 5 displays, each with varying letters. The letters for each display can be cycled with the up and down arrows. 
In the regular manual, there is a list of words. Using the provided letters in the moddule, one of these words can be "typed" into the module. 
Thankfully, the expert can do all of that for you. After entering the module, the expert asks for all of the provided letters in the first column. 
Enter these letters with no seperation. The order does not matter, just that you enter ALL of the letters in a given display. 
The expert will continues to ask for the letters in each display, until only one word from the list can be made, 
in which the expert will give you that word after about 2 or 3 displays, but it is able to ask for all five in the case of a particularlly 
annoying module. 

### Example:
1) The Player enters the passwords module with `p`
2) The Expert asks for the possible letters in the first display
2) The Player, after scrolling through the display, sees the letters A, D, O, B, and G
3) The Player inputs `adobg`
4) The Expert asks for the next display
5) The Player inputs `uobei`
6) The Expert asks for the third display
7) The Player inputs `ojdke`
8) The Expert tells the player to input the word `about` into the module
9) The Player scrolls through the displays until ABOUT appears, and presses SUBMIT
10) *Module Complete, move on to the next one.*

# Needy Modules
Later in KTANE, there are modules that must be attended to regularly and in a timely manner. These are the Needy Modules (can you guess why)
There a 3 needy modules currently in the game. These are Venting Gas, Capacitor Discharge, and Knobs
Both Venting Gas and Capacitor Discharge do not require any input from the Expert, and are very simple to complete:

*Venting Gas: Follow the prompts on the screen with the express purpose of venting gas
*Cap Discharge: Pump the lever to keep the power meter from reaching the top. If it reaches the top, the cap will explode and you will recieve a strike

## Knobs
Knobs is a bit more complicated.
The knobs needy module consists of 12 leds and a knob with 4 possible positions.
Depending on which leds are lit, and the possition of the "UP", you will move the arrow to the appropriate position.
Unlike most of the other modules, there is no "OKAY" or "SUBMIT" button, rather, the module submits your answer at the end of its little timer.
When you launch KTANExpert.py, two windows will open (or one and a program selector from Windows). One of the windows, titled "KTANExpert by Reese Ford" is the regular module expert
The window titled "NeedyModule Sub-Expert" is the sub-expert that handles the needy modules. These were split up so that you can jump back and forth between regular and needy modules.
Because knobs is the only needy module requiring input, the Sub-Expert automatically selects it. 
To use this module, enter the leds in binary form from topleft across to topright, then bottomleft across to bottomright without any seperators.
Then the module will ask for the position of the "UP" in cardinal directions. If you happen to live under a rock, North is the top with East South and West going around counter-clockwise.
Once you enter the position of "UP", the module will tell you what position to put the arrow in. For this, IGNORE THE UP. Inputting the "UP" position allows the module to compensate. Just pretend the up isn't even there when moving the arrow to the given position

### Example:
0) After doing one module, KTANE lights up the Knobs needy module with only 3 leds lit, and the "UP" on the bottom of the dial
1) The Player enters `000010000110` into the Sub-Expert
2) The Sub-Expert asks for the position of "UP"
3) The Player enters `south`
4) The Sub-Expert tells the player to `Turn the knob to the east position`
5) The Player moves the arrow until it is facing left and continues on with whatever regular module they were working on.
6) The Knobs module starts beeping with 3 seconds left, and then stops beeping, because the arrow was in the correct location at the end of the timer.