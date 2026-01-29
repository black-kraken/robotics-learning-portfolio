from gpiozero import Button, LED
from signal import pause

led = LED(17)
button = Button(27, pull_up=True)

def toggle_led():
    if led.is_lit:
        led.off()
        print("LED OFF")
    else:
        led.on()
        print("LED ON")

button.when_pressed = toggle_led

print("Press the button to toggle the LED. Ctrl+C to quit.")
pause()
