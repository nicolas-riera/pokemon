import json
import os

from src.pokemon.Pokemon import Pokemon

class Combat:
    def __init__(self):
        pass

    def calculate_attack_mult(self, attack_type:str, enemy:object):
        mult = 1
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "data", "pokemons_type_stats.json"), "r", encoding="UTF-8") as f:
            types = json.load(f)
        for def_type in enemy.get_types():
            mult *= types[attack_type][def_type]
        return mult
            

