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