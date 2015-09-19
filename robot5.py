import RPi.GPIO as gpio
import time
import sys
import Tkinter as tk
from sensor import distance
import random

def init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(7, gpio.OUT)
    gpio.setup(11, gpio.OUT)
    gpio.setup(13, gpio.OUT)
    gpio.setup(15, gpio.OUT)

def forward(tf):
    gpio.output(7,  True)
    gpio.output(11, False)
    gpio.output(13, True)
    gpio.output(15, False)
    time.sleep(tf)
    gpio.cleanup()

def reverse(tf):
    gpio.output(7,  False)
    gpio.output(11, True)
    gpio.output(13, False)
    gpio.output(15, True)
    time.sleep(tf)
    gpio.cleanup()

def turn_right(tf):
    gpio.output(7,  False)
    gpio.output(11, False)
    gpio.output(13, True)
    gpio.output(15, False)
    time.sleep(tf)
    gpio.cleanup()

def turn_left(tf):
    gpio.output(7, True)
    gpio.output(11, False)
    gpio.output(13, False)
    gpio.output(15, False)
    time.sleep(tf)
    gpio.cleanup()

def reverse_right(tf):
    gpio.output(7, False)
    gpio.output(11, True)
    gpio.output(13, False)
    gpio.output(15, False)
    time.sleep(tf)
    gpio.cleanup()

def reverse_left(tf):
    gpio.output(7, False)
    gpio.output(11, False)
    gpio.output(13, False)
    gpio.output(15, True)
    time.sleep(tf)
    gpio.cleanup()

def pivot_left(tf):
    gpio.output(7, True)
    gpio.output(11, False)
    gpio.output(13, False)
    gpio.output(15, True)
    time.sleep(tf)
    gpio.cleanup()

def pivot_right(tf):
    gpio.output(7, False)
    gpio.output(11, True)
    gpio.output(13, True)
    gpio.output(15, False)
    time.sleep(tf)
    gpio.cleanup()

'''
def key_input(event):
    init()
    print'Key:', event.char
    key_press = event.char
    st = 0.030

    if key_press.lower() == 'w':
        forward(st)
    elif key_press.lower() == 's':
        reverse(st)
    elif key_press.lower() == 'a':
        turn_left(st)
    elif key_press.lower() == 'd':
        turn_right(st)
    elif key_press.lower() == 'q':
        pivot_left(st)
    elif key_press.lower() == 'e':
        pivot_right(st)
    else:
        pass

    curDist = distance('cm')
    print('current distance is', curDist)

    if curDist < 20:
        init()
        pivot_right(.5)

command = tk.Tk()
command.bind('<KeyPress>', key_input)
command.mainloop()
'''

def check_front():
    init()
    dist = distance()
    while dist < 15 :
        print('Too close', dist)
        init()
        pivot_right(.25)
  
        
def search():
    init()
    tf = 0.030
    dist = distance()
    if dist < 15:
        init()
        pivot_right(.25)
        check_front()
    else:
        init()
        forward(3)

for z in range(30):
    search()


'''

def autonomy():
    tf =0.030
    x = random.randrange(0, 4)

    if x == 0:
        for y in range(30):
            check_front()
            init()
            forward(tf)
    elif x == 1:
        for y in range(30):
            check_front()
            init()
            pivot_left(tf)
    elif x == 2:
        for y in range(30):
            check_front()
            init()
            pivot_right(tf)
    elif x == 3:
        for y in range(30):
            check_front()
            init()
            forward(tf)

for z in range(10):
    autonomy()

'''

