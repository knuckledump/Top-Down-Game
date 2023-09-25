import pygame as p
import math
import random
from config import *
from environment import *
from interactables import *
from ui import *


    
class animator:
    def __init__(self,location,owner):
        
        self.owner = owner
        
        self.right_mouvement = spritesheet("images/characters/"+ location + "/right_mouvement/right_run.png")
        self.left_mouvement = spritesheet("images/characters/"+ str(location) + "/left_mouvement/left_run.png")
        self.up_mouvement = spritesheet("images/characters/"+ str(location) + "/up_mouvement/up_run.png")
        self.down_mouvement = spritesheet("images/characters/"+ str(location) + "/down_mouvement/down_run.png")
        
        self.right_attack = spritesheet("images/characters/"+ str(location) + "/right_mouvement/right_attack.png")
        self.left_attack = spritesheet("images/characters/"+ str(location) + "/left_mouvement/left_attack.png")
        self.up_attack = spritesheet("images/characters/"+ str(location) + "/up_mouvement/up_attack.png")
        self.down_attack = spritesheet("images/characters/"+ str(location) + "/down_mouvement/down_attack.png")
        
        self.idle = spritesheet("images/characters/"+ str(location) + "/idle/idle.png")
    
    def right_run_animation(self):
        
        right_mouvement_list = [self.right_mouvement.get_sprite(0,0,self.owner.width,self.owner.height),
                           self.right_mouvement.get_sprite(64,0,self.owner.width,self.owner.height),
                           self.right_mouvement.get_sprite(64*2,0,self.owner.width,self.owner.height),
                           self.right_mouvement.get_sprite(64*3,0,self.owner.width,self.owner.height),
                           self.right_mouvement.get_sprite(0,64,self.owner.width,self.owner.height)
                            ]
        
        self.owner.image = right_mouvement_list[math.floor(self.owner.animation_loop)]
        self.owner.animation_loop += 0.1
        if self.owner.animation_loop > 4:
            self.owner.animation_loop = 0
    
    def left_run_animation(self):
        
        left_mouvement_list = [self.left_mouvement.get_sprite(0,0,self.owner.width,self.owner.height),
                           self.left_mouvement.get_sprite(64,0,self.owner.width,self.owner.height),
                           self.left_mouvement.get_sprite(64*2,0,self.owner.width,self.owner.height),
                           self.left_mouvement.get_sprite(64*3,0,self.owner.width,self.owner.height),
                           self.left_mouvement.get_sprite(0,64,self.owner.width,self.owner.height)
                            ]
        
        self.owner.image = left_mouvement_list[math.floor(self.owner.animation_loop)]
        self.owner.animation_loop += 0.1
        if self.owner.animation_loop > 4:
            self.owner.animation_loop = 0
    
    def up_run_animation(self):
        
        up_mouvement_list = [self.up_mouvement.get_sprite(0,0,self.owner.width,self.owner.height),
                           self.up_mouvement.get_sprite(64,0,self.owner.width,self.owner.height),
                           self.up_mouvement.get_sprite(64*2,0,self.owner.width,self.owner.height),
                           self.up_mouvement.get_sprite(64*3,0,self.owner.width,self.owner.height),
                           self.up_mouvement.get_sprite(0,64,self.owner.width,self.owner.height)
                            ]
        
        self.owner.image = up_mouvement_list[math.floor(self.owner.animation_loop)]
        self.owner.animation_loop += 0.1
        if self.owner.animation_loop > 4:
            self.owner.animation_loop = 0
    
    def down_run_animation(self):
        
        down_mouvement_list = [self.down_mouvement.get_sprite(0,0,self.owner.width,self.owner.height),
                           self.down_mouvement.get_sprite(64,0,self.owner.width,self.owner.height),
                           self.down_mouvement.get_sprite(64*2,0,self.owner.width,self.owner.height),
                           self.down_mouvement.get_sprite(64*3,0,self.owner.width,self.owner.height),
                           self.down_mouvement.get_sprite(0,64,self.owner.width,self.owner.height)
                            ]
        
        self.owner.image = down_mouvement_list[math.floor(self.owner.animation_loop)]
        self.owner.animation_loop += 0.1
        if self.owner.animation_loop > 4:
            self.owner.animation_loop = 0
    
    def idle_animation(self):
        
        idle_list = [self.idle.get_sprite(0,0,self.owner.width,self.owner.height),
                           self.idle.get_sprite(64,0,self.owner.width,self.owner.height),
                           self.idle.get_sprite(64*2,0,self.owner.width,self.owner.height),
                           self.idle.get_sprite(64*3,0,self.owner.width,self.owner.height)
                            ]
        
        self.owner.image = idle_list[math.floor(self.owner.animation_loop)]
        self.owner.animation_loop += 0.1
        if self.owner.animation_loop > 3:
            self.owner.animation_loop = 0
    
    def up_attack_animation(self):
        
        up_attack_list = [self.up_attack.get_sprite(0,0,self.owner.width,self.owner.height),
                          self.up_attack.get_sprite(64,0,self.owner.width,self.owner.height),
                          self.up_attack.get_sprite(0,64,self.owner.width,self.owner.height),
                          self.up_attack.get_sprite(0,0,self.owner.width,self.owner.height)
                          ]
        
        self.owner.image = up_attack_list[math.floor(self.owner.animation_loop)]
        self.owner.animation_loop += 0.1
        if self.owner.animation_loop > 2:
            self.owner.animation_loop = 0
    
    def down_attack_animation(self):
        
        down_attack_list = [self.down_attack.get_sprite(0,0,self.owner.width,self.owner.height),
                          self.down_attack.get_sprite(64,0,self.owner.width,self.owner.height),
                          self.down_attack.get_sprite(0,64,self.owner.width,self.owner.height),
                          self.down_attack.get_sprite(0,0,self.owner.width,self.owner.height)
                          ]
        
        self.owner.image = down_attack_list[math.floor(self.owner.animation_loop)]
        self.owner.animation_loop += 0.05
        if self.owner.animation_loop > 2:
            self.owner.animation_loop = 0
    
    def left_attack_animation(self):
        
        left_attack_list = [self.left_attack.get_sprite(0,0,self.owner.width,self.owner.height),
                          self.left_attack.get_sprite(64,0,self.owner.width,self.owner.height),
                          self.left_attack.get_sprite(0,64,self.owner.width,self.owner.height),
                          self.left_attack.get_sprite(0,0,self.owner.width,self.owner.height)
                          ]
        
        self.owner.image = left_attack_list[math.floor(self.owner.animation_loop)]
        self.owner.animation_loop += 0.1
        if self.owner.animation_loop > 2:
            self.owner.animation_loop = 0
    
    def right_attack_animation(self):
        
        right_attack_list = [self.right_attack.get_sprite(0,0,self.owner.width,self.owner.height),
                          self.right_attack.get_sprite(64,0,self.owner.width,self.owner.height),
                          self.right_attack.get_sprite(0,64,self.owner.width,self.owner.height),
                          self.right_attack.get_sprite(0,0,self.owner.width,self.owner.height)
                          ]
        
        self.owner.image = right_attack_list[math.floor(self.owner.animation_loop)]
        self.owner.animation_loop += 0.1
        if self.owner.animation_loop > 2:
            self.owner.animation_loop = 0
            
        
    
