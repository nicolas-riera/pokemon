import os
import pygame
import json

from src.assets_loading import POKEDEX_BACKGROUND, BASE_DIR, POKEMON_DATA
from src.pokemon.Pokemon import Pokemon

class Pokedex:
    def __init__(self): 

        '''
        Initialize Pokedex class
        '''

        self.pokedex_objects = []
        self.page_index = 0
        self.pokemons_per_page = 5 # amount of pokemon per page to be changed later
        print(f"DEBUG: {self.list_pokemon}")

    @staticmethod
    def pokedex_rendering(screen):
        screen.blit(POKEDEX_BACKGROUND, (0, 0))

    def load_json(self):
        with open(os.path.join(BASE_DIR, "..", "..", "data", "pokedex.json"), 'r') as file:
            self.pokedex_data = json.load(file)

    def write_json(self):
        pass 
        # todo

    def load_pokedex_objects(self):

        for instance_val in self.pokedex_data.values():
            target_id = instance_val["id"]

            if target_id in POKEMON_DATA:
                pokemon_info = POKEMON_DATA[target_id]

                p = Pokemon(pokemon_info["name"])
                p.set_types(pokemon_info["type"])
                p.set_attack(pokemon_info["attack"])
                p.set_defense(pokemon_info["defense"])
                p.set_hp(instance_val["hp"])
                #todo
                self.pokedex_objects.append(p)
