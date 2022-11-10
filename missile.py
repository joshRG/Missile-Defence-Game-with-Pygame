import pygame
import math
from config import *
from functions import *
from explosion import Explosion

class Missile():
    def __init__(self, origin_pos, target_pos, incoming = True, speed = 1,
                points = 10, trail_color = WARHEAD_TRAIL, warhead_color = WARHEAD):
        self.origin_pos = origin_pos
        self.target_pos = target_pos
        if incoming == True:
            self.incoming = 1
        else:
            self.incoming  = -1
        self.speed = speed
        self.points = points
        self.travel_dist = 1
        self.warhead_color = warhead_color
        self.trail_color = trail_color
        self.pos = origin_pos
        self.warhead_size = 2
        self.trail_width = 1
        self.x = target_pos[0] - origin_pos[0]
        self.y = target_pos[1] - origin_pos[1]
        if self.y != 0:
            self.m = self.x / self.y
        else:
            self.m = 1
        self.angle = math.atan(self.m)
        self.dist_to_target = distance(origin_pos, target_pos)
        self.detonated = False
        #Function to draw the missile and the trail
    def draw(self, screen):
        #missile trail
        pygame.draw.line(screen, self.trail_color, self.pos, self.origin_pos, self.trail_width)
        #warhead
        pygame.draw.circle(screen, self.warhead_color, self.pos, self.warhead_size)
    def update(self, explosion_list):
        if not self.detonated:
            self.pos = (self.origin_pos[0] + int(self.travel_dist * math.sin(self.angle) * self.incoming), 
                        self.origin_pos[1] + int(self.travel_dist * math.cos(self.angle) * self.incoming))
            self.travel_dist += self.speed
            #when reaching the target point : detonate!
            if self.travel_dist > self.dist_to_target and not self.detonated:
                self.explode(explosion_list)
                #function to explosion itself
    def explode(self, explosion_list):
        self.detonated = True
        if self.incoming !=1:
            points_multiplier = 1
            explosion_radius = INTERCEPT_RADIUS
            explosion_color = INTERCEPTER_EXPLOSION
        else:
            points_multiplier = 0
            explosion_radius = NUKE_RADIUS
            explosion_color = NUKE_EXPLOSION
        explosion_list.append(Explosion(self.pos, points_multiplier, explosion_radius, explosion_color))
                
                #function to return the current position
    def get_pos(self):
        return self.pos
                
    def get_points(self):
        return self.points

                
