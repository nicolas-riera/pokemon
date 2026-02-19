# Pokémon

![pythonversion](https://img.shields.io/badge/python-3.x-blue)
![pygame](https://img.shields.io/badge/pygame-required-green)

### Disclaimer

*This project is a school project for educational purposes only. All characters, images, sounds, and trademarks used in this game are the property of Nintendo, Game Freak, and The Pokémon Company.*

*No part of this project is intended for sale or commercial use. It is provided solely for learning and demonstration purposes.*

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

#Architecture

```mermaid

classDiagram

%% Core Architecture

PygameApp *-- Menu : creates

PygameApp *-- Pokedex : creates

PygameApp *-- Combat : creates


%% AI-Deduced Relationships (What Pyreverse missed!)

Pokedex o-- Pokemon : manages list of (pokedex_objects)

Combat --> Pokemon : uses (ally & enemy)



class PygameApp {

+Surface screen

+Clock clock

+bool running

+str state

+list gamestates

+Menu menu

+Pokedex pokedex

+Combat combat

+__init__(w, h)

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

+menu_logic(escpressed, mouseclicked, state) str

}



class Pokedex {

+dict pokedex_data

+list~Pokemon~ pokedex_objects

+int page_index

+int pokemons_per_page

+Pokemon hovered_pokemon

+__init__()

+pokedex_music()

+load_json()

+write_json()

+load_pokedex_objects()

+add_pokemon_to_pokedex(pokemon_id, hp, level, xp)

+draw_text_aligned(surface, text, font, color, container_rect, align, padding, id)

+draw_pokedex(screen, font)

+pokedex_logic(escpressed, state, mouseclicked_left, mouseclicked_right) str

}



class Combat {

-bool __first_run

-Pokemon __ally

-Pokemon __enemy

-str __state

-Rect __ack_button

-Rect __run_button

-Rect __type1_button

-Rect __type2_button

-Rect __back_button

+__init__()

-__calculate_attack_mult(attack_type, enemy)$

-__select_random_pokemon_from_POKEMON_DATA(ally)$

-__attack(src, dest)

-__run()

+events()

+draw(screen, font)

+logic(ally, escpressed, mouseclicked_left) str

}



class Pokemon {

-str __name

-list __types

-int __attack

-int __defense

-int __hp

-int __level

-int __xp

-str __id

-bool __in_use

+__init__(name)

+load_from_POKEMON_DATA_dict(dict)

+is_alive() bool

+receive_attack(hp)

+getters()

+setters()

}

```

# Authors

This project has been realised by [Nicolas](https://github.com/nicolas-riera), [André](https://github.com/andrebtw) and [Hugo](https://github.com/hugo-belaloui).
