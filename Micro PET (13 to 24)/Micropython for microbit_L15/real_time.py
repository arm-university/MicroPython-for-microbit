# Add your Python code here. E.g.
from microbit import *

while True:
    temp = temperature()
    if temp > 26:
        display.scroll("Hot")
    elif temp > 6 < 15:    
        display.scroll("Just right")
    else:
        display.scroll("Too cold")