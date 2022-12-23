import pgzrun

WIDTH = 600
HEIGHT = 400

paletka = Actor("paletka", (400, 350))
pilka = Actor("pilka", (300, 200))
pilka.predkosc_x = 5
pilka.predkosc_y = 5


cegly = []

gra_gra = True

for i in range(5):
    for j in range(5):
        cegly.append(Actor("paletka", (1.1 * i * 100 + 75, 25 * j + 25)))


def draw():
    screen.fill((45, 211, 245))
    paletka.draw()
    pilka.draw()

    for cegla in cegly:
        cegla.draw()
    if not gra_gra:
        screen.draw.text(
            "Przegrales! \n Kliknij tutaj zeby rozpoczac ponownie gre :) \n Lub kliknij 'X' zeby wyjsc z gry",
            center=(WIDTH / 2, HEIGHT / 2),
        )
        if keyboard.X:
            pygame.quit()


def update():
    global gra_gra

    if gra_gra:
        gracz_sterowanie()
        pilka_sterowanie()
    if len(cegly) == 0:
        gra_gra = False
    print(len(cegly))


def gracz_sterowanie():
    if keyboard.right:
        paletka.x += 5
    if keyboard.left:
        paletka.x -= 5
    if paletka.right > WIDTH:
        paletka.x -= 5
    if paletka.left < 0:
        paletka.x += 5


def pilka_sterowanie():
    global gra_gra
    pilka.x += pilka.predkosc_x
    pilka.y += pilka.predkosc_y

    if pilka.x > WIDTH:
        pilka.predkosc_x *= -1
    if pilka.x < 0:
        pilka.predkosc_x *= -1
    if pilka.y > HEIGHT:
        # pilka.predkosc_y *= -1
        gra_gra = False
    if pilka.y < 0:
        pilka.predkosc_y *= -1
    if pilka.colliderect(paletka):
        pilka.predkosc_y *= -1
    for index, cegla in enumerate(cegly):
        if pilka.colliderect(cegla):
            pilka.predkosc_y *= -1
            cegly.pop(index)
            print(cegly)


def on_mouse_down():
    global gra_gra, paletka, pilka, cegly

    if not gra_gra:
        paletka = Actor("paletka", (400, 350))
        pilka = Actor("pilka", (300, 200))
        pilka.predkosc_x = 5
        pilka.predkosc_y = 5
        cegly.clear()
        for i in range(5):
            for j in range(5):
                cegly.append(Actor("paletka", (1.1 * i * 100 + 75, 25 * j + 25)))
    gra_gra = True


pgzrun.go()