########################################################################## PLAYER CLASS ####################################################################################################################
class player(p.sprite.Sprite):
    
    def __init__(self,g,x,y):
        
        self.game = g    
        self.groups = self.game.all_sprites, self.game.players
        self._layer = PLAYER_LAYER
        p.sprite.Sprite.__init__(self,self.groups)
        
        self.width = 64
        self.height = 64
        
        self.image = spritesheet("images/characters/player/idle/idle.png").get_sprite(0,0,self.width,self.height)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.mask = p.mask.from_surface(self.image)
        
        self.animation_loop = 1
        self.animator = animator("player", self)
        self.facing = "down"
        
        self.speed = PLAYER_SPEED
        self.speed_potion_timer = 0
        
        self.x_change = 0
        self.y_change = 0
        self.can_go_up = True
        self.can_go_down = True
        self.can_go_right = True
        self.can_go_left = True
        
        self.attacking = False
        self.attack_loop = 0
        self.attack_cd = PLAYER_ATTACK_CD
        self.damage_done = 1
        self.attack_potion_timer = 0
        
        self.can_interact = False
        
        self.health = 10
        self.healthbar = player_healthbar(self.game)
        
        self.mana = 10
        self.manabar = player_manabar(self.game)
        
        self.inventory = {"health_potion": 0, "mana_potion": 0, "attack_potion": 0, "speed_potion": 0}
        
        self.inventory_ui = player_inventory(self.game,self)
        self.selected_inventory_slot = 1
        self.use_cd = 10
        
        self.health_potion_ui = health_ui_potion(self.game)
        self.mana_potion_ui = mana_ui_potion(self.game)
        self.attack_potion_ui = attack_ui_potion(self.game)
        self.speed_potion_ui = speed_ui_potion(self.game)
        
        
    def update(self):
        self.speed_potion_tick()
        self.attack_potion_tick()
        self.use_cd_tick()
        
        self.mouvement()
        self.animate()
        self.attack_cd_ticker()
        self.check_for_interactables()
            
    def attack(self):
        ennemy_hits = p.sprite.spritecollide(self, self.game.enemies, False)
        if ennemy_hits:
            for hit in ennemy_hits:
                if p.sprite.collide_mask(self,hit) !=None:
                    hit.health -= self.damage_done
        
    def mouvement(self):
        self.x_change = 0
        self.y_change = 0
        
        keys = p.key.get_pressed()
        if keys[p.K_z] and self.can_go_up:
            self.y_change = -self.speed
            self.facing = "up"
        if keys[p.K_s] and self.can_go_down:
            self.y_change = self.speed
            self.facing = "down"
        if keys[p.K_q] and self.can_go_left:
            self.x_change = -self.speed
            self.facing = "left"
        if keys[p.K_d] and self.can_go_right:
            self.x_change = self.speed
            self.facing = "right"
            
        if keys[p.K_SPACE] and self.attack_cd >= PLAYER_ATTACK_CD and self.mana > 0:
            self.attacking = True
            self.attack_cd = 0
            self.mana -= 1
            self.attack()
            
        if keys[p.K_e] and self.can_interact:
            interactable_hits = p.sprite.spritecollide(self, self.game.interactables, False)
            interactable_hits[0].interact()
            
        if keys[p.K_1]:
            self.selected_inventory_slot = 1
        if keys[p.K_2]:
            self.selected_inventory_slot = 2
        if keys[p.K_3]:
            self.selected_inventory_slot = 3
        if keys[p.K_4]:
            self.selected_inventory_slot = 4
        
        if keys[p.K_u] and self.use_cd >= 10:
            if self.selected_inventory_slot == 1 and self.health < 10 and self.inventory["health_potion"] > 0:
                self.inventory["health_potion"] -= 1
                self.health += 5
                if self.health > 10:
                    self.health = 10
            
            elif self.selected_inventory_slot == 2 and self.mana < 10 and self.inventory["mana_potion"] >0:
                self.inventory["mana_potion"] -= 1
                self.mana += 5
                if self.mana > 10:
                    self.mana = 10
            
            elif self.selected_inventory_slot == 3 and self.inventory["speed_potion"] > 0:
                self.inventory["speed_potion"] -= 1
                self.speed_potion_timer = SPEED_POTION_DURATION
            
            elif self.selected_inventory_slot == 4 and self.inventory["attack_potion"] > 0:
                self.inventory["attack_potion"] -= 1
                self.attack_potion_timer = ATTACK_POTION_DURATION
                
            self.use_cd = 0
            
        
        for s in self.game.all_sprites:
            if s not in self.game.projectiles and s not in self.game.ui:
                s.rect.x -= self.x_change                                     # SIMULATING CAMERA MOUVEMENT
                s.rect.y -= self.y_change
        
        if self.x_change == 0 and self.y_change == 0:
            self.facing = ""
        
        self.reset_mouvement_permission()
        
        self.rect.x += self.x_change
        self.collide("x")
        self.rect.y += self.y_change
        self.collide("y")
    
    def use_cd_tick(self):
        if self.use_cd < 10:
            self.use_cd +=0.1
            
    def attack_potion_tick(self):
        self.damage_done = 1
        if self.attack_potion_timer > 0:
            self.damage_done = 2
            self.attack_potion_timer -= 0.02
            
    def speed_potion_tick(self):
        self.speed = PLAYER_SPEED
        if self.speed_potion_timer > 0:
            self.speed = PLAYER_SPEED + 2
            self.speed_potion_timer -= 0.02
        
    def reset_mouvement_permission(self):                        # RESETTING MOVEMENT PERMISSION AFTER COLLISION
        self.can_go_up = True
        self.can_go_down = True
        self.can_go_left = True
        self.can_go_right = True
        
    def attack_timer(self):
        
        self.attack_loop += 0.1
        if self.attack_loop > 3:                                  # USED IN ATTACK ANIMATION
            self.attacking = False
            self.attack_loop = 0
    
    def attack_cd_ticker(self):
        if self.attack_cd < PLAYER_ATTACK_CD:                          # COUNTING ATTACK CD
            self.attack_cd += 0.05
                
            
    def animate(self):
        if self.attacking:
            self.attack_timer()
            if self.facing == "up":
                self.animator.up_attack_animation()
            if self.facing == "down" or self.facing == "":
                self.animator.down_attack_animation()
            if self.facing =="left":
                self.animator.left_attack_animation()
            if self.facing == "right":
                self.animator.right_attack_animation()
                
        else:   
            if self.facing == "up":
                self.animator.up_run_animation()
            if self.facing == "down":
                self.animator.down_run_animation()
            if self.facing =="left":
                self.animator.left_run_animation()
            if self.facing == "right":
                self.animator.right_run_animation()
            if self.facing =="":
                self.animator.idle_animation()
        
    def collide(self,direction):
        
        if direction == "x":
            wall_hits = p.sprite.spritecollide(self, self.game.walls, False)
            if wall_hits:
                for hit in wall_hits:
                    if p.sprite.collide_mask(self,hit) !=None:
                        if self.rect.x < hit.rect.x:
                            self.can_go_right = False
                        else:
                            self.can_go_left = False
                    
        if direction == "y":  
            wall_hits = p.sprite.spritecollide(self, self.game.walls, False)
            if wall_hits:
                for hit in wall_hits:
                    if p.sprite.collide_mask(self,hit) !=None:
                        if self.rect.y < hit.rect.y:
                            self.can_go_down = False
                        else:
                            self.can_go_up = False
        
    def check_for_interactables(self):
        interactable_hits = p.sprite.spritecollide(self, self.game.interactables, False)
        if interactable_hits:
            self.can_interact = True
        else:
            self.can_interact = False
        
                  
       
                    
            
            
                
                
    
