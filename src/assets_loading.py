import pygame
import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

LOGO_TITLE = pygame.image.load(os.path.join(BASE_DIR, "..", "assets", "img", "pokemon_logo.png"))
LOGO_TITLE_RECT = LOGO_TITLE.get_rect(center=(1420, 550))
LOGO_TITLE_SCALED = pygame.transform.smoothscale(LOGO_TITLE, (LOGO_TITLE.get_size()[0]*0.2, LOGO_TITLE.get_size()[1]*0.2))

CURSOR = pygame.image.load(os.path.join(BASE_DIR, "..", "assets", "img", "cursor.png"))

POKEDEX_BACKGROUND = pygame.image.load(os.path.join(BASE_DIR, "..", "assets", "img", "pokedex_bg.png"))

with open(os.path.join(BASE_DIR, "..", "data", "pokemons_type_stats.json"), "r", encoding="UTF-8") as f:
    POKEMONS_TYPE_STATS = json.load(f)
        
with open(os.path.join(BASE_DIR, "..", "data", "pokemon.json"), 'r', encoding="UTF-8") as f:
    POKEMON_DATA = json.load(f)
