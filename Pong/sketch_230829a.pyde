x, y, speedX, speedY = 0.0, 0.0, 0.0, 0.0
diam = 10.0
rectSize = 200.0

def setup():
    fullScreen()
    fill(0, 255, 0)
    reset()

def reset():
    global x, y, speedX, speedY
    x = width/2
    y = height/2
    speedX = random(3, 5)
    speedY = random(3, 5)

def draw():
    global x, y, speedX, speedY
    background(0)
    ball = Particle(x, y, diam)
    ellipse(x, y, diam, diam)
    rect(0, 0, 20, height)
    rect(width-30, mouseY-rectSize/2, 10, rectSize)
    x += speedX
    y += speedY

    # if ball hits the moveable bar, invert X direction
    if x > width-30 and x < width -20 and y > mouseY-rectSize/2 and y < mouseY+rectSize/2:
        speedX = speedX * -1

    # if ball hits wall, change direction of X
    if x < 25:
        speedX *= -1.1
        speedY *= 1.1
        x += speedX

    # if ball hits up or down, change direction of Y
    if y > height or y < 0:
        speedY *= -1

class Particle(object):
    def __init__(self, x, y, diam):
        self.x = x
        self.y = y
        self.diam =  diam
    
    def drawSelf(self):
        ellipse(self.x, self.y, self.diam, self.diam)

def mousePressed():
    reset()
