from gpiozero import LED

led = LED(17)

print("Type 'on', 'off', or 'quit'")

while True:
    command = input("> ").strip().lower()

    if command == "on":
        led.on()
        print("LED ON")

    elif command == "off":
        led.off()
        print("LED OFF")

    elif command == "quit":
        led.off()
        print("Exiting program")
        break

    else:
        print("Unknown command")