######################################################################################################## ENNEMY CLASS ###################################################################################    
class enemy(p.sprite.Sprite):
    
    def __init__(self,g,x,y):
        
        self.game = g    
        self.groups = self.game.all_sprites, self.game.enemies
        self._layer = PLAYER_LAYER
        p.sprite.Sprite.__init__(self,self.groups)
        
        self.width = 64
        self.height = 64
        
        self.image = spritesheet("images/characters/ennemy_2/idle/idle.png").get_sprite(0,0,self.width,self.height)
        self.rect = self.image.get_rect()
        self.rect.x = x*TILESIZE
        self.rect.y = y*TILESIZE
        
        self.mask = p.mask.from_surface(self.image)
        
        self.animation_loop = 1
        self.animator = animator("ennemy_2", self)
        self.facing = "down"
        
        self.x_change = 0
        self.y_change = 0
        
        self.can_go_up = True
        self.can_go_down = True
        self.can_go_right = True
        self.can_go_left = True
        
        self.detected_player = False
        
        self.chasing_player = False
        
        self.attacking = False
        self.attack_loop = 0
        self.attack_cd = PLAYER_ATTACK_CD
        
        self.health = 3
        self.healthbar = enemy_healthbar(self.game, self)
        
    def update(self):
        
        self.mouvement()
        self.player_collide()
        self.animate()
        self.attack_cd_ticker()
        self.do_damage()
        self.check_if_dead()
        
    def mouvement(self):
        if self.chasing_player:
            if self.game.player.rect.x < self.rect.x and self.can_go_left:
                if abs(self.game.player.rect.x - self.rect.x) >= ENNEMY_SPEED:          # FIXING GO BACK AND FORTH BUG
                    self.x_change = -ENNEMY_SPEED
                else:
                    self.x_change = -abs(self.game.player.rect.x - self.rect.x)                               
                self.facing = "left"
            elif self.game.player.rect.x > self.rect.x and self.can_go_right:
                if abs(self.game.player.rect.x - self.rect.x) >= ENNEMY_SPEED:
                    self.x_change = ENNEMY_SPEED
                else:
                    self.x_change = abs(self.game.player.rect.x - self.rect.x)
                self.facing = "right"
            
            if self.game.player.rect.y < self.rect.y and self.can_go_up:
                if abs(self.game.player.rect.y - self.rect.y) >= ENNEMY_SPEED:
                    self.y_change = -ENNEMY_SPEED
                else:
                    self.y_change = -abs(self.game.player.rect.y - self.rect.y)
                
            elif self.game.player.rect.y > self.rect.y and self.can_go_down:
                if abs(self.game.player.rect.y - self.rect.y) >= ENNEMY_SPEED:
                    self.y_change = ENNEMY_SPEED
                else:
                    self.y_change = abs(self.game.player.rect.y - self.rect.y)
            
        if not self.detected_player:
            self.facing = ""                                      # IDLE STATE IF PLAYER IS NOT NEAR
            self.check_player_is_near()
        else:
            
            self.chasing_player = True
            self.reset_mouvement_permission()
            self.rect.x += self.x_change                          # CHASING PLAYER STATE
            self.collide("x")
            self.rect.y += self.y_change
            self.collide("y")
        
        
        self.x_change = 0
        self.y_change = 0
    
    def do_damage(self):
        if self.attacking and self.attack_cd >= PLAYER_ATTACK_CD:
            self.game.player.health -= 1
            self.attack_cd = 0
    
    def attack_timer(self):
        
        self.attack_loop += 0.1
        if self.attack_loop > 3:                                  # USED IN ATTACK ANIMATION
            self.attacking = False
            self.attack_loop = 0
    
    def attack_cd_ticker(self):
        if self.attack_cd < PLAYER_ATTACK_CD:                          # COUNTING ATTACK CD
            self.attack_cd += 0.05
    
    def animate(self):
        if self.attacking:
            self.attack_timer()
            if self.facing == "left":
                self.animator.left_attack_animation()
            if self.facing == "right":
                self.animator.right_attack_animation()
        else:
            if self.facing =="left":
                self.animator.left_run_animation()
            if self.facing == "right":
                self.animator.right_run_animation()
            if self.facing =="":
                self.animator.idle_animation()
                
        self.mask = p.mask.from_surface(self.image)
        
    def check_if_dead(self):
        if self.health <= 0:
            self.game.all_sprites.remove(self,self.healthbar)
            self.game.enemies.remove(self)
            self.game.ui.remove(self.healthbar)
            
    def check_player_is_near(self):                                         
        
        if self.rect.x - ENNEMY_DETECTION_RADIUS < self.game.player.rect.x and self.rect.x + ENNEMY_DETECTION_RADIUS > self.game.player.rect.x :
            if self.rect.y - ENNEMY_DETECTION_RADIUS < self.game.player.rect.y and self.rect.y + ENNEMY_DETECTION_RADIUS > self.game.player.rect.y :
                self.detected_player = True
    
    def player_collide(self):
        player_hits = p.sprite.spritecollide(self, self.game.players, False)
        if player_hits:
            for hit in player_hits:
                if p.sprite.collide_mask(self,hit)!= None:
                    self.block_mouvement_permission()
                    self.attacking = True
                    self.chasing_player = False
        else:
            self.attacking = False
            self.chasing_player = True
        
    def collide(self,direction):
        
        if direction == "x":
            wall_hits = p.sprite.spritecollide(self, self.game.walls, False)
            if wall_hits:
                for hit in wall_hits:
                    if p.sprite.collide_mask(self,hit) !=None:
                        if self.rect.x < hit.rect.x:
                            self.can_go_right = False
                        else:
                            self.can_go_left = False
                    
        if direction == "y":  
            wall_hits = p.sprite.spritecollide(self, self.game.walls, False)
            if wall_hits:
                for hit in wall_hits:
                    if p.sprite.collide_mask(self,hit) !=None:
                        if self.rect.y < hit.rect.y:
                            self.can_go_down = False
                        else:
                            self.can_go_up = False
        
                        
    def reset_mouvement_permission(self):
        self.can_go_up = True
        self.can_go_down = True
        self.can_go_left = True
        self.can_go_right = True
    
    def block_mouvement_permission(self):
        self.can_go_up = False
        self.can_go_down = False
        self.can_go_left = False
        self.can_go_right = False
        
           
