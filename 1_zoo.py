# Add your Python code here. E.g.
from microbit import *
import time

while True:
    if pin0.is_touched():
        display.show(Image.DUCK)
        sleep(10)
    elif pin1.is_touched():
        display.show(Image.COW)
        sleep(10)
    elif pin2.is_touched():
        display.show(Image.BUTTERFLY)
        sleep(10)
    else:
        display.show(Image.SKULL)
        sleep(1)
