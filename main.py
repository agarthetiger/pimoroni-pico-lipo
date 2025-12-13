# Imports
from machine import Pin, ADC
# Christmas Lights
# Code to work with the 15 led string from the Pi Hut Let It Glow advent calendar kit.
# See https://thepihut.com/blogs/raspberry-pi-tutorials/let-it-glow-maker-advent-calendar-day-10-ultra-blinky for
# the instructions for the day using this LED string, and also
# https://thepihut.com/blogs/raspberry-pi-tutorials/let-it-glow-maker-advent-calendar-day-8-rainbow-ring where the basis
# for this code came from.

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
        
while True:
    randomled = random.randint(0, led_count-1)
    ring[randomled] = (random.randint(0,50), random.randint(0,50), random.randint(0,50))
    ring.write()        
    time.sleep(0.03)

