# Add your Python code here. E.g.
#radio 1
from microbit import *
import radio

radio.on()

radio.config(channel=5)        

while True:
    if button_a.was_pressed():
        my_message = "Y"
        radio.send(my_message)
        sleep(200)
    elif button_b.was_pressed():
        my_message = "N"
        radio.send(my_message)
        sleep(200)
        



