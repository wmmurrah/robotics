import RPi.GPIO as gpio
import time
import motor as mr


def distance(measure='cm'):
    gpio.setmode(gpio.BOARD)
    gpio.setup(12, gpio.OUT)
    gpio.setup(16, gpio.IN)

    #  Get time signal sent
    gpio.output(12, False)
    while gpio.input(16) == 0:
        nosig = time.time()
    #  Get time signal received
    while gpio.input(16) == 1:
        sig = time.time()

    #  Get elapsed time which we use to estimate distancels
    tl = sig - nosig
    if measure == 'cm':
        distance = tl / 0.000058
    elif measure == 'in':
        distance = tl / 0.000148
    else:
        print('measure must be in or cm')
        distance = None

    gpio.cleanup()
    return distance


def check_distance():
    mr.init()
    dist = distance()
    while dist < 15:
        print('Too close', dist)
        mr.init()
        mr.random_reorient()
