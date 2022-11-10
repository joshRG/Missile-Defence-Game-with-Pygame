import pygame
from config import *

class Explosion(object):
    def __init__(self, pos, points_multiplier = 0, blast_radius = 50, 
        blast_color = NUKE_EXPLOSION, expand_rate = 30, dwell_time = 0):
        self.pos = pos
        self.points_multiplier = points_multiplier
        self.blast_radius = blast_radius
        self.blast_color = blast_color
        self.expand_rate = expand_rate
        self.radius = 0
        self.complete = False

    def draw(self, screen):
        return pygame.draw.circle(screen, self.blast_color,
                                self.pos, self.radius)

    #The explosion logic here
    def update(self):
        if not self.complete:
            self.radius += self.expand_rate
        if self.radius > self.blast_radius:
            self.complete = True

    def get_center(self):
        return self.pos

    def get_radius(self):
        return self.radius

    def get_points_multiplier(self):
        return self.points_multiplier