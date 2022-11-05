# Add your Python code here. E.g.
# radio 2
from microbit import *
import radio
radio.on()

# any channel from 0 to 100 can be used for privacy.
radio.config(channel=5)

while True:
    msg = radio.receive()
    if msg != None:
        if msg == 'HAPPY':
            display.show(Image.HAPPY)
            sleep(200)
            display.clear()
        elif msg == 'SAD':
            display.show(Image.SAD)
            sleep(200)
            display.clear()