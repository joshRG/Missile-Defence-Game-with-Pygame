import pygame
import math
from config import *
from missile import Missile

class Defence():
    def __init__(self):
        self.pos = (SCREENSIZE[0] // 2, SCREENSIZE[1] - GROUND_LEVEL)
        self.target_pos = pygame.mouse.get_pos()
        self.gun_end = self.pos
        self.gun_size = 18
        self.color = DEFENCE
        self.x = self.target_pos[0] - self.pos[0]
        self.y = self.target_pos[1] - self.pos[1]
        self.m = 0
        self.angle = math.atan(self.m)
        self.destroyed = False
        self.ammo = 30
        #you can determine the number of ammo you want here

    def draw(self, screen):
        #Drawing the base
        pygame.draw.circle(screen, self.color, self.pos, 8)
        #Drawing the launcher
        pygame.draw.line(screen, self.color, self.pos, self.gun_end, 3)
    def update(self):
        self.target_pos = pygame.mouse.get_pos()
        #Calculate the line to target point
        self.x = self.target_pos[0] - self.pos[0]
        self.y = self.target_pos[1] - self.pos[1]
        if self.y != 0:
            self.m = self.x / self.y
            self.angle = math.atan(self.m) + math.pi
            self.gun_end = (self.pos[0] + int(self.gun_size * math.sin(self.angle)), self.pos[1] + int(self.gun_size * math.cos(self.angle)))
    
    def shoot(self, missile_list):
        if self.ammo > 0:
            missile_list.append(Missile(self.pos, self.target_pos, False, 8, 0, INTERCEPTER_TRAIL, INTERCEPTER))
            self.ammo -=1
    
    def get_ammo(self):
        return self.get_ammo
    
    def set_ammo(self, ammo):
        self.ammo = ammo