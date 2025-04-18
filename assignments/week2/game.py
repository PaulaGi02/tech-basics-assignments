import time

#start game "your potato destiny"
print("Welcome to your potato destiny. Today we want to find the perfect patato dish for \033[1myou\033[0m,\nbecause potato day is every day!")
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

#time effort
while True:
    try:
        time = int(input("\nHow long would you like your potatoes to cook. Give me a number from five to 90 minutes?"))
        if time <= 5 or time <= 90:
            break
        else:
            print("\nPlease enter a number between 5 and 90.")

#end recipe
if diet == "vegan":
    if role == "main":
        if form == "whole" and method == "boil" and time <=40:
            result = "Vegan Mashed Potato Bowl with Lentil Gravy"
        elif form == "whole" and method == "roast" and time <=50:
            result = "Vegan Roasted Whole Potatoes with Tahini Sauce"
        elif form == "whole" and method == "bake" and time <=40:
            result = "Vegan Baked Potatoes Stuffed with Spiced Chickpeas"
        elif form == "sliced" and method == "boil" and time <=30:
            result = "Warm Vegan Potato & Spinach Salad"
        elif form == "sliced" and method == "roast" and time <=40:
            result = "Crispy Roasted Potato Wedges with Paprika"
        elif form == "sliced" and method == "bake" and time <=30:
            result = "Vegan Potato Bake with Tomatoes & Zucchini"
        elif form == "mashed" and method == "boil" and time <=40:
            result = "Creamy Vegan Garlic Mashed Potatoes"
        elif form == "mashed" and method == "roast" and time <=30:
            result = "Vegan Mashed Potato Patties"
        elif form == "mashed" and method == "bake" and time >=50:
            result = "Vegan Shepherd’s Pie with Mashed Potato Top"

if diet == "vegan":
    if role == "sidekick":
        if form == "whole" and method == "boil" and time <= 30:
            result = "Vegan Mashed Potato Bowl with Lentil Gravy"
        elif form == "whole" and method == "roast" and time <= 30:
            result = ""
        elif form == "whole" and method == "bake" and time <= 30:
            result = ""
        elif form == "sliced" and method == "boil" and time <= 30:
            result = ""
        elif form == "sliced" and method == "roast" and time <= 30:
            result = ""
        elif form == "sliced" and method == "bake" and time <= 30:
            result = ""
        elif form == "mashed" and method == "boil" and time <= 30:
            result = ""
        elif form == "mashed" and method == "roast" and time <= 30:
            result = ""
        elif form == "mashed" and method == "bake" and time <= 30:
            result = ""

if diet == "vegetarian":
     if role == "main":
        if form == "whole" and method == "boil" and time <= 30:
            result = "Vegan Mashed Potato Bowl with Lentil Gravy"
        elif form == "whole" and method == "roast" and time <= 30:
            result = ""
        elif form == "whole" and method == "bake" and time <= 30:
            result = ""
        elif form == "sliced" and method == "boil" and time <= 30:
            result = ""
        elif form == "sliced" and method == "roast" and time <= 30:
            result = ""
        elif form == "sliced" and method == "bake" and time <= 30:
            result = ""
        elif form == "mashed" and method == "boil" and time <= 30:
            result = ""
        elif form == "mashed" and method == "roast" and time <= 30:
            result = ""
        elif form == "mashed" and method == "bake" and time <= 30:
            result = ""

if diet == "vegetarian":
     if role == "sidekick":
        if form == "whole" and method == "boil" and time <= 30:
            result = "Vegan Mashed Potato Bowl with Lentil Gravy"
        elif form == "whole" and method == "roast" and time <= 30:
            result = ""
        elif form == "whole" and method == "bake" and time <= 30:
            result = ""
        elif form == "sliced" and method == "boil" and time <= 30:
            result = ""
        elif form == "sliced" and method == "roast" and time <= 30:
            result = ""
        elif form == "sliced" and method == "bake" and time <= 30:
            result = ""
        elif form == "mashed" and method == "boil" and time <= 30:
            result = ""
        elif form == "mashed" and method == "roast" and time <= 30:
            result = ""
        elif form == "mashed" and method == "bake" and time <= 30:
            result = ""
else:
    result = "Oops, that's not a valid diet. Potato wizard confused. 🧙‍♂️🥔"