################################################################################################### CLASS PLAYER PROJECTILE ########################################################################################
class player_projectile(p.sprite.Sprite):
    def __init__(self,g,x,y):
        self.game = g
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites , self.game.projectiles
        p.sprite.Sprite.__init__(self,self.groups)
        
        self.width = 20
        self.height = 20
        
        self.image = spritesheet("images/projectiles/player_projectile.png").get_sprite(0,0,self.width,self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.game.player.rect.x + self.game.player.width //2
        self.rect.y = self.game.player.rect.y + self.game.player.height // 2
        
        self.x_goal = x
        self.y_goal = y
    
    def update(self):
        if self.rect.x > self.x_goal:
            if abs(self.rect.x - self.x_goal)>= PROJECTILE_SPEED:
                self.rect.x -= PROJECTILE_SPEED
            else:
                self.rect.x -= abs(self.rect.x - self.x_goal)
        elif self.rect.x < self.x_goal:
            if abs(self.rect.x - self.x_goal)>= PROJECTILE_SPEED:
                self.rect.x += PROJECTILE_SPEED
            else:
                self.rect.x += abs(self.rect.x - self.x_goal)
        
        if self.rect.y > self.y_goal:
            if abs(self.rect.y - self.y_goal)>= PROJECTILE_SPEED:
                self.rect.y -= PROJECTILE_SPEED
            else:
                self.rect.y -= abs(self.rect.y - self.y_goal)
        elif self.rect.y < self.y_goal:
            if abs(self.rect.y - self.y_goal)>= PROJECTILE_SPEED:
                self.rect.y += PROJECTILE_SPEED
            else:
                self.rect.y += abs(self.rect.y - self.y_goal)
        
        
    
    
    
    
    
    
    
    
    
    
#################################################################################### EXPOLOSION CLASS #######################################################################################################
class explosion (p.sprite.Sprite):
    
    def __init__(self,game,x,y):
           
        self.game=game
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites
        p.sprite.Sprite.__init__(self,self.groups)
        
        self.width = TILESIZE
        self.height = TILESIZE
        
        self.img_spritesheet = spritesheet("images/explosion.png")
        self.image = self.img_spritesheet.get_sprite(0,0,self.width,self.height)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.animation_loop=0
        
    def update(self):
        self.animation_loop +=0.4
        if self.animation_loop >3:
            self.game.all_sprites.remove(self)
            return
            
        animations = [self.img_spritesheet.get_sprite(0,0,self.width,self.height),
                      self.img_spritesheet.get_sprite(33,0,self.width,self.height),
                      self.img_spritesheet.get_sprite(67,0,self.width,self.height)]
        self.image = animations[math.floor(self.animation_loop)]
            
    
    
###########################################################################################     ############################################################################################################# 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        