# Christmas Lights
# Code to work with the 15 led string from the Pi Hut Let It Glow advent calendar kit.
# See https://thepihut.com/blogs/raspberry-pi-tutorials/let-it-glow-maker-advent-calendar-day-10-ultra-blinky for
# the instructions for the day using this LED string, and also
# https://thepihut.com/blogs/raspberry-pi-tutorials/let-it-glow-maker-advent-calendar-day-8-rainbow-ring where the basis
# for this code came from.

from machine import Pin
from neopixel import NeoPixel
import time
import random

# Define the strip GPIO Pin number (2) and number of LEDs (12)
# On this board, the GPIO pin numbers are silk-screened onto the PCB.
led_count = 15
ring = NeoPixel(Pin(2), led_count)

# Turn off all LEDs before program start
ring.fill((0,0,0))
ring.write()
time.sleep(1)

## Main program loop
try:
    while True:
        randomled = random.randint(0, led_count-1)
        ring[randomled] = (random.randint(0,50), random.randint(0,50), random.randint(0,50))
        ring.write()        
        time.sleep(0.03)

except KeyboardInterrupt:
    # here you put any code you want to run before the program
    # exits when you press CTRL+C
    print("Caught KeybardInterput, terminating program.")

#except:
    # this catches ALL other exceptions including errors.
    # You won't get any error messages for debugging
    # so only use it once your code is working
#    print("Unhandled error occurred, terminating program.")

finally:
    print("Shutting down.")
    ring.fill((0,0,0))
    ring.write()
