import random
import time
import sys


# Function to get integer input within a given range
def get_int_input(prompt, min_val, max_val):
    while True:
        try:
            value = int(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"Please choose a number between {min_val} to {max_val}.")
        except ValueError:
            print("Please enter a valid number.")


# Function to get 1–5 user-specified symbols or choose random defaults
def get_symbol_input():
    while True:
        user_chars = input(
            "Please enter 1 to 5 signs to build the windows and facade (e.g.: #|[]+o),\n"
            "or press Enter for random characters: ")
        if user_chars == "":
            return ["#", "|", "+", "o", "[]"]
        elif 1 <= len(user_chars) <= 5 and all(
            c.isprintable() and c not in " ,"
            for c in user_chars
        ):
            return list(user_chars)
        else:
            print("Please enter 1-5 visible characters without spaces or commas.")


# Simulated loading animation shown before skyline is built
def loading_animation(duration=3):
    frames = [
        "[      ]", "[=     ]", "[==    ]", "[===   ]",
        "[ ===  ]", "[  === ]", "[   ===]", "[    ==]"
    ]

    start_time = time.time()
    while time.time() - start_time < duration:
        for frame in frames:
            sys.stdout.write('\rLade Skyline ' + frame)
            sys.stdout.flush()
            time.sleep(0.15)
            if time.time() - start_time >= duration:
                break


# Function to generate an individual ASCII building
def generate_building(height, width, symbol):
    building = []

    # Roof of the building
    roof = "+" + "-" * (width - 2) + "+"
    building.append(roof)

    # Middle floors with chosen symbol
    symbol_width = len(symbol)
    repeat_count = (width - 2) // symbol_width
    for _ in range(height - 2):  # Leave space for roof and ground floor
        content = (symbol * repeat_count).ljust(width - 2)
        row = "|" + content + "|"
        building.append(row)

    # Ground floor with centered door
    door_row = "|" + " " * (width - 2) + "|"
    door_width = 2
    mid = width // 2
    door_start = mid - door_width // 2
    door_row = (
        door_row[:door_start] + "[]" + door_row[door_start + door_width:]
    )
    building.append(door_row)

    return building  # Return list of strings representing the building


# Main function controlling the program flow
def main():
    print("Welcome to the tower generator! 🏙️")
    time.sleep(1)

    # User input
    number_of_buildings = get_int_input(
        "How many towers would you like to build? Choose a number between 1 and 20: ", 1, 20
    )
    buildings_per_row = get_int_input(
        f"How many towers should be in one row? (1-{number_of_buildings}): ",
        1, number_of_buildings
    )
    building_symbols = get_symbol_input()

    loading_animation()

    print("\nYour skyline is ready! 🌆\n")

    # Generate buildings with random height and chosen symbol
    buildings = []
    fixed_width = 14  # Ensures all symbols fit and buildings align
    for _ in range(number_of_buildings):
        height = random.randint(5, 20)
        symbol = random.choice(building_symbols)
        building = generate_building(height, fixed_width, symbol)
        buildings.append((building, fixed_width))


    for row_start in range(0, number_of_buildings, buildings_per_row):
        current_row_buildings = buildings[row_start:row_start + buildings_per_row]
        max_height = max(len(b[0]) for b in current_row_buildings)


        padded_buildings = []
        for building, width in current_row_buildings:
            padding = [" " * width] * (max_height - len(building))
            padded_buildings.append((padding + building, width))


        for line_index in range(max_height):
            for building_lines, width in padded_buildings:
                print(building_lines[line_index].ljust(width), end="   ")
            print()
        print()
        time.sleep(0.3)


# Run the program
if __name__ == "__main__":
    main()
