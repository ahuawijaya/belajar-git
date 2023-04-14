from tkinter import *
from tkinter import ttk
gui=Tk()

gui.geometry('400x400')
gui.title('First tittle')
a=Label(gui,text=' Username =').grid(row=1,column=1)
E=Entry(gui).grid(row=1,column=2)

b=Label(gui,text=' Password =').grid(row=2,column=1)
f=Entry(gui,show='**').grid(row=2,column=2)

c=ttk.Button(gui,text='Submit').grid(row=3,column=1)

gui.mainloop()
