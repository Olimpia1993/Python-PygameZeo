
import pgzrun

x = 200
y = 200

def draw():
    screen.clear()
    screen.draw.circle((x, y),50,(150,230,255))
def update():
    global x, y
    if keyboard.right:
        x +=1
    if keyboard.left:
        x -=10
    if keyboard.up:
        y -=3
    if keyboard.down:
        y +=1

pgzrun.go()