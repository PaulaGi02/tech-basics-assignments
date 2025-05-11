import random
import sys
import time

# --- Typewriter Effect ---
def typewriter(text, delay=0.02):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

# --- Game State ---
inventory = []
MAX_INVENTORY_SIZE = 5
PEEVES_PRESENT = False
map_skip_used = False
current_room = "Common Room"

# --- Rooms and Items ---
rooms = {
    "Common Room": [
        {"name": "Broken Quill", "type": "junk", "description": "Doesn't work anymore."},
        {"name": "Pumpkin Juice", "type": "food", "description": "A tasty Hogwarts drink."},
        {"name": "Key", "type": "tool", "description": "Opens locked doors."}
    ],
    "Library": [
        {"name": "Chocolate Frog", "type": "food", "description": "Restores energy."},
        {"name": "Invisibility Cloak", "type": "tool", "description": "Makes you invisible to Peeves."},
    ],
    "Staircase": [
        {"name": "Marauder's Map", "type": "tool", "description": "Reveals hidden rooms."},
    ],
    "Hidden Hallway": [
        {"name": "Wand", "type": "tool", "description": "Used to cast spells."}
    ],
    "Transfiguration Classroom": []
}

room_sequence = [
    {"name": "Common Room", "requires": None},
    {"name": "Library", "requires": "Key"},
    {"name": "Staircase", "requires": "Invisibility Cloak"},
    {"name": "Hidden Hallway", "requires": "Marauder's Map"},
    {"name": "Transfiguration Classroom", "requires": "Wand"},
]

# --- Helpers ---
def get_items_in_current_room():
    return rooms[current_room]

def show_inventory():
    if not inventory:
        typewriter("You’re not carrying anything.")
    else:
        typewriter("You are carrying:")
        for item in inventory:
            typewriter(f"- {item['name']}")

def show_room_items():
    items = get_items_in_current_room()
    if not items:
        typewriter("There’s nothing interesting here.")
    else:
        typewriter(f"In the {current_room}, you see:")
        for item in items:
            typewriter(f"- {item['name']}: {item['description']}")

def present_item_options(item):
    #options = []
    name = item['name'].lower()

    if name == "key":
        options = ["Try to open a nearby locked door.",
                   "Scratch your name into the wood.",
                   "Drop it and kick it around like a football."]
    elif name == "marauder's map":
        options = ["Use it to find a hidden path.",
                   "Fold it into a paper hat.",
                   "Tap it and say 'Mischief Managed'."]
    elif name == "pumpkin juice":
        options = ["Drink it.",
                   "Throw it on the wall.",
                   "Use it to water a plant."]
    elif name == "chocolate frog":
        options = ["Eat it.",
                   "Let it hop around.",
                   "Trade it with a friend."]
    elif name == "wand":
        options = ["Cast Lumos.",
                   "Use it as a drumstick.",
                   "Try to transfigure your shoe."]
    else:
        options = ["Put it in your pocket.",
                   "Sniff it cautiously.",
                   "Tap it on your head."]

    typewriter("What would you like to do with the item?")
    for i, option in enumerate(options, 1):
        typewriter(f"  {i}) {option}")
    choice = input("> ").strip()

    if name == "key" and choice == "1":
        advance_to_room("Library")
    elif name == "marauder's map" and choice == "1":
        reveal_hidden_path()
    elif name == "wand" and choice == "1":
        typewriter("You cast Lumos. The room glows with light.")
    elif name == "pumpkin juice" and choice == "1":
        typewriter("Delicious! You feel warm inside.")
    elif name == "chocolate frog" and choice == "1":
        typewriter("It wiggles in your mouth! You gain energy.")
    else:
        typewriter("Nothing much happens, but it was worth a try.")

def reveal_hidden_path():
    global map_skip_used
    if map_skip_used:
        typewriter("You've already used the map once. It fades away.")
    else:
        map_skip_used = True
        typewriter("You find a secret stairwell behind the bookshelf!")
        advance_to_room("Hidden Hallway")

def pick_up(item_name):
    if len(inventory) >= MAX_INVENTORY_SIZE:
        typewriter("You can't carry any more items.")
        return

    for item in get_items_in_current_room():
        if item['name'].lower() == item_name.lower():
            if item['name'].lower() == "chocolate frog" and random.random() < 0.5:
                typewriter("The chocolate frog jumps away!")
                return
            inventory.append(item)
            get_items_in_current_room().remove(item)
            typewriter(f"You picked up the {item['name']}.")
            present_item_options(item)
            return

    typewriter("That item isn't here.")

def examine(item_name):
    for item in inventory + get_items_in_current_room():
        if item['name'].lower() == item_name.lower():
            typewriter(f"You examine the {item['name']}. {item['description']}")
            present_item_options(item)
            return
    typewriter("You can’t find that item to examine.")

def advance_to_room(target_room):
    global current_room, PEEVES_PRESENT
    current_room = target_room
    typewriter(f"You move into the {target_room}.")
    if random.random() < 0.3:
        PEEVES_PRESENT = True
        typewriter("👻 Peeves the Poltergeist appears! He cackles wildly.")
    else:
        PEEVES_PRESENT = False
    show_room_items()
    if target_room == "Transfiguration Classroom":
        if any(i['name'].lower() == "wand" for i in inventory):
            typewriter("✨ Professor McGonagall nods approvingly. You've made it with your wand. You win! ✨")
            sys.exit()
        else:
            typewriter("You're here... but no wand? Go back and find it!")

def game_intro():
    typewriter("\n\U0001F3EB Welcome to the Hogwarts Adventure Game!\n")
    typewriter("You wake up in the Gryffindor Common Room. Classes are about to begin.")
    typewriter("Your goal: Reach the Transfiguration Classroom in time – and don’t forget your wand!")
    typewriter("Along the way, collect magical tools, dodge Peeves, and unlock secret paths.")
    typewriter("Type commands like: pickup [item], examine [item], inventory, or quit\n")
    show_room_items()

def game_loop():
    game_intro()
    while True:
        command = input("\n> ").strip().lower()

        if command == "quit":
            typewriter("Thanks for playing! Mischief managed.")
            break
        elif command == "inventory":
            show_inventory()
        elif command == "look":
            show_room_items()
        elif command.startswith("pickup "):
            pick_up(command[7:].strip())
        elif command.startswith("examine "):
            examine(command[8:].strip())
        else:
            typewriter("Unknown command. Try: pickup, examine, inventory, or quit.")

if __name__ == "__main__":
    game_loop()
