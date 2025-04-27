import random
import time
import sys

while True:
    user_input = int(input("How many Emojis in a row do you want? Enter a number between 1 and 5: ").lower())
    if user_input <1 or user_input >5:
        print("Invalid input. Try again.")
    else:
        break

while True:
    mood = input("please enter a mood: choose between \033[1mshocked\033[0m, \033[1mhappy\033[0m or \033[1mdance\033[0m: ").lower()
    if mood == "shocked" or mood == "happy" or mood == "dance":
        break
    else:
        print("Invalid input. Try again.")

while True:
    lines = int(input("How many lines do you want? Choose a number between 3 and 10: ").lower())
    if lines < 3 or lines > 10:
        print("Invalid input. Try again.")
    else:
        break

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

shocked = [r"＜('0')＞¯", r"૮(°□°'˶)ა", r"( ˶°ㅁ°)", r"(⚆ᗝ⚆)", r"(⊙_⊙)"]
happy = [r"(๑ˇεˇ๑)", r"(◕‿◕✿)", r"/(≧∇≦)/", r"(●＾o＾●)", r"(＾▽＾)", r"( ˶ˆᗜˆ˵ )"]
dance = [r"ᕕ( ᐛ )ᕗ", r"¯\_(ツ)_/¯", r"(ง ˙˘˙ )ว", r"♪┏(・o･)┛♪", r"( ノ・・)ノ", r"(~‾⌣‾)~"]

random_shocked = random.sample(shocked, user_input)
random_happy = random.sample(happy, user_input)
random_dance = random.sample(dance, user_input)

if mood == "shocked":
    for _ in range(lines):
        random_emojis = random.sample(shocked, user_input)
        print(' ' * 10, end='')
        for emoji in random_emojis:
            print(emoji, end=' ')
            sleep_time = 0.15
        print()
elif mood == "happy":
    for _ in range(lines):
        random_emojis = random.sample(happy, user_input)
        print(' ' * 10, end='')
        for emoji in random_emojis:
            print(emoji, end=' ')
            time.sleep(0.1)
        print()
elif mood == "dance":
    for _ in range(lines):
        random_emojis = random.sample(dance, user_input)
        print(' ' * 10, end='')
        for emoji in random_emojis:
            print(emoji, end=' ')
            sleep_time = 0.05
        print()
else:
    print("Sorry, you typed in something wrong")


