import pgzrun
import math
import time

WIDTH = 800
HEIGHT = 600

car = Actor('car1', (50, 500))
car.angle = 90
speed = 0

RED = (255,0,0)
BOX1 = Rect((100, HEIGHT-400), (100, 400))
BOX2 = Rect((400, 0), (100, 400))
BOX3 = Rect((600, HEIGHT-400), (75, 400))

box_list = [BOX1, BOX2, BOX3]

META = Rect((685,500), (115,25))

def draw():
    screen.fill((0,0,0))
    #screen.blit('4a', (0,0))

    screen.draw.filled_rect(BOX1, RED)
    screen.draw.filled_rect(BOX2, RED)
    screen.draw.filled_rect(BOX3, RED)
    car.draw()
    screen.draw.filled_rect(META,(255,255,255))


def update():
    global speed

    car_rad = math.radians(car.angle)
    car.x += speed * math.cos(car_rad)
    car.y += -speed * math.sin(car_rad)

    speed = speed * 0.99

    if keyboard.LEFT:
        car.angle += 1
    if keyboard.RIGHT:
        car.angle -= 1

    if keyboard.UP:
        if speed < 5:
            speed += 1

    if keyboard.DOWN:
        if speed < 5:
            speed += -1

    if keyboard.U:
        if speed < -1:
            speed -= 1


    for box in box_list:
        if car.colliderect(box):
            time.sleep(1)
            car.pos = (75,500)
            speed = 0
            car.angle = 90
            screen.draw.text("Przegrana", center=(WIDTH / 2, HEIGHT / 2), fontsize = 100)

    if car.colliderect(box):
        speed = 0
        print("Brawko")


    print(speed)
    #print("cos: " + str(math.cos(car_rad)))
    #print("sin: " + str(math.sin(car_rad)))



pgzrun.go()
