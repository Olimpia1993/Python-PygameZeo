import time
import random

WIDTH = 500
HEIGHT = 500

pozycja_x = 500
pozycja_y = 400

x1 = 100
y1 = 400

x2 = 400
y2 = 400

x3 = 400
y3 = 100

x4 = 100
y4 = 100

aktualnyWierzcholek = 1

def draw():
    screen.draw.filled_circle((x1,y1),20,(0,255,0))
    screen.draw.filled_circle((x2,y2),20,(0,255,0))
    screen.draw.filled_circle((x3,y3),20,(0,255,0))
    screen.draw.filled_circle((x4,y4),20,(0,255,0))

    #punkt kroczący
    screen.draw.filled_circle((pozycja_x,pozycja_y),5,(255,255,255))

def update():
    global pozycja_x, pozycja_y, aktualnyWierzcholek
    losuj = random.randint(0,4)
    if losuj == 1:
        if aktualnyWierzcholek != 3:
            pozycja_x = (x1 + pozycja_x) / 2
            pozycja_y = (y1 + pozycja_y) / 2
            aktualnyWierzcholek = 1

    if losuj == 2:
        if aktualnyWierzcholek != 4:
            pozycja_x = (x2 + pozycja_x) / 2
            pozycja_y = (y2 + pozycja_y) / 2
            aktualnyWierzcholek = 2

    if losuj == 3:
        if aktualnyWierzcholek != 1:
            pozycja_x = (x3 + pozycja_x) / 2
            pozycja_y = (y3 + pozycja_y) / 2
            aktualnyWierzcholek = 3

    if losuj == 4:
        if aktualnyWierzcholek != 2:
            pozycja_x = (x4 + pozycja_x) / 2
            pozycja_y = (y4 + pozycja_y) / 2
            aktualnyWierzcholek = 4

    #time.sleep(0.5)
