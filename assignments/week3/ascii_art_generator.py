import random


shocked = [r"＜('0')＞¯", r"૮(°□°'˶)ა", r"( ˶°ㅁ°)", r"(⚆ᗝ⚆)", r"(⊙_⊙)"]
happy = [r"(๑ˇεˇ๑)", r"(◕‿◕✿)", r"/(≧∇≦)/", r"(●＾o＾●)", r"(＾▽＾)", r"( ˶ˆᗜˆ˵ )"]
dance = [r"ᕕ( ᐛ )ᕗ", r"¯\_(ツ)_/¯", r"(ง ˙˘˙ )ว", r"♪┏(・o･)┛♪", r"( ノ・・)ノ", r"(~‾⌣‾)~"]

three_random_shocked = random.sample(shocked, 3)
three_random_happy = random.sample(happy, 3)
three_random_dance = random.sample(dance, 3)

for _ in range(5):
    for emoji in three_random_shocked:
        print(emoji, end=' ')
    print()