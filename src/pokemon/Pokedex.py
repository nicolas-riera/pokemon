import os
import pygame
import json

from src.assets_loading import POKEDEX_BACKGROUND, POKEMON_DATA
from src.pokemon.Pokemon import Pokemon

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class Pokedex:
    def __init__(self): 

        '''
        Initialize Pokedex class
        '''
        self.pokedex_data = {} #dict to save our pokemons
        self.pokedex_objects = []
        self.page_index = 0
        self.pokemons_per_page = 5 # amount of pokemon per page to be changed later

        # we load the data when creating the class to not do it again
        self.load_json()
        self.load_pokedex_objects()

    def load_json(self):
        with open(os.path.join(BASE_DIR, "..", "..", "data", "pokedex.json"), 'r') as file:
            self.pokedex_data = json.load(file)

    def write_json(self):
        with open(os.path.join(BASE_DIR, "..", "..", "data", "pokedex.json"), 'w') as file:
            json.dump(self.pokedex_data, file, indent=4)
        

    def load_pokedex_objects(self):
        self.pokedex_objects.clear() # clear the list to not load the pokemons twice 
        for instance_val in self.pokedex_data.values():
            target_id = instance_val["id"]

            if target_id in POKEMON_DATA:
                pokemon_info = POKEMON_DATA[target_id]

                p = Pokemon()
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

    def draw_pokedex(self, screen, font):
        screen.blit(POKEDEX_BACKGROUND, (0, 0))

        beginning_page_index = self.page_index * self.pokemons_per_page # get the index of the first element and multiply it by the number of page to get the first item for example page two starts with the pokemon indexed at ten
        ending_page_index = beginning_page_index + self.pokemons_per_page
        pokemons_displayed = self.pokedex_objects [beginning_page_index:ending_page_index]
        position_y = 50
        for p in pokemons_displayed:
            text = f"{p.get_name()}"
            surface_text = font.render(text, True, (0, 0, 0)) 
            screen.blit(surface_text, (50, position_y))
            position_y += 50 # spacing between lines 
