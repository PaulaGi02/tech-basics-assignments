import random

user_input = int(input("Enter a number between 1 and 5: "))
mood = input("please enter a mood: choose between shocked, happy or dance")

shocked = [r"＜('0')＞¯", r"૮(°□°'˶)ა", r"( ˶°ㅁ°)", r"(⚆ᗝ⚆)", r"(⊙_⊙)"]
happy = [r"(๑ˇεˇ๑)", r"(◕‿◕✿)", r"/(≧∇≦)/", r"(●＾o＾●)", r"(＾▽＾)", r"( ˶ˆᗜˆ˵ )"]
dance = [r"ᕕ( ᐛ )ᕗ", r"¯\_(ツ)_/¯", r"(ง ˙˘˙ )ว", r"♪┏(・o･)┛♪", r"( ノ・・)ノ", r"(~‾⌣‾)~"]

random_shocked = random.sample(shocked, user_input)
random_happy = random.sample(happy, user_input)
random_dance = random.sample(dance, user_input)

if mood == "shocked":
    for _ in range(5):
        for emoji in random_shocked:
            print(emoji, end=' ')
        print()
elif mood == "happy":
    for _ in range(5):
        for emoji in random_happy:
            print(emoji, end=' ')
        print()
elif mood == "dance":
    for _ in range(5):
        for emoji in random_dance:
            print(emoji, end=' ')
        print()
else:
    print("Sorry, you typed in something wrong")