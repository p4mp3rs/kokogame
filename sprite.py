from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self,image_name, x, y, width, height):
        self.image = transform.scale(image.load(image_name),(width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def draw(self,window):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):

    def move(self):
        keys = key.get_pressed()
        if key == [K_LEFT] and self.rect.x != 5:
            self.rect.x -= 5
        elif key == [K_RIGHT] and self.rect.x != 695:
            self.rect.x += 5

class Egg(GameSprite):
    pass
    


