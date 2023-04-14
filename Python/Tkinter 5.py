from tkinter import *
from tkinter import filedialog

def Newfile():
    print('New filee')
def Openfile():
    name=filedialog()
    print('Name')
def About():
    print('This is a simple example of a menu')

xp=Tk()
menu=Menu(xp)
xp.config(menu=menu)
filemenu=Menu(menu)
menu.add_cascade(label='File',menu=filemenu)
filemenu.add_command(label='New',command=Newfile)
filemenu.add_command(label='Open',command=Newfile)
filemenu.add_separator()
filemenu.add_command(label='Exit',command=xp.quit)

helpmenu=Menu(menu)
menu.add_cascade(label='Help',menu=helpmenu)
helpmenu.add_command(label='About...',command=About)
xp.mainloop()
