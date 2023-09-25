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
    
    
############################################################################## CHEST CLASS ####################################################################
class chest(p.sprite.Sprite):
    
    def __init__(self,g,x,y):
        self.game = g
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites, self.game.interactables, self.game.walls
        p.sprite.Sprite.__init__(self,self.groups)
        
        self.width = 36
        self.height = 32
        self.image = spritesheet("images/interactables/chest.png").get_sprite(0,0,self.width,self.height)
        self.rect = self.image.get_rect()
        self.rect.x = x*TILESIZE
        self.rect.y = y*TILESIZE
        
        self.is_opened = False
    
    def update(self):
        pass
    
    def interact(self):
        self.is_opened = True
        self.image = spritesheet("images/interactables/chest.png").get_sprite(0,46,self.width,self.height*2)
        self.game.interactables.remove(self)
        self.rect.y -= 32//2                                #READJUSTING CHEST POSITION TO REMOVE PICTURE OFFSET 
        
        # choice = random.randint(0,3)
        # if choice == 0:
        #     pick_up_health_potion(self.game, self.rect.x + 5, self.rect.y + self.height + 20)
        # if choice == 1:
        #     pick_up_mana_potion(self.game, self.rect.x + 5, self.rect.y + self.height + 20)
        # if choice == 2:
        #     pick_up_speed_potion(self.game, self.rect.x + 5, self.rect.y + self.height + 20)
        # else:
        #     pick_up_attack_potion(self.game, self.rect.x + 5, self.rect.y + self.height + 20)
        pick_up_health_potion(self.game, self.rect.x + 5, self.rect.y + self.height + 20)
        pick_up_mana_potion(self.game, self.rect.x + 5, self.rect.y + self.height + 20)
        pick_up_speed_potion(self.game, self.rect.x + 5, self.rect.y + self.height + 20)
        pick_up_attack_potion(self.game, self.rect.x + 5, self.rect.y + self.height + 20)
        pick_up_speed_potion(self.game, self.rect.x + 5, self.rect.y + self.height + 20)
        

        
        

########################################################################### PICK_UP_POTION CLASS ##############################################################################
class pick_up_potion(p.sprite.Sprite):
    
    def __init__(self,g,x,y):
        self.game = g
        self._layer = PICKUP_LAYER
        self.groups = self.game.all_sprites, self.game.interactables
        p.sprite.Sprite.__init__(self,self.groups)
        
        self.width = 22
        self.height = 26
        self.image = spritesheet("images/interactables/potions.png").get_sprite(0,0,self.width,self.height)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.is_interactable = False
        self.interact_count = 0
    
    def update(self):
        if self.interact_count < 5:
            self.interact_count += 0.5
        else:
            self.is_interactable = True
    
    def interact(self):
        if self.is_interactable:
            self.game.all_sprites.remove(self)
            self.game.interactables.remove(self)
            

class pick_up_health_potion(pick_up_potion):
    def __init__(self,g,x,y):
        pick_up_potion.__init__(self,g,x,y)
        self.image = spritesheet("images/interactables/potions.png").get_sprite(0,0,self.width,self.height)
    
    def interact(self):
        pick_up_potion.interact(self)
        if self.is_interactable:
            self.game.player.inventory["health_potion"]+=1

class pick_up_mana_potion(pick_up_potion):
    def __init__(self,g,x,y):
        pick_up_potion.__init__(self,g,x,y)
        self.image = spritesheet("images/interactables/potions.png").get_sprite(32,0,self.width,self.height)
        
    def interact(self):
        pick_up_potion.interact(self)
        if self.is_interactable:
            self.game.player.inventory["mana_potion"]+=1

class pick_up_speed_potion(pick_up_potion):
    def __init__(self,g,x,y):
        pick_up_potion.__init__(self,g,x,y)
        self.image = spritesheet("images/interactables/potions.png").get_sprite(64,0,self.width,self.height)
        
    def interact(self):
        pick_up_potion.interact(self)
        if self.is_interactable:
            self.game.player.inventory["speed_potion"]+=1

class pick_up_attack_potion(pick_up_potion):
    def __init__(self,g,x,y):
        pick_up_potion.__init__(self,g,x,y)
        self.image = spritesheet("images/interactables/potions.png").get_sprite(96,0,self.width,self.height)
        
    def interact(self):
        pick_up_potion.interact(self)
        if self.is_interactable:
            self.game.player.inventory["attack_potion"]+=1
    

        






