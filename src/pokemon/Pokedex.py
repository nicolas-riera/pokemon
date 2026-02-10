import sys
import os

# Get the absolute path of the current file's directory
current_dir = os.path.dirname(os.path.abspath(__file__))
# Go up two levels to get the project root (The 'POKEMON' folder)
# current_dir is ".../src/pokemon", parent is ".../src", grand-parent is ".../POKEMON"
project_root = os.path.abspath(os.path.join(current_dir, '..', '..'))
# Add the root to sys.path
sys.path.append(project_root)
from src.PygameApp import PygameApp





class Pokedex:
    def __init__(self, data_pokemon): 
        self.all_pokemons = data_pokemon
        self.list_pokemon = PygameApp.load_pokemons(data_pokemon)
        print(f"DEBUG: {self.list_pokemon}")
        

if __name__ == "__main__":
    printing = Pokedex(["Venusaur"])