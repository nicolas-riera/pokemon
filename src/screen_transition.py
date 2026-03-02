from pygame import display
from time import sleep
from game.CombatIntro import CombatIntro

import pygame

def screen_transition(screen, clock, state):

    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_WAIT)

    pygame.mixer.music.pause()
    pygame.mixer.music.unload()

    screen.fill("white")
    display.flip()
    sleep(0.5)

    if state == "game":
        CombatIntro.combat_intro(screen, clock)

    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

