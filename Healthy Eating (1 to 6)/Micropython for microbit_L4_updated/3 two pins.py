# Add your Python code here. E.g.
from microbit import *

while True:
    if pin0.is_touched():
        display.show(Image.SQUARE_SMALL)
        sleep(500)
        display.show(Image.SQUARE)
        sleep(500)
    elif pin1.is_touched(): 
        display.scroll("SAFE")
    else:
        display.show(Image.CHESSBOARD)
