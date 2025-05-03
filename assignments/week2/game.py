#This little game is ann interactive program that helps users discover their ideal potato dish based on preferences

import time, sys

#constants
typewriter_speed = 0.02
diets = ["vegetarian", "vegan"]
role= ["main", "sidekick"]
form = ["mashed", "whole", "sliced"]
method = ["boil", "roast", "bake"]

#design functions
def typewriter(text): #simulates a typewriter effect
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.02)

def print_boxed(message): #prints message in a box to highlight it
    border = "═" * (len(message) + 4)
    print(f"╔{border}╗")
    print(f"║  {message}  ║")
    print(f"╚{border}╝")

# Set default fallback result
result = "Oops, that's not a valid diet. You have probably spelled something wrong. Potato wizard confused. 🧙‍♂️🥔"

#start game "your potato destiny"
typewriter ("Welcome to your potato destiny. Today we want to find the perfect potato dish for \033[1myou\033[0m,\n 🥔 because potato day is every day🥔!",)
time.sleep(3)
typewriter ("\nSo let's start with your preferred diet\n")


while True:
    diet = str(input("\nwould you like the dish to be \033[1mvegetarian\033[0m or \033[1mvegan\033[0m?🍃").lower())

    if diet == "vegetarian" or diet == "vegan":
        break

    else:
        print ("Please enter a valid diet type.")

while True:
    role = str(input("\nshould the potato be the \033[1mmain\033[0m ingredient or a \033[1msidekick\033[0m?🍽️").lower())

    if role == "main" or role == "sidekick":
        break

    else:
        print ("Please enter a valid option.")

while True:
    form = str(input("\nwould you like your potatoes \033[1mmashed\033[0m, \033[1mwhole\033[0m or \033[1msliced\033[0m?🍠").lower())

    if form == "mashed" or form == "whole" or form == "sliced":
        break

    else:
        print ("Please enter a valid option.")


while True:
    method = str(input("\nwould you like to \033[1mroast\033[0m, \033[1mbake\033[0m or \033[1mboil\033[0m the potatoes?🔥").lower())

    if method == "roast" or method == "bake" or method == "boil":
        break

    else:
        print ("Please enter a valid option.")


#end recipe
if diet == "vegan":
    if role == "main":
        if form == "whole" and method == "boil":
            result = "Vegan Mashed Potato Bowl with Lentil Gravy"
        elif form == "whole" and method == "roast":
            result = "Vegan Roasted Whole Potatoes with Tahini Sauce"
        elif form == "whole" and method == "bake":
            result = "Vegan Baked Potatoes Stuffed with Spiced Chickpeas"
        elif form == "sliced" and method == "boil":
            result = "Warm Vegan Potato & Spinach Salad"
        elif form == "sliced" and method == "roast":
            result = "Crispy Roasted Potato Wedges with Paprika"
        elif form == "sliced" and method == "bake":
            result = "Vegan Potato Bake with Tomatoes & Zucchini"
        elif form == "mashed" and method == "boil":
            result = "Creamy Vegan Garlic Mashed Potatoes"
        elif form == "mashed" and method == "roast":
            result = "Vegan Mashed Potato Patties"
        elif form == "mashed" and method == "bake":
            result = "Vegan Shepherd’s Pie with Mashed Potato Top"

    elif role == "sidekick":
        if form == "whole" and method == "boil":
            result = "Simple Boiled Potatoes with Olive Oil & Herbs"
        elif form == "whole" and method == "roast":
            result = "Garlic-Roasted Baby Potatoes"
        elif form == "whole" and method == "bake":
            result = "Oven-Baked Mini Potatoes with Sea Salt"
        elif form == "sliced" and method == "boil":
            result = "Sliced Potatoes with Lemon & Dill"
        elif form == "sliced" and method == "roast":
            result = "Vegan Patatas Bravas"
        elif form == "sliced" and method == "bake":
            result = "Layered Potato Gratin with Coconut Cream"
        elif form == "mashed" and method == "boil":
            result = "Fluffy Mashed Potatoes with Vegan Butter"
        elif form == "mashed" and method == "roast":
            result = "Mashed Potato Balls with Crunchy Crust"
        elif form == "mashed" and method == "bake":
            result = "Baked Vegan Duchess Potatoes"

elif diet == "vegetarian":
     if role == "main":
        if form == "whole" and method == "boil":
            result = "Mashed Potatoes with Cheese & Chives"
        elif form == "whole" and method == "roast":
            result = "Crispy Herb Roasted Potatoes with Feta"
        elif form == "whole" and method == "bake":
            result = "Baked Potatoes Stuffed with Broccoli & Cheese"
        elif form == "sliced" and method == "boil":
            result = "Sliced Potatoes in Creamy Spinach Sauce"
        elif form == "sliced" and method == "roast":
            result = "Parmesan Roasted Potato Slices"
        elif form == "sliced" and method == "bake":
            result = "Cheesy Potato & Tomato Bake"
        elif form == "mashed" and method == "boil":
            result = "Cheddar Mashed Potatoes"
        elif form == "mashed" and method == "roast":
            result = "Mashed Potato Cakes with Sour Cream"
        elif form == "mashed" and method == "bake":
            result = "Potato Casserole with Egg & Cheese"


     elif role == "sidekick":
        if form == "whole" and method == "boil":
            result = "Buttered New Potatoes with Parsley"
        elif form == "whole" and method == "roast":
            result = "Garlic and Herb Roasted Potatoes"
        elif form == "whole" and method == "bake":
            result = "Baked Mini Potatoes with Cream Cheese"
        elif form == "sliced" and method == "boil":
            result = "Sliced Potatoes with Sour Cream Dressing"
        elif form == "sliced" and method == "roast":
            result = "Cheesy Potato Slices with Thyme"
        elif form == "sliced" and method == "bake":
            result = "Layered Potato Bake with Gruyère"
        elif form == "mashed" and method == "boil":
            result = "Creamy Mashed Potatoes with Nutmeg"
        elif form == "mashed" and method == "roast":
            result = "Mashed Potato Puffs"
        elif form == "mashed" and method == "bake":
            result = "Baked Mashed Potato Swirls with Cheese"
else:
    result = "Oops, that's not a valid diet. Potato wizard confused. 🧙‍♂️🥔"

# Reveal the potato destiny
time.sleep(1)
typewriter ("\n🥔 Your ideal potato dish is... \n" )
time.sleep(3)

print_boxed (result)


while True:
    rating = int(input("\nrate your potato destiny on a scale from 1 👎 to 10 👍?"))

    if rating < 1 or rating > 10:
        print("\nPlease enter a number between 1 and 10.")

    else:
            break