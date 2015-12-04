import motor.py as mt
import sonar.py as sn
import random as rnd
import Tkinter as tk


def autonomy():
    tf = 0.030
    x = rnd.randrange(0, 4)

    if x == 0:
        for y in range(30):
            sn.check_distance()
            mt.init()
            mt.forward(tf)
    elif x == 1:
        for y in range(30):
            sn.check_distance()
            mt.init()
            mt.pivot_left(tf)
    elif x == 2:
        for y in range(30):
            sn.check_distance()
            mt.init()
            mt.pivot_right(tf)
    elif x == 3:
        for y in range(30):
            sn.check_distance()
            mt.init()
            mt.forward(tf)


command = tk.Tk()
command.bind('<KeyPress>', key_input
