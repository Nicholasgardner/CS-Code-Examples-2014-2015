#TK trials
from Tkinter import *
import random
while flag:
    def redrawAll():
        canvas.delete(ALL)
        canvas.create_rectangle(0,0, canvas.data.width + 10, canvas.data.height + 10, fill = canvas.data.color1)
        canvas.create_rectangle(canvas.data.x1, canvas.data.y1, canvas.data.x1 + 20 * canvas.data.addmultiplier, canvas.data.y1 + 20, fill = canvas.data.color)
        #canvas.create_rectangle(canvas.data.blockx1, canvas.data.blocky1, canvas.data.blockx1 + 20, canvas.data.blocky1 + 20, fill = "magenta")
        canvas.create_image(canvas.data.x1, canvas.data.y1, image=canvas.photo)
        canvas.create_image(canvas.data.food2x1, canvas.data.food2y1, image=canvas.food2photo)
        canvas.create_image(canvas.data.food3x1, canvas.data.food3y1, image=canvas.food3photo)
        canvas.create_image(canvas.data.food4x1, canvas.data.food4y1, image=canvas.food4photo)
        canvas.create_rectangle(canvas.data.food2x1, canvas.data.food2y1, canvas.data.food2x2, canvas.data.food2y2, fill = "")
        canvas.create_rectangle(canvas.data.food3x1, canvas.data.food3y1, canvas.data.food3x2, canvas.data.food3y2, fill = "")
        canvas.create_rectangle(canvas.data.food4x1, canvas.data.food4y1, canvas.data.food4x2, canvas.data.food4y2, fill = "")

    def keyPressed(event):
        canvas.data.count += 1
        print event.keysym
        if(event.keysym == "Up" and canvas.data.y1 > 10):
            canvas.data.y1 -= 10
            canvas.data.y2 -= 10
        elif(event.keysym == "Down" and canvas.data.y2 < 990):
            canvas.data.y1 += 10
            canvas.data.y2 += 10
        elif(event.keysym == "Right" and canvas.data.x2 < 990):
            canvas.data.x1 += 10
            canvas.data.x2 += 10
        elif(event.keysym == "Left" and canvas.data.x1 > 10):
            canvas.data.x1 -= 10
            canvas.data.x2 -= 10
        else:
            pass

    def timerFired():
        redrawAll()
        canvas.after(canvas.data.delay, timerFired)
        '''if(canvas.data.direction == "up" and canvas.data.y1 > 10):
            canvas.data.y1 -= 10
            canvas.data.y2 -= 10
        elif(canvas.data.direction == "down" and canvas.data.y2 < 990):
            canvas.data.y1 += 10
            canvas.data.y2 += 10
        elif(canvas.data.direction == "Right" and canvas.data.x2 < 990):
            canvas.data.x1 += 10
            canvas.data.x2 += 10
        elif(canvas.data.direction == "Left" and canvas.data.x1 > 10):
            canvas.data.x1 -= 10
            canvas.data.x2 -= 10'''
        '''
        if(canvas.data.x2 >= 950 and canvas.data.y2 >= 950):
            canvas.data.color = "magenta"
        else:
            canvas.data.color = "green"'''

        if(canvas.data.x1 <= 11):
            flag = False
        elif(canvas.data.x2 >= 989):
            flag = False
        elif(canvas.data.y1 <= 11):
            flag = False
        elif(canvas.data.y2 >= 989):
            flag = False
        else:
            flag = True

        if(canvas.data.x1 == canvas.data.foodx1 and canvas.data.y1 == canvas.data.foody1 and canvas.data.x2 == canvas.data.foodx2 and canvas.data.y2 == canvas.data.foody2):
            addmultiplier()
            canvas.data.foodx1 = random.randrange(10, 900, 10)
            canvas.data.foody1 = random.randrange(10, 900, 10)  
            canvas.data.foodx2 = canvas.data.foodx1 + 20  
            canvas.data.foody2 = canvas.data.foody1 + 20
            canvas.data.color1 = "red"
            canvas.data.count = 0
        elif(canvas.data.x1 == canvas.data.food2x1 and canvas.data.y1 == canvas.data.food2y1 and canvas.data.x2 == canvas.data.food2x2 and canvas.data.y2 == canvas.data.food2y2):
            addmultiplier()
            canvas.data.food2x1 = random.randrange(10, 900, 10)
            canvas.data.food2y1 = random.randrange(10, 900, 10)  
            canvas.data.food2x2 = canvas.data.food2x1 + 20  
            canvas.data.food2y2 = canvas.data.food2y1 + 20
            canvas.data.color1 = "red"
            canvas.data.count = 0
        elif(canvas.data.x1 == canvas.data.food3x1 and canvas.data.y1 == canvas.data.food3y1 and canvas.data.x2 == canvas.data.food3x2 and canvas.data.y2 == canvas.data.food3y2):
            addmultiplier()
            canvas.data.food3x1 = random.randrange(10, 900, 10)
            canvas.data.food3y1 = random.randrange(10, 900, 10)  
            canvas.data.food3x2 = canvas.data.food3x1 + 20  
            canvas.data.food3y2 = canvas.data.food3y1 + 20
            canvas.data.color1 = "red"
            canvas.data.count = 0
        elif(canvas.data.x1 == canvas.data.food4x1 and canvas.data.y1 == canvas.data.food4y1 and canvas.data.x2 == canvas.data.food4x2 and canvas.data.y2 == canvas.data.food4y2):
            addmultiplier()
            canvas.data.food4x1 = random.randrange(10, 900, 10)
            canvas.data.food4y1 = random.randrange(10, 900, 10)  
            canvas.data.food4x2 = canvas.data.food4x1 + 20  
            canvas.data.food4y2 = canvas.data.food4y1 + 20
            canvas.data.color1 = "red"
            canvas.data.count = 0

        if(canvas.data.count > 0):
            canvas.data.color1 = "black"
    def addmultiplier():
        canvas.data.addmultiplier += 1
    def init():
    	#Block
        canvas.data.x1 = 140
        canvas.data.y1 = 90
        canvas.data.y2 = 110
        canvas.data.x2 = 160
        canvas.data.color = "green"
        #other
        #direction = event.keysym
        #canvas.data.direction = ""
        canvas.data.color1 = "black"
        flag = True
        canvas.data.count = 0
        canvas.data.addmultiplier = 1
        canvas.data.width = 1000
        canvas.data.height = 1000
        canvas.data.delay = 1
        #second block
        canvas.data.blockx1 = 170
        canvas.data.blocky1 = 170
        canvas.data.color = "Saddle Brown"
        #image
        photo = PhotoImage(file="Freddy.gif")
        canvas.photo = photo
        photo = PhotoImage(file="Cupcake.gif")
        canvas.food2photo = photo
        photo= PhotoImage(file="Cupcake.gif")
        canvas.food3photo = photo
        photo= PhotoImage(file="Cupcake.gif")
        canvas.food4photo = photo
        #food
        canvas.data.foodx1 = random.randrange(10, 900, 10)
        canvas.data.foody1 = random.randrange(10, 900, 10)  
        canvas.data.foodx2 = canvas.data.foodx1 + 20  
        canvas.data.foody2 = canvas.data.foody1 + 20
        #food2
        canvas.data.food2x1 = random.randrange(10, 900, 10)
        canvas.data.food2y1 = random.randrange(10, 900, 10)  
        canvas.data.food2x2 = canvas.data.food2x1 + 20  
        canvas.data.food2y2 = canvas.data.food2y1 + 20
        #food3
        canvas.data.food3x1 = random.randrange(10, 900, 10)
        canvas.data.food3y1 = random.randrange(10, 900, 10)  
        canvas.data.food3x2 = canvas.data.food3x1 + 20  
        canvas.data.food3y2 = canvas.data.food3y1 + 20
        #food4
        canvas.data.food4x1 = random.randrange(10, 900, 10)
        canvas.data.food4y1 = random.randrange(10, 900, 10)  
        canvas.data.food4x2 = canvas.data.food4x1 + 20  
        canvas.data.food4y2 = canvas.data.food4y1 + 20

        canvas.data.red_delay = 0

    def main():
        global root
        root = Tk()
        global canvas
        canvas = Canvas(root, width = 1000, height = 1000)
        canvas.pack()
        class Struct(): pass
        canvas.data = Struct()
        init()
        timerFired()
        root.bind("<Key>", keyPressed)
        root.mainloop()

    main()
