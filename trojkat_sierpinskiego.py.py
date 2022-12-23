import time
import random

WIDTH = 500
HEIGHT = 500

pozycja_x = 500
pozycja_y = 400

x1 = 0
y1 = 400

x2 = 500
y2 = 400

x3 = 250
y3 = 100

def draw():
    screen.draw.filled_circle((x1,y1),20,(0,255,0))
    screen.draw.filled_circle((x2,y2),20,(0,255,0))
    screen.draw.filled_circle((x3,y3),20,(0,255,0))

    #punkt kroczący
    screen.draw.filled_circle((pozycja_x,pozycja_y),5,(255,255,255))

def update():
    global pozycja_x, pozycja_y
    losuj = random.randint(0,2)
    if losuj == 0:
        pozycja_x = (x1 + pozycja_x) / 2
        pozycja_y = (y1 + pozycja_y) / 2
    elif losuj == 1:
        pozycja_x =(x2 + pozycja_x) / 2
        pozycja_y = (y2 + pozycja_y) / 2
    elif losuj == 2:
        pozycja_x =(x3 + pozycja_x) / 2
        pozycja_y = (y3 + pozycja_y) / 2

    #time.sleep(0.5)
