from tkinter import *
import time
xp=Tk()
xp.geometry('800x800')
c=Canvas(xp,width=800,height=800,bg='blue')
c.pack()
oval=c.create_oval(5,5,60,60,fill='yellow')
xd=9
yd=27
while(True):
    c.move(oval,xd,yd)
    p=c.coords(oval)
    if p[3]>=800 or p[1]<=0:
        yd=-yd
    if p[2]>=800 or p[0]<=0:
        xd=-xd
    xp.update()
    time.sleep(0.025)
xp.title('F')
xp.mainloop()
