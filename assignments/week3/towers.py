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
                print(f"Please choose a number between {min_val} to {max_val} .")
        except ValueError:
            print("Please enter a valid number.")
# Function to get 1–5 user-specified symbols or choose random defaults
def get_symbol_input():
    while True:
        user_chars = input(
            "Please enter 1 to 5 signs to build the windows and facade (z. B.: #|[]+o),\n"
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
frames = [
    "[      ]",
    "[=     ]",
    "[==    ]",
    "[===   ]",
    "[ ===  ]",
    "[  === ]",
    "[   ===]",
    "[    ==]"
]

duration = 5  # seconds
start_time = time.time()

while time.time() - start_time < duration:
    for frame in frames:
        sys.stdout.write('\rLoading ' + frame)
        sys.stdout.flush()
        time.sleep(0.2)
        if time.time() - start_time >= duration:
            break
print("\nLoading complete!\n")


# Function to generate an individual ASCII building
def generate_building(height, width, symbol):
    building = []
    roof = "+" + "-"
    building.append(roof)
    door_row = "|" + " "
    door_width = 2
    mid = width // 2
    door_start = mid - door_width // 2
    door_row = (
            door_row[:door_start] + "[]" + door_row[door_start + door_width:]
    )
    building.append(door_row)
    return building

# Roof of the building
# Middle floors with chosen symbol
# Ground floor with centered door
# Main function controlling the program flow
def main():
    print("Welcome to the tower generator! 🏙️")
    time.sleep(1)

    # input
    number_of_buildings = get_int_input(
        "How many tower would you like to build? Choose a number between one and twenty: ", 1, 20
    )
    buildings_per_row = get_int_input(
        f"How many towers are supposed to be generated in one line? Choose a number between (1-{number_of_buildings}): ",
        1, number_of_buildings
    )
    building_symbols = get_symbol_input()

    loading_animation()

    print("\nYour skyline is ready! 🌆\n")

# Generate buildings with random height and chosen symbol
    buildings = []
    for _ in range(number_of_buildings):
        height = random.randint(5, 20)
        symbol = random.choice(building_symbols)
        width = 7
        building = generate_building(height, width, symbol)
        buildings.append((building, width))

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