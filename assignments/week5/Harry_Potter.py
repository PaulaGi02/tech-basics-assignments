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
