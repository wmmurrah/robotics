import RPi.GPIO as gpio
import time
import Tkinter as tk


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

command = tk.Tk()
command.bind('<KeyPress>', key_input)
command.mainloop()
