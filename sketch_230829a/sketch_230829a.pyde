x, y, speedX, speedY = 0, 0, 0, 0
diam = 10
barSize = 100
objs = []

def setup():
    size(600, 500)
    fill(255, 255, 255)
    restart()

def draw():
    global x, y, speedX, speedY, objs
    background(0)
    
    ball = Particle(x, y, diam)
    wall = Rectangle(0, 0, 20, height)
    bar = Rectangle(width-15, mouseY-rectSize/2, 8, rectSize)
    objs = [ball, wall, bar]
    for obj in objs:
        obj.drawSelf()
    
    x += speedX
    y += speedY

def restart():
    global x, y, speedX, speedY
    x = width/2
    y = height/2
    speedX = 4
    speedY = 4
    
def keyPressed():
    restart()

class Particle(object):
    def __init__(self, x, y, diam):
        self.x = x
        self.y = y
        self.diam =  diam
    
    def drawSelf(self):
        circle(self.x, self.y, self.diam)
        
class Rectangle(object):
    def __init__(self, xcoord, ycoord, rectWidth, rectHeight):
        self.xcoord = xcoord
        self.ycoord = ycoord
        self.rectWidth = rectWidth
        self.rectHeight = rectHeight
    
    def drawSelf(self):
        rect(self.xcoord, self.ycoord, self.rectWidth, self.rectHeight)
