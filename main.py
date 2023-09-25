import pygame as p
import sys
from sprites import *
from config import *



class game:
    
    def __init__(self):
        self.screen = p.display.set_mode((WIDTH,HEIGHT))
        self.clock = p.time.Clock()
        self.running = True
        self.playing = False
        
        self.all_sprites = p.sprite.LayeredUpdates()
        self.enemies = p.sprite.LayeredUpdates()
        self.players = p.sprite.LayeredUpdates()
        self.projectiles = p.sprite.LayeredUpdates()
        self.walls = p.sprite.LayeredUpdates()
        self.interactables = p.sprite.LayeredUpdates()
        self.ui = p.sprite.LayeredUpdates()
    
    def create_map(self):
        for j in range(len(LVL1)):
            for i in range(len(LVL1[j])):
                if LVL1[j][i] == '.':
                    floor(self,i,j)
                if LVL1[j][i] == "R":
                    road(self,i,j)
                if LVL1[j][i] == "W":
                    img_x = random.randint(1,5)*TILESIZE
                    front_wall(self,i,j,LVL1[j][i],img_x)
                    front_wall(self,i,j+1,LVL1[j+1][i],img_x)
                if LVL1[j][i] == "B":
                    back_wall(self,i,j,LVL1[j][i])
                    back_wall(self,i,j+1,LVL1[j+1][i])
                if LVL1[j][i] == "e":
                    enemy(self,i,j)
                if LVL1[j][i] == "c":
                    chest(self,i,j)
                if LVL1[j][i] == "t":
                    side_wall(self,i,j,LVL1[j][i])
                if LVL1[j][i] == "T":
                    side_wall(self, i, j, LVL1[j][i])
                if LVL1[j][i] == "r":
                    rock(self,i,j)
                    
    def new(self):
        self.playing = True
        self.create_map()
        
        self.player = player(self,200,200)
        
        
    
    def events(self):
        for event in p.event.get():
            if event.type == p.QUIT:
                p.quit()
                sys.exit()
        
    def update(self):
        self.all_sprites.update()
          
    def draw(self):
        self.screen.fill(GREEN)
        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS) 
        p.display.update()
        
    def main(self):
        while self.playing:
            self.events()
            self.update()
            self.draw()
        self.running = False
    

g = game()
g.new()

while g.running:
    g.main()

p.quit()
sys.exit()
