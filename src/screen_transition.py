from pygame import display
from time import sleep

import pygame

def screen_transition(screen):

    pygame.mixer.music.pause()
    pygame.mixer.music.unload()

    screen.fill("white")
    display.flip()
    sleep(0.5)

    