import tkinter
import random

colours=['red','blue','pink','yellow','green','orange','black','white','purple','brown']
score=0
timeleft=30
def startgame(event):
    if timeleft==30:
        countdown()
    nextColour()

def nextColour():
    global score
    global timeleft
    if timeleft >0:
        e.focus_set()
        if e.get().lower()==colours[1].lower():
            score+=1
        e.delete(0,tkinter.END)
        random.shuffle(colours)
        label.config(fg=str(colours[1]),text=str(colours[0]))
        scoreLabel.config(text='Score:'+str(score))

def countdown():
    global timeleft
    if timeleft > 0 :
        timeleft-=1
        timeLabel.config(text='Time left:'+str(timeleft))
        timeLabel.after(1000,countdown)

xp=tkinter.Tk()
xp.title('Colorgame')
xp.geometry('375x200')
instruction=tkinter.Label(xp,text='Type in the colour of the words,and not the word text',font=
                           ('Helvetica',12))
instruction.pack()
scoreLabel=tkinter.Label(xp,text='Press enter to start',font=
                           ('Helvetica',12))
scoreLabel.pack()
timeLabel=tkinter.Label(xp,text='Time left'+str(timeleft),font=
                           ('Helvetica',12))
timeLabel.pack()
label=tkinter.Label(xp,font=('Helvetica',60))
label.pack()
e=tkinter.Entry(xp)
xp.bind('<Return>',startgame)
e.pack()
