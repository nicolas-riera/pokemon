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

SFX_PRESS_AB = os.path.join(BASE_DIR, "..", "assets", "sound", "sfx", "SFX_PRESS_AB.mp3")

SFX_RUN = os.path.join(BASE_DIR, "..", "assets", "sound", "sfx", "SFX_RUN.mp3")

# Used when selecting main pokemon
SFX_SWAP = os.path.join(BASE_DIR, "..", "assets", "sound", "sfx", "SFX_SWAP.mp3")

# Used when pressing esc
SFX_TINK = os.path.join(BASE_DIR, "..", "assets", "sound", "sfx", "SFX_TINK.mp3")

# Combat
HIT_NORMAL_SFX = os.path.join(BASE_DIR, "..", "assets", "sound", "sfx", "attack_sfx", "hit_normal.mp3")
HIT_SUPER_SFX = os.path.join(BASE_DIR, "..", "assets", "sound", "sfx", "attack_sfx", "hit_super.mp3")
HIT_WEAK_SFX = os.path.join(BASE_DIR, "..", "assets", "sound", "sfx", "attack_sfx", "hit_weak.mp3")

BUG_SFX = os.path.join(BASE_DIR, "..", "assets", "sound", "sfx", "attack_sfx", "bug.mp3")
DARK_SFX = os.path.join(BASE_DIR, "..", "assets", "sound", "sfx", "attack_sfx", "dark.mp3")
DRAGON_SFX = os.path.join(BASE_DIR, "..", "assets", "sound", "sfx", "attack_sfx", "dragon.mp3")
ELECTRIC_SFX = os.path.join(BASE_DIR, "..", "assets", "sound", "sfx", "attack_sfx", "electric.mp3")
FAIRY_SFX = os.path.join(BASE_DIR, "..", "assets", "sound", "sfx", "attack_sfx", "fairy.mp3")
FIRE_SFX = os.path.join(BASE_DIR, "..", "assets", "sound", "sfx", "attack_sfx", "fire.mp3")
FLYING_SFX = os.path.join(BASE_DIR, "..", "assets", "sound", "sfx", "attack_sfx", "flying.mp3")
GHOST_SFX = os.path.join(BASE_DIR, "..", "assets", "sound", "sfx", "attack_sfx", "ghost.mp3")
GRASS_SFX = os.path.join(BASE_DIR, "..", "assets", "sound", "sfx", "attack_sfx", "grass.mp3")
GROUND_SFX = os.path.join(BASE_DIR, "..", "assets", "sound", "sfx", "attack_sfx", "ground.mp3")
ICE_SFX = os.path.join(BASE_DIR, "..", "assets", "sound", "sfx", "attack_sfx", "ice.mp3")
POISON_SFX = os.path.join(BASE_DIR, "..", "assets", "sound", "sfx", "attack_sfx", "poison.mp3")
PSYCHIC_SFX = os.path.join(BASE_DIR, "..", "assets", "sound", "sfx", "attack_sfx", "psychic.mp3")
ROCK_SFX = os.path.join(BASE_DIR, "..", "assets", "sound", "sfx", "attack_sfx", "rock.mp3")
STEEL_SFX = os.path.join(BASE_DIR, "..", "assets", "sound", "sfx", "attack_sfx", "steel.mp3")
WATER_SFX = os.path.join(BASE_DIR, "..", "assets", "sound", "sfx", "attack_sfx", "water.mp3")