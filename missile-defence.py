import pygame
import random
import time
from config import *
from city import City
from missile import Missile
from explosion import Explosion
from defence import Defence
from mcgame import McGame
from text import InputBox
from functions import *

#Initializing the main game engine, screen and clock
pygame.init()
screen = pygame.display.set_mode(SCREENSIZE)
pygame.mouse.set_visible(SHOW_MOUSE)
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()

#Main function
def main():
    global current_game_state

    #Load high scores
    high_scores = load_score("scores.json")

    #producing random trajectories
    random.seed()

    #active explosions
    explosion_list = []

    #Active missiles
    missile_list = []

    #Active cities
    city_list = []

    for counter in range(1, NUM_CITIES):
        """This Loop is in charge of set the cities ammounts drawed in the game, always 2 less than setted in the config.py file"""
        if counter == NUM_CITIES // 2:
            pass
        else: 
            city_list.append(City(counter, (NUM_CITIES - 1)))
        
    #Instantiate a Defence class
    defence = Defence()

    #Set the game running
    current_game_state = GAME_STATE_RUNNING
    show_high_scores(screen, high_scores)

    #Setting upt the AI MC Game
    mcgame = McGame(1, high_scores["1"]["score"])
    validate = True
    while validate:
        #All event handlers
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    defence.shoot(missile_list)
                if event.button == 2:
                    pass
                if event.button == 3:
                    pass
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    exit_game(screen)
                if event.key == K_SPACE:
                    defence.shoot(missile_list)
                if event.key == K_p:
                    pause_game(screen)
            
            if event.type == KEYUP:
                pass
        
        #Clear the screen before drawing
        screen.fill(BACKGROUND)

        #///////// GAME LOGIC ///////////

        # 1 cities
        for cities in city_list:
            cities.draw(screen)
        
        #Intercepter turret
        defence.update()
        defence.draw(screen)

        #Missiles
        for missiles in missile_list[:]:
            missiles.update(explosion_list)
            missiles.draw(screen)
            if missiles.detonated:
                missile_list.remove(missiles)
        
        for explosion in explosion_list[:]:
            explosion.update()
            explosion.draw(screen)
            if explosion.complete:
                explosion_list.remove(explosion)
        
        #Drawing the interface
        mcgame.draw(screen, defence)
        
        #Update the MCGAME
        if current_game_state == GAME_STATE_RUNNING:
            current_game_state = mcgame.update(missile_list, explosion_list, city_list)

        #Load game over message and continue to high-score / menu
        if current_game_state == GAME_STATE_OVER:
            mcgame.game_over(screen)

        #Load a message and set new game values for start new level
        if current_game_state == GAME_STATE_NEW_LEVEL:
            mcgame.new_level(screen, defence)
        
        #Update the display
        pygame.display.update()

        #Hold for seconds before starting new level
        if current_game_state == GAME_STATE_NEW_LEVEL:
            time.sleep(5)
            current_game_state = GAME_STATE_RUNNING
        
        #Hold for few seconds before proceeding to high score
        if current_game_state == GAME_STATE_OVER:
            input_box = InputBox(100, 100, 140, 32)
            while input_box.check_finished() == False:
                for event in pygame.event.get():
                    input_box.handle_event(event)
                input_box.update()
                input_box.draw(screen)
            
            current_game_state = GAME_STATE_MENU
        
        #DISPLAYING HIGH SCORES
        if current_game_state == GAME_STATE_MENU:
            show_high_scores(screen, high_scores)
            current_game_state = 0

        #run at pre-set frame-persecond
        clock.tick(FPS)

if __name__=="__main__":
    main()