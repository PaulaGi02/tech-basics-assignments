inventory = []
MAX_INVENTORY_SIZE = 5

rooms = {
    "Common Room": [
        {"name": "Wand", "type": "tool", "description": "Used to cast spells."},
        {"name": "Marauder's Map", "type": "tool", "description": "Reveals hidden rooms."},
        {"name": "Chocolate Frog", "type": "food", "description": "Restores energy."},
        {"name": "Broken Quill", "type": "junk", "description": "Doesn't work anymore."},
        {"name": "Invisibility Cloak", "type": "tool", "description": "Makes you invisible to Peeves."},
        {"name": "Pumpkin Juice", "type": "food", "description": "A tasty Hogwarts drink."}
    ],
    "Library": [],
    "Staircase": [],
    "Hidden Hallway": [],
    "Transfiguration Classroom": []
}
current_room = "Common Room"

# Utility
def get_items_in_current_room():
    return rooms[current_room]

# Display Inventory
def show_inventory():
    if len(inventory) == 0:
        print("Inventory is empty.")
    else:
        print("You are carrying:")
        for item in inventory:
            print(f"- {item['name']}")

# Display Room Items
def show_room_items():
    items_in_room = get_items_in_current_room()
    if len(items_in_room) == 0:
        print("The room is empty.")
    else:
        print(f"In the {current_room}, you see:")
        for item in items_in_room:
            print(f"- {item['name']}: {item['description']}")

# Pick Up
def pick_up(item_name):
    items_in_room = get_items_in_current_room()
    if len(inventory) >= MAX_INVENTORY_SIZE:
        print("Your inventory is full.")
        return

    for item in items_in_room:
        if item['name'].lower() == item_name.lower():
            inventory.append(item)
            items_in_room.remove(item)
            print(f"You picked up the {item['name']}.")
            return

    print(f"There is no {item_name} here.")

# Drop
def drop_item(item_name):
    for item in inventory:
        if item['name'].lower() == item_name.lower():
            inventory.remove(item)
            get_items_in_current_room().append(item)
            print(f"You dropped the {item['name']}.")
            return
    print(f"You don’t have {item_name} in your inventory.")

# Use Item
def use(item_name):
    for item in inventory:
        if item['name'].lower() == item_name.lower():
            if item['type'] == "food":
                print(f"You eat the {item['name']}. You feel refreshed.")
                inventory.remove(item)
            elif item['type'] == "tool":
                if item['name'].lower() == "wand":
                    print("You cast Lumos. The hallway lights up.")
                elif item['name'].lower() == "marauder's map":
                    print("You unfold the Marauder’s Map. A hidden path is revealed.")
                elif item['name'].lower() == "invisibility cloak":
                    print("You vanish under the Invisibility Cloak.")
                else:
                    print(f"You use the {item['name']}, but nothing happens.")
            else:
                print("You can’t use that.")
            return
    print(f"You don’t have {item_name} in your inventory.")

# Examine
def examine(item_name):
    for item in inventory:
        if item['name'].lower() == item_name.lower():
            print(f"{item['type']}: {item['description']}")
            return

    for item in get_items_in_current_room():
        if item['name'].lower() == item_name.lower():
            print(f"{item['type']}: {item['description']}")
            return

    print(f"You don't see any item called '{item_name}'.")

# Move Between Rooms
def move(room_name):
    global current_room
    room_name = room_name.title()

    if room_name not in rooms:
        print("That room doesn't exist.")
        return

    if room_name == "Hidden Hallway":
        has_map = any(item['name'].lower() == "marauder's map" for item in inventory)
        if not has_map:
            print("You need the Marauder’s Map to find that room.")
            return

    current_room = room_name
    print(f"You move to the {room_name}.")
    show_room_items()

    # Check victory
    if current_room == "Transfiguration Classroom":
        has_wand = any(item['name'].lower() == "wand" for item in inventory)
        if has_wand:
            print("✨ Professor McGonagall nods approvingly. You've made it to class with your wand. You win! ✨")
            exit()
        else:
            print("You made it to the classroom, but you forgot your wand! Go back and get it.")

# Game Loop
def game_loop():
    print("🏰 Welcome to Hogwarts Adventure!")
    print("Type 'help' to see a list of commands.")

    while True:
        command = input("\n> ").strip().lower()

        if command == "help":
            print("Commands:")
            print("  inventory - Show your items")
            print("  look - Look around the room")
            print("  pickup [item] - Pick up an item")
            print("  drop [item] - Drop an item")
            print("  use [item] - Use an item")
            print("  examine [item] - Look at an item")
            print("  go [room] - Move to another room")
            print("  quit - Exit game")

        elif command == "inventory":
            show_inventory()

        elif command == "look":
            show_room_items()

        elif command.startswith("pickup "):
            pick_up(command[7:].strip())

        elif command.startswith("drop "):
            drop_item(command[5:].strip())

        elif command.startswith("use "):
            use(command[4:].strip())

        elif command.startswith("examine "):
            examine(command[8:].strip())

        elif command.startswith("go "):
            move(command[3:].strip())

        elif command == "quit":
            print("Thanks for playing! Goodbye.")
            break

        else:
            print("Unknown command. Type 'help' for a list.")

# Start Game
if __name__ == "__main__":
    game_loop()
