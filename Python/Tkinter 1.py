from tkinter import *
from tkinter import ttk
gui=Tk()
gui.configure(background='black')
def display():
    print('hello world')
label=Label(gui, text='hello world',fg='white',bg='black').grid()
gui.title('First tittle ')
gui.geometry('500x300')
ttk.Button(gui, text='hello',command=display).grid()
gui.mainloop()
