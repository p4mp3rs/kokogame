from pygame import *
from button import Button
window = display.set_mode((700,500))

game = True
clock = time.Clock()

btn1 = Button('start.png', 100,100,100,50)
btn2 = Button('exit.png', 100,150,100,50)
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    window.fill((255,255,255))
    if btn1.draw(window):
        print('Pressed')
    if btn2.draw(window):
        print('Pressed')
    display.update()
    clock.tick(60)