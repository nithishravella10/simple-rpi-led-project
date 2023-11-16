# Simple Raspberry Pi LED Project

A basic Raspberry Pi project to control two LEDs (red and green) using GPIO pins.

## Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Installation and Usage](#installation-and-usage)
- [Conclusion](#conclusion)

## Introduction

This project demonstrates how to control two LEDs connected to GPIO pins on a Raspberry Pi. The LEDs (red and green) alternate between being turned on and off in a continuous loop.

## Prerequisites

### Hardware Requirements

- Raspberry Pi (any model with GPIO pins, I have used Raspberry Pi Model B with 512 MB memory)
- Breadboard
- Two LEDs (red and green)
- Two Resistors (appropriate values for the LEDs, > 200 ohms should provide a safe current for the LED)
- Jumper wires
#### Hardware setup:
  ![Hardware setup](https://github.com/nithishravella10/simple-rpi-led-project/blob/main/hardware-setup.jpg)

### Software Requirements

- Raspbian OS installed on your Raspberry Pi
- Python installed on your Raspberry Pi
- Basic knowledge of Raspberry Pi GPIO and Python

## Hardware Setup
1. **Identifying GPIO's on your RPi:**
   
   a. The first step in identifying GPIO pins is to refer to the pinout diagram of your specific Raspberry Pi model. Pinout diagrams provide a visual representation of the Raspberry Pi's GPIO pins, their numbers, and their corresponding functions. You can find official pinout diagrams on the [Raspberry Pi website](https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#gpio-and-the-40-pin-header)
   
   b. More info at [pinout.xyz](https://pinout.xyz/)
   
3. **Connect LEDs to GPIO pins:**

   a. Connect the anode (longer leg) of the **green LED** to GPIO pin 17.

   b. Connect the cathode (shorter leg) of the green LED to a resistor (e.g., 220 ohms).

   c. Connect the other end of the resistor to the ground (GND) pin on the Raspberry Pi.

   d. Connect the anode of the **red LED** to GPIO pin 27.

   e. Connect the cathode of the green LED to a resistor (e.g., 220 ohms).

   f. Connect the other end of the resistor to the ground (GND) pin on the Raspberry Pi.

5. **Ensure proper connections:**

   - Double-check your wiring to ensure all connections are secure.
   - Confirm that the GPIO pins match the ones specified in the code.
## Installation and Usage

1. Clone the repository to your Raspberry Pi:

   ```bash
   git clone https://github.com/nithishravella10/simple-rpi-led-project.git
   
2. Navigate to the project directory:

   ```bash
   cd simple-rpi-led-project

3. Run the project:

   ```bash
   python led_project.py
## Conclusion
This simple Raspberry Pi LED project demonstrates the basics of controlling LEDs using GPIO pins. Through the hardware setup and code implementation, you've gained hands-on experience with Raspberry Pi GPIO and Python programming. Next step is to try something more advanced, like controlling these LEDs remotely. Keep exploring and use ChatGPT for more fun!
