#This little game is ann interactive program that helps users discover their ideal potato dish based on preferences
import time
import sys

#constants
typewriter_speed = 0.02
DIET = ["vegetarian", "vegan"]
ROLE= ["main", "sidekick"]
FORM = ["mashed", "whole", "sliced"]
METHOD = ["boil", "roast", "bake"]

#Simulates a typewriter effect for printed text
def typewriter(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.02)

#Prints a message in a stylized box
def print_boxed(message):
    border = "═" * (len(message) + 4)
    print(f"╔{border}╗")
    print(f"║  {message}  ║")
    print(f"╚{border}╝")

#checks if input is valid
def user_choice(prompt, options):
    while True:
        choice = input(prompt).lower()
        if choice in options:
            return choice
        print("Please enter a valid option.")


#Returns the potato dish based on user preferences
def determine_potato_destiny(diet, role, form, method):
    # Define dish combinations
    dishes = {
        "vegan": {
            "main": {
                "whole": {
                    "boil": "Vegan Mashed Potato Bowl with Lentil Gravy",
                    "roast": "Vegan Roasted Whole Potatoes with Tahini Sauce",
                    "bake": "Vegan Baked Potatoes Stuffed with Spiced Chickpeas",
                },
                "sliced": {
                    "boil": "Warm Vegan Potato & Spinach Salad",
                    "roast": "Crispy Roasted Potato Wedges with Paprika",
                    "bake": "Vegan Potato Bake with Tomatoes & Zucchini",
                },
                "mashed": {
                    "boil": "Creamy Vegan Garlic Mashed Potatoes",
                    "roast": "Vegan Mashed Potato Patties",
                    "bake": "Vegan Shepherd’s Pie with Mashed Potato Top",
                },
            },
            "sidekick": {
                "whole": {
                    "boil": "Simple Boiled Potatoes with Olive Oil & Herbs",
                    "roast": "Garlic-Roasted Baby Potatoes",
                    "bake": "Oven-Baked Mini Potatoes with Sea Salt",
                },
                "sliced": {
                    "boil": "Sliced Potatoes with Lemon & Dill",
                    "roast": "Vegan Patatas Bravas",
                    "bake": "Layered Potato Gratin with Coconut Cream",
                },
                "mashed": {
                    "boil": "Fluffy Mashed Potatoes with Vegan Butter",
                    "roast": "Mashed Potato Balls with Crunchy Crust",
                    "bake": "Baked Vegan Duchess Potatoes",
                },
            },
        },
        "vegetarian": {
            "main": {
                "whole": {
                    "boil": "Mashed Potatoes with Cheese & Chives",
                    "roast": "Crispy Herb Roasted Potatoes with Feta",
                    "bake": "Baked Potatoes Stuffed with Broccoli & Cheese",
                },
                "sliced": {
                    "boil": "Sliced Potatoes in Creamy Spinach Sauce",
                    "roast": "Parmesan Roasted Potato Slices",
                    "bake": "Cheesy Potato & Tomato Bake",
                },
                "mashed": {
                    "boil": "Cheddar Mashed Potatoes",
                    "roast": "Mashed Potato Cakes with Sour Cream",
                    "bake": "Potato Casserole with Egg & Cheese",
                },
            },
            "sidekick": {
                "whole": {
                    "boil": "Buttered New Potatoes with Parsley",
                    "roast": "Garlic and Herb Roasted Potatoes",
                    "bake": "Baked Mini Potatoes with Cream Cheese",
                },
                "sliced": {
                    "boil": "Sliced Potatoes with Sour Cream Dressing",
                    "roast": "Cheesy Potato Slices with Thyme",
                    "bake": "Layered Potato Bake with Gruyère",
                },
                "mashed": {
                    "boil": "Creamy Mashed Potatoes with Nutmeg",
                    "roast": "Mashed Potato Puffs",
                    "bake": "Baked Mashed Potato Swirls with Cheese",
                },
            },
        }
    }

    return dishes.get(diet, {}).get(role, {}).get(form, {}).get(method,
        "Oops, that's not a valid combo. Potato wizard confused. 🧙‍♂️🥔")

#Game logic
#first the mane logic, that runs the game
def main():
    typewriter(
        "Welcome to your potato destiny. Today we want to find the perfect potato dish for \033[1myou\033[0m,\n 🥔 because potato day is every day🥔!", )
    time.sleep(3)
    typewriter("\nSo let's start with your preferred diet\n")


diet = user_choice("\nwould you like the dish to be \033[1mvegetarian\033[0m or \033[1mvegan\033[0m?🍃", DIET)
role = user_choice("\nshould the potato be the \033[1mmain\033[0m ingredient or a \033[1msidekick\033[0m?🍽️", ROLE)
form = user_choice("\nwould you like your potatoes \033[1mmashed\033[0m, \033[1mwhole\033[0m or \033[1msliced\033[0m?🍠", FORM)
method = user_choice("\nwould you like to \033[1mroast\033[0m, \033[1mbake\033[0m or \033[1mboil\033[0m the potatoes?🔥", METHOD)

# Reveal the potato destiny
typewriter("\n🥔 Your ideal potato dish is...\n")
time.sleep(2)
final_dish = determine_potato_destiny(diet, role, form, method)
print_boxed(final_dish)

while True:
    try:
        rating = int(input("\nRate your potato destiny on a scale from 1 👎 to 10 👍: "))
        if 1 <= rating <= 10:
            print("Thanks for your feedback! 🥔✨")
            break
        else:
            print("Please enter a number between 1 and 10.")
    except ValueError:
        print("Please enter a valid number.")

# ==== RUN ====
if __name__ == "__main__":
    main()