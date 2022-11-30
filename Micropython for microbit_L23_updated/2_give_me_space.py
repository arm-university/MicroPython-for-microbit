# Add your Python code here. E.g.
from microbit import *
import speech
import time

while True:
    light = display.read_light_level()
    #display.scroll(light)
    sleep(5)
    if light > 50:
        display.show(Image.HAPPY)
    else:
        display.show(Image.SAD)
        speech.say("give me some space", pitch=64, speed=72, mouth=128, throat=128)

