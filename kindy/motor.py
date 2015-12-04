import RPi.GPIO as gpio
import time
import random


def init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(7, gpio.OUT)
    gpio.setup(11, gpio.OUT)
    gpio.setup(13, gpio.OUT)
    gpio.setup(15, gpio.OUT)


#  Basic Movements
def forward(tf):
    init()
    gpio.output(7,  True)
    gpio.output(11, False)
    gpio.output(13, True)
    gpio.output(15, False)
    time.sleep(tf)
    gpio.cleanup()


def reverse(tf):
    init()
    gpio.output(7,  False)
    gpio.output(11, True)
    gpio.output(13, False)
    gpio.output(15, True)
    time.sleep(tf)
    gpio.cleanup()


def turn_right(tf):
    init()
    gpio.output(7,  False)
    gpio.output(11, False)
    gpio.output(13, True)
    gpio.output(15, False)
    time.sleep(tf)
    gpio.cleanup()


def turn_left(tf):
    init()
    gpio.output(7,  True)
    gpio.output(11, False)
    gpio.output(13, False)
    gpio.output(15, False)
    time.sleep(tf)
    gpio.cleanup()


def reverse_right(tf):
    init()
    gpio.output(7, False)
    gpio.output(11, True)
    gpio.output(13, False)
    gpio.output(15, False)
    time.sleep(tf)
    gpio.cleanup()


def reverse_left(tf):
    init()
    gpio.output(7,  False)
    gpio.output(11, False)
    gpio.output(13, False)
    gpio.output(15, True)
    time.sleep(tf)
    gpio.cleanup()


def pivot_left(tf):
    init()
    gpio.output(7,  True)
    gpio.output(11, False)
    gpio.output(13, False)
    gpio.output(15, True)
    time.sleep(tf)
    gpio.cleanup()


def pivot_right(tf):
    init()
    gpio.output(7,  False)
    gpio.output(11, True)
    gpio.output(13, True)
    gpio.output(15, False)
    time.sleep(tf)
    gpio.cleanup()


# Complex Movements
def random_reorient(deg):
    direction = random.choice(['left', 'right'])
    if direction == 'left':
        pivot_left(deg)
    else:
        pivot_right(deg)
