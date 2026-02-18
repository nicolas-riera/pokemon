import random
import pygame
import time

from src.assets_loading import POKEMONS_TYPE_STATS, POKEMON_DATA, SFX_RUN, SFX_PRESS_AB, CURSOR
from src.pokemon.Pokemon import Pokemon
from src.game.Combat_draw import Combat_draw
from src.game.game_main_text_rendering import draw_text_block

class Combat:
    def __init__(self):
        self.__first_run = True
        self.__ally = None
        self.__enemy = None
        self.__state = "game"
        self.__ack_button = pygame.Rect((473, 628, 187, 38))
        self.__run_button = pygame.Rect((473, 679, 88, 38))

    @staticmethod
    def __calculate_attack_mult(attack_type:str, enemy:object):
        mult = 1
        for def_type in enemy.get_types():
            mult *= POKEMONS_TYPE_STATS[attack_type][def_type]

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

    def __attack(self, src, dest):
        dest.receive_attack(src.get_attack())

    def events(self):
        pass

    def __run(self):
        pygame.mixer.music.pause()
        pygame.mixer.music.unload()
        pygame.mixer.Sound(SFX_RUN).play()
        self.music = None
        self.__state = "menu"

    def draw(self, screen, font):

        Combat_draw.display_pokemon(self.__ally, self.__enemy, screen, self.__start_timer)
        
        if time.monotonic() - self.__start_timer > 1:
            Combat_draw.display_ally_block(self.__ally, screen, font)
            Combat_draw.display_enemy_block(self.__enemy, screen, font)

        Combat_draw.display_main_text_block(screen)

        if self.__state == "game":
            draw_text_block(screen, f"A wild {self.__enemy.get_name()} has appeared!", font)
        elif self.__state == "choose_action":
            Combat_draw.display_choose_action_block(screen, font)   
            if self.__ack_button.collidepoint(pygame.mouse.get_pos()):
                screen.blit(CURSOR, (440, 630)) 
            elif self.__run_button.collidepoint(pygame.mouse.get_pos()):
                screen.blit(CURSOR, (440, 680))  

    def logic(self, ally, escpressed, mouseclicked_left):

        if self.__first_run:
            self.__ally = ally
            self.__first_run = False
            self.__enemy = self.__select_random_pokemon_from_POKEMON_DATA(ally)
            self.__start_timer = time.monotonic()

        if escpressed:
            self.__run()

        elif time.monotonic() - self.__start_timer > 4 and self.__state == "game":
            self.__state = "choose_action"

        elif self.__state == "choose_action":
            if self.__ack_button.collidepoint(pygame.mouse.get_pos()) or self.__run_button.collidepoint(pygame.mouse.get_pos()):
                if mouseclicked_left:
                    pygame.mixer.Sound(SFX_PRESS_AB).play()
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                    if self.__ack_button.collidepoint(pygame.mouse.get_pos()):
                        self.__state = "choose_attack_type"
                    else:
                        self.__run()
                else:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)


        return self.__state