import pygame
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class Combat_draw:
    def __init__(self):
        pass

    @staticmethod
    def display_pokemon(ally, enemy, screen):
        ally_sprite = pygame.image.load(os.path.join(BASE_DIR, "..", "..", "assets", "img", "pokemon_sprites", "back", f"{ally.get_id()}.png"))
        ally_sprite_rect = ally_sprite.get_rect(center=(200, 600))
        screen.blit(ally_sprite, ally_sprite_rect)
