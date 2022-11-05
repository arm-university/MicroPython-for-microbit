# Add your Python code here. E.g.
from microbit import *

while True:
    gesture = accelerometer.current_gesture()
    if gesture == "right":
        display.show(Image.ARROW_E)
    elif gesture == "left":
        display.show(Image.ARROW_W)    
    else:
        display.show(Image.SKULL)
