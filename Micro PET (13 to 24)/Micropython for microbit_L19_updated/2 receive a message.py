# Add your Python code here. E.g.
#RADIO 2
from microbit import *
import radio
radio.on()

# any channel from 0 to 100 can be used for privacy.
radio.config(channel=5)

while True:
        #radio.send(my_message)
        incoming = radio.receive()
        if incoming is not None:
            display.show(incoming)
            print(incoming)
            sleep(500)
            display.clear()