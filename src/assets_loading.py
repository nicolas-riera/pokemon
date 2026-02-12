import pygame
import os
import json

from src.pyinstaller.data_path import get_data_path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Images

LOGO_TITLE = pygame.image.load(os.path.join(BASE_DIR, "..", "assets", "img", "pokemon_logo.png"))
LOGO_TITLE_RECT = LOGO_TITLE.get_rect(center=(1420, 550))
LOGO_TITLE_SCALED = pygame.transform.smoothscale(LOGO_TITLE, (LOGO_TITLE.get_size()[0]*0.2, LOGO_TITLE.get_size()[1]*0.2))

CURSOR = pygame.image.load(os.path.join(BASE_DIR, "..", "assets", "img", "cursor.png"))

POKEDEX_BACKGROUND = pygame.image.load(os.path.join(BASE_DIR, "..", "assets", "img", "pokedex_bg.png"))

# File data

with open(get_data_path("pokemons_type_stats.json"), "r", encoding="UTF-8") as f:
    POKEMONS_TYPE_STATS = json.load(f)
        
with open(get_data_path("pokemon.json"), 'r', encoding="UTF-8") as f:
    POKEMON_DATA = json.load(f)

# Audio

INTRO_TITLE_MUSIC = os.path.join(BASE_DIR, "..", "assets", "sound", "music", "intro_title_screen.mp3")
TITLE_MUSIC = os.path.join(BASE_DIR, "..", "assets", "sound", "music", "title_screen.mp3")

POKEMON_CENTER_MUSIC = os.path.join(BASE_DIR, "..", "assets", "sound", "music", "pokemon_center.mp3")

INTRO_BATTLE_MUSIC = os.path.join(BASE_DIR, "..", "assets", "sound", "music", "intro_battle.mp3")
BATTLE_MUSIC = os.path.join(BASE_DIR, "..", "assets", "sound", "music", "battle.mp3")
