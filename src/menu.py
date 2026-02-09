import pygame

from src.assets_loading import LOGO_TITLE_SCALED, LOGO_TITLE_RECT

class Menu:
    def __init__(self):
        pass

    def menu_rendering(self, screen):
        screen.blit(LOGO_TITLE_SCALED, LOGO_TITLE_RECT)
        