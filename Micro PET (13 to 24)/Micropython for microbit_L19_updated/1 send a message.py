# Add your Python code here. E.g.
#radio 1
from microbit import *
import radio

radio.on()

radio.config(channel=5)        

while True:
    if button_a.was_pressed():
        my_message = "A"
        radio.send(my_message)
        sleep(200)



