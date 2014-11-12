#########################################
#
#    100pt - Putting it together!
#
#########################################

# Animate the target area to bounce from left to right.
# Add in buttons for movement left, right, up and down
# Add in boundary detection for the edges (don't let the player move off screen)
# Add in collision detection - and STOP the target when you catch it!

from Tkinter import *
root = Tk()
drawpad = Canvas(root, width=480,height=320, background='white')
targetx1 = 200
targety1 = 20
targetx2 = 280
targety2 = 80
target = drawpad.create_rectangle(targetx1,targety1,targetx2,targety2, fill="blue")
player = drawpad.create_rectangle(240,240,260,260, fill="pink")
direction = 4


class MyApp:
	def __init__(self, parent):
	        global drawpad
		self.myParent = parent  
		self.myContainer1 = Frame(parent)
		self.myContainer1.pack()
		
		self.up = Button(self.myContainer1)
		self.up.configure(text="Up", background= "purple")
		self.up.grid(row=0,column=0)												
		self.up.bind("<Button-1>", self.moveUp)
                
                self.up = Button(self.myContainer1)
		self.up.configure(text="Down", background= "orange")
		self.up.grid(row=1,column=0)												
		self.up.bind("<Button-1>", self.moveDown)
		
		self.up = Button(self.myContainer1)
		self.up.configure(text="Right", background= "red")
		self.up.grid(row=0,column=1)												
		self.up.bind("<Button-1>", self.moveRight)
		
		self.up = Button(self.myContainer1)
		self.up.configure(text="Left", background= "yellow")
		self.up.grid(row=1,column=1)												
		self.up.bind("<Button-1>", self.moveLeft)
		  
		drawpad.pack()
		self.animate()

		
	def moveUp(self, event):   
		global player
		global drawpad
		x1,y1,x2,y2 = drawpad.coords(player)
	        if y1 > 0:
                    drawpad.move(player,0,-10)
                   
        def moveDown(self, event):   
		global player
		global drawpad
                x1,y1,x2,y2 = drawpad.coords(player)
	        if y2 < drawpad.winfo_height():
                    drawpad.move(player,0,10)
        
        def moveRight(self, event):   
		global player
		global drawpad
                x1,y1,x2,y2 = drawpad.coords(player)
	        if x2 <drawpad.winfo_width():
	           drawpad.move(player,10,0)
            
        def moveLeft(self, event):   
		global player
		global drawpad
                x1,y1,x2,y2 = drawpad.coords(player)
	        if x1 >0:
	           drawpad.move(player,-10,0)
        
	def animate(self):
	    global target
	    global direction
	    tx1,ty1,tx2,ty2=drawpad.coords(target)
	    if tx1 < 0:
	       direction = 10
	    if tx2 > 480:
	       direction = -10
	    drawpad.move(target,direction,0)
	    didWeHit = self.collisionDetect()
            if didWeHit:
                drawpad.after(10, self.animate)
            
	def collisionDetect(self):
                global target
		global drawpad
                global player
                x1,y1,x2,y2=drawpad.coords(player)
                tx1,ty1,tx2,ty2=drawpad.coords(target)
                if (x1 > tx1 and x2 < tx2) and (y1 > ty1 and y2 < ty2):
                    return False
                else:
                    return True             
		
myapp = MyApp(root)

root.mainloop()