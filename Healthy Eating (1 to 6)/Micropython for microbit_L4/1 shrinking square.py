# Add your Python code here. E.g.
from microbit import *

while True:
    if pin0.is_touched():
        display.show(Image.SQUARE_SMALL)
    else:
        display.show(Image.SQUARE)
