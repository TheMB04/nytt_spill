# Example file showing a basic pygame "game loop"
import pygame
from figur import Figur
from hinder import Hinder
from random import randint
import math as m


# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

fart = 13

figur = Figur(300, 670, fart)
hindre = []
points = 0


space = False
oppover = True
alive = True
font = pygame.font.SysFont("Impact", 104)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                space = True

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("skyblue")

    # LAG SPILLET DIT HER:
    if alive:
        figur.tegn_figur(screen)
        if space and oppover:
            if figur.get_y() <= 300:
                oppover = False
            else:
                figur.hopp_opp()
        elif oppover == False and figur.get_y() <= 669:
            figur.hopp_ned()
        else:
            space = False
            oppover = True
            figur.tilbakestill_fart(fart)

        bredde = randint(100, 220)
        hoyde = 320 - bredde
        
        if len(hindre) == 0:
            hinder = Hinder(1280, (720-hoyde), 5, bredde, hoyde)
            hindre.append(hinder)
        elif len(hindre) < 2 and (hindre[0]).hent_x() < 590:
            hinder = Hinder(1280, (720-hoyde), 5, bredde, hoyde)
            hindre.append(hinder)

        for hinder in hindre:
            hinder.tegn_hinder(screen)
            hinder.flytt_hinder()
            if hinder.hent_x() <= -100:
                hindre.remove(hinder)
                del hinder
                points += 1
                    

                


        if points >= 10:
            score = font.render(f"{points}", True, (255, 255, 255))
            screen.blit(score, (588, 20))
        elif points >= 100:
            score = font.render(f"{points}", True, (255, 255, 255))
            screen.blit(score, (562, 20))
        else:
            score = font.render(f"{points}", True, (255, 255, 255))
            screen.blit(score, (614, 20))
        
    

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()