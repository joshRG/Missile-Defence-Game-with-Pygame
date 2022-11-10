import pygame
import random
from config import *
from functions import *
from missile import *

class McGame():
    def __init__(self, difficulty = 1, high_score = 0):
        self.player_score = 0
        self.high_score = high_score
        self.high_score_text = game_font.render("HIGH: {}".format(self.high_score), False, INTERFACE_SEC)
        self.high_score_text_pos = SCREENSIZE[0] - self.high_score_text.get_width() - 5
        self.max_missile_count = 8
        self.missile_count = 0
        self.difficulty = difficulty
        self.difficulty_increment = 3
        self.missile_loop = 7
        self.missile_frequency = self.missile_loop - self.difficulty
        self.missile_interval = 1
        self.ground_level = SCREENSIZE[1] - GROUND_LEVEL
    
    def draw(self, screen, defence):
        pygame.draw.line(screen, INTERCEFACE_PRI, [0, SKY_LEVEL], [SCREENSIZE[0], SKY_LEVEL], 2)
        pygame.draw.rect(screen, INTERCEFACE_PRI, (0, SCREENSIZE[1] - GROUND_LEVEL, SCREENSIZE[0], SCREENSIZE[1]))
        score_text = game_font.render("SCORE: {}".format(self.player_score), False, INTERFACE_SEC)
        screen.blit(score_text, (5, 10))
        screen.blit(self.high_score_text, (self.high_score_text_pos, 10))
        ammo_text = game_font.render("AMMO: {}".format(defence.get_ammo()), False, INTERFACE_SEC)
    
    def update(self, missile_list, explosion_list, city_list):
        if self.missile_frequency % self.missile_interval == 0 and self.missile_count < self.max_missile_count:
            missile_list.append(Missile(self.get_origin(), self.get_target()))
            self.missile_count += 1
        #Increment for frequency count
        self.missile_interval += 1
        if self.missile_interval > self.missile_loop:
            self.missile_interval = 1
        
        #Check for collision
        self.player_score += check_collision(missile_list, explosion_list, city_list)

        #Check if all cities have been destroyed
        if city_list == []:
            return GAME_STATE_OVER

        #Starting a new level
        if missile_list == [] and explosion_list == []:
            return GAME_STATE_NEW_LEVEL

        return GAME_STATE_RUNNING

    #Start a new level
    def new_level(self, screen, defence):
        #Setting new level difficulty parameters
        self.max_missile_count += self.difficulty_increment
        self.missile_count = 0
        self.difficulty += 1
        self.difficulty_increment += self.difficulty
        self.missile_frequency = self.missile_loop - self.difficulty
        self.missile_interval = 1
        defence.set_ammo(30)

        new_level = game_font.render("NEW INVOUND MISSILES DETECTED", False, INTERFACE_SEC)
        get_ready = game_font.render("GET READY", False, INTERFACE_SEC)
        new_level_pos = (SCREENSIZE[0] // 2 - (new_level.get_width() // 2), SCREENSIZE[1] // 2 - (new_level.get_height() // 2))
        get_ready_pos = (SCREENSIZE[0] // 2 - (get_ready.get_width() // 2), SCREENSIZE[1] // 2 - (get_ready.get_height() // 2) + new_level.get_height())
        screen.blit(new_level, new_level_pos)
        screen.blit(get_ready, get_ready_pos)

        #Game Over - All cities destroyed
    def game_over(self, screen):
            game_over_msg = game_font.render("YOUR CITIES ARE DESTROYED!", False, INTERFACE_SEC)
            score_msg = game_font.render("SCORED: {}".format(self.player_score), False, INTERFACE_SEC)
            game_over_msg_pos = (SCREENSIZE[0] // 2 - (game_over_msg.get_width() // 2), SCREENSIZE[1] // 2 - (game_over_msg.get_height() // 2))
            score_msg_pos = (SCREENSIZE[0] // 2 - (score_msg.get_width() // 2), SCREENSIZE[1] // 2 - (score_msg.get_height() // 2) + game_over_msg.get_height())

    def get_target(self):
            return(random.randint(0, SCREENSIZE[0]), self.ground_level)
        
    def get_origin(self):
            return(random.randint(0, SCREENSIZE[0]), self.ground_level)

    def set_difficulty(self, new_difficulty):
            self.difficulty = new_difficulty
        
    def get_player_score(self):
            return self.player_score



