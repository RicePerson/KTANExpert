# KTANExpert
A Phython BombManual Expert for the game, **Keep Talking and Nobody Explodes**
It's not done yet. As of right now, it only does:
* Wires
* Button*
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
## Wires
Select the number of wires present in the module (including cut wires from previous attempts).
Enter each wire color from the top (which is considered the first wire in the expert) to the bottom.
Follow the given instructions.

### Example:
1. KTANE gives you a wire module that goes:
-       -
-  RED  -
-  RED  -
-       -
-  BLUE -
- WHITE -

2. You input "4" as the wire number, and enter **r** ENTER **r** ENTER **blu** ENTER **w**
3. The expert then asks you for the last digit of the serial number, which you enter "3"
4. The expert asks you to **Cut the last RED wire**, which prompts you to cut the 3rd wire. *Module Complete, move on to the next one.* 

## Button
*Module being reworked due to poor design*

## Keypad
Once you enter the keypad module in the expert, it will list all possible keypad symbols, and then ask for the first one.
It does not matter what order you input the key's, only that you enter all four, one after another.
Find the symbol name from the list provided that most-closly matches the symbol in KTANE, and enter it, pressing ENTER after each symbol
Repeat until provivded a Final List. Enter these in order to complete the module

### Example
1. The module in KTANE has an **omega, ae, trident, and squished 6**
2. In the expert, input **ae** ENTER **trident** ENTER **omega** ENTER **6**
3. The expert will then output **Final: ['6', 'ae', 'trident', 'omega']**
4. Click these inorder in KTANE. *Module Complete, move on to the next one.* 

## Simon Says
This can be considered the worst game of simon says, because you don't repeat it back.
Once the simon says module is selected in the expert (selected by "s"), it will ask a couple of preliminary questions about the bomb, which will determine which lookup-table it will use.
After answering these questions, watch the KTANE module for its ENTIRE flash sequence (the module starts with one flash, then increases by one with every sucessfull button-press)
The module will flash relatively quickly, and then repeat the sequence after a long pause.
Enter each flash color IN ORDER with an ENTER between each. Once all colors have been entered, input "end".
Click the colored buttons in the given order.
Repeat until the module is complete. To exit the module on the expert, input "done" at any step.

### Example
*0) The bomb has a vowel, and is sitting at one strike. The red button is currently flashing slowly.*
1) The player selects the simon says expert module
2) Player~:red_circle:~ inputs `y` then `1`
3) Player~:red_circle:~ input `r` then `end`
4) Expert~:blue_circle:~ outputs **Input: ['y']**
5) Player~:red_circle:~ clicks the yellow button in KTANE
omega) Repeat until module is complete, then Player~:red_circle:~ inputs **done** into the expert~:blue_circle:~.

Note: If for some reason, after clicking a colorred button, it markes it as wrong and gives you a strike, 
enter **done** into the expert and start over, as the current number of strikes affects the module.

## Who's on First


## Morse-Code
Enter the morse code as it is flashed to you in the module. 
Use period( . ) and minus( - ) with a space between letters to input the morse (represented by a longer space in the flasing module.)
When the module stop flashing the longest and then starts again, it means the word is restarting. 
The program does NOT require that you start at the beginning of the word, only that you don't duplicate any letters already input.
Once you have the morse word input (with no duplication), press ENTER, and input the frequency provided.

### Example:
1. KTANE flashes: .. -.-. -.-   - .-. .. -.-. -.-   - .-. .. -.-. -.-   - .-. .. -.-. -.-   etc.
2. You input: **.. -.-. -.- - .-.** into the program and press ENTER
3. The Programs gives you: **Word was: Trick    Input 3.532 MHz**
4. You set the frequency to 3.532 MHz in KTANE. *Module Complete, move on to the next one.* 

## Complicated Wires
Going one wire at a time, answer the given questions with **y** for Yes and **n** for No. If you make a mistake, the function will be ended, and you will have to re-enter it at the Module Selector.
Once you have input the details, the Expert will give you a command. Use the following table to find out what you have to do to that wire:

| Command | Do to Wire |
| ------- | ---------- |
| Cut     | Cut that Wire |
| Do not Cut | Do not cut that wire, just move on |
| If 2 Battery, cut | Cut only if there are 2 or more batteries on the bomb |
| If Parallel port, cut | If there is a long parallel port on the bomb, cut that wire |
| If Serial even, cut | If the last digit of the serial number is even, cut that wire |

Once you have recieved a command, the Expert will ask if the wires are done. If not, answer **n**, and continue the module. If you are done, answer **y**, and you will be put back to the Module Selector. 

### Example:
1. KTANE gives you a red and blue twisted wire with an LED and no Star.
2. You enter **y** for Blue? Red? and LED?
3. You enter **n** for Star?
4. The Expert gives you **If Serial even, cut**
5. You check the Serial Number on the Bomb, its last number is 6
6. You cut that wire, and nothing happens
7. Repeat until module is done. 
8. Once the module is done, answer **y** to the loop question in the Expert. *Module Complete, move on to the next one.* 

## Wire Sequences
Again, going one wire at a time, enter the wire color and placement into the Expert, and follow the instructions that it gives you. When you see the module, there will be 4 sections, not all visable yet. **DO NOT PRESS THE ARROW UNTIL YOU ARE DONE WITH THAT SECITON!!!!** Enter the wires into the Expert in numerical order with the numbers on the left. Starting with 1, give the Expert the color (blu, bla, or red) and the letter that wire goes to (A, B, or C). Capitalization matters. Repeat until the module is complete, then type just "exit" as the wire color (leave the letter blank), and you will be returned to the Module Selector.

### Example:
1. KTANE gives you 2 wires in the first section. A Blue in 1 and B, and a Black in 1 and B.
2. You enter **blu B** and press enter.
3. The Expert tells you to Cut the Wire. Cut it
4. The Expert then asks for the next wire, you enter **bla B**
5. The Expert tells you to Cut that Wire as well. Do It
6. Now that the wires on that section have been processed, you click the down arrow to move on.
7. Repeat until done. Type **exit** as the next input to return to Module Selection. *Module Complete, move on to the next one.* 
