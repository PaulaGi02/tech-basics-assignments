import time

#start game "your potato destiny"
print("Welcome to your potato destiny. Today we want to find the perfect potato dish for \033[1myou\033[0m, because potato day is every day!")

time.sleep(3)
print("So lets start with your preferenced diet")

#diet preference
diet = input("\n would you like the dish to be vegetarian or vegan?").lower()

#potato role
role = input ("\n should the potato be the main ingredient or a sidekick?").lower()

#potato form
form = input ("\n would you like your potatoes mashed, whole or sliced").lower()

#cooking method
method = input("\n would you like to roast, bake or boil the potatoes? ").lower()

'''while True:
    try:
        time = int(input("\nHow long would you like your potatoes to cook. Give me a number from five to 90 minutes?"))
        if time <= 5 or time <= 90:
            break
        else:
            print("\nPlease enter a number between 5 and 90.")'''

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

if diet == "vegan":
    if role == "sidekick":
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

if diet == "vegetarian":
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

elif diet == "vegetarian":
     if role == "sidekick":
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


time.sleep(1)
print("\n🥔 Your ideal potato dish is...")
time.sleep(2)
print("\n✨ {result} ✨\n")
print("Happy cooking! 🍽️")

while True:
    rating = int(input("\nrate your potato destiny on a scale from 1 👎 to 10 👍?"))

    if rating <= 1 and rating <= 10:
        break

    else:
            print("\nPlease enter a number between 1 and 10.")