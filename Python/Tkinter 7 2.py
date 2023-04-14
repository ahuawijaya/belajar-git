from tkinter import Tk, Canvas, Frame, BOTH, W
from tkinter import *

class example(Frame):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.master.title('Lyrics')
        self.pack(fill=BOTH, expand=1)
        canvas=Canvas(self)
        canvas.create_text(20,30,anchor=W,font='Purisa',text='Most relationships seem so transitory')
        canvas.create_text(20,60,anchor=W,font='Purisa',text='They are good but not the permanent one')
        canvas.create_text(20,130,anchor=W,font='Purisa',text='Who does not long for someone to hold')
        canvas.create_text(20,160,anchor=W,font='Purisa',text='Who knows how to love without being told')
        canvas.create_text(20,190,anchor=W,font='Purisa',text='Somebody tell me why Im on my own')
        canvas.create_text(20,30,anchor=W,font='Purisa',text='If there is a soulmate everyone')
        canvas.pack(fill=BOTH, expand=1)
def main():
            xp=Tk()
            ex= example()
            xp.geometry('420x250+500+300')
            xp.mainloop()

if __name__=='__main__':
            main()
