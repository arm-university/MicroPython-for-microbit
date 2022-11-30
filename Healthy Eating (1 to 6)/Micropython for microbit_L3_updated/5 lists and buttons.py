# Add your Python code here. E.g.
from microbit import *

shopping_list = ("cheese", "beans", "apples")
x = 0

while True:
    if button_a.is_pressed():
        display.scroll(str(shopping_list[x]))
    if button_b.is_pressed(): 
        x = x + 1
        sleep(1000)
    else:
        display.clear()


