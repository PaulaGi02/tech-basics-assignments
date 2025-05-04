# This little game is ann interactive program that helps users discover their ideal potato dish based on preferences
import time
import sys

# constants
typewriter_speed = 0.02
DIET = ["vegetarian", "vegan"]
ROLE = ["main", "sidekick"]
FORM = ["mashed", "whole", "sliced"]
METHOD = ["boil", "roast", "bake"]


# Simulates a typewriter effect for printed text
def typewriter(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.02)


# Prints a message in a stylized box
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

#defining rating logic
def get_rating():
    while True:
        try:
            rating = int(input("\nRate your potato destiny on a scale from 1 👎 to 10 👍: "))
            if 1 <= rating <= 10:
                return rating
            print("Please enter a number between 1 and 10.")
        except ValueError:
            print("Please enter a valid number.")


# Returns the potato dish based on user preferences
def determine_potato_destiny(diet, role, form, method):
    #nested dictionary with all options and results
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
    #this line gets final recipe from nested dictionary
    return dishes.get(diet, {}).get(role, {}).get(form, {}).get(method, "Oops, that's not a valid combo. Potato wizard confused. 🧙‍♂️🥔")


#Game logic
#Collects user choices for diet, role, form, and method
def get_user_preferences():
    diet = user_choice("\nWould you like the dish to be vegetarian or vegan?🍃 ", DIET)
    role = user_choice("\nShould the potato be the main ingredient or a sidekick?🍽️ ", ROLE)
    form = user_choice("\nWould you like your potatoes mashed, whole or sliced?🍠 ", FORM)
    method = user_choice("\nWould you like to roast, bake or boil the potatoes?🔥 ", METHOD)
    return diet, role, form, method

#game process
def main():
    typewriter(
        "Welcome to your potato destiny. Today we want to find the perfect potato dish for \033[1myou\033[0m,\n 🥔 because potato day is every day! 🥔")
    time.sleep(2)
    typewriter("\nSo let's start with your preferred diet.\n")

    diet, role, form, method = get_user_preferences()

    typewriter("\n🥔 Your ideal potato dish is...\n")
    time.sleep(2)
    final_dish = determine_potato_destiny(diet, role, form, method)
    print_boxed(final_dish)

    rating = get_rating()
    print("Thanks for your feedback! 🥔✨")

# run
main()
