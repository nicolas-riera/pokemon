import random
import pygame
import time
import os
import json

from src.assets_loading import (
    POKEMONS_TYPE_STATS,
    POKEMON_DATA,
    SFX_RUN,
    SFX_PRESS_AB,
    CURSOR,
    POKEMON_SOUND_PATH,
    HIT_NORMAL_SFX,
    HIT_SUPER_SFX,
    HIT_WEAK_SFX,
    BUG_SFX,
    DARK_SFX,
    DRAGON_SFX,
    ELECTRIC_SFX,
    FAIRY_SFX,
    FIRE_SFX,
    FLYING_SFX,
    GHOST_SFX,
    GRASS_SFX,
    GROUND_SFX,
    ICE_SFX,
    POISON_SFX,
    PSYCHIC_SFX,
    ROCK_SFX,
    STEEL_SFX,
    WATER_SFX,
)
from src.pokemon.Pokemon import Pokemon
from src.game.CombatDraw import CombatDraw
from src.game.game_main_text_rendering import draw_text_block
from src.pyinstaller.data_path import get_data_path


class Combat:
    def __init__(self):
        self.__first_run = True
        self.__ally = None
        self.__enemy = None
        self.__state = "game"
        self.__attack_type = None

        self.__ack_button = pygame.Rect((473, 624, 187, 38))
        self.__change_pokemon_button = pygame.Rect((473, 674, 220, 38))
        self.__run_button = pygame.Rect((473, 724, 88, 38))

        self.__type1_button = pygame.Rect((370, 624, 300, 38))
        self.__type2_button = pygame.Rect((370, 674, 300, 38))
        self.__back_button = pygame.Rect((370, 724, 130, 38))

        self.__message = ""
        self.__message_step = ""
        self.__next_state = "choose_action"

        self.__misc_path = get_data_path("misc.json")

        self.__sfx_cache = {}
        self.__type_sfx = {
            "bug": BUG_SFX,
            "dark": DARK_SFX,
            "dragon": DRAGON_SFX,
            "electric": ELECTRIC_SFX,
            "fairy": FAIRY_SFX,
            "fire": FIRE_SFX,
            "flying": FLYING_SFX,
            "ghost": GHOST_SFX,
            "grass": GRASS_SFX,
            "ground": GROUND_SFX,
            "ice": ICE_SFX,
            "poison": POISON_SFX,
            "psychic": PSYCHIC_SFX,
            "rock": ROCK_SFX,
            "steel": STEEL_SFX,
            "water": WATER_SFX,
        }

    def __get_sfx(self, path):
        if path in self.__sfx_cache:
            return self.__sfx_cache[path]
        try:
            s = pygame.mixer.Sound(path)
            self.__sfx_cache[path] = s
            return s
        except:
            return None

    def __play_sfx(self, path):
        s = self.__get_sfx(path)
        if s:
            s.play()

    def __read_misc(self):
        try:
            with open(self.__misc_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, dict):
                    return data
        except:
            pass
        return {}

    def __write_misc(self, data):
        try:
            with open(self.__misc_path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)
        except:
            pass

    def __set_misc_enemy_state(self):
        data = self.__read_misc()
        data["enemy_id"] = self.__enemy.get_id()
        data["enemy_hp"] = self.__enemy.get_hp()
        data["enemy_level"] = self.__enemy.get_level()
        if "match_counter" not in data:
            data["match_counter"] = 0
        self.__write_misc(data)

    def __clear_misc_enemy_state(self):
        data = self.__read_misc()
        if "enemy_id" in data:
            del data["enemy_id"]
        if "enemy_hp" in data:
            del data["enemy_hp"]
        if "enemy_level" in data:
            del data["enemy_level"]
        if "match_counter" not in data:
            data["match_counter"] = 0
        self.__write_misc(data)

    def __inc_misc_match_counter(self):
        data = self.__read_misc()
        if "match_counter" not in data:
            data["match_counter"] = 0
        data["match_counter"] += 1
        self.__write_misc(data)
        return data["match_counter"]

    def __maybe_heal_all_pokemons(self, pokedex, match_counter):
        if match_counter <= 0:
            return
        if match_counter % 5 != 0:
            return

        for key, val in pokedex.pokedex_data.items():
            pid = val.get("id")
            if pid in POKEMON_DATA:
                pokedex.pokedex_data[key]["hp"] = POKEMON_DATA[pid]["hp"]

        pokedex.write_json()
        pokedex.load_pokedex_objects()

    def __end_match(self, pokedex):
        match_counter = self.__inc_misc_match_counter()
        self.__maybe_heal_all_pokemons(pokedex, match_counter)
        self.__clear_misc_enemy_state()

    def __load_enemy_from_misc(self, misc):
        enemy_id = misc.get("enemy_id", None)
        enemy_hp = misc.get("enemy_hp", None)
        enemy_level = misc.get("enemy_level", None)

        if enemy_id is None or enemy_hp is None or enemy_level is None:
            return None
        if enemy_id not in POKEMON_DATA:
            return None

        try:
            enemy_hp = float(enemy_hp)
            enemy_level = int(enemy_level)
        except:
            return None

        if enemy_hp <= 0:
            return None

        p = Pokemon()
        p.load_from_POKEMON_DATA_dict(POKEMON_DATA[enemy_id])
        p.set_id(enemy_id)
        p.set_level(max(1, enemy_level))
        p.set_hp(enemy_hp)
        return p

    @staticmethod
    def __calculate_attack_mult(attack_type: str, enemy: object):
        mult = 1.0
        for def_type in enemy.get_types():
            mult *= POKEMONS_TYPE_STATS[attack_type.upper()][def_type.upper()]
        return mult

    @staticmethod
    def __select_random_pokemon_from_POKEMON_DATA(ally):
        pokemon = Pokemon()
        random_id, random_pokemon_dict = random.choice(list(POKEMON_DATA.items()))

        pokemon.load_from_POKEMON_DATA_dict(random_pokemon_dict)
        pokemon.set_id(random_id)
        pokemon.set_level(max(1, random.choice([ally.get_level() - 1, ally.get_level(), ally.get_level() + 1])))

        return pokemon

    def __play_attack_sfx(self, attack_type, mult):
        t = str(attack_type).lower()

        if t in self.__type_sfx:
            self.__play_sfx(self.__type_sfx[t])

        if mult > 1:
            self.__play_sfx(HIT_SUPER_SFX)
        elif mult < 1:
            self.__play_sfx(HIT_WEAK_SFX)
        else:
            self.__play_sfx(HIT_NORMAL_SFX)

    def __attack(self, src, dest):
        mult = self.__calculate_attack_mult(self.__attack_type, dest)
        self.__play_attack_sfx(self.__attack_type, mult)
        damage = mult * src.get_attack()
        src.attack(dest, damage)

    def __run(self, pokedex):
        pygame.mixer.music.pause()
        pygame.mixer.music.unload()
        pygame.mixer.Sound(SFX_RUN).play()
        self.music = None
        self.__end_match(pokedex)
        self.__state = "menu"

    def __save_ally_to_pokedex(self, pokedex):
        ally_id = self.__ally.get_id()
        for key, val in pokedex.pokedex_data.items():
            if val.get("id") == ally_id:
                pokedex.pokedex_data[key]["hp"] = self.__ally.get_hp()
                pokedex.pokedex_data[key]["level"] = self.__ally.get_level()
                pokedex.pokedex_data[key]["xp"] = self.__ally.get_xp()
                pokedex.pokedex_data[key]["in_use"] = self.__ally.get_in_use()
                pokedex.write_json()
                break

    def draw(self, screen, font):
        CombatDraw.display_pokemon(self.__ally, self.__enemy, screen, self.__start_timer)

        if time.monotonic() - self.__start_timer > 1:
            CombatDraw.display_ally_block(self.__ally, screen, font)
            CombatDraw.display_enemy_block(self.__enemy, screen, font)

        CombatDraw.display_main_text_block(screen)

        if self.__state == "game":
            draw_text_block(screen, f"A wild {self.__enemy.get_name()} has appeared!", font)
        elif self.__state == "message":
            draw_text_block(screen, self.__message, font)
        elif self.__state == "choose_action":
            CombatDraw.display_choose_action_block(screen, font)
            if self.__ack_button.collidepoint(pygame.mouse.get_pos()):
                screen.blit(CURSOR, (440, 625))
            elif self.__change_pokemon_button.collidepoint(pygame.mouse.get_pos()):
                screen.blit(CURSOR, (440, 675))
            elif self.__run_button.collidepoint(pygame.mouse.get_pos()):
                screen.blit(CURSOR, (440, 725))
        elif self.__state == "choose_attack_type":
            CombatDraw.display_choose_attack_type(screen, font, self.__ally)
            if self.__type1_button.collidepoint(pygame.mouse.get_pos()):
                screen.blit(CURSOR, (340, 625))
            elif self.__type2_button.collidepoint(pygame.mouse.get_pos()) and len(self.__ally.get_types()) == 2:
                screen.blit(CURSOR, (340, 675))
            elif self.__back_button.collidepoint(pygame.mouse.get_pos()):
                screen.blit(CURSOR, (340, 725))

    def logic(self, ally, pokedex, escpressed, mouseclicked_left):
        if self.__first_run:
            self.__ally = ally
            self.__first_run = False

            misc = self.__read_misc()
            loaded_enemy = self.__load_enemy_from_misc(misc)

            if loaded_enemy:
                self.__enemy = loaded_enemy
            else:
                self.__enemy = self.__select_random_pokemon_from_POKEMON_DATA(ally)
                self.__set_misc_enemy_state()

            self.__enemy_sound = os.path.join(POKEMON_SOUND_PATH, f"{self.__enemy.get_id()}.mp3")
            self.__start_timer = time.monotonic()

        if escpressed:
            self.__run(pokedex)
            return self.__state

        if time.monotonic() - self.__start_timer >= 1.0 and self.__enemy_sound:
            try:
                pygame.mixer.Sound(self.__enemy_sound).play()
            except:
                pass
            self.__enemy_sound = None

        if time.monotonic() - self.__start_timer > 4 and self.__state == "game":
            self.__state = "choose_action"

        if self.__state == "message":
            if mouseclicked_left:
                pygame.mixer.Sound(SFX_PRESS_AB).play()

                if self.__message_step == "after_ally_attack":
                    self.__attack_type = random.choice(self.__enemy.get_types())
                    self.__attack(self.__enemy, self.__ally)
                    self.__save_ally_to_pokedex(pokedex)

                    if self.__ally.is_alive() is False:
                        self.__message = f"{self.__enemy.get_name()} attacked {self.__ally.get_name()}! {self.__ally.get_name()} fainted! Returning to menu."
                        self.__message_step = "end_to_menu"
                        self.__next_state = "menu"
                        self.__state = "message"
                        self.__end_match(pokedex)
                        return self.__state

                    self.__message = f"{self.__enemy.get_name()} attacked {self.__ally.get_name()}!"
                    self.__message_step = "back_to_action"
                    self.__next_state = "choose_action"
                    self.__state = "message"
                    return self.__state

                if self.__message_step == "caught_to_menu":
                    self.__end_match(pokedex)
                    self.__state = "menu"
                    return self.__state

                if self.__message_step == "end_to_menu":
                    self.__state = "menu"
                    return self.__state

                self.__state = self.__next_state
            return self.__state

        if self.__state == "choose_action":
            if (
                self.__ack_button.collidepoint(pygame.mouse.get_pos())
                or self.__change_pokemon_button.collidepoint(pygame.mouse.get_pos())
                or self.__run_button.collidepoint(pygame.mouse.get_pos())
            ):
                if mouseclicked_left:
                    pygame.mixer.Sound(SFX_PRESS_AB).play()
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                    if self.__ack_button.collidepoint(pygame.mouse.get_pos()):
                        self.__state = "choose_attack_type"
                    elif self.__change_pokemon_button.collidepoint(pygame.mouse.get_pos()):
                        pass
                    else:
                        self.__run(pokedex)
                else:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        elif self.__state == "choose_attack_type":
            on_type1 = self.__type1_button.collidepoint(pygame.mouse.get_pos())
            on_type2 = self.__type2_button.collidepoint(pygame.mouse.get_pos()) and len(self.__ally.get_types()) == 2
            on_back = self.__back_button.collidepoint(pygame.mouse.get_pos())

            if on_type1 or on_type2 or on_back:
                if mouseclicked_left:
                    pygame.mixer.Sound(SFX_PRESS_AB).play()
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

                    if on_back:
                        self.__state = "choose_action"
                        return self.__state

                    if on_type1:
                        self.__attack_type = self.__ally.get_types()[0]
                    elif on_type2:
                        self.__attack_type = self.__ally.get_types()[1]
                    else:
                        self.__state = "choose_action"
                        return self.__state

                    self.__attack(self.__ally, self.__enemy)
                    self.__set_misc_enemy_state()

                    if self.__enemy.is_alive() is False:
                        enemy_id = self.__enemy.get_id()
                        base_hp = POKEMON_DATA[enemy_id]["hp"]
                        pokedex.add_pokemon_to_pokedex(enemy_id, base_hp, self.__enemy.get_level(), 0)

                        xp_gain = 20 + self.__enemy.get_level() * 10
                        levels = self.__ally.gain_xp_and_level_up(xp_gain)
                        self.__save_ally_to_pokedex(pokedex)

                        if levels > 0:
                            self.__message = f"{self.__ally.get_name()} attacked {self.__enemy.get_name()}! {self.__enemy.get_name()} has been caught and added to the Pokédex! {self.__ally.get_name()} gained {xp_gain} XP and leveled up to LVL {self.__ally.get_level()}!"
                        else:
                            self.__message = f"{self.__ally.get_name()} attacked {self.__enemy.get_name()}! {self.__enemy.get_name()} has been caught and added to the Pokédex! {self.__ally.get_name()} gained {xp_gain} XP!"

                        self.__message_step = "caught_to_menu"
                        self.__next_state = "menu"
                        self.__state = "message"
                        return self.__state

                    self.__message = f"{self.__ally.get_name()} attacked {self.__enemy.get_name()}!"
                    self.__message_step = "after_ally_attack"
                    self.__state = "message"
                    return self.__state

                else:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        return self.__state
