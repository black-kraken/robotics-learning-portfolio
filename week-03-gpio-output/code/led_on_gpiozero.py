from gpiozero import LED
from time import sleep

led = LED(17)   # GPIO 17 (BCM), physical pin 11

led.on()
sleep(5)
led.off()
