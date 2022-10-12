# KTANExpert
A Python BombManual Expert for the game, **Keep Talking and Nobody Explodes**
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

(For more information on modules, visit bombmanual.com)

# TO INSTALL:
Download the KTANExpert folder and run KTANExpert.py


# Module Instructions

## How to read these instructions
For every completed module in this Expert, there are accompanying instructions on how to properly input details and comply with instructions.
Every module has a description with basic instructions, as well as an example with real-world modules with what the player enters and what the expert outputs
For ease of following the plot, the Player is marked by a :red_circle: and the Expert is followed by a :large_blue_circle:.
Anything that would be typed into the command window or is recieved from the command window with look like `this`. To enter a module, type the module code that follows the name in these instructions when the expert asks `Module? (...): `

### Glossary
There are some words used in these instructions that may mean something other than what common sense would infer. Here is what those words mean.
- **KTANE Module:** A module on the bomb in Keep Talking and Nobody Explodes
- **Expert:large_blue_circle::** The program this README accompanys
- **Player:red_circle::** You!
- **Repeat:** Some modules require that you do the module a few times, each with differing details. Each time you do the module is a Repeat
- **Command Window:** The window that you enter inputs into
- **Input(s):** Things the Player will type into the command window, then press ENTER
- **Output(s):** Things the Expert will tell the Player in the command window
- **ENTER:** Represents pressing the Enter Key

### Codes
There are short-hand codes used throughout to make inputs generally faster. Here they are
| Shorthand | What it means|
| ----- | ----- |
| KTANE | Keep Talking and Nobody Explodes |
| y | Yes |
| n | No |
| r | Red |
| blu | Blue |
| bla | Black |
| w | White |
| y | Yellow |
| g | Green |



## Wires `w`
Select the number of wires present in the module (including cut wires from previous attempts).
Enter each wire color from the top (which is considered the first wire in the expert) to the bottom.
Follow the given instructions.

### Example:
*0) KTANE gives you a wire module that goes:*
- *Empty* 
-  *RED*  
-  *RED*  
- *Empty* 
-  *BLUE* 
- *WHITE* 

1) The Player:red_circle: inputs `4` as the wire number, 
2) The Expert:large_blue_circle: asks `Wire 1? (r/y/blu/bla/r): `
3) The Player:red_circle: then inputs `r` ENTER `r` ENTER `blu` ENTER `w`
4) The Expert:large_blue_circle: then asks `Last Digit of Serial: `
5) The Player:red_circle: checks the bomb for a serial number sticker, then inputs what the last digit is, which in the case of this example, is `3`
6) The Expert:large_blue_circle: asks you to `Cut the last RED wire`, which prompts the player to cut the 3rd wire. *Module Complete, move on to the next one.* 


## Button `b`
*Instructions to come, but the module is fairly straigtforward*

## Keypad `k`
Once you enter the keypad module in the expert, it will list all possible keypad symbols, and then ask for the first one.
It does not matter what order you input the key's, only that you enter all four, one after another.
Find the symbol name from the list provided that most-closly matches the symbol in KTANE, and enter it, pressing ENTER after each symbol
Repeat until provivded a Final List. Enter these in order to complete the module

### Example
*0) The module in KTANE has an omega, ae, trident, and squished 6*
1) The Player:red_circle: inputs `ae` ENTER `trident` ENTER `omega` ENTER `6`
2) The Expert:large_blue_circle: will then output `Click these buttons in order: 1)6 2)ae 3)trident 4)omega`
3) The Player:red_circle: clicks these inorder in KTANE. *Module Complete, move on to the next one.* 


## Simon Says `s`
This can be considered the worst game of simon says, because you don't repeat it back exactly as it is presented to you.
Once the simon says module is selected in the expert (selected by `s`), it will ask a couple of preliminary questions about the bomb, which will determine which lookup-table it will use.
After answering these questions, watch the KTANE module for its ENTIRE flash sequence (the module starts with one flash, then increases by one with every sucessfull button-press)
The module will flash relatively quickly, and then repeat the sequence after a long pause.
Enter each flash color IN ORDER with an ENTER between each. Once all colors have been entered, input `end`.
Click the colored buttons in the given order.
Repeat until the module is complete. To exit the module on the expert, input `done` at any step.

### Example
*0) The bomb has a vowel, and is sitting at one strike. The red button is currently flashing slowly.*
1) The player selects the simon says expert module
2) Player:red_circle: inputs `y` ENTER `1`
3) Player:red_circle: inputs `r` ENTER `end`
4) Expert:large_blue_circle: outputs `Click these buttons in order: Yellow`
5) Player:red_circle: clicks the yellow button in KTANE
6) Repeat until module is complete, then Player:red_circle: inputs `done` into the expert:large_blue_circle:. *Module Complete, move on to the next one.*

Note: If for some reason, after clicking a colored button, it markes it as wrong and gives you a strike, 
enter `done` into the expert and start the module over, as the current number of strikes affects the module.


## Who's on First `who`
This module includes a display and six buttons. There are TWO seperate steps to this module, so don't go clicking all willy-nilly
The first part of this module is inputing the display *(Note: a possible word for the display is just a blank display with nothing written on it. In this case, enter `*blank*` for the word)*, and inputing the word on the provided button
I specificlly coded this module to make the steps VERY CLEAR because of the nature of the module. Try the module, and if it still doesn't make sense, check out the example

