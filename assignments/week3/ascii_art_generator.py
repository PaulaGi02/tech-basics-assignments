import random


my_list = [r"¯\_(ツ)_/¯", r"=^_^=", r"(ಥ﹏ಥ)"]
random.shuffle(my_list)

for _ in range(5):
    for emoji in my_list:
        print(emoji, end=' ')
    print()
