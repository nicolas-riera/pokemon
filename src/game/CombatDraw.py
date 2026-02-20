import pygame
import os
import time

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class CombatDraw:
    def __init__(self):
        pass

    @staticmethod
    def display_pokemon(ally, enemy, screen, start_timer):

        ally_sprite = pygame.image.load(os.path.join(BASE_DIR, "..", "..", "assets", "img", "pokemon_sprites", "back", f"{ally.get_id()}.png"))
        ally_sprite_scaled = pygame.transform.scale(ally_sprite, (200, 200))
        ally_sprite_rect = ally_sprite.get_rect(center=(max(120, (500-((time.monotonic() - start_timer)*550))), 400))
        screen.blit(ally_sprite_scaled, ally_sprite_rect)

        enemy_sprite = pygame.image.load(os.path.join(BASE_DIR, "..", "..", "assets", "img", "pokemon_sprites", "front", f"{enemy.get_id()}.png"))
        enemy_sprite_scaled = pygame.transform.scale(enemy_sprite, (200, 200))
        enemy_sprite_rect = enemy_sprite.get_rect(center=(min(500, (120+((time.monotonic() - start_timer)*550))), 150))
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
        ally_type_text = font[1].render(" / ".join(ally.get_types()), True, (0, 0, 0))
        screen.blit(ally_type_text, (360, 520))

    @staticmethod
    def display_enemy_block(enemy, screen, font):
        
        pygame.draw.line(screen, (0, 0, 0), (72, 160), (417, 160), width=5)
        pygame.draw.line(screen, (0, 0, 0), (72, 300), (417, 300), width=5)

        pygame.draw.line(screen, (0, 0, 0), (72, 160), (72, 300), width=5)
        pygame.draw.line(screen, (0, 0, 0), (417, 160), (417, 300), width=5)

        enemy_name_text = font[1].render(enemy.get_name(), True, (0, 0, 0))
        screen.blit(enemy_name_text, (81, 170))
        enemy_level_text = font[1].render(f"LVL : {enemy.get_level()}", True, (0, 0, 0))
        screen.blit(enemy_level_text, (81, 200))
        enemy_hp_text = font[1].render(f"HP : {enemy.get_hp()}", True, (0, 0, 0))
        screen.blit(enemy_hp_text, (81, 230))
        enemy_type_text = font[1].render(" / ".join(enemy.get_types()), True, (0, 0, 0))
        screen.blit(enemy_type_text, (81, 260))

    @staticmethod
    def display_main_text_block(screen):

        pygame.draw.line(screen, (0, 0, 0), (20, 600), (780, 600), width=5)
        pygame.draw.line(screen, (0, 0, 0), (20, 780), (780, 780), width=5)

        pygame.draw.line(screen, (0, 0, 0), (20, 600), (20, 780), width=5)
        pygame.draw.line(screen, (0, 0, 0), (780, 600), (780, 780), width=5)


    @staticmethod
    def display_choose_action_block(screen, font):

        pygame.draw.line(screen, (0, 0, 0), (420, 610), (770, 610), width=5)
        pygame.draw.line(screen, (0, 0, 0), (420, 770), (770, 770), width=5)

        pygame.draw.line(screen, (0, 0, 0), (420, 610), (420, 770), width=5)
        pygame.draw.line(screen, (0, 0, 0), (770, 610), (770, 770), width=5)

        ack_text = font[0].render("Attack", True, (0, 0, 0))
        screen.blit(ack_text, (483, 630))
        run_text = font[0].render("Run", True, (0, 0, 0))
        screen.blit(run_text, (483, 680))

    @staticmethod
    def display_choose_attack_type(screen, font, ally):
        
        pygame.draw.line(screen, (0, 0, 0), (320, 610), (770, 610), width=5)
        pygame.draw.line(screen, (0, 0, 0), (320, 770), (770, 770), width=5)

        pygame.draw.line(screen, (0, 0, 0), (320, 610), (320, 770), width=5)
        pygame.draw.line(screen, (0, 0, 0), (770, 610), (770, 770), width=5)

        type1_text = font[0].render(ally.get_types()[0].capitalize(), True, (0, 0, 0))
        screen.blit(type1_text, (383, 625))
        type2_text = font[0].render(ally.get_types()[1].capitalize(), True, (0, 0, 0))
        screen.blit(type2_text, (383, 675))
        back_text = font[0].render("Back", True, (0, 0, 0))
        screen.blit(back_text, (383, 725))
        
