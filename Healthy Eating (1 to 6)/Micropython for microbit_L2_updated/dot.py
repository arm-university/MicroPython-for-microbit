# Add your Python code here. E.g.
from microbit import *
from time import sleep

dot1 = Image("00000:"
             "00000:"
             "00000:"
             "00000:"
             "50000")
             
dot2 = Image("00000:"
             "00000:"
             "00000:"
             "00000:"
             "05000")

dot3 = Image("00000:"
             "00000:"
             "00000:"
             "00000:"
             "00500")             

display.show(dot1)
sleep(0.5)
display.show(dot2)
sleep(0.5)
display.show(dot3)
sleep(0.5)