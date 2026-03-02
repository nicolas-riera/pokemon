import random
import pygame
import time
import os

from src.assets_loading import POKEMONS_TYPE_STATS, POKEMON_DATA, SFX_RUN, SFX_PRESS_AB, CURSOR, POKEMON_SOUND_PATH
from src.pokemon.Pokemon import Pokemon
from src.game.CombatDraw import CombatDraw
from src.game.game_main_text_rendering import draw_text_block

class Combat:
    def __init__(self):
        self.__first_run = True
        self.__ally = None
        self.__enemy = None
        self.__state = "game"
        self.__ally_attack_type = None
        self.__enemy_attack_type = None

        # choose_action
        self.__ack_button = pygame.Rect((473, 624, 187, 38))
        self.__change_pokemon_button = pygame.Rect((473, 674, 220, 38))
        self.__run_button = pygame.Rect((473, 724, 88, 38))

        # choose_attack_type
        self.__type1_button = pygame.Rect((370, 624, 300, 38))
        self.__type2_button = pygame.Rect((370, 674, 300, 38))
        self.__back_button = pygame.Rect((370, 724, 130, 38))

    @staticmethod
    def __calculate_attack_mult(attack_type:str, enemy:object):
        mult = 1.0
        for def_type in enemy.get_types():
            mult *= POKEMONS_TYPE_STATS[attack_type.upper()][def_type.upper()]

        return mult
    
    @staticmethod
    def __select_random_pokemon_from_POKEMON_DATA(ally):
        pokemon = Pokemon()
        random_id, random_pokemon_dict = random.choice(list(POKEMON_DATA.items()))
        
        pokemon.load_from_POKEMON_DATA_dict(random_pokemon_dict)
        pokemon.set_id(random_id)
        pokemon.set_level(max(1, random.choice(
            [ally.get_level() - 1, ally.get_level(), ally.get_level() + 1])
        ))

        return pokemon

    def __check_winner(self):
        if self.__ally and self.__enemy:
            if self.__ally.is_alive() is False:
                self.__state = "enemy_won"
                return self.__enemy.get_name()

            elif self.__enemy.is_alive() is False:
                self.__state = "ally_won"
                return self.__ally.get_name()

        return None

    def __attack(self, src, dest):
        src.attack(dest, self.__calculate_attack_mult(self.__attack_type, dest) * src.get_attack())

    def events(self):
        pass

    def __run(self):
        pygame.mixer.music.pause()
        pygame.mixer.music.unload()
        pygame.mixer.Sound(SFX_RUN).play()
        self.music = None
        self.__state = "menu"

    def draw(self, screen, font):

        CombatDraw.display_pokemon(self.__ally, self.__enemy, screen, self.__start_timer)
        
        if time.monotonic() - self.__start_timer > 1:
            CombatDraw.display_ally_block(self.__ally, screen, font)
            CombatDraw.display_enemy_block(self.__enemy, screen, font)

        CombatDraw.display_main_text_block(screen)

        if self.__state == "game":
            draw_text_block(screen, f"A wild {self.__enemy.get_name()} has appeared!", font)
        elif self.__state == "choose_action":
            CombatDraw.display_choose_action_block(screen, font)   
            if self.__ack_button.collidepoint(pygame.mouse.get_pos()):
                screen.blit(CURSOR, (440, 625)) 
            elif self.__change_pokemon_button.collidepoint(pygame.mouse.get_pos()):
                screen.blit(CURSOR, (440, 675))
            elif self.__run_button.collidepoint(pygame.mouse.get_pos()):
                screen.blit(CURSOR, (440, 725))  
        elif self.__state == "choose_attack_type":
            CombatDraw.display_choose_attack_type(screen, font, self.__ally)
            if self.__type1_button.collidepoint(pygame.mouse.get_pos()):
                screen.blit(CURSOR, (340, 625)) 
            elif self.__type2_button.collidepoint(pygame.mouse.get_pos()) and len(self.__ally.get_types()) == 2:
                screen.blit(CURSOR, (340, 675)) 
            elif self.__back_button.collidepoint(pygame.mouse.get_pos()):
                screen.blit(CURSOR, (340, 725))  

    def logic(self, ally, escpressed, mouseclicked_left):
        
        self.__check_winner()

        if self.__first_run:
            self.__ally = ally
            self.__first_run = False
            self.__enemy = self.__select_random_pokemon_from_POKEMON_DATA(ally)
            self.__enemy_sound = os.path.join(POKEMON_SOUND_PATH, f"{self.__enemy.get_id()}.mp3")
            self.__start_timer = time.monotonic()

        if escpressed:
            self.__run()

        elif time.monotonic() - self.__start_timer >= 1.0 and self.__enemy_sound:
            pygame.mixer.Sound(self.__enemy_sound).play()
            self.__enemy_sound = None

        elif time.monotonic() - self.__start_timer > 4 and self.__state == "game":
            self.__state = "choose_action"

        elif self.__state == "choose_action":
            if self.__ack_button.collidepoint(pygame.mouse.get_pos()) or self.__change_pokemon_button.collidepoint(pygame.mouse.get_pos()) or self.__run_button.collidepoint(pygame.mouse.get_pos()):
                if mouseclicked_left:
                    pygame.mixer.Sound(SFX_PRESS_AB).play()
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                    if self.__ack_button.collidepoint(pygame.mouse.get_pos()):
                        self.__state = "choose_attack_type"
                    elif self.__change_pokemon_button.collidepoint(pygame.mouse.get_pos()):
                        pass #temp
                    else:
                        self.__run()
                else:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        
        elif self.__state == "choose_attack_type":
            if self.__type1_button.collidepoint(pygame.mouse.get_pos()) or (self.__type2_button.collidepoint(pygame.mouse.get_pos()) and len(self.__ally.get_types()) == 2) or self.__back_button.collidepoint(pygame.mouse.get_pos()):
                if mouseclicked_left:
                    pygame.mixer.Sound(SFX_PRESS_AB).play()
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                    if self.__type1_button.collidepoint(pygame.mouse.get_pos()):
                        self.__attack_type = self.__ally.get_types()[0]
                        self.__attack(self.__ally, self.__enemy)
                        self.__state = "enemy_attack"
                    elif self.__type2_button.collidepoint(pygame.mouse.get_pos()) and len(self.__ally.get_types()) == 2:
                        self.__attack_type = self.__ally.get_types()[1]
                        self.__attack(self.__ally, self.__enemy)
                        self.__state = "enemy_attack"
                    else:
                        self.__state = "choose_action"
                else:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        
        if self.__state == "enemy_attack":
            self.__check_winner()
            self.__attack(self.__enemy, self.__ally)
            self.__state = "choose_action"

        if self.__state == "enemy_won" or self.__state == "ally_won":
            return self.__state

        return self.__state
