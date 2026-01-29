# Week 4 — GPIO Input (Buttons)

## Goals
- Read physical button input
- Use internal pull-up resistors
- Control an LED with a button
- Learn about switch bounce and noise

## What I Built
- A button input test using gpiozero
- A button-controlled LED toggle system
- A live GPIO state viewer for debugging

## Concepts Learned
- Active-low inputs
- Pull-up resistors
- Switch bounce
- Event-driven GPIO
- Hardware vs software reliability

## Notes
Some flicker was observed due to the quality of the push button and breadboard contacts.
This is a real-world hardware issue and was mitigated using software debounce.
