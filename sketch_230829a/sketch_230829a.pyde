x, y, speedX, speedY = 0, 0, 0, 0
diam = 10
rectSize = 200

def setup():
    size(600, 500)
    fill(255, 255, 255)
    reset()

def reset():
    global x, y, speedX, speedY
    x = width/2
    y = height/2
    speedX = 4
    speedY = 4

def draw():
    global x, y, speedX, speedY
    background(0)
    ball = Particle(x, y, diam)
    ball.drawSelf()
    
    rect(0, 0, 20, height)
    rect(width-30, mouseY-rectSize/2, 10, rectSize)
    x += speedX
    y += speedY

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

def mousePressed():
    reset()
