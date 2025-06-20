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
line 22-30: def draw - <br>
line 41-20: def flip/ update_flip <br>
line 52-74: class Game - <br>
line 76-102: def generate_cards - <br>
line 104-122: def handle_click <br>
line 124-147: def update <br>
line 149-176: def draw <br>
line 178-179: def reset <br>

display.py <br>
line 1: importing pygame <br>
line 3-8: class Display - defining the screen: setting width, height and name of game <br>
line 10-11: def clear - method that clears the screen filling it with black

main.py <br>
line 1-3: importing pygame and the files game.py and display.py <br>
line 5-9: def main <br>
line 11-29: clock - <br>
line 31-41: clear - <br>
line 43-65: class Menu - <br>
line 67-68: main==main