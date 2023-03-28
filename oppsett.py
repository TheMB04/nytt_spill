# Example file showing a basic pygame "game loop"
import pygame
from figur import Figur
from hinder import Hinder

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

fart = 13

figur = Figur(300, 670, fart)
hindre = []


space = False
oppover = True

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

    if len(hindre) == 0:
        hinder = Hinder(1280, 620, 5)
        hindre.append(hinder)
    elif len(hindre) <= 2 and (hindre[0]).hent_x() < 590:
        hinder = Hinder(1280, 620, 5)
        hindre.append(hinder)

    for hinder in hindre:
        hinder.tegn_hinder(screen)
        hinder.flytt_hinder()
        if hinder.hent_x() <= -100:
            hindre.remove(hinder)
            del hinder
    
    

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()