# Add your Python code here. E.g.
from microbit import *
import time
# Servo control:
# 100 = 1 millisecond pulse all right
# 200 = 2 millisecond pulse all left
# 150 = 1.5 millisecond pulse center
# 10 is 10 milliseconds for period 1/100 Hz
pin1.set_analog_period(10)

while True:
    if button_a.is_pressed():
        display.clear()
        pin1.write_analog(200) 
        sleep(2000)
        pin1.write_analog(0) 
    elif button_b.is_pressed():
        display.clear()
        pin1.write_analog(100)
        sleep(2000)
        pin1.write_analog(0) 
    else:
        display.show(Image.ASLEEP)
    