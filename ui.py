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
    
####################################################################### PLAYER HEALTHBAR CLASS #####################################################################
class player_healthbar(p.sprite.Sprite):
    def __init__(self,g):
        self.game = g
        self._layer = UI_LAYER
        self.groups = self.game.all_sprites, self.game.ui
        p.sprite.Sprite.__init__(self,self.groups)
        
        self.width = 333
        self.height = 24
        
        self.img_spritesheet = spritesheet("images/UI/player_healthbar.png")
        self.image = self.img_spritesheet.get_sprite(0,0,self.width,self.height)
        self.rect = self.image.get_rect()
        self.rect.x = 20
        self.rect.y = HEIGHT - 2*self.height - 20
    
    def update(self):
        self.rect.x = 20
        self.rect.y = HEIGHT - 2*self.height - 20
        self.image = self.img_spritesheet.get_sprite(0,(10-self.game.player.health)*self.height,self.width,self.height)

################################################################### PLAYER MANABAR CLASS ######################################################################
class player_manabar(p.sprite.Sprite):
    def __init__(self,g):
        self.game = g
        self._layer = UI_LAYER
        self.groups = self.game.all_sprites, self.game.ui
        p.sprite.Sprite.__init__(self,self.groups)
        
        self.width = 333
        self.height = 24
        
        self.img_spritesheet = spritesheet("images/UI/player_manabar.png")
        self.image = self.img_spritesheet.get_sprite(0,0,self.width,self.height)
        self.rect = self.image.get_rect()
        self.rect.x = 20
        self.rect.y = HEIGHT - self.height - 20
    
    def update(self):
        self.rect.x = 20
        self.rect.y = HEIGHT - self.height - 20
        self.image = self.img_spritesheet.get_sprite(0,(10-self.game.player.mana)*self.height,self.width,self.height)

############################################################################## ENEMY HEALTHBAR CLASS ######################################################################
class enemy_healthbar(p.sprite.Sprite):
    def __init__(self,g,o):
        self.game = g
        self._layer = UI_LAYER
        self.groups = self.game.all_sprites , self.game.ui
        p.sprite.Sprite.__init__(self,self.groups)
        
        self.owner = o
        
        self.width = 90
        self.height = 8
        
        self.img_spritesheet = spritesheet("images/UI/enemy_healthbar.png")
        self.image = self.img_spritesheet.get_sprite(0,0,self.width,self.height)
        self.rect = self.image.get_rect()
        self.rect.x = o.rect.x 
        self.rect.y = o.rect.y 
    
    def update(self):
        self.rect.x = self.owner.rect.x 
        self.rect.y = self.owner.rect.y 
        self.image = self.img_spritesheet.get_sprite(0,(3-self.owner.health)*self.height,self.width,self.height)
        
############################################################################# PLAYER INVENTORY CLASS ###########################################################################        
class player_inventory(p.sprite.Sprite):
    def __init__(self,g,o):
        self.game = g
        self._layer = UI_LAYER
        self.groups = self.game.all_sprites , self.game.ui
        p.sprite.Sprite.__init__(self,self.groups)
        
        self.owner = o
        
        self.width = 272
        self.height = 99
        
        self.img_spritesheet = spritesheet("images/UI/player_inventory.png")
        self.image = self.img_spritesheet.get_sprite(0,0,self.width,self.height)
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH - self.width - 20
        self.rect.y = HEIGHT - self.height - 20
    
    def update(self):
        if self.owner.selected_inventory_slot == 1:
            self.image = self.img_spritesheet.get_sprite(0,0,self.width,self.height)
        if self.owner.selected_inventory_slot == 2:
            self.image = self.img_spritesheet.get_sprite(0,101,self.width,self.height)
        if self.owner.selected_inventory_slot == 3:
            self.image = self.img_spritesheet.get_sprite(0,201,self.width,self.height)
        if self.owner.selected_inventory_slot == 4:
            self.image = self.img_spritesheet.get_sprite(0,301,self.width,self.height)
            
        self.rect.x = WIDTH - self.width - 20
        self.rect.y = HEIGHT - self.height - 20
        
############################################################################### POTION ICONS CLASS ###############################################################################       
class ui_potion(p.sprite.Sprite):
    
    def __init__(self,g):
        self.game = g
        self._layer = UI_LAYER
        self.groups = self.game.all_sprites, self.game.ui
        p.sprite.Sprite.__init__(self,self.groups)
        
        self.width = 22
        self.height = 26
        self.image = spritesheet("images/interactables/potions.png").get_sprite(0,40,self.width,self.height)
        self.rect = self.image.get_rect()
    
    def update(self):
        pass

class health_ui_potion(ui_potion):
    def __init__(self,g):
        ui_potion.__init__(self,g)
        self.rect.x = WIDTH - 257
        self.rect.y = HEIGHT - 79
        
    def update(self):
        if self.game.player.inventory["health_potion"] > 0:
            self.image = spritesheet("images/interactables/potions.png").get_sprite(0,0,self.width,self.height)
        else:
            self.image = spritesheet("images/interactables/potions.png").get_sprite(0,40,self.width,self.height)
        
class mana_ui_potion(ui_potion):
    def __init__(self,g):
        ui_potion.__init__(self,g)
        self.rect.x = WIDTH - 197
        self.rect.y = HEIGHT - 79 
        
    def update(self):
        if self.game.player.inventory["mana_potion"] > 0:
            self.image = spritesheet("images/interactables/potions.png").get_sprite(32,0,self.width,self.height)    
        else:
            self.image = spritesheet("images/interactables/potions.png").get_sprite(0,40,self.width,self.height)
        
class speed_ui_potion(ui_potion):
    def __init__(self,g):
        ui_potion.__init__(self,g)
        self.rect.x = WIDTH - 137
        self.rect.y = HEIGHT - 79
        
    def update(self):
        if self.game.player.inventory["speed_potion"] > 0:
            self.image = spritesheet("images/interactables/potions.png").get_sprite(64,0,self.width,self.height)  
        else:
            self.image = spritesheet("images/interactables/potions.png").get_sprite(0,40,self.width,self.height)
            
class attack_ui_potion(ui_potion):
    def __init__(self,g):
        ui_potion.__init__(self,g)
        self.rect.x = WIDTH - 77
        self.rect.y = HEIGHT - 79
        
    def update(self):
        if self.game.player.inventory["attack_potion"] > 0:
            self.image = spritesheet("images/interactables/potions.png").get_sprite(96,0,self.width,self.height)  
        else:
            self.image = spritesheet("images/interactables/potions.png").get_sprite(0,40,self.width,self.height)
        
        
        
        
        
        
        
        
        
        
        
        
        















