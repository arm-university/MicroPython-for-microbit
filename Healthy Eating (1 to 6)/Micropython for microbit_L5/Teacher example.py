# Add your Python code here. E.g.
from microbit import *

display.scroll("The Food Quiz")
display.scroll("Get Ready")
sleep(2000)

#1
display.scroll("Q1")
display.scroll("Yes = A: No = B")
display.scroll("Do you eat chocolate every day?")

while True:    
    if button_a.is_pressed():
            display.scroll("Too much")
            display.show(Image.SAD)
            sleep(2000)
            break
                
    elif button_b.is_pressed():
            display.scroll("Good")
            display.show(Image.SMILE) 
            sleep(2000)
            break
            
#2
display.scroll("Q2")
display.scroll("Yes = A: No = B")
display.scroll("Do you sleep well?") 

while True:    
    if button_a.is_pressed():
            display.scroll("That is important")
            display.show(Image.SMILE)
            sleep(2000)
            break
                
    elif button_b.is_pressed():
            display.scroll("Get some")
            display.show(Image.SAD) 
            sleep(2000)
            break
