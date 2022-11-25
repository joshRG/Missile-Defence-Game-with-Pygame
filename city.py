import pygame
from config import *

class City(object):
    def __init__(self, number, max_cities):
        self.pos = (number * SCREENSIZE[0] // (max_cities + 1), SCREENSIZE[1] - GROUND_LEVEL)
        self.color = CITY
        self.size = 15
        self.destroyed = False

    def draw(self, screen):
        if self.destroyed != True:
            return pygame.draw.circle(screen, self.color, self.pos, self.size)

    def update(self):
        pass

    def set_destroyed(self, status):
        self.destroyed = status

    def get_destroyed(self):
        return self.destroyed

    def get_pos(self):
        return self.pos