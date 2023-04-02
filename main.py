from pygame import *

window = display.set_mode((700,500))

game = True
clock = time.Clock()

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    window.fill((255,255,255))

    display.update()
    clock.tick(60)