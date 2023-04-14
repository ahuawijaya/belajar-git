from tkinter import *
from tkinter import ttk
import random
gui=Tk()
gui.geometry('400x400')
gui.title('First title')
canvas=Canvas(gui,width=300,height=300,bg='black')
canvas.pack()
blackline=canvas.create_rectangle(0,0,203,203,fill='yellow')
greenline=canvas.create_line(20,20,0,0,fill='green')
ovl=canvas.create_arc(0,2,203,203,extent=90,fill='blue')
gui.mainloop()
