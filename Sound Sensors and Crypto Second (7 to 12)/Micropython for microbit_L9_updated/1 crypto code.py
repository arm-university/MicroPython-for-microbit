# Add your Python code here. E.g.
from microbit import *

import random
while True:
    if button_a.is_pressed():
        display.show(str(random.randint(1, 6)))
        sleep(2000)
    else:
        display.show(Image.TSHIRT)