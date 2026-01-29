from gpiozero import Button
from time import sleep

button = Button(27, pull_up=True)

while True:
    print("PRESSED" if button.is_pressed else "released")
    sleep(0.1)
