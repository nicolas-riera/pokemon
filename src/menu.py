import pygame

from src.assets_loading import LOGO_TITLE_SCALED, LOGO_TITLE_RECT

class Menu:
    def __init__(self):
        pass

    def menu_rendering(self, screen, font):

        screen.blit(LOGO_TITLE_SCALED, LOGO_TITLE_RECT)

        play_button_text = font.render("Play", True, (0, 0, 0))
        screen.blit(play_button_text, (355, 430))
        add_pokemon_text = font.render("Add Pokemon", True, (0, 0, 0))
        screen.blit (add_pokemon_text, (260, 500))
        pokedex_text = font.render("Pokedex", True, (0, 0, 0))
        screen.blit (pokedex_text, (307, 570))

        pygame.draw.line(screen, (0, 0, 0), (200, 400), (600, 400), width=5)
        pygame.draw.line(screen, (0, 0, 0), (200, 640), (600, 640), width=5)

        pygame.draw.line(screen, (0, 0, 0), (200, 400), (200, 640), width=5)
        pygame.draw.line(screen, (0, 0, 0), (600, 400), (600, 640), width=5)
        