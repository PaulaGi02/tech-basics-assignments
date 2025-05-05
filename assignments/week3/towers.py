import random
import time
import sys


# Function to get integer input within a given range
# Function to get 1–5 user-specified symbols or choose random defaults
# Simulated loading animation shown before skyline is built
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


# Function to generate an individual ASCII building
# Roof of the building
# Middle floors with chosen symbol
# Ground floor with centered door
# Main function controlling the program flow
# Generate buildings with random height and chosen symbol
# Run the program
if __name__ == "__main__":
    main()