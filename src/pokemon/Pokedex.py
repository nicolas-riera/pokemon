import os
import pygame
import json
import time

from src.assets_loading import POKEDEX_BACKGROUND, POKEMON_DATA, POKEMON_CENTER_MUSIC, SFX_SWAP, SFX_TINK
from src.pokemon.Pokemon import Pokemon
from src.pyinstaller.data_path import get_data_path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class Pokedex:
    def __init__(self): 

        '''
        Initialize Pokedex data and pagination setting
        '''
        self.pokedex_data = {} #dict to save our pokemons
        self.pokedex_objects = []
        self.page_index = 0
        self.pokemons_per_page = 5 # amount of pokemon per page to be changed later
        self.music = None

        # we load the data when creating the class to not do it again
        self.load_json()
        self.load_pokedex_objects()

    def pokedex_music(self):
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.load(POKEMON_CENTER_MUSIC)
            pygame.mixer.music.play(-1)
        elif self.music != "pokedex":
            self.music = "pokedex"
            pygame.mixer.music.pause()
            pygame.mixer.music.unload()
            
    def load_json(self):
        with open(get_data_path("pokedex.json"), 'r') as file:
            self.pokedex_data = json.load(file)

    def write_json(self):
        with open(get_data_path("pokedex.json"), 'w') as file:
            json.dump(self.pokedex_data, file, indent=4)
        

    def load_pokedex_objects(self):
        self.pokedex_objects.clear() # clear the list to not load the pokemons twice 
        for instance_val in self.pokedex_data.values():
            target_id = instance_val["id"]

            if target_id in POKEMON_DATA:
                pokemon_info = POKEMON_DATA[target_id]

                p = Pokemon(pokemon_info["name"])
                p.set_types(pokemon_info["type"])
                p.set_attack(pokemon_info["attack"])
                p.set_defense(pokemon_info["defense"])
                p.set_hp(instance_val["hp"])
                p.set_level(instance_val["level"])
                p.set_xp(instance_val["xp"])
                self.pokedex_objects.append(p)

    def add_pokemon_to_pokedex(self, pokemon_id, hp, level, xp):
        """
        Method called to capture a pokemon and save it into the pokedex JSON
        Create a new entry for the captured pokemon using the next available index
        """
        next_index = str(len(self.pokedex_data)) # simply find the next next index for pagination purposes 

        new_pokemon = { #we init our pokemon as dict 
            "id": pokemon_id,
            "hp": hp,
            "level": level,
            "xp": xp
        }
        self.pokedex_data[next_index] = new_pokemon # set our new pokemon in the next index in pokemon data 

        self.write_json() # call function to dump new pokemon in json
        self.load_pokedex_objects() # actualize pokedex and clear 

    def draw_text_aligned(self, surface, text, font, color, container_rect, align="center", padding=(0,0)):
        """
        draw an alligned text according to the given rect
        align: "center", "topleft", "midleft", "midright"
        padding: tuple (x, y) to move our text
        """
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        if align == "center":
            text_rect.center = container_rect.center #allign
        elif align == "midleft":
            text_rect.midleft = container_rect.midleft
            text_rect.x += padding[0] #add margin 
        elif align == "midright":
            text_rect.midright = container_rect.midright
            text_rect.x -= padding[0] 
        elif align == "midtop":
            text_rect.midtop = container_rect.midtop
            # text_rect.x += padding[0]
            # text_rect.y += padding[1]
        surface.blit(text_surface, text_rect)

    def draw_pokedex(self, screen, font):
        screen.blit(POKEDEX_BACKGROUND, (0, 0))

        beginning_page_index = self.page_index * self.pokemons_per_page # get the index of the first element and multiply it by the number of page to get the first item for example page two starts with the pokemon indexed at ten
        ending_page_index = beginning_page_index + self.pokemons_per_page
        pokemons_displayed = self.pokedex_objects [beginning_page_index:ending_page_index]
        position_y = 145
        for p in pokemons_displayed:
            # Draw.rect(surface, color, (x position, y position, x width, y width))
            #     pygame.draw.rect(
            #     surface,
            #     (255, 0, 0),          # color
            #     pygame.Rect(50, 50, 200, 100),  # rect
            #     border_radius=20      # radius of the corners
            # )

            pygame.draw.rect(screen, (185, 185, 185), (85, position_y,630, 90), border_radius = 10)
            rect = pygame.Rect((85, position_y,630, 90))
            name_pokemon = f"{p.get_name()}"
            type_pokemon = f"{p.get_types()}"
            stats_pokemon = f"ATT : {p.get_attack()} DEF : {p.get_defense()} HP : {p.get_hp()} LVL : {p.get_level()} XP :{p.get_xp()}"
            self.draw_text_aligned(screen, name_pokemon, font, (0, 0, 0), rect, "midtop", padding=any)
            self.draw_text_aligned(screen, type_pokemon, font, (0, 0, 0), rect, "midright", padding= (10,0))
            self.draw_text_aligned(screen, stats_pokemon, font, (0, 0, 0), rect, "midleft", padding=(10,0))

            # surface_text_name = font.render(name_pokemon, True, (0, 0, 0))
            # surface_text_type = font.render(type_poekmon, True, (0, 0, 0)) 
            # surface_text_stats = font.render(stats_pokemon, True, (0, 0, 0)) 
            # screen.blit(surface_text_name, (315, position_y))
            # screen.blit(surface_text_type, (90, position_y - 20))
            # screen.blit(surface_text_stats, (540, position_y - 20))


            position_y += 100 # spacing between lines 
        # print(pygame.mouse.get_pos())

    def pokedex_logic(self, escpressed, state, mouseclicked):
        """
        Method managing pokedex inputs
        param escpressed : get escape input
        param state : get GAMESTATE
        """

        self.pokedex_music()

        if escpressed:
            pygame.mixer.music.pause()
            pygame.mixer.music.unload()
            pygame.mixer.Sound(SFX_TINK).play()
            self.music = None
            state = "menu"
        
        # Re-calculate the displayed items to check for collisions
        beginning_page_index = self.page_index * self.pokemons_per_page
        ending_page_index = beginning_page_index + self.pokemons_per_page
        pokemons_displayed = self.pokedex_objects[beginning_page_index:ending_page_index]

        position_y = 145
        hover = False
        
        for p in pokemons_displayed:
            # Create a Rect matching the one drawn in draw_pokedex
            button_rect = pygame.Rect(85, position_y, 630, 90)
            if button_rect.collidepoint(pygame.mouse.get_pos()):
                if mouseclicked:
                    pygame.mixer.Sound(SFX_SWAP).play()
                    print(f"Clicked on {p.get_name()}")
                else:
                    hover = True
            position_y += 100

        if hover:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)  
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        return state

