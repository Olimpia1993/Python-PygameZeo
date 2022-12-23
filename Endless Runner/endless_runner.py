import pgzrun


WIDTH = 800
HEIGHT = 600

player = Actor('fairy', (WIDTH / 7, HEIGHT- 32 - 125 - 256))
sky = Actor('sky', (400, HEIGHT-378))
floor = Actor('podloga', (400,HEIGHT-64))
tree = Actor('tree', (WIDTH - 32, HEIGHT - 160))

speedy = 0
counter = 0
points = 0
player.death = False

def animation_player():
    global counter
    counter +=1
    if counter % 25 >= 0:
        player.image = 'fairy2'
    if counter % 25 >= 5:
        player.image = 'fairy'
    if counter % 25 >= 10:
        player.image = 'fairy2'
    if counter % 25 >= 15:
        player.image = 'fairy'
    if counter % 25 >= 20:
        player.image = 'fairy2'

def draw():
    global points
    screen.fill((245,211,243))
    floor.draw()
    sky.draw()
    tree.draw()
    player.draw()

    screen.draw.text("Punkty: " + str(points), (20,30), fontsize = 70)

    if points > 20:
        screen.draw.text("Mistrzunio!", (80,80), fontsize = 100)

    if player.death:
        screen.draw.text("Przegrana", center=(WIDTH / 2, HEIGHT / 2), fontsize = 100)

def update():
    global speedy, points


    if player.death == False:
        if player.colliderect(floor):
            if keyboard.space:
                speedy = -13
                player.image = 'fairy_jump'
            else:
                speedy = 0
                player.y = HEIGHT - 32 - 125
                animation_player()
        else:
            speedy = speedy + 0.5
        player.y += speedy

        tree.x -= 5
        if tree.x < 30:
            tree.x = WIDTH - 32
            points += 10
        if player.colliderect(tree):
            player.death = True


pgzrun.go()


