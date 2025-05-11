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
        {"name": "Invisibility Cloak", "type": "tool", "description": "Makes you invisible to Peeves."},
        {"name": "Spellbook", "type": "tool", "description": "Contains powerful spells for advanced wizards."},
        {"name": "Quill of Quick Quotes", "type": "tool",
         "description": "Writes down everything you say, often exaggerated."},
        {"name": "Marauder's Map", "type": "tool", "description": "Reveals hidden rooms."},
    ],
    "Staircase": [
        {"name": "Marauder's Map", "type": "tool", "description": "Reveals hidden rooms."},
        {"name": "Vanishing Cabinet Handle", "type": "junk", "description": "A broken part from a Vanishing Cabinet."},
        {"name": "Exploding Snap Cards", "type": "game", "description": "Be careful! They might explode in your hand."}
    ],
    "Hidden Hallway": [
        {"name": "Wand", "type": "tool", "description": "Used to cast spells."},
        {"name": "Dobby", "type": "toy", "description": "A tiny elf, sometimes searching for trouble."},
        {"name": "Chocolate Frog", "type": "food", "description": "Restores energy."}
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


# Helpers
def get_items_in_current_room():
    return rooms[current_room]


def show_inventory():
    if not inventory:
        typewriter("You're not carrying anything.")
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


def present_item_options(item):
    name = item['name'].lower()
    if name == "key":
        options = ["Try to open a nearby locked door.", "Scratch your name into the wood.",
                   "Drop it and kick it around like a football."]
    elif name == "marauder's map":
        options = ["Fold it into a paper hat.", "Tap it and say 'Mischief Managed'.", "Use it to find a hidden path."]
    elif name == "pumpkin juice":
        options = ["Drink it.", "Throw it on the wall.", "Use it to water a plant."]
    elif name == "chocolate frog":
        options = ["Eat it.", "Let it hop around.", "Trade it with a friend."]
    elif name == "wand":
        options = ["Cast Lumos.", "Use it as a drumstick.", "Try to transfigure your shoe."]
    elif name == "invisibility cloak":
        options = ["Put it on your head.", "Use it to make shadow puppets.", "Bundle it like a pillow."]
    elif name == "dobby":
        options = ["Command Dobby to moonwalk.", "Give him a tiny sock.", "Give him a high five."]
    else:
        options = ["Put it in your pocket.", "Sniff it cautiously.", "Tap it on your head."]

    typewriter("What would you like to do with the item? Choose a number: 1,2 or 3.")
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
        typewriter("You were able to sneak quietly through the library and enter the staircase.")
        advance_to_room("Staircase")
    elif name == "dobby" and choice == "1":
        typewriter("Dobby busts out a moonwalk. It's oddly inspiring.")
    elif name == "dobby" and choice == "2":
        typewriter(
            "You make Dobby the happiest elf. He taps and suddenly you find yourself in the Transfiguration Classroom.")
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
            get_items_in_current_room().remove(item)
            typewriter(f"You picked up {item['name']}.")
            return

    typewriter("That item isn't here.")


def drop(item_name):
    for item in inventory:
        if item['name'].lower() == item_name.lower():
            inventory.remove(item)
            rooms[current_room].append(item)
            typewriter(f"You dropped {item['name']}.")
            return
    typewriter("You don’t have that item to drop.")


def examine(item_name):
    for item in inventory + get_items_in_current_room():
        if item['name'].lower() == item_name.lower():
            typewriter(f"You examine {item['name']}: {item['description']}")
            return
    typewriter("You can’t find that item to examine.")


def use(item_name):
    global map_skip_used
    for item in inventory:
        if item['name'].lower() == item_name.lower():
            item_name_lower = item['name'].lower()

            if item_name_lower == "marauder's map":
                if current_room == "Library":
                    if PEEVES_PRESENT:
                        typewriter("👻 Peeves is causing chaos in the Library! You can't focus on the map right now.")
                        return
                    if not map_skip_used:
                        map_skip_used = True
                        typewriter("The map glows and reveals a hidden hallway behind the bookshelves!")
                        advance_to_room("Hidden Hallway")
                    return

                elif current_room == "Staircase":
                    if not map_skip_used:
                        map_skip_used = True
                        typewriter("You tap the Marauder's Map and it reveals a hidden stairwell!")
                        advance_to_room("Hidden Hallway")
                    return
                else:
                    typewriter("You can’t use the map here.")
                    return

            if item_name_lower == "invisibility cloak":
                if current_room == "Library":
                    typewriter("You wear the Invisibility Cloak and sneak past Peeves.")
                    advance_to_room("Staircase")
                else:
                    typewriter("You hide under the cloak, but nothing interesting happens here.")
                return

            # Default option menu for other items
            present_item_options(item)
            return

    typewriter("You're not carrying that item.")




def advance_to_room(target_room):
    global current_room, PEEVES_PRESENT

    if target_room == "Staircase":
        if PEEVES_PRESENT:
            if not any(i['name'].lower() == "invisibility cloak" for i in inventory):
                typewriter("👻 Peeves blocks your way! You need the Invisibility Cloak to sneak past.")
                return
        else:
            if not any(i['name'].lower() in ["invisibility cloak", "marauder's map"] for i in inventory):
                typewriter("You need either the Invisibility Cloak or the Marauder’s Map to proceed.")
                return

    elif target_room == "Hidden Hallway":
        if not map_skip_used:
            if not any(i['name'].lower() == "marauder's map" for i in inventory):
                typewriter("You need the Marauder’s Map to find the hidden hallway.")
                return

    elif target_room == "Transfiguration Classroom":
        if not any(i['name'].lower() == "wand" for i in inventory):
            typewriter("You’re here… but no wand? McGonagall looks disappointed!")
            sys.exit()

    # Move to room
    current_room = target_room
    typewriter(f"You move into the {target_room}.")

    if target_room == "Transfiguration Classroom":
        typewriter("✨ Professor McGonagall nods approvingly. You've made it with your wand. You win! ✨")
        sys.exit()
    elif target_room == "Library":
        PEEVES_PRESENT = random.random() < 0.5
        if PEEVES_PRESENT:
            typewriter("👻 Peeves the Poltergeist appears! He cackles wildly. Try to sneak around him.")
    show_room_items()



def show_help():
    typewriter("Available commands:")
    typewriter("- look: view items in the room")
    typewriter("- inventory: check what you’re carrying")
    typewriter("- pickup [item]")
    typewriter("- drop [item]")
    typewriter("- examine [item]")
    typewriter("- use [item]")
    typewriter("- help")
    typewriter("- quit")


def game_intro():
    typewriter("\n🏰 Welcome to the Hogwarts Adventure Game!\n")
    typewriter("You wake up in the Gryffindor Common Room. Classes are about to begin.")
    typewriter("Your goal: Reach the Transfiguration Classroom – and don’t forget your wand!")
    typewriter("Collect magical tools, dodge Peeves, and unlock secret paths.")
    typewriter("Type commands like: pickup [item], use [item], drop [item], examine [item], inventory, or help\n")
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
        elif command == "help":
            show_help()
        elif command.startswith("pickup "):
            pick_up(command[7:].strip())
        elif command.startswith("drop "):
            drop(command[5:].strip())
        elif command.startswith("examine "):
            examine(command[8:].strip())
        elif command.startswith("use "):
            use(command[4:].strip())
        else:
            typewriter("Unknown command. Try: pickup, drop, examine, use, inventory, or help.")


if __name__ == "__main__":
    game_loop()
