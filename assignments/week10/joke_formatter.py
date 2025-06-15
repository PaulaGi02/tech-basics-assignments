from colorama import Fore, Style
import emoji

# Animal-to-emoji map
animal_emojis = {
    "cow": "🐮",
    "tux": "🐧",
    "dragon": "🐉",
    "ghostbusters": "👻",
    "kitty": "🐱",
    "turkey": "🦃",
    "stegosaurus": "🦖",
    "daemon": "😈",
    "pig": "🐷",
    "cheese": "🧀",
    "turtle": "🐢",
    "milk": "🥛",
    "meow": "🐾",
    "stimpy": "😺",
    "beavis": "🤪"
}

# Supported animals list
supported_animals = list(animal_emojis.keys())

def format_joke(joke):
    # Add color and emojis to the joke text
    formatted = f"{Fore.YELLOW}{emoji.emojize(':laughing:')} {joke} {emoji.emojize(':cow:')}{Style.RESET_ALL}"
    return formatted
