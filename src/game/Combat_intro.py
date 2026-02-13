import pygame
import time
import math

from src.assets_loading import INTRO_BATTLE_MUSIC

class Combat_intro:
    def __init__(self):
        pass

    @staticmethod
    def battle_intro_music():
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.load(INTRO_BATTLE_MUSIC)
            pygame.mixer.music.play()

    @staticmethod
    def combat_intro(screen, clock):

        time_start = time.monotonic()

        Combat_intro.battle_intro_music()
        while time.monotonic() - time_start < 2.8:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    exit()
                    
            screen.fill("white")

            alpha = ((math.sin(time.monotonic() * 10) + 1) / 2) * 255
            
            screen_fade = pygame.Surface((screen.get_width(), screen.get_height()))
            screen_fade.fill((0, 0, 0))
            screen_fade.set_alpha(alpha)
            screen.blit(screen_fade, (0, 0))

            pygame.display.flip()
            clock.tick(60)