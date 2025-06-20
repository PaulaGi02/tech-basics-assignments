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