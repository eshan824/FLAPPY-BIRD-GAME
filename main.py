# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 22:04:39 2021

@author: DELL
"""

import pygame
import random

pygame.font.init()
START_FONT = pygame.font.SysFont("comicsans", 70)
END_FONT = pygame.font.SysFont("comicsans", 90)
RESTART_FONT = pygame.font.SysFont("comicsans", 60)
SCORE_FONT = pygame.font.SysFont("comicsans", 65)

FPS = 120 

BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (150,255,0)
RED = (255,0,50)

HIT = pygame.USEREVENT

WIDTH , HEIGHT = 1000,700
WINDOW = pygame.display.set_mode((WIDTH , HEIGHT))
pygame.display.set_caption("FLAPPY BIRD GAME")

BIRD_IMAGE = pygame.transform.scale(
    pygame.image.load("E:/PROJECTS/PYTHON PROJECTS/GAMES/FLAPPY BIRD GAME/bird.png") , (40,30))



BACKGROUND = pygame.image.load("E:/PROJECTS/PYTHON PROJECTS/GAMES/FLAPPY BIRD GAME/background.jpg")


def waiting_board():
    #WINDOW.fill(WHITE)
    WINDOW.blit(BACKGROUND, (0,0))
    WINDOW.blit(BACKGROUND, (500,0))
    START_TEXT = START_FONT.render("PRESS SPACEBAR", 1, BLACK)
    WINDOW.blit(START_TEXT, (WIDTH/2 - START_TEXT.get_width()/2 , 180))
    
    START_TEXT = START_FONT.render("TO START GAME", 1, BLACK)
    WINDOW.blit(START_TEXT, (WIDTH/2 - START_TEXT.get_width()/2 , 250))
    pygame.display.update()


def draw(UPPER_PIPE, LOWER_PIPE, SCORE, BIRD):
    WINDOW.blit(BACKGROUND, (0,0))
    WINDOW.blit(BACKGROUND, (500,0))
    
    pygame.draw.rect(WINDOW, GREEN, UPPER_PIPE)
    UPPER_PIPE.x -= 1
    
    pygame.draw.rect(WINDOW, GREEN, LOWER_PIPE)
    LOWER_PIPE.x -= 1
    
    SCORE_TEXT = SCORE_FONT.render("SCORE: " + str(SCORE), 1, BLACK)
    WINDOW.blit(SCORE_TEXT, (20 , 20))

    WINDOW.blit(BIRD_IMAGE, BIRD)
    
    pygame.display.update()

    
    
def collision(UPPER_PIPE, LOWER_PIPE, BIRD):
    if BIRD.colliderect(UPPER_PIPE):
        pygame.event.post(pygame.event.Event(HIT))
    if BIRD.colliderect(LOWER_PIPE):
        pygame.event.post(pygame.event.Event(HIT))
    
def game_end(SCORE):
    END_TEXT = END_FONT.render("GAME OVER!", 1, RED)
    WINDOW.blit(END_TEXT, (WIDTH/2 - END_TEXT.get_width()/2 , HEIGHT/2 - END_TEXT.get_height()/2 - 30))
    
    RESTART_TEXT = RESTART_FONT.render("PRESS SPACEBAR", 1, BLACK)
    WINDOW.blit(RESTART_TEXT, (WIDTH/2 - RESTART_TEXT.get_width()/2 , 420))
    
    RESTART_TEXT_1 = RESTART_FONT.render("TO RESTART GAME", 1, BLACK)
    WINDOW.blit(RESTART_TEXT_1, (WIDTH/2 - RESTART_TEXT_1.get_width()/2 , 460))
    
    SCORE_TEXT = SCORE_FONT.render("SCORE : " + str(SCORE), 1, BLACK)
    WINDOW.blit(SCORE_TEXT, (WIDTH/2 - END_TEXT.get_width()/4 , HEIGHT/2 - END_TEXT.get_height()/2 - 100))
    
    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                main()
            if event.type == pygame.QUIT:
                pygame.quit()
    
    pygame.display.update()

waiting = True
while waiting:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                waiting = False
    waiting_board()


def main():    
    clock = pygame.time.Clock()
    
    BIRD = BIRD_IMAGE.get_rect()
    BIRD.topleft = (150, 250)
    
    UPPER_PIPE_HEIGHT = random.randrange(150, 450)
    UPPER_PIPE = pygame.Rect(WIDTH + WIDTH/2, 0, 40, UPPER_PIPE_HEIGHT)

    GAP = 150
    GAP_HEIGHT = UPPER_PIPE_HEIGHT
    GAP_END = GAP_HEIGHT + GAP

    LOWER_PIPE_HEIGHT = 636 - GAP_END
    LOWER_PIPE = pygame.Rect(WIDTH + WIDTH/2, GAP_END, 40, LOWER_PIPE_HEIGHT)    
    
    BIRD_y_CHANGE = 2
    
    SCORE = 0
    draw(UPPER_PIPE, LOWER_PIPE, SCORE, BIRD)
    collision(UPPER_PIPE, LOWER_PIPE, BIRD)
    
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                #  if you press spacebar you will move up
                    BIRD_y_CHANGE = -4

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                # when u release space bar you will move down automatically
                    BIRD_y_CHANGE = 2
                  
                    
            if event.type == HIT:
                wait = True
                while wait:
                    game_end(SCORE)
                    for event in pygame.event.get():
                        if event.type == pygame.KEYUP:
                            if event.key == pygame.K_SPACE:
                                pygame.time.delay(3000)
                                wait = False
                        if event.type == pygame.QUIT:
                            pygame.quit()
                             #wait = False
                main()
                
                
            
        BIRD.y += BIRD_y_CHANGE
        if BIRD.y <= 0:
            BIRD.y = 0
        if BIRD.y >= 607:
            pygame.event.post(pygame.event.Event(HIT))
            
            
        if UPPER_PIPE.x + 40 == 151 and LOWER_PIPE.x +40 == 151:
            SCORE += 1
            
        if UPPER_PIPE.x < 5 and LOWER_PIPE.x < 5:
            UPPER_PIPE.x = WIDTH
            LOWER_PIPE.x = WIDTH
            UPPER_PIPE_HEIGHT = random.randrange(150, 450)
            UPPER_PIPE = pygame.Rect(WIDTH , 0, 40, UPPER_PIPE_HEIGHT)

            GAP = 150
            GAP_HEIGHT = UPPER_PIPE_HEIGHT
            GAP_END = GAP_HEIGHT + GAP

            LOWER_PIPE_HEIGHT = 636 - GAP_END
            LOWER_PIPE = pygame.Rect(WIDTH , GAP_END, 40, LOWER_PIPE_HEIGHT)
        
        
        draw(UPPER_PIPE, LOWER_PIPE, SCORE, BIRD)
        collision(UPPER_PIPE, LOWER_PIPE, BIRD)
        
    pygame.quit()
    
    
if __name__ == "__main__":
    main()