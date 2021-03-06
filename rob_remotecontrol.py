import Tkinter as tk
import rob_moves as mv


def key_input(event):
    mv.init()
    print'Key:', event.char
    key_press = event.char
    st = 0.030
    if key_press.lower() == 'w':
        mv.forward(st)
    elif key_press.lower() == 's':
        mv.reverse(st)
    elif key_press.lower() == 'a':
        mv.turn_left(st)
    elif key_press.lower() == 'd':
        mv.turn_right(st)
    elif key_press.lower() == 'q':
        mv.pivot_left(st)
    elif key_press.lower() == 'e':
        mv.pivot_right(st)
    elif key_press.lower() == 'z':
        mv.reverse_left(st)
    elif key_press.lower() == 'x':
        mv.reverse_right(st)
    else:
        pass

command = tk.Tk()
command.bind('<KeyPress>', key_input)
command.mainloop()
