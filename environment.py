import pygame as p
import math
import random
from config import *


class spritesheet:
    def __init__(self,file):
        self.sheet = p.image.load(file)
        
    def get_sprite(self,x,y,width,height):
        sprite = p.Surface([width,height])
        sprite.blit(self.sheet,(0,0),(x,y,width,height))
        sprite.set_colorkey(WHITE)
        return(sprite)


class floor(p.sprite.Sprite):
    def __init__(self,g,x,y):
        self.game = g
        self.groups = self.game.all_sprites
        self._layer = GROUND_LAYER
        p.sprite.Sprite.__init__(self,self.groups)
        
        img_x = random.randint(0,1)*TILESIZE
        img_y = random.randint(0,3)*TILESIZE
        self.image = spritesheet("images/environment/floor.png").get_sprite(img_x,img_y,TILESIZE,TILESIZE)
        self.rect = self.image.get_rect()
        self.rect.x = x*TILESIZE
        self.rect.y = y*TILESIZE
        
    def update(self):
        pass

class road(p.sprite.Sprite):
    def __init__(self,g,x,y):
        self.game = g
        self.groups = self.game.all_sprites
        self._layer = GROUND_LAYER
        p.sprite.Sprite.__init__(self,self.groups)
        
        img_x = random.randint(0,7)*TILESIZE
        img_y = random.randint(4,7)*TILESIZE
        self.image = spritesheet("images/environment/floor.png").get_sprite(img_x,img_y,TILESIZE,TILESIZE)
        self.rect = self.image.get_rect()
        self.rect.x = x*TILESIZE
        self.rect.y = y*TILESIZE
        
    def update(self):
        pass
    
    
class front_wall(p.sprite.Sprite):
    def __init__(self,g,x,y,t,img_x):
        self.game = g
        self.groups = self.game.all_sprites, self.game.walls
        self._layer = GROUND_LAYER
        p.sprite.Sprite.__init__(self,self.groups)
        
        self.type = t
        
        if self.type == "W":
            img_y = 6*TILESIZE
        elif self.type == "w":
            img_y = 7*TILESIZE
            
        self.image = spritesheet("images/environment/wall.png").get_sprite(img_x,img_y,TILESIZE,TILESIZE)
        self.mask = p.mask.from_surface(self.image)
        self.mask.fill()
        
        self.rect = self.image.get_rect()
        self.rect.x = x*TILESIZE
        self.rect.y = y*TILESIZE
        
    def update(self):
        pass
    
class back_wall(p.sprite.Sprite):
    def __init__(self,g,x,y,t):
        self.game = g
        self.groups = self.game.all_sprites, self.game.walls
        self._layer = GROUND_LAYER
        p.sprite.Sprite.__init__(self,self.groups)
        
        self.type = t
        
        if self.type == "B":
            img_y = 289
        elif self.type == "b":
            img_y = 289 + TILESIZE
            
        self.image = spritesheet("images/environment/wall.png").get_sprite(292,img_y,TILESIZE,TILESIZE)
        self.mask = p.mask.from_surface(self.image)
        self.mask.fill()
        
        self.rect = self.image.get_rect()
        self.rect.x = x*TILESIZE
        self.rect.y = y*TILESIZE
        
    def update(self):
        pass


class side_wall(p.sprite.Sprite):
    def __init__(self,g,x,y,t):
        self.game = g
        self.groups = self.game.all_sprites, self.game.walls
        self._layer = GROUND_LAYER
        p.sprite.Sprite.__init__(self,self.groups)
        
        self.type = t
        if self.type == "T":
            self.image = spritesheet("images/environment/wall.png").get_sprite(279,173,TILESIZE,TILESIZE)
        elif self.type =="t":
            self.image = spritesheet("images/environment/wall.png").get_sprite(261,173,TILESIZE,TILESIZE)
            
        self.mask = p.mask.from_surface(self.image)
        
        self.rect = self.image.get_rect()
        self.rect.x = x*TILESIZE
        self.rect.y = y*TILESIZE
        
    def update(self):
        pass


class rock(p.sprite.Sprite):
    def __init__(self,g,x,y):
        self.game = g
        self.groups = self.game.all_sprites, self.game.walls
        self._layer = GROUND_LAYER
        p.sprite.Sprite.__init__(self,self.groups)
        
        choice = random.randint(0,4)
        self.image = spritesheet("images/environment/rocks.png").get_sprite(40,14,17,14)
        if choice == 1:
            self.image = spritesheet("images/environment/rocks.png").get_sprite(100,11,25,19)
        elif choice == 2:
            self.image = spritesheet("images/environment/rocks.png").get_sprite(68,11,25,19)
        elif choice == 3:
            self.image = spritesheet("images/environment/rocks.png").get_sprite(130,8,29,22)
        elif choice == 4:
            self.image = spritesheet("images/environment/rocks.png").get_sprite(162,6,29,27)
            
        self.mask = p.mask.from_surface(self.image)
        
        self.rect = self.image.get_rect()
        self.rect.x = x*TILESIZE
        self.rect.y = y*TILESIZE
        
    def update(self):
        pass