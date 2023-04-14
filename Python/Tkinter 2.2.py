from tkinter import *
from tkinter import ttk
gui=Tk()
gui.geometry('400x400')
def login(us1,pw1,us,pw):
    if us1==us and pw1==pw:
        i=Label(gui, text='Login sukses').grid(row=6,column=0)
        print('Login sukses')
    else:
        print('Wrong pass')
        j=Label(gui, text='Login gagal').grid(row=6,column=0)

gui.title('Account')
a=Label(gui,text='Username').grid(row=0,column=0)
b=Label(gui,text='Password').grid(row=1,column=0)
c=Entry(gui).grid(row=0,column=1)
d=Entry(gui,show='**').grid(row=1,column=1)
e=ttk.Button(gui, text='Create Account').grid(row=2,column=0)
al=Label(gui,text='Username').grid(row=4,column=0)
bl=Label(gui,text='Password').grid(row=5,column=0)
cl=Entry(gui).grid(row=4,column=1)
dl=Entry(gui,show='**').grid(row=5,column=1)
el=ttk.Button(gui,text='Login',command=lambda:login(c,d,cl,dl)).grid(row=6,column=0)
gui.mainloop()