### Example
*0) The KTANE module has the word "first" in the display, and more words on the buttons below*
1) The Expert:large_blue_circle: asks for the word in the display, which the Player:red_circle: inputs `first`
2) The Expert:large_blue_circle: then asks for the word in the TopRight, which the Player:red_circle: DOES NOT CLICK IT, but inputs `wait`
3) The Expert:large_blue_circle: then starts asking if certain words exist on the buttons. It firsts aks `Is the word uhhh there?`. The Player:red_circle: answers `n`, because it is not there
4) Now, the Expert:large_blue_circle: asks 'Is the word no there?'. Because "no" is on one of the buttons, the Player:red_circle: answers `y`
5) The Expert:large_blue_circle: says `Click the word no`. The Player:red_circle: complys. Because this happens to be the 3rd and final repeat of the module, the Player:red_circle: now inputs `n` to the Experts:large_blue_circle: questions, `Are there more steps?`
6) *Module Complete, move on to the next one.* 


## Memory `m`
This module consists of a display with a single digit and four buttons with numbers 1-4 on them, in an order that changes after every repeat, of which there are five.
This is a back-and-forth with the expert:large_blue_circle:, and is fairly straightforward. At every repeat, input the numbers in the order: Display first-button second-button third-button fourth-button
The expert:large_blue_circle: will then output some debug information, alongside an instruction, in the form of `Press the button labeled  #`. Follow this instruction.
Repeat until the module is complete. If you ever mess up, the KTANE module will reset back to stage one. To reset the expert:large_blue_circle:, input `r` at any step.

### Example
*0) The KTANE module starts with the display being 4 and the buttons being, from left to right, 1 3 2 4*
1) The Expert:large_blue_circle: asks for the stage 1 numbers, which the Player:red_circle: inputs `4 1 3 2 4`
2) The Expert:large_blue_circle: gives the instruction `Press the button labeled 4`. The Player:red_circle: complys. The numbers on the KTANE module change
3) Repeat 1 and 2 until the module is complete. *Module Complete, move on to the next one.* 


## Morse-Code `mO`
Enter the morse code as it is flashed to you in the module. 
Use period( . ) and minus( - ) with a space between letters to input the morse (represented by a longer space in the flasing module.)
When the module stop flashing the longest and then starts again, it means the word is restarting. 
The program does NOT require that you start at the beginning of the word, only that you don't duplicate any letters already input.
Once you have the morse word input (with no duplication), press ENTER, and input the frequency provided.

### Example:
*0) KTANE mnodule is flashing .. -.-. -.-   - .-. .. -.-. -.-   - .-. .. -.-. -.-   - .-. .. -.-. -.- repeating indefinitely*
1) The Player:red_circle: inputs `.. -.-. -.- - .-. ENTER`
2) The Expert:large_blue_circle: outputs `Word was: Trick    Input 3.532 MHz`
3) Player:red_circle: sets the frequency to 3.532 MHz in KTANE, and clicks TX. *Module Complete, move on to the next one.* 


## Complicated Wires `cW`
Going one wire at a time, answer the given questions with `y` for Yes and `n` for No. If you make a mistake, the module will be ended, and you will have to re-enter it at the Module Selector.
Once you have input the details about a wire, the Expert may ask you for more details about the bomb. For this module, it may ask about the last digit of the serial number, if the bomb has a parallel port *(The long, purple port)*, or how many batteries there are on the bomb. If you have entered any of these details in a earlier module, the expert will use those. Likewise, once you enter the detail in this module, it will be used in all of the others if they require it.

Once you have recieved an instruction, the Expert will ask if the wires are done. If not, answer `n`, and continue the module. If you are done, answer `y`, and you will be put back to the Module Selector. 

### Example:
*0) KTANE gives you a red and blue twisted wire with an LED and no Star.*
1) The Player:red_circle: selects the Complicated Wires module with `cW`
2) The Expert:large_blue_circle: asks the player `Does the wire have blue coloring? (y/n): `
3) The Player:red_circle: enters `y` because there is blue coloring
4) The Expert:large_blue_circle: continues asking questions about the wire until it has the details it needs
5) The Expert:large_blue_circle: then asks `What is the last number of the bomb serial number?: `
6) The Player:red_circle: checks around the bomb to find that it is 6, so they enter `6`
7) The Expert:large_blue_circle: tells the player to `Cut this wire`, so the player complys
8) The Expert:large_blue_circle: asks the player `Are there more wires to process? (y/n): `
9) Because there are a few more wires, the player:red_circle: answers `y`, and repeats this until the module is complete
10) *Module Complete, move on to the next one.* 


## Wire Sequences `wS`
This module consists of four panel repeats, each with up to 3 wires of various color and endpoints. The goal is to cut specific wires based on their occurances and endpoints. Don't worry, the expert has got you covered :)
After selecting this module, the expert will ask for a "wire code". This is a way to encode the panel so that the expert can process it and give you instructions. Below is a guide for these wire codes:

`(r,blu,bla)>(A,B,C);(r,blu,bla)>(A,B,C);(r,blu,bla)>(A,B,C)`

For each wire, there is a color>endpoint code, with each wire seperated by a `;`. Using the standard shorthand (which can be found at the top of this readme), input the color and endpoint for each wire in the order they appear on the panel (the order of the wires is important, and is determined by the number on the left start point of the wire). If there is no wire for a startpoint (i.e. the startpoint is just a hole), just enter `blank` inplace of the color>endpoint code.

### Example:
*0) KTANE gives you 2 wires in the first section. A Blue in 1 and B, and a Black in 3 and B.*
1) The Player:red_circle: selects the Wire Sequences module with `wS`
2) The Expert:large_blue_circle: asks for the wire code (see above for explanation)
3) The Player:red_circle: enters `blu>B;blank;bla>B`
4) The Expert:large_blue_circle: tells the player to cut Wire 1 and Wire 3, ignoring wire 2 (because there is no wire 2)
5) The Player:red_circle: repeats this until all four panels are complete
6) *Module Complete, move on to the next one.* 
