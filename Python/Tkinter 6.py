from tkinter import *
from tkinter import Menu
xp=Tk()
xp.title('Welcome to Binomo')
menu=Menu(xp)
new_item=Menu(menu)
new_item.add_command(label='New')
new_item.add_separator()
new_item.add_command(label='Edit')
menu.add_cascade(label='File',menu=new_item)
xp.config(menu=menu)
xp.mainloop()
