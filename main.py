from pygame import *
import pygame
from button import Button
from sprite import Player,Egg,GameSprite
from random import randint
window = display.set_mode((700,500))

background_image = image.load('bg.png')
background_image = transform.scale(background_image, (700,500))
game = True
clock = time.Clock()

btn1 = Button('start.png', 300,150,100,50)
btn2 = Button('exit.png', 300,200,100,50)

eggs = []
run = False
hen = Player('kokohen.png',345,400,45,45,10)
for i in range(6):
    egg = Egg('kokoegg.png',randint(80,650),randint(0,80),30,30,randint(1,2))
    eggs.append(egg)

font.init() 
font = font.SysFont("Arial",20)
score = 0
text = font.render('Score:'+str(score),True,(255,212,57))
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                run = False
    


    if run:
        window.blit(background_image, (0,0)) 
        hen.draw(window)
        hen.move()
        for e in eggs:
            e.update(window)
        
        for e in eggs:
            if e.rect.colliderect(hen.rect):
                score += 1
                egg.rect.y = randint(0,80)
                egg.rect.x = randint(50,650)
                egg.speed = randint(1,2)

        
        window.blit(text,(20,20))
        

        
    else:
        if btn1.draw(window):   
            run = True   
        if btn2.draw(window):
            game = False
    display.update()
    clock.tick(60)