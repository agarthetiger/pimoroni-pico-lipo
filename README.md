# Pimoroni Pico Lipo

My collection of scripts and code to run on my [Pimoroni Pico Lipo](https://shop.pimoroni.com/products/pimoroni-pico-lipo?variant=39386149093459) (4MB version).

## Specifications

* Powered by RP2040
* Dual ARM Cortex M0+ running at up to 133Mhz
* 264kB of SRAM
* 4MB/16MB of QSPI flash supporting XiP
* MCP73831 charger with 215mA charging current (datasheet)
* XB6096I2S battery protector (datasheet)
* USB-C connector for power, programming, and data transfer
* 4 pin Qw-ST (Qwiic / STEMMA QT) connector
* 3 pin debug connector (JST-SH)*
* 2-pole JST PH battery connector, with polarity marked on the board
* Switch for basic input (doubles up as DFU select on boot)
* Power button
* Power, charging and user LED indicators
* On-board 3V3 regulator (max regulator current output 600mA)
* Input voltage range 3V - 5.5V
* Compatible with Raspberry Pi Pico add-ons

## Initialisation

Board flashed with [Pimoroni's firmware v1.23.0-1](https://github.com/pimoroni/pimoroni-pico/releases/tag/v1.23.0-1). Hold down the BOOT button and press the Power button twice to put the device into bootloader mode. If the device isn't mounted under /Volumes check the USB-C cable is rated for data transfer and not just charging.

## Scripts

### main.py

The file has to be called this in order to run when the board is powered on. This is currently a script to control a string of 15 LED lights around a miniature wooden Christmas tree. It randomly changes the lights continuously until shut off.

### battery-charging-status.py

Modified example script to read the battery voltage (assuming there is one connected) and also indivate whether the battery is currently charging. LED status light for the battery lights up as follows:

* Solid Red - Charging
* ...

# system-information.py

Print to the console a bunch of information about the system environment. Note that some of these commands are different from a Raspberry Pico, probably due to the Pimoroni firmware being used.


