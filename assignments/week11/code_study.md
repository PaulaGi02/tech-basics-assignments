# Final Project - Frieda and Paula
The program is an interactive, Python-based learning platform that combines spaced repetition 
with gamification to make studying more engaging and visually rewarding. At its core, 
users create or import flashcard decks to review educational content. 
Each session spent playing learning-focused minigames 
contributes to the growth of a virtual plant—starting from a seed and evolving 
through various life stages like sprout, leaf, and bloom.
As users invest more time, new minigames unlock, each reinforcing knowledge in 
fun and varied ways. 


<b>memory game:</b><br>
https://github.com/JohnDev19/Memory-Match-Game/blob/main/game.py <br>

*file structure -> display.py, game.py, main.py* <br>

game.py: <br>
line 1-7: importing libraries and initialising pygame/ mixer module <br>
line 9-20: class Card - defining starting point of the cards (color, format, revealed, matched) <br>
line 22-30: def draw -  handles how the card is displayed, animates flipping, if revealed or matched, shows its color, all cards get a black border<br>
line 41-20: def flip/ update_flip - begins flipping animation, increments progress and toggles revealed once the animation is complete <br>
line 52-74: class Game - Stores board size, tracks score, time, clicked cards, and loads images and sound. Initializes font and game state <br>
line 76-102: def generate_cards - defines, shuffles, places and appends cards on a grid with calculated (x,y) positions<br>
line 104-122: def handle_click - detects if a card was clicked and is eligible to flip, plays sound for first second and third click<br>
line 124-147: def update - updates the flipping status. if two cards are revealed compares colors, if match: sets both as matched, adds score, plays sound. if not: flips back, plays fail sound. Ends game if all cards match <br>
line 149-176: def draw - draws background, cards, score, moves, timer<br>
line 178-179: def reset - resets the game by reinitializing with the same board size <br>

display.py <br>
line 1: importing pygame <br>
line 3-8: class Display - defining the screen: setting width, height and name of game <br>
line 10-11: def clear - method that clears the screen filling it with black

main.py <br>
line 1-3: importing pygame and the files game.py and display.py <br>
line 5-9: def main - initializes all Pygame modules, creates game screen, indicates currently at the main menu<br>
line 11-29: clock - clock regulates frame rate, running controls wether the loop continues, iterates through Pygame events, separates behavior depending on you're in a game or in the menu <br>
line 31-41: clear - clears screen before drawing, if game runs updates the state and draws it otherwise shows menu, sets the frame rate limit<br>
line 43-65: class Menu - displays difficult level, easy, medium, hard, handles menu rendering, detects users clicked option<br>
line 67-68: main==main - ensures main is only running if the file is executed

Flashcards <br>
https://github.com/ebisu-flashcards/flashcards-cli/tree/main/flashcards_cli

file structure -> \_init.py\_, \_main.py\_, main.py, study.py <br>
\_init.py\_ :  Imports the main() function from main.py for CLI interface exposure when the module is used  <br>
\_main.py\_:  Also imports main() for CLI entrypoint if python -m flashcards_cli is used.

<br> main.py <br>

1-9: Imports sys, click, sleep, PyInquirer, and functions from internal modules, initializer from core library, study(), edit() <br>
12-46: def main() — main interactive CLI loop <br>
17: Creates DB session using init_db()<br>
18-20: Prints CLI welcome banner using click.echo<br>
21-42: Infinite loop that:<br>
    22-31: Prompts user to choose operation: ["Study", "Edit", "Quit"]<br>
    32-33: If "Study", calls study(session)<br>
    34-35: If "Edit", calls edit(session)<br>
    36-38: If "Quit", prints exit message and returns<br>
    39-42: Fallback exit for other/invalid input (with sleep)<br>
    45: if \__name\__ == "\__main\__": main() - ensures program runs only when executed directly <br>

study.py <br>

1-7: Imports click, PyInquirer, and relevant DB/Scheduler/Errors modules<br>
8: def study(session: Session)<br>
12: Fetches all decks from the database<br>
13-15: If no decks, informs user and returns early<br>
17-27: Prompts user to select a deck <br>
29-30: If user cancels or chooses "< Back>", exits study session<br>
32: Gets the selected deck by name from DB<br>
33: Initializes scheduler for that deck<br>
35-42: Try to fetch first card using scheduler.next_card()<br>
    - If no cards are due: display message and return<br>
44-83: While loop that handles reviewing each flashcard:<br>
    44: Shows card number<br>
    48-58: Prompts user with question, waits for input<br>
    60-64: If user enters nothing, exit with goodbye message<br>
    67-72: Check if answer is correct or wrong, give feedback using click.echo<br>
    75: Increments reviewed card count<br>
    76-83: Try getting next card; exit loop if no more cards to study<br>


*Quiz Game*<br>
https://github.com/shriyaa01/Python_Quiz_Game/blob/main/quiz_game.py

1: importing random<br>
3-99: quiz_data - dictionary with questions and answers<br>
101-109: prints questions and options, gets user input and validates if input is right<br>
111-122: loops through the questions, prints correct if answer is right and adds one point to the score or prints wrong + correct answer <br>
