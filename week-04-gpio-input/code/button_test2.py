from gpiozero import Button
from signal import pause

button = Button(27, pull_up=True)

button.when_pressed = lambda: print("PRESSED")
button.when_released = lambda: print("RELEASED")

print("Ready. Press the button (Ctrl+C to quit).")
pause()
