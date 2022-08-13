from tkinter import Tk
from tkinter import Label
import time
import sys

master = Tk()   # this will create a window 

master.title("Digital clock")

def get_time():
    timeVar = time.strftime("%I:%M:%S %p")  #  represent time in their string form.
    clock.config(text = timeVar)
    clock.after(1000,get_time)   # this will run the function get_time after every 0.2 seconds.



clock = Label(master , font=("Calibri",90),bg="grey",fg="Lightblue")
clock.pack()

get_time()

master.mainloop()  # this will keep runnig the windows.


