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

    @staticmethod
    def display_ally_block(ally, screen, font):
        
        pygame.draw.line(screen, (0, 0, 0), (350, 417), (695, 417), width=5)
        pygame.draw.line(screen, (0, 0, 0), (350, 557), (695, 557), width=5)

        pygame.draw.line(screen, (0, 0, 0), (350, 417), (350, 557), width=5)
        pygame.draw.line(screen, (0, 0, 0), (695, 417), (695, 557), width=5)

        ally_name_text = font[1].render(ally.get_name(), True, (0, 0, 0))
        screen.blit(ally_name_text, (360, 429))
        ally_level_text = font[1].render(f"LVL : {ally.get_level()}", True, (0, 0, 0))
        screen.blit(ally_level_text, (360, 460))
        ally_hp_text = font[1].render(f"HP : {ally.get_hp()}", True, (0, 0, 0))
        screen.blit(ally_hp_text, (360, 490))




