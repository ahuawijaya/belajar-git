from tkinter import *
import time
gui=Tk()
var=IntVar()
gui.geometry('400x400')
canvas=Canvas(gui, width=300,height=300,bg='black')
canvas.pack()
ovl=canvas.create_oval(5,5,60,60,fill='green')
a=5
b=5
for x in range(0,100):
    canvas.move(ovl,a,b)
    gui.update()
    time.sleep(.05)
gui.title('Canvas')
gui.mainloop()
