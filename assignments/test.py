import time
import sys

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

while True:
    for frame in frames:
        sys.stdout.write('\r' + frame)
        sys.stdout.flush()
        time.sleep(0.2)