import random
import sys
import time

# Typewriter Effect
def typewriter(text, delay=0.02):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

# Game State
inventory = []
MAX_INVENTORY_SIZE = 5
PEEVES_PRESENT = False
map_skip_used = False
current_room = "Common Room"

# Rooms and Items
rooms = {
    "Common Room": [
        {"name": "Broken Quill", "type": "junk", "description": "Doesn't work anymore."},
        {"name": "Pumpkin Juice", "type": "food", "description": "A tasty Hogwarts drink."},
        {"name": "Key", "type": "tool", "description": "Opens locked doors."},
        {"name": "Gryffindor Scarf", "type": "clothing", "description": "Keeps you warm and shows your house pride."},
    ],
    "Library": [
        {"name": "Chocolate Frog", "type": "food", "description": "Restores energy."},
        {"name": "Invisibility Cloak", "type": "tool", "description": "Makes you invisible to Peeves."},
        {"name": "Spellbook", "type": "tool", "description": "Contains powerful spells for advanced wizards."},
        {"name": "Quill of Quick Quotes", "type": "tool", "description": "Writes down everything you say, often exaggerated."}
    ],
    "Staircase": [
        {"name": "Marauder's Map", "type": "tool", "description": "Reveals hidden rooms."},
        {"name": "Vanishing Cabinet Handle", "type": "junk", "description": "A broken part from a Vanishing Cabinet."},
        {"name": "Exploding Snap Cards", "type": "game", "description": "Be careful! They might explode in your hand."}
    ],
    "Hidden Hallway": [
        {"name": "Wand", "type": "tool", "description": "Used to cast spells."},
        {"name": "Dobby", "type": "toy", "description": "A tiny elf, sometimes searching for trouble."}
    ],
    "Transfiguration Classroom": []
}

room_sequence = [
    {"name": "Common Room", "requires": None},
    {"name": "Library", "requires": "Key"},
    {"name": "Staircase", "requires": "Invisibility Cloak"},  # Logic adjusted for Peeves
    {"name": "Hidden Hallway", "requires": "Marauder's Map"},
    {"name": "Transfiguration Classroom", "requires": "Wand"},
]

# Helpers
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
    if current_room == "Transfiguration Classroom":
        return
    if not items:
        typewriter("There’s nothing interesting here.")
    else:
        typewriter(f"In the {current_room}, you see:")
        for item in items:
            typewriter(f"- {item['name']}")

def drop(item_name):
    for item in inventory:
        if item['name'].lower() == item_name.lower():
            inventory.remove(item)
            rooms[current_room].append(item)
            typewriter(f"You dropped the {item['name']}.")
            return
    typewriter("You don’t have that item.")

def use(item_name):
    for item in inventory:
        if item['name'].lower() == item_name.lower():
            present_item_options(item)
            return
    typewriter("You don’t have that item.")

def present_item_options(item):
    name = item['name'].lower()
    if name == "key":
        options = ["Try to open a nearby locked door.",
                   "Scratch your name into the wood.",
                   "Drop it and kick it around like a football."]
    elif name == "marauder's map":
        options = ["Fold it into a paper hat.",
                   "Tap it and say 'Mischief Managed'.",
                   "Use it to find a hidden path."]
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
    elif name == "invisibility cloak":
        options = ["Put it on your head.",
                   "Use it to make shadow puppets.",
                   "Bundle it like a pillow."]
    elif name == "dobby":
        options = ["command dobby to moonwalk.",
                   "Give him a tiny sock.",
                   "give him high five."]
    else:
        options = ["Put it in your pocket.",
                   "Sniff it cautiously.",
                   "Tap it on your head."]

    typewriter("What would you like to do with the item?")
    for i, option in enumerate(options, 1):
        typewriter(f"  {i}) {option}")
    choice = input("> ").strip()

    # Handle item logic
    if name == "key" and choice == "1":
        advance_to_room("Library")
    elif name == "marauder's map" and choice == "3":
        reveal_hidden_path()
    elif name == "wand" and choice == "1":
        typewriter("You cast Lumos. The room glows with light.")
    elif name == "pumpkin juice" and choice == "1":
        typewriter("Delicious! You feel warm inside.")
    elif name == "chocolate frog" and choice == "1":
        typewriter("It wiggles in your mouth! You gain energy.")
    elif name == "invisibility cloak" and choice == "1":
        typewriter("You were able to sneak quietly through the library.")
        advance_to_room("Staircase")
    elif name == "dobby" and choice == "1":
        typewriter("dobby busts out a moonwalk. It's oddly inspiring. ")
    elif name == "dobby" and choice == "2":
        typewriter ("You make Dobby the happiest elf. He taps and suddenly you find yourself in the Transfiguration Classroom")
        advance_to_room("Transfiguration Classroom")
    else:
        typewriter("Nothing much happens, but it was worth a try.")

def reveal_hidden_path():
    global map_skip_used
    if map_skip_used:
        typewriter("You've already used the map once. It fades away.")
    else:
        map_skip_used = True
        typewriter("You find a secret stairwell!")
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
            typewriter(f"You picked up the {item['name']}.")
            return

    typewriter("That item isn't here.")

def examine(item_name):
    for item in inventory + get_items_in_current_room():
        if item['name'].lower() == item_name.lower():
            typewriter(f"You examine the {item['name']}: {item['description']}")
            return
    typewriter("You can’t find that item to examine.")

def advance_to_room(target_room):
    global current_room, PEEVES_PRESENT

    # Determine room requirement
    current_req = next((r["requires"] for r in room_sequence if r["name"] == target_room), None)

    if target_room == "Staircase":
        if PEEVES_PRESENT:
            if not any(i['name'].lower() == "invisibility cloak" for i in inventory):
                typewriter("👻 Peeves blocks your way! You need the Invisibility Cloak to sneak past.")
                return
        else:
            if not any(i['name'].lower() in ["invisibility cloak", "marauder's map"] for i in inventory):
                typewriter("You need either the Invisibility Cloak or the Marauder’s Map to proceed.")
                return
    elif current_req:
        if not any(i['name'].lower() == current_req.lower() for i in inventory):
            typewriter(f"You need the {current_req} to enter {target_room}.")
            return

    current_room = target_room
    typewriter(f"You move into the {target_room}.")

    # Peeves only appears in Library
    PEEVES_PRESENT = (target_room == "Library" and random.random() < 0.5)
    if PEEVES_PRESENT:
        typewriter("👻 Peeves the Poltergeist appears! He cackles wildly. Try to sneak around him.")

    show_room_items()

    if target_room == "Transfiguration Classroom":
        if any(i['name'].lower() == "wand" for i in inventory):
            typewriter("✨ Professor McGonagall nods approvingly. You've made it with your wand. You win! ✨")
            sys.exit()
        else:
            typewriter("You're here... but no wand? Go back and find it!")

def game_intro():
    typewriter("\n🏰 Welcome to the Hogwarts Adventure Game!\n")
    typewriter("You wake up in the Gryffindor Common Room. Classes are about to begin.")
    typewriter("Your goal: Reach the Transfiguration Classroom – and don’t forget your wand!")
    typewriter("Collect magical tools, dodge Peeves, and unlock secret paths.")
    typewriter("Type commands like: pickup [item], use [item], examine [item], drop [item], or inventory. \n "
               "if you enter 'help', all commands will be displayed again")
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
        elif command.startswith("pickup "):
            pick_up(command[7:].strip())
        elif command.startswith("drop "):
            drop(command[5:].strip())
        elif command.startswith("use "):
            use(command[4:].strip())
        elif command.startswith("examine "):
            examine(command[8:].strip())
        elif command == "help":
            typewriter("Commands: inventory, pickup [item], drop [item], use [item], examine [item], help")
        else:
            typewriter("Unknown command. Try: pickup, use, examine, inventory, drop, pickup or help.")

if __name__ == "__main__":
    game_loop()
