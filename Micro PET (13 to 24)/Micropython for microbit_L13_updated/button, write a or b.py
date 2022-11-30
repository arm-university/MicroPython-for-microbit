# Add your Python code here. E.g.
from microbit import *
import os

while True:
    with open('hello.txt', 'w') as newFile:
        if button_a.is_pressed():
            newFile.write("Arch")
        elif button_b.is_pressed():
            newFile.write("Linux")
        else:
            pass
        
    with open('hello.txt') as file:
        output=file.readline()
        
    display.scroll(output)
