# Add your Python code here. E.g.
from microbit import *
import time
import music

while True:
    if pin0.is_touched():
        tune = ["A2:4"]
        music.play(tune)
        sleep(4)
    elif pin1.is_touched():
        tune = ["B2:4"]
        music.play(tune)
        sleep(4)
    elif pin2.is_touched():
        tune = ["C2:4"]
        music.play(tune)
        sleep(4)
    else:
        display.show(Image.SKULL)
        sleep(1)
