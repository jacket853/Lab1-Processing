'''
Name: Jack Harvey
Date: 9/6/23
Description: The classic video game Pong, reimagined in Processing's wonderful Python v2.7
'''

# clearing console??
# import os
# os.system('cls' if os.name == 'nt' else 'clear')

x, y, velX, velY = 0, 0, 0, 0
DIAM = 10
RECTSIZE = 100
objs = []
score = 0

def setup():
    size(800,550)
    restart()

def draw():
    global x, y, velX, velY, objs
    background(0)
    
    # creating objs
    ball = Particle(x, y, DIAM)
    wall = Rectangle(0, 0, 20, height)
    bar = Rectangle(width-15, mouseY-RECTSIZE/2, 8, RECTSIZE) # the bar is drawn every time at the same height as the user's mouse
    # put them all in a list - since they have the same method name (drawSelf()), we can iterate through to draw
    objs = [ball, wall, bar]
    for obj in objs:
        obj.drawSelf()
    
    checkHit()
    x += velX
    y += velY

def restart():
    # This function redraws the board (upon startup and when a key is pressed), resets the ball's coordinates/speed, and prints the game's score
    global x, y, velX, velY, score
    
    print("Your current score is: {}".format(score)) # f-strings don't come out until python 3
    score = 0 # reset game score
    x = width/2
    y = height/2
    velX = random(2,5)
    velY = random(3,6)

def keyPressed():
    # This function, upon a keypress, will call the above restart() function
    restart()

def checkHit():
    # This function runs to check if the ball has touched (if its coordinates are greater/less than the coordinates of) the bar, wall, or edges of the window. If so, it changes the ball's direction and adds speed
    global velX, velY, x, y, score
    if y > height or y < 0:
        velY *= -1
    elif (x > width-15) and (x < width-10) and (y > mouseY-RECTSIZE/2) and (y < mouseY+RECTSIZE/2):
        velX = velX*-1.2 # just a little bit faster when the ball hits the bar vs the edge
        score += 1
    elif x < 20:
        velX *= -1.1
        velY *= 1.1
        x += velX # velX is more of a vector/heading with magnitude than it is speed
    
class Particle(object):
    # This is the class for the ball, which is a circle with coordinates. It affects the rest of the game based on those coordinates
    def __init__(self, x, y, diam):
        self.x = x
        self.y = y
        self.diam = diam
    
    def drawSelf(self):
        # This method simply draws the object and fills it with white color
        fill(255, 255, 255)
        circle(self.x, self.y, self.diam)
        
class Rectangle(object):
    # This is the class used for both the user's bar and the edge - its attributes are similar to those used in the rect() function
    def __init__(self, xcoord, ycoord, rectWidth, rectHeight):
        self.xcoord = xcoord
        self.ycoord = ycoord
        self.rectWidth = rectWidth
        self.rectHeight = rectHeight
    
    def drawSelf(self):
        # This method is identical to its sibling in the previous class so that we can go through the list of objects and call the same function
        fill(255, 255, 255)
        rect(self.xcoord, self.ycoord, self.rectWidth, self.rectHeight)
