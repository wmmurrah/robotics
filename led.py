# led.py
"""LED for kindy"""


import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)
gpio.setup(18, gpio.OUT)
gpio.output(18, True)
time.sleep(0.5)

gpio.cleanup()
