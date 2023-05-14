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

normaleggs = []
goldeneggs = []
diamondeggs = []
amethysteggs = []
run = False
hen = Player('kokohen.png',345,400,45,45,10)
for i in range(4):
    normalegg = Egg('kokonormalegg.png',randint(80,650),randint(0,80),60,60,randint(1,2))
    normaleggs.append(normalegg)
for i in range(1):
    goldenegg = Egg('kokogoldenegg.png',randint(80,650),randint(0,80),60,60,randint(5,10))
    goldeneggs.append(goldenegg)
for i in range(1):
    diamondegg = Egg('kokodiamondegg.png',randint(80,650),randint(0,80),60,60,randint(5,15))
    diamondeggs.append(diamondegg)
for i in range(1):
    amethystegg = Egg('kokoamethystegg.png',randint(80,650),randint(0,80),60,60,randint(10,20))
    amethysteggs.append(amethystegg)

font.init() 
font = font.SysFont("Arial",20)

score = 0
lost = 0
text = font.render('Score:'+str(score),True,(255,212,57))
text2 = font.render('Lost:  '+str(lost),True,(255,212,57))
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
        for n in normaleggs:
            n.update(window)
        for g in goldeneggs:
            g.update(window)
        for d in diamondeggs:
            d.update(window)
        for a in amethysteggs:
            a.update(window)            
        window.blit(text,(20,20))
        window.blit(text2,(20,50))
        
        for n in normaleggs:
            if n.rect.colliderect(hen.rect):
                score += 1
                n.rect.y = randint(0,80)
                n.rect.x = randint(50,650)
                n.speed = randint(1,2)
                text = font.render('Score:'+str(score),True,(255,212,57))
                window.blit(text,(20,20))
            if n.rect.y > 490:
                lost += 1
                n.rect.y = randint(0,80)
                n.rect.x = randint(50,650)
                n.speed = randint(1,2)
                text2 = font.render('Lost:  '+str(lost),True,(255,212,57))
                window.blit(text2,(20,50))
            
            for g in goldeneggs:
                if g.rect.colliderect(hen.rect):
                    score += 2
                    g.rect.y = randint(0,80)
                    g.rect.x = randint(50,650)
                    g.speed = randint(5,10)
                    text = font.render('Score:'+str(score),True,(255,212,57))
                    window.blit(text,(20,20))
                if g.rect.y > 490:
                    lost += 1
                    g.rect.y = randint(0,80)
                    g.rect.x = randint(50,650)
                    g.speed = randint(5,10)
                    text2 = font.render('Lost:  '+str(lost),True,(255,212,57))
                    window.blit(text2,(20,50))
            for d in diamondeggs:
                if d.rect.colliderect(hen.rect):
                    score += 5
                    d.rect.y = randint(0,80)
                    d.rect.x = randint(50,650)
                    d.speed = randint(7,15)
                    text = font.render('Score:'+str(score),True,(255,212,57))
                    window.blit(text,(20,20))
                if n.rect.y > 490:
                    lost += 1
                    d.rect.y = randint(0,80)
                    d.rect.x = randint(50,650)
                    d.speed = randint(7,15)
                    text2 = font.render('Lost:  '+str(lost),True,(255,212,57))
                    window.blit(text2,(20,50))
            for a in amethysteggs:
                if a.rect.colliderect(hen.rect):
                    score += 10
                    a.rect.y = randint(0,80)
                    a.rect.x = randint(50,650)
                    a.speed = randint(10,20)
                    text = font.render('Score:'+str(score),True,(255,212,57))
                    window.blit(text,(20,20))
                if a.rect.y > 490:
                    lost += 1
                    a.rect.y = randint(0,80)
                    a.rect.x = randint(50,650)
                    a.speed = randint(10,20)
                    text2 = font.render('Lost:  '+str(lost),True,(255,212,57))
                    window.blit(text2,(20,50))
    else:
        if btn1.draw(window):   
            run = True   
        if btn2.draw(window):
            game = False
    display.update()
    clock.tick(60)