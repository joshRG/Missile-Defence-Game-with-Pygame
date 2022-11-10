import pygame
from pygame.locals import *
import os
import math
from config import *
import json

#Exit Game function
def exit_game(screen):
    pause = 0
    screen.fill(BACKGROUND)
    pygame.display.update()


    #Display of a message to confirm exit and game`s status
    exit_msg = game_font.render('Quitting...uh, weak', False, INTERFACE_SEC)
    question_msg = game_font.render("Are you sure you wanna take the way of the weak?", False, INTERFACE_SEC)
    confirm_msg = game_font.render("(Y/N)", False, INTERFACE_SEC)

    #Position the messages on the grid
    exit_msg_pos = (SCREENSIZE[0]//2 - (exit_msg.get_width()//2), SCREENSIZE[1]//2 - (exit_msg.get_height()//2))
    
    question_msg_pos = (SCREENSIZE[0]//2 - (question_msg.get_width()//2), SCREENSIZE[1]//2 - (question_msg.get_height()//2) + exit_msg.get_height())
    
    confirm_msg_pos = (SCREENSIZE[0]//2 - (confirm_msg.get_width()//2), SCREENSIZE[1]//2 - (confirm_msg.get_height()//2) + exit_msg.get_height() + question_msg.get_height())

    screen.blit(exit_msg, exit_msg_pos)
    screen.blit(question_msg, question_msg_pos)
    screen.blit(confirm_msg, confirm_msg_pos)
    pygame.display.update()

    #Wait for player to confirm exit or not
    while pause == 0:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_y:
                    exit()
                elif event.key == K_n:
                    pause = -1

def pause_game(screen):
    pause = 0

    #Displaying a Message if game is paused
    pause_msg = game_font.render("GAME PAUSED!", False, INTERFACE_SEC)
    confirm_msg = game_font.render("PRESS 'P' TO RESUME", False, INTERFACE_SEC)
    
    #Positions
    pause_msg_pos = (SCREENSIZE[0]//2 - (pause_msg.get_width()//2), SCREENSIZE[1]//2 - (pause_msg.get_height()//2))

    confirm_msg_pos = (SCREENSIZE[0]//2 - (confirm_msg.get_width()//2), SCREENSIZE[1]//2 - (confirm_msg.get_height()//2) + pause_msg.get_height())

    screen.blit(pause_msg, pause_msg_pos)
    screen.blit(confirm_msg, confirm_msg_pos)
    pygame.display.update()

    #Wait for player to unpause
    while pause == 0:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_p:
                    pause = -1
    
def distance(p,q):
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2 )

def check_collision(missile_list, explosion_list, city_list):
    score = 0
    for explosion in explosion_list:
        for missile in missile_list[:]:
            if explosion.get_radius() > distance(explosion.get_center(), missile.get_pos()):
                score += missile.get_points() * explosion.get_points_multiplier()
                missile_list.remove(missile)
        for city in city_list:
            if explosion.get_radius() > distance(explosion.get_center(), city.get_pos()):
                city.set_destroyed(True)
                city_list.remove(city)
    return score

# You'll need to create a Json file for dummy data
def load_score(file):
    #Open json data file and return  dict
    with open(file) as f:
        return json.load(f)
    
def update_high_scores(score, name, high_score):
    #check the higher score and make a top 10
    score_pos = check_high_score(score, high_score)
    if score_pos > 0:
        max_pos = 10

        for pos in range(max_pos, score_pos, -1):
            #move the score down a position
            if pos <= max_pos and pos > 1:
                high_score[str(pos)]["name"] = high_score[str(pos-1)]["name"]
                high_score[str(pos)]["score"] = high_score[str(pos-1)]["score"]
        #Here we're inserting the new score
        high_score[str(score_pos)]["name"] = name
        high_score[str(score_pos)]["score"] = int(score)
    
    return high_score

def check_high_score(score, high_scores):
    score_pos = 0
    for pos, record in high_scores.items():
        if score > int(record["score"]) and score_pos == 0:
            score_pos = int(pos)
    return score_pos

def save_high_scores(file, high_scores):
    #Saving high scores to a file
    j = json.dumps(high_scores)
    f = open(file, "w")
    f.write(j)
    f.close()

def show_high_scores(screen, high_scores):
    screen.fill(BACKGROUND)
    pygame.display.update()
    pause = 0

    #Heading message, position and blit
    high_score_heading = game_font.render("HIGH SCORES", False, INTERFACE_SEC)
    text_height = high_score_heading.get_height()
    text_y_pos_multiplier = 7
    wide_score = 0 
    high_score_heading_pos = (SCREENSIZE[0] // 2 - (high_score_heading.get_width() // 2),
                            SCREENSIZE[1] // 2 - (text_height * text_y_pos_multiplier))
    
    screen.blit(high_score_heading, high_score_heading_pos)
    text_y_pos_multiplier -= 2

    #Iterating over high_scores dictionary
    for pos, record in high_scores.items():
        if len(pos) == 1:
            pos = " " + pos
        record["score"] = str(record["score"])
        if wide_score <= len(record["score"]):
            wide_score = len(record["score"])
        else:
            record["score"] = (" " * (wide_score - len(record["score"]))) + record["score"]
        score_text = game_font.render(pos + " " + record["name"] + " " + record["score"],
                                    False, INTERFACE_SEC)
        score_text_pos = (SCREENSIZE[0] // 2 - (high_score_heading.get_width() // 2),
                            SCREENSIZE[1] // 2 - (text_height * text_y_pos_multiplier))
        screen.blit(score_text, score_text_pos)
        text_y_pos_multiplier -= 1

        #Generating instruction msg, position and blit
        text_y_pos_multiplier -= 1 
        high_score_msg = game_font.render("PRESS 'SPACE' TO CONTINUE", False, INTERFACE_SEC)
        high_score_msg_pos = (SCREENSIZE[0] // 2 - (high_score_msg.get_width() // 2),
                            SCREENSIZE[1] // 2 - (text_height * text_y_pos_multiplier))
        
        screen.blit(high_score_msg, high_score_msg_pos)

        #Update the display
        pygame.display.update()
        #Infinite loop to liste for continue
        while pause == 0:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        pause -= 1