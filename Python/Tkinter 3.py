from tkinter import *
from tkinter import ttk
gui=Tk()
var=IntVar()
gui.geometry('400x400')
Radiobutton(gui,text='Hello',value=1).grid(row=0,column=0)
Radiobutton(gui,text='HI',value=2).grid(row=1,column=0)
Radiobutton(gui,text='bye',value=3).grid(row=2,column=0)
Radiobutton(gui,text='good bye',value=4).grid(row=3,column=0)
Radiobutton(gui,text='bad boy',value=5).grid(row=4,column=0)
gui.title('First title')
o=ttk.Button(gui,text='Hello').grid(row=5,column=0)
gui.mainloop()


from tkinter import *
from tkinter import ttk
gui=Tk()
var=IntVar()
gui.geometry('400x400')
Checkbutton(gui,text='Hello').grid(row=0,column=0)
Checkbutton(gui,text='HI').grid(row=1,column=0)
Checkbutton(gui,text='bye').grid(row=2,column=0)
Checkbutton(gui,text='good bye').grid(row=3,column=0)
Checkbutton(gui,text='bad boy').grid(row=4,column=0)
gui.title('First title')
o=ttk.Button(gui,text='Hello').grid(row=5,column=0)
gui.mainloop()
