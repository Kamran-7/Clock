# importing the entire tkinter module

from tkinter import *
from tkinter.ttk import *

# to retrieve the system's time, you can need to import the strftime function

from time import strftime

# creation of the tkinter window
root = Tk()
root.title("clock")


# This function displays the current time on the label defined herein

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)


# creating an attractive look: needs styling the label widget

label = Label(root, font=("ds-digital", 80), background="black", foreground="cyan")

# defining how to place the digital clock at the centre tkinter's window
label.pack(anchor='center')
time()

mainloop()
