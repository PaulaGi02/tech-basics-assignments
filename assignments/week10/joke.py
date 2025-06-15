import pyjokes
import cowsay
import random
from joke_formatter import format_joke, supported_animals, animal_emojis

joke = pyjokes.get_joke()
colored_joke = format_joke(joke)

random_animal = random.choice(supported_animals)
emoji = animal_emojis.get(random_animal, "🎭")

cowsay_func = getattr(cowsay, random_animal)
cowsay_func(colored_joke)

print(f"\nToday's speaker: {random_animal} {emoji}\n")
