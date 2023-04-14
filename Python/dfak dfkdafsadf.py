from tkinter import *
from tkinter import ttk
gui= Tk()
gui.configure(background='black')
def callback():
    label=Label(gui,text='helloworld',fg='white',bg='black').grid()
gui.title('First title')
gui.geometry('500x300')
ttk.Button(gui,text='hello',command=callback).grid()
gui.mainloop()
