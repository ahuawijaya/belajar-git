from tkinter import *
from tkinter import messagebox

def answer():
    showerror('Answer','Sorry, no answer available')
def callback():
    if tkMessageBox.askyesno('Verify', 'Really quit?'):
        showwarning('Yes','Not yet implemented')
    else:
        showinfo('No','quir has been cancelled')

Button(text='QUit',command=callback).pack(fill=X)
Button(text='Answer',command=answer).pack(fill=X)
mainloop()
