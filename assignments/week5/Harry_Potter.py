inventory = []

# Items available in Gryffindor Common Room
items_in_room = [{"name": "Wand", "type": "tool", "description": "Used to cast spells."},
                 {"name": "Marauder's Map", "type": "tool", "description": "Reveals hidden rooms."},
                 {"name": "Chocolate Frog", "type": "food", "description": "Restores energy."},
                 {"name": "Broken Quill", "type": "junk", "description": "Doesn't work anymore."},
                 {"name": "Invisibility Cloak", "type": "tool", "description": "Makes you invisible to Peeves."},
                 {"name": "Pumpkin Juice", "type": "food", "description": "A tasty Hogwarts drink."}
                 ]
MAX_INVENTORY_SIZE = 5


# displays all items you are carrying
def show_inventory():
    if len(inventory) == 0:
        print("inventory is empty")
    else:
        print("You are carrying: ")
        for items in inventory:
            print(f"- {items['name']}")

# displays all items currently in the room
def show_room_items():
    if len(inventory) == 0:
        print("the room is empty")
    else:
        print("You are carrying: ")
        for items in items_in_room:
            print(f"- {items['name']}: {items['description']}")

# picking up items
def pick_up(item_name):
    if len(inventory) >= MAX_INVENTORY_SIZE:
        print("Your inventory is full")
        return

    for item in items_in_room:
        if item['name'].lower() == item_name.lower():
            inventory.append(item)
            items_in_room.remove(item)
            print(f"You've picked up {item['name']}.")
            return

        print(f"There's no {item_name} here.")

#dropping items
def drop_item(item_name):
    for item in items_in_room:
        if item['name'].lower() == item_name.lower():
            inventory.remove(item)
            items_in_room.append(item)
            print(f"You've dropped {item['name']}.")
            return
        print(f"There's no {item_name} in your inventory.")

#use_items
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

#examine item
def examine (item_name):
    for item in inventory:
        if item['name'].lower() == item_name.lower():
            print(f"{item['type']}: {item['description']}")
            return

    for item in items_in_room:
        if item['name'].lower() == item_name.lower():
            print(f"{item['type']}: {item['description']}")
            return

    print(f"You don't see any item called {item_name}.")

#rooms
rooms = {
    "Common Room": [
        {"name": "Wand", "type": "tool", "description": "Used to cast spells."}
    ],
    "Library": [
        {"name": "Marauder's Map", "type": "tool", "description": "Reveals hidden rooms."}
    ],
    "Staircase": [
        {"name": "Chocolate Frog", "type": "food", "description": "Restores energy."}
    ],
    "Hidden Hallway": [],  # Only becomes accessible with Map
    "Transfiguration Classroom": []  # Final room
}
current_room = "Common Room"

def get_items_in_current_room():
    return rooms[current_room]

def move(room_name):
    global current_room
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

    # Check for victory
    if current_room == "Transfiguration Classroom":
        has_wand = any(item['name'].lower() == "wand" for item in inventory)
        if has_wand:
            print("✨ Professor McGonagall nods approvingly. You've made it to class with your wand. You win! ✨")
            exit()
        else:
            print("You made it to the classroom, but you forgot your wand! Go back and get it.")

def game_loop ():
    elif command.startswith("go "):
    room_name = command[3:].title()  # capitalize first letter
    move(room_name)