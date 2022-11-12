# Add your Python code here. E.g.
from microbit import *
# Servo control:
# 100 = 1 millisecond pulse all right
# 200 = 2 millisecond pulse all left
# 150 = 1.5 millisecond pulse center
# 10 is 10 milliseconds for period 1/100 Hz
while True:
    pin1.set_analog_period(10)
    pin1.write_analog(100)
    sleep(1000)
    