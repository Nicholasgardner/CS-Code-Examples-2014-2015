#Block the pig 
from Tkinter import *
import random

def redrawAll():
    canvas.delete(ALL)
    canvas.create_rectangle(0,0, canvas.data.width + 10, canvas.data.height + 10)
    canvas.create_image(0,0, image=canvas.photo)
    canvas.create_rectangle(canvas.data.x1, canvas.data.y1, canvas.data.x1 + 40, canvas.data.y1 + 40)
    canvas.create_image(canvas.data.x1 + 20, canvas.data.y1 + 20, image = canvas.photo2)
        

def keyPressed(event):
    print event.keysym
        
def timerFired():
    redrawAll()
    canvas.after(canvas.data.delay, timerFired)

        
def init():
    #canvas
    photo = PhotoImage(file="grass.gif")
    canvas.photo = photo	
    canvas.data.width = 500
    canvas.data.height = 500
    #other
    canvas.data.delay = 1
    #pig
    canvas.data.x1 = 100
    canvas.data.y1 = 220
    photo = PhotoImage(file="blockpig.gif")
    canvas.photo2 = photo

        

        
def main():
    global root
    root = Tk()
    global canvas
    canvas = Canvas(root, width = 500, height = 500)
    canvas.pack()
    class Struct(): pass
    canvas.data = Struct()
    init()
    timerFired()
    root.bind("<Key>", keyPressed)
    root.mainloop()

main()






#board size = 200 x 440
#pixels per tile = 40 x 40
