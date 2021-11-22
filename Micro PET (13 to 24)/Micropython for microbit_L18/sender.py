# Add your Python code here. E.g.
#radio 1
from microbit import *

import radio
radio.on()

# any channel from 0 to 100 can be used for privacy.
radio.config(channel=5)

while True:
    if button_a.was_pressed():
        radio.send('HAPPY')
        sleep(200)
    elif button_b.was_pressed():
        radio.send('SAD')
        sleep(200)

