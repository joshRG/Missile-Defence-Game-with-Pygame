import pygame
from config import *
from functions import *

class InputBox(object):
    def __init__(self, x, y, w, h, text=""):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = (255, 255, 255)
        self.text = text
        self.txt_surface = game_font.render(text, True, self.color)
        self.active = False
        self.finished = False
    
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = (255, 255, 255) if self.active else(255, 0, 255)
        
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)
                    self.text = ""
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    if len(self.text) < 3:
                        self.text += event. unicode
                
                self.txt_surface = game_font.render(self.text, True, self.color) 
    
    def update(self):
        width = max(200, self.txt_surface.get_width() + 10)

    def draw(self, screen):
        screen.fill(BACKGROUND)
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        #blit the rect
        pygame.draw.rect(screen, self.color, self.rect, 2)
        pygame.display.update()
    
    def check_finished(self):
        return self.finished
