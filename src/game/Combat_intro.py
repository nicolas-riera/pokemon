import pygame

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
    def combat_intro():

        Combat_intro.battle_intro_music()