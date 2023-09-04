x, y, velX, velY = 0, 0, 0, 0
diam = 10
rectSize = 100
objs = []

def restart():
    global x, y, velX, velY
    # set ball coordinates to middle of screen once game restarts
    x = width/2
    y = height/2
    velX = random(2,6)
    velY = random(3,6)

def setup():
    size(800,550)
    restart()

def draw():
    global x, y, velX, velY, objs
    background(0)
    
    ball = Particle(x, y, diam)
    wall = Rectangle(0, 0, 20, height)
    bar = Rectangle(width-15, mouseY-rectSize/2, 8, rectSize)
    objs = [ball, wall, bar]
    for obj in objs:
        obj.drawSelf()
    
    checkHit()
    x += velX
    y += velY

def keyPressed():
    restart()

def checkHit():
    global velX, velY, x, y
    if y > height or y < 0:
        velY *= -1
    elif (x > width-15) and (x < width-10) and (y > mouseY-rectSize/2) and (y < mouseY+rectSize/2):
        velX = velX*-1
    elif x < 20:
        velX *= -1.3
        velY *= 1.3
        x += velX
    
class Particle(object):
    def __init__(self, x, y, diam):
        self.x = x
        self.y = y
        self.diam =  diam
    
    def drawSelf(self):
        fill(255, 255, 255)
        circle(self.x, self.y, self.diam)
        
class Rectangle(object):
    def __init__(self, xcoord, ycoord, rectWidth, rectHeight):
        self.xcoord = xcoord
        self.ycoord = ycoord
        self.rectWidth = rectWidth
        self.rectHeight = rectHeight
    
    def drawSelf(self):
        fill(255, 255, 255)
        rect(self.xcoord, self.ycoord, self.rectWidth, self.rectHeight)
