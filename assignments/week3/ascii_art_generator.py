import random
import time


while True:
    user_input = int(input("How many Emojis in a row do you want? Enter a number between 1 and 5: ").lower())
    if user_input <1 or user_input >5:
        print("Invalid input. Try again.")
    else:
        break

while True:
    mood = input("please enter a mood: choose between shocked, happy or dance").lower()
    if mood == "shocked" or mood == "happy" or mood == "dance":
        break
    else:
        print("Invalid input. Try again.")

while True:
    lines = int(input("How many lines do you want? Choose a number between 3 and 10 ").lower())
    if lines < 3 or lines > 10:
        print("Invalid input. Try again.")
    else:
        break


shocked = [r"＜('0')＞¯", r"૮(°□°'˶)ა", r"( ˶°ㅁ°)", r"(⚆ᗝ⚆)", r"(⊙_⊙)"]
happy = [r"(๑ˇεˇ๑)", r"(◕‿◕✿)", r"/(≧∇≦)/", r"(●＾o＾●)", r"(＾▽＾)", r"( ˶ˆᗜˆ˵ )"]
dance = [r"ᕕ( ᐛ )ᕗ", r"¯\_(ツ)_/¯", r"(ง ˙˘˙ )ว", r"♪┏(・o･)┛♪", r"( ノ・・)ノ", r"(~‾⌣‾)~"]

random_shocked = random.sample(shocked, user_input)
random_happy = random.sample(happy, user_input)
random_dance = random.sample(dance, user_input)

if mood == "shocked":
    for _ in range(lines):
        random_emojis = random.sample(shocked, user_input)
        for emoji in random_emojis:
            print(emoji, end=' ')
            time.sleep(0.1)
        print()
elif mood == "happy":
    for _ in range(lines):
        random_emojis = random.sample(happy, user_input)
        for emoji in random_emojis:
            print(emoji, end=' ')
            time.sleep(0.1)
        print()
elif mood == "dance":
    for _ in range(lines):
        random_emojis = random.sample(dance, user_input)
        for emoji in random_emojis:
            print(emoji, end=' ')
            time.sleep(0.1)
        print()
else:
    print("Sorry, you typed in something wrong")
