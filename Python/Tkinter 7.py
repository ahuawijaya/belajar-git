from tkinter import Tk, Canvas, Frame , BOTH


class Example(Frame):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title('Lines')
        self.pack(fill=BOTH, expand=1)
        canvas=Canvas(self)
        canvas.create_line(15,25,200,25)
        canvas.create_line(300,35,300,200, dash=(4,2))
        canvas.create_line(55,85,155,85,105,180,55,85)
        canvas.pack(fill=BOTH, expand=1)

def main ():
    xp=Tk()
    ex=Example()
    xp.geometry('400x250+300+300')
    xp.mainloop()

if __name__== '__main__':
    main()

from tkinter import Tk, Canvas, Frame , BOTH


class Example(Frame):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title('Colours')
        self.pack(fill=BOTH, expand=1)
        canvas=Canvas(self)
        canvas.create_rectangle(30,10,120,80,outline='#fb0',fill='#fb0')
        canvas.create_rectangle(150,10,240,80,outline='#f50',fill='#f50')
        canvas.create_rectangle(270,10,370,80,outline='#f05',fill='#05f')
        canvas.pack(fill=BOTH, expand=1)

def main ():
    xp=Tk()
    ex=Example()
    xp.geometry('400x250+300+300')
    xp.mainloop()

if __name__== '__main__':
    main()
