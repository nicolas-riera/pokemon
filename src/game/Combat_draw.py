import pygame
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class Combat_draw:
    def __init__(self):
        pass

    @staticmethod
    def display_pokemon(ally, enemy, screen):

        ally_sprite = pygame.image.load(os.path.join(BASE_DIR, "..", "..", "assets", "img", "pokemon_sprites", "back", f"{ally.get_id()}.png"))
        ally_sprite_scaled = pygame.transform.scale(ally_sprite, (200, 200))
        ally_sprite_rect = ally_sprite.get_rect(center=(110, 400))
        screen.blit(ally_sprite_scaled, ally_sprite_rect)

        enemy_sprite = pygame.image.load(os.path.join(BASE_DIR, "..", "..", "assets", "img", "pokemon_sprites", "front", f"{enemy.get_id()}.png"))
        enemy_sprite_scaled = pygame.transform.scale(enemy_sprite, (200, 200))
        enemy_sprite_rect = enemy_sprite.get_rect(center=(500, 150))
        screen.blit(enemy_sprite_scaled, enemy_sprite_rect)
