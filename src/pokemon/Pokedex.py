import sys
import os
import pygame

# Get the absolute path of the current file's directory
current_dir = os.path.dirname(os.path.abspath(__file__))
# Go up two levels to get the project root (The 'POKEMON' folder)
# current_dir is ".../src/pokemon", parent is ".../src", grand-parent is ".../POKEMON"
project_root = os.path.abspath(os.path.join(current_dir, '..', '..'))
# Add the root to sys.path
sys.path.append(project_root)


from src.assets_loading import POKEDEX_BACKGROUND


class Pokedex:
    def __init__(self, data_pokemon): 
        '''
        Initialize our Pokedex class
        :param data_pokemon: dictionnary containing all the informations about Pokemons (received from PagameApp.py)
        '''
        self.all_pokemons = data_pokemon
        if isinstance(data_pokemon, dict): # checking if the data is a dict or list
            self.list_pokemon = list(data_pokemon.values()) #convert the JSON dict into a list to get access to index
        elif isinstance(data_pokemon, list):
            self.list_pokemon = data_pokemon
        else:
            self.list_pokemon = [] #error handling the data isn't a list and isn't handled by our pokedex
        
        self.page_index = 0
        self.pokemons_per_page = 5 # amount of pokemon per page to be changed later
        print(f"DEBUG: {self.list_pokemon}")
    @staticmethod
    def pokedex_rendering(screen):
        screen.blit(POKEDEX_BACKGROUND, (0, 0))

# if __name__ == "__main__":
#     printing = PygameApp.load_pokemons([]) #takes pokemon names as an argument and return pokemon data as a list
#     print(printing)
