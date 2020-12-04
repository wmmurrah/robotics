# dist_test.py
"""Test distance with sonar on kindy"""


import RPi.GPIO as gpio
import time


trig_pin = 12
echo_pin = 16
gpio.setmode(gpio.BOARD)
gpio.setup(trig_pin, gpio.OUT)
gpio.setup(echo_pin, gpio.IN)


def send_trig():
    gpio.output(trig_pin, True)
    time.sleep(0.0001)
    gpio.output(trig_pin, False)


def wait_echo(value, timeout):
    count = timeout
    while gpio.input(echo_pin) != value and count > 0:
        count = count - 1

     
def ping_dist():
    send_trig()
    wait_echo(True, 10000)
    start = time.time()
    wait_echo(False, 10000)
    finish = time.time()
    pulse_len = finish - start
    distance_cm = pulse_len / 0.000058
    distance_in = distance_cm / 2.5
    return (distance_cm, distance_in)


while True:
    print("cm=%f\tinches=%f" % ping_dist())
    time.sleep(1)


  
