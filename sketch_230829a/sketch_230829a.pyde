x, y, speedX, speedY = 0, 0, 0, 0
diam = 10
rectSize = 200

def setup():
    size(600, 500)
    fill(0, 255, 0)
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
    ellipse(x, y, diam, diam)

class Particle(object):
    def __init__(self, x, y, diam):
        self.x = x
        self.y = y
        self.diam =  diam
    
    def drawSelf(self):
        ellipse(self.x, self.y, self.diam, self.diam)

def mousePressed():
    reset()
