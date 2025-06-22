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
I chose this project because it’s built with Pygame and structured cleanly across files. Also the memory-card-game fitted as a game for the final project

What does the program do? What's the general structure of the program?<br>
- This is a card-matching memory game. Players click to flip cards and try to match colors. <br>
- General Structure:
  - game.py handles game logic (cards, flipping, matching, drawing).
  - display.py sets up the game screen.
  - main.py contains the main loop, handles menu interactions. <br>

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

Function analysis: pick one function and analyze it in detail: <br>
game.py, ine 124-147:
- What does it do?
  - Updates the state of each card (animation). 
  - Handles logic for checking if two flipped cards match. 
  - Plays appropriate sounds and updates the score. 
  - Ends the game when all cards are matched.

- inputs/ outputs:
  - Inputs: Internal game state (flipped cards, score, sound).
  - Outputs: Updates to game logic (score, matched status, game over).

- How does it work?:<br>
  - Loop through all cards to update their flip status.
  - Check if two cards are flipped and finished animating:
    - If they match, mark as matched and play a sound.
    - If not, flip back and reduce score.
  - Reset card selections.
  - End the game if all cards are matched.

Takeaways: <br>
- Efficient handling of animations and game logic in one method. 
- Clear separation of concerns between drawing, updating, and clicking. 
- we can probably adapt our code to this example, just need to figure out, how we can add the flashcards on the memory cards

What was confusing?:
- At first I did not know what the .mixer was, but after my own research I understood that it was needed for sound effects


__Flashcards__ <br>
https://github.com/ebisu-flashcards/flashcards-cli/tree/main/flashcards_cli <br>
I chose it because it demonstrates an interactive CLI tool with practical features like spaced repetition, database integration, and dynamic user input.<br>

__What does the program do?__<br>
A command-line flashcard study tool. It allows users to create, edit, and study flashcard decks. It selects cards based on spaced repetition and schedules future reviews.

__General Structure__<br>
flashcards_cli/<br>
- \__init\__.py<br>
- \__main\__.py         ← entry point<br>
-  main.py             ← main menu logic<br>
- study.py            ← study logic<br>
- edit/<br>
    - \__init\__.py     ← launches edit menu<br>
     - decks.py        ← create/edit/delete decks<br>
     - cards.py        ← create/edit/delete cards<br>

__How does it work?__<br>
study.py, def study(session: Session):
- Loads all decks. Uses Deck.get_all() to retrieve available decks.
- Prompts user to select one or go back.
- Uses get_scheduler_for_deck() to prepare the deck for studying.
- scheduler.next_card() fetches the next card to review.
- Main study loop:
- Prompts the user with the card's question.
- Gets their answer and compares it to the correct one.
- Provides feedback ("Correct" or "Wrong").
- Records the result via scheduler.process_test_result().
- Repeat: Continues until no more cards are ready or user exits.

__Input/Output:__<br>
Input:
session: a SQLAlchemy Session object used for database access.<br>
Output:
None directly. User interaction happens via terminal output and user input. State is updated in the DB through scheduler.

__Takeaways:__<br>
- Good CLI UX: The use of PyInquirer provides a friendly interface in the terminal, making it feel more interactive and less tedious.
- Error handling: Graceful fallback for user interruptions (e.g., Ctrl+C) and empty input. 
- Scheduler logic: Delegating spaced repetition to a scheduler shows good separation of concerns.

__What parts of the code were confusing or difficult at the beginning to understand?__
- the file structure was the most complicated, because there were several files and at first I was confused which files were and weren't important for the code to work.


