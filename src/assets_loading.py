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

    # Music

INTRO_TITLE_MUSIC = os.path.join(BASE_DIR, "..", "assets", "sound", "music", "intro_title_screen.mp3")
TITLE_MUSIC = os.path.join(BASE_DIR, "..", "assets", "sound", "music", "title_screen.mp3")

POKEMON_CENTER_MUSIC = os.path.join(BASE_DIR, "..", "assets", "sound", "music", "pokemon_center.mp3")

INTRO_BATTLE_MUSIC = os.path.join(BASE_DIR, "..", "assets", "sound", "music", "intro_battle.mp3")
BATTLE_MUSIC = os.path.join(BASE_DIR, "..", "assets", "sound", "music", "battle.mp3")

CAUGHT_POKEMON_MUSIC = os.path.join(BASE_DIR, "..", "assets", "sound", "music", "caught_pokemon.mp3")

POKEMON_HEALED_MUSIC = os.path.join(BASE_DIR, "..", "assets", "sound", "music", "pokemon_healed.mp3")

INTRO_EVOLUTION_MUSIC = os.path.join(BASE_DIR, "..", "assets", "sound", "music", "intro_evolution.mp3")
EVOLUTION_MUSIC = os.path.join(BASE_DIR, "..", "assets", "sound", "music", "evolution.mp3")
POKEMON_EVOLVED_MUSIC = os.path.join(BASE_DIR, "..", "assets", "sound", "music", "pokemon_evolved.mp3")

INTRO_VICTORY_MUSIC = os.path.join(BASE_DIR, "..", "assets", "sound", "music", "intro_victory.mp3")
VICTORY_MUSIC = os.path.join(BASE_DIR, "..", "assets", "sound", "music", "victory.mp3")

    # SFX

SFX_PRESS_AB = os.path.join(BASE_DIR, "..", "assets", "sound", "sfx", "SFX_PRESS_AB.wav")

SFX_RUN = os.path.join(BASE_DIR, "..", "assets", "sound", "sfx", "SFX_RUN.wav")

# Used for deleting pokemon from pokedex
SFX_SWAP = os.path.join(BASE_DIR, "..", "assets", "sound", "sfx", "SFX_SWAP.wav")

# Used for selecting main pokemon
SFX_TINK = os.path.join(BASE_DIR, "..", "assets", "sound", "sfx", "SFX_TINK.wav")
