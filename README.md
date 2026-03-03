# Pokémon

![pythonversion](https://img.shields.io/badge/python-3.x-blue)
![pygame](https://img.shields.io/badge/pygame-required-green)

### Disclaimer

*This project is a school project for educational purposes only. All characters, images, sounds, and trademarks used in this game are the property of Nintendo, Game Freak, and The Pokémon Company.*

*No part of this project is intended for sale or commercial use. It is provided solely for learning and demonstration purposes.*

## Description

This is a recreation of Pokémon's famous combat system, where you battle against other pokémons, in Python and Pygame.

This game includes pokémons from gen 1 and gen 2.

![screenshot_1](/assets/img/screenshot_1.png)

## Controls

- Left mouse click to interact with most things
- In **Pokedex**:
    - Left click to select a pokémon and switch pages (with the arrows)
    - Right click to delete a pokémon
- ESC key to go back

## Installation (Windows only)

Download the latest release of the executable here: https://github.com/nicolas-riera/pokemon/releases/latest

After downloading it, simply run ```Pokemon_[version].exe``` to launch the game.

## Run and Build from source

### Requirements
- Python **3.x**
- pygame -> ```python -m pip install pygame```
- PyInstaller -> ```python -m pip install pyinstaller```

### Run

From the root folder, run :

```bash
python main.py
```

### Build

To build the game (in .exe for Windows, in .app on MacOs, and as a binary file on Linux), use pyinstaller :

```bash
pyinstaller main.py --onefile --noconsole --icon=assets/img/logo.ico --hidden-import=pygame --name "Pokémon" --add-data="assets;assets" --add-data="data;data"
```

On ```--add-data```, replace ";" by ":" if you are on MacOS or Linux.

# Architecture

```mermaid

classDiagram
    class PygameApp {
        +Surface screen
        +Clock clock
        +bool running
        +list pokemon_objects
        +tuple font
        +str state
        +list gamestates
        +Menu menu
        +Pokedex pokedex
        +Combat combat
        +bool escpressed
        +bool mouseclicked_left
        +bool mouseclicked_right
        +bool changed_state
        +__init__(w: int, h: int)
        +reset_all_class()
        +events()
        +draw()
        +logic()
        +loop()
    }

    class Menu {
        -Rect __play_button
        -Rect __enemy_pokemon_button
        -Rect __pokedex_button
        +__init__()
        +menu_intro_music()$
        +menu_rendering(screen, font)
        +menu_logic(escpressed: bool, mouseclicked: bool, state: str) str
    }

    class Pokedex {
        +dict pokedex_data
        +list~Pokemon~ pokedex_objects
        +int page_index
        +int pokemons_per_page
        +str music
        +str font_path
        +Pokemon hovered_pokemon
        +__init__()
        +get_pokemon_id_in_use() int
        +pokedex_music()
        +load_json()
        +write_json()
        +load_pokedex_objects()
        +add_pokemon_to_pokedex(pokemon_id, hp, level, xp)
        +draw_text_aligned(surface, text, font, color, container_rect, align, padding, id)
        +draw_pokedex(screen, font)
        +pokedex_logic(escpressed: bool, state: str, mouseclicked_left: bool, mouseclicked_right: bool) str
    }

    class Combat {
        -bool __first_run
        -Pokemon __ally
        -Pokemon __enemy
        -str __state
        -str __attack_type
        -Rect __ack_button
        -Rect __change_pokemon_button
        -Rect __run_button
        -Rect __type1_button
        -Rect __type2_button
        -Rect __back_button
        -str __message
        -str __message_step
        -str __next_state
        -str __misc_path
        -dict __sfx_cache
        -dict __type_sfx
        -str __enemy_sound
        -float __start_timer
        +str music
        +__init__()
        -__get_sfx(path: str)
        -__play_sfx(path: str)
        -__read_misc() dict
        -__write_misc(data: dict)
        -__set_misc_enemy_state()
        -__clear_misc_enemy_state()
        -__inc_misc_match_counter() int
        -__maybe_heal_all_pokemons(pokedex: Pokedex, match_counter: int)
        -__end_match(pokedex: Pokedex)
        -__load_enemy_from_misc(misc: dict) Pokemon
        -__calculate_attack_mult(attack_type: str, enemy: Pokemon)$ float
        -__select_random_pokemon_from_POKEMON_DATA(ally: Pokemon)$ Pokemon
        -__play_attack_sfx(attack_type: str, mult: float)
        -__attack(src: Pokemon, dest: Pokemon) int
        -__run(pokedex: Pokedex)
        -__save_ally_to_pokedex(pokedex: Pokedex)
        +draw(screen: Surface, font: tuple)
        +logic(ally: Pokemon, pokedex: Pokedex, escpressed: bool, mouseclicked_left: bool) str
    }

    class Pokemon {
        -str __name
        -list __types
        -int __attack
        -int __defense
        -float __hp
        -int __level
        -int __xp
        -str __id
        -bool __in_use
        +__init__(name: str)
        +load_from_POKEMON_DATA_dict(dict)
        +is_alive() bool
        +attack(enemy: Pokemon, hp: float)
        +get_name() str
        +get_types() list
        +get_attack() int
        +get_defense() int
        +get_hp() float
        +get_level() int
        +get_xp() int
        +get_id() str
        +get_in_use() bool
        +set_name(name: str)
        +set_types(types: list)
        +set_attack(attack: int)
        +set_defense(defense: int)
        +set_hp(hp: float)
        +set_level(level: int)
        +set_xp(xp: int)
        +set_id(str_id: str)
        +set_in_use(in_use: bool)
        +add_xp(xp: int)
        +add_level()
        +xp_needed_for_next_level() int
        +gain_xp_and_level_up(xp_amount: int) bool
    }

    class CombatDraw {
        +__init__()
        +display_pokemon(ally: Pokemon, enemy: Pokemon, screen: Surface, start_timer: float)$
        +display_ally_block(ally: Pokemon, screen: Surface, font: tuple)$
        +display_enemy_block(enemy: Pokemon, screen: Surface, font: tuple)$
        +display_main_text_block(screen: Surface)$
        +display_choose_action_block(screen: Surface, font: tuple)$
        +display_choose_attack_type(screen: Surface, font: tuple, ally: Pokemon)$
    }

    class CombatIntro {
        +__init__()
        +battle_intro_music()$
        +combat_intro(screen: Surface, clock: Clock)$
    }

    %% Relations entre les classes
    PygameApp *-- Menu : compose
    PygameApp *-- Pokedex : compose
    PygameApp *-- Combat : compose
    Pokedex o-- Pokemon : aggrège
    Combat --> Pokemon : interagit avec
    Combat ..> CombatDraw : utilise
    PygameApp ..> CombatIntro : utilise (via screen_transition)

```

# Authors

This project has been realised by [Nicolas](https://github.com/nicolas-riera), [André](https://github.com/andrebtw) and [Hugo](https://github.com/hugo-belaloui).